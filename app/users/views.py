from django.contrib.auth import authenticate, password_validation
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views import View
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from app.config import common as settings
from app.users.forms import NewPasswordForm, EmailForm
from app.users.utils import get_user, validate_email
from .models import User
from .serializers import CreateUserSerializer, UserSerializer
from .swagger import user_list_swagger, user_detail_swagger, user_update_swagger, logged_in_user_swagger, \
    login_swagger, get_user_id_by_username_swagger, create_user_swagger


class UserListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    @user_list_swagger()
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @get_user_id_by_username_swagger()
    @action(detail=False, methods=['GET'])
    def get_user_id_by_username(self, request):
        username = request.query_params.get('username', None)
        if not username:
            return Response({'error': 'Username not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username)
            return Response({'user_id': user.id}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class UserDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    @user_detail_swagger()
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class UserUpdateAndDestroyView(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    @user_update_swagger()
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class LoggedInUserView(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @logged_in_user_swagger()
    @action(detail=False, methods=['GET'])
    def get_logged_in_user(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CustomPasswordResetView(View):
    
    def get(self, request):
        form = EmailForm()
        return render(request, 'password_reset_form.html', {'form': form})
    
    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email=form.cleaned_data['email']).first()
            if user != None:
                if validate_email(user.email):
                    token = default_token_generator.make_token(user)
                    uid = urlsafe_base64_encode(force_bytes(user.pk))
                    new_password_url = reverse('change_password', args=[uid, token])

                    template = get_template('password_reset_email.html')
                    content = template.render(
                        {'new_password_url': request.build_absolute_uri('/') + new_password_url[1:], 'username': user.username})
                    message = EmailMultiAlternatives(
                        'Cambio de contraseña',
                        content,
                        settings.Common.EMAIL_HOST_USER,
                        [user.email]
                    )

                    message.attach_alternative(content, 'text/html')
                    message.send()
                    return redirect('/api/v1/password-sended/')
            else:
                error_message = 'No se encontró un usuario con ese email.'
        return render(request, 'password_reset_form.html', {'form': form, 'error_message': error_message})

class ChangePasswordView(View):

    def get(self, request, uidb64, token):
        user = get_user(uidb64)
        if user is not None and default_token_generator.check_token(user, token):
            form = NewPasswordForm()
            return render(request, 'password_reset_confirm.html', {'form': form})
        else:
            return redirect('/?message=Error al cambiar la contraseña&status=Error')

    def post(self, request, uidb64, token):
        user = get_user(uidb64)
        if user is not None and default_token_generator.check_token(user, token):
            form = NewPasswordForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data['password']
                password_validation.validate_password(password, user)

                user.set_password(password)
                user.save()
                return redirect('/api/v1/password-success/')
            return render(request, 'password_reset_confirm.html', {'form': form})
        return redirect('/?message=Error al cambiar la contraseña&status=Error')

    
class CustomPasswordSendedView(View):
    
    def get(self, request):
        return render(request, 'password_reset_sended.html')
    
class CustomPasswordSuccesView(View):
        
    def get(self, request):
        return render(request, 'password_reset_success.html')


class CreateUserView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    @create_user_swagger()
    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Validación de la contraseña usando los validadores de Django
        password = serializer.validated_data.get('password')
        password_validation.validate_password(password, serializer.instance)

        user = serializer.save()

        username = serializer.validated_data.get('username')
        email = serializer.validated_data.get('email')

        try:
            if validate_email(email):
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                new_password_url = reverse('verification_success', args=[uid, token])

                template = get_template('verification_signup_email.html')
                content = template.render(
                    {'verification_url': request.build_absolute_uri('/') + new_password_url[1:], 'username': username})
                message = EmailMultiAlternatives(
                    'Verificación de Cuenta FixYourPlants',
                    content,
                    settings.Common.EMAIL_HOST_USER,
                    [request.data.get('email')]
                )
                message.attach_alternative(content, 'text/html')
                message.send()

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
        except DjangoValidationError as e:
            error_data = {}
            for field, errors in e.error_dict.items():
                error_data[field] = errors[0]  # Assuming you want the first error message for each field
            return Response({'errors': error_data}, status=status.HTTP_400_BAD_REQUEST)



class ConfirmEmailView(View):
    
    def get(self, request, uidb64, token):
        user = get_user(uidb64)
        if user is not None and default_token_generator.check_token(user, token):
            user.email_verified = True
            user.save()
            print(user)
            return render(request, 'email_verification_success.html')
        else:
            return redirect('/docs/?message=Correo electrónico no verificado&status=Error')

class LoginView(viewsets.GenericViewSet):
    
    @login_swagger()
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

    
        user = authenticate(username=username, password=password)
        
        if User.objects.filter(username=username).exists():
            user_models = User.objects.filter(username=username).first()
            if not user_models.email_verified:
                return Response({'email': 'El email no ha sido verificado'}, status=400)
        if user is None:
            return Response({'error': 'Usuario o contraseña incorrectos'}, status=401)
        
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'userId': user.id,  # Aquí devolvemos el userID
            'message': 'Login successful'
        }, status=status.HTTP_200_OK)