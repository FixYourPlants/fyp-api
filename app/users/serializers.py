from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'image', 'about_me', 'favourite_plant','affected_sicknesses','googleAccount')
        read_only_fields = ('username',)

    def update(self, instance, validated_data):
        # Remover el campo 'favourite_plant' de los datos validados
        validated_data.pop('favourite_plant', None)
        validated_data.pop('affected_sicknesses', None)
        return super().update(instance, validated_data)

    def validate_username(self, value):
        # Validar que el nombre de usuario no esté en uso
        if User.objects.exclude(id=self.instance.id).filter(username=value).exists():
            raise serializers.ValidationError("Este nombre de usuario ya está en uso.")
        return value

    def validate_email(self, value):
        # Validar que el correo electrónico no esté en uso
        if User.objects.exclude(id=self.instance.id).filter(email=value).exists():
            raise serializers.ValidationError("Este correo electrónico ya está en uso.")
        return value

class CreateUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    
    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    class Meta:
        model = User
        fields = ('id', 'username', 'password','password2', 'first_name', 'last_name', 'email', 'auth_token','googleAccount')
        read_only_fields = ('auth_token',)
        extra_kwargs = {'password': {'write_only': True}}

