from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

def get_user_id_by_username_swagger():
    return swagger_auto_schema(
        operation_summary="Get User ID by Username",
        operation_description="Retrieve the user ID by providing the username. If the username is found, the user ID is returned. Otherwise, an error message is returned.",
        tags=['User'],
        manual_parameters=[
            openapi.Parameter('username', openapi.IN_QUERY, type=openapi.TYPE_STRING, description='Username of the user', required=True),
        ],
        responses={
            200: openapi.Response(
                description="User found",
                examples={
                    "application/json": {
                        "user_id": "374e2243-6fbb-4c3b-9185-ca56cdcd81f3"
                    }
                }
            ),
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "error": "Username not provided"
                    }
                }
            ),
            404: openapi.Response(
                description="Not Found",
                examples={
                    "application/json": {
                        "error": "User not found"
                    }
                }
            )
        }
    )

def user_list_swagger():
    return swagger_auto_schema(
        operation_summary="List of Users",
        operation_description="Retrieve a list of all users in the system. This endpoint returns detailed information about each user, including their ID, username, email, profile image, and other related attributes.",
        tags=['User'],
        responses={
            200: openapi.Response(
                description="List of users",
                examples={
                    "application/json": [
                        {
                            "id": "374e2243-6fbb-4c3b-9185-ca56cdcd81f3",
                            "username": "admin",
                            "first_name": "Rafa",
                            "last_name": "Corcho",
                            "email": "admin@us.es",
                            "image": "http://localhost:8000/media/users/image_45copEQ.jpg",
                            "about_me": "hola",
                            "favourite_plant": [
                                "15fe39ec-5071-4940-9d14-cb80bdc8bc27",
                                "ef2bf25e-fc21-4853-907b-cf4fc97dd4e3"
                            ],
                            "googleAccount": False
                        }
                    ]
                }
            )
        }
    )

def user_detail_swagger():
    return swagger_auto_schema(
        operation_summary="Retrieve a User",
        operation_description="Fetch detailed information of a specific user by their ID. This endpoint returns comprehensive details including user attributes, profile image, and related fields.",
        tags=['User'],
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                description="Token used for authentication. Format: Bearer <token>",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                name='user_id',
                in_=openapi.IN_PATH,
                description="ID of the user to retrieve",
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={
            200: openapi.Response(
                description="User details",
                examples={
                    "application/json": {
                        "id": "374e2243-6fbb-4c3b-9185-ca56cdcd81f3",
                        "username": "admin",
                        "first_name": "Rafa",
                        "last_name": "Corcho",
                        "email": "admin@us.es",
                        "image": "http://localhost:8000/media/users/image_45copEQ.jpg",
                        "about_me": "hola",
                        "favourite_plant": [
                            "15fe39ec-5071-4940-9d14-cb80bdc8bc27",
                            "ef2bf25e-fc21-4853-907b-cf4fc97dd4e3"
                        ],
                        "googleAccount": False
                    }
                }
            ),
            404: openapi.Response(
                description="User Not Found",
                examples={
                    "application/json": {
                        "detail": "User with the specified ID was not found."
                    }
                }
            )
        }
    )

def user_detail_swagger():
    return swagger_auto_schema(
        operation_summary="Retrieve a User",
        operation_description="Fetch detailed information of a specific user by their ID. This endpoint returns comprehensive details including user attributes, profile image, and related fields.",
        tags=['User'],
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                description="Token used for authentication. Format: Bearer <token>",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                name='user_id',
                in_=openapi.IN_PATH,
                description="ID of the user to retrieve",
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={
            200: openapi.Response(
                description="User details",
                examples={
                    "application/json": {
                        "id": "374e2243-6fbb-4c3b-9185-ca56cdcd81f3",
                        "username": "admin",
                        "first_name": "Rafa",
                        "last_name": "Corcho",
                        "email": "admin@us.es",
                        "image": "http://localhost:8000/media/users/image_45copEQ.jpg",
                        "about_me": "hola",
                        "favourite_plant": [
                            "15fe39ec-5071-4940-9d14-cb80bdc8bc27",
                            "ef2bf25e-fc21-4853-907b-cf4fc97dd4e3"
                        ],
                        "googleAccount": False
                    }
                }
            ),
            404: openapi.Response(
                description="User Not Found",
                examples={
                    "application/json": {
                        "detail": "User with the specified ID was not found."
                    }
                }
            )
        }
    )

def user_update_swagger():
    return swagger_auto_schema(
        operation_summary="Update a User",
        operation_description="Update the details of a specific user by their ID. This endpoint allows modifications to user attributes such as username, email, and profile information. Authentication is required.",
        tags=['User'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Updated username'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Updated email address'),
                'about_me': openapi.Schema(type=openapi.TYPE_STRING, description='Updated information about the user'),
                'googleAccount': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Indicates if the user has a Google account')
            },
            required=['username', 'email']
        ),
        responses={
            200: openapi.Response(
                description="User successfully updated",
                examples={
                    "application/json": {
                        "id": "374e2243-6fbb-4c3b-9185-ca56cdcd81f3",
                        "username": "admin",
                        "first_name": "Rafa",
                        "last_name": "Corcho",
                        "email": "admin@us.es",
                        "image": "http://localhost:8000/media/users/image_45copEQ.jpg",
                        "about_me": "hola",
                        "favourite_plant": [
                            "15fe39ec-5071-4940-9d14-cb80bdc8bc27",
                            "ef2bf25e-fc21-4853-907b-cf4fc97dd4e3"
                        ],
                        "googleAccount": False
                    }
                }
            ),
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "errors": {
                            "username": ["This field is required."],
                            "email": ["Enter a valid email address."]
                        }
                    }
                }
            ),
            404: openapi.Response(
                description="User Not Found",
                examples={
                    "application/json": {
                        "detail": "User with the specified ID was not found."
                    }
                }
            )
        }
    )

def logged_in_user_swagger():
    return swagger_auto_schema(
        operation_summary="Get Logged In User",
        operation_description="Retrieve details of the currently logged-in user. This endpoint returns user-specific information including profile details and related fields.",
        tags=['User'],
        responses={
            200: openapi.Response(
                description="Details of the logged-in user",
                examples={
                    "application/json": {
                        "id": "374e2243-6fbb-4c3b-9185-ca56cdcd81f3",
                        "username": "admin",
                        "first_name": "Rafa",
                        "last_name": "Corcho",
                        "email": "admin@us.es",
                        "image": "http://localhost:8000/media/users/image_45copEQ.jpg",
                        "about_me": "hola",
                        "favourite_plant": [
                            "15fe39ec-5071-4940-9d14-cb80bdc8bc27",
                            "ef2bf25e-fc21-4853-907b-cf4fc97dd4e3"
                        ],
                        "googleAccount": False
                    }
                }
            ),
            401: openapi.Response(
                description="Unauthorized",
                examples={
                    "application/json": {
                        "detail": "Authentication credentials were not provided or are invalid."
                    }
                }
            )
        }
    )

def login_swagger():
    return swagger_auto_schema(
        operation_summary="User Login",
        operation_description="Authenticate a user by providing username and password. If successful, this endpoint returns a JSON Web Token (JWT) for authentication in subsequent requests. The response includes the JWT tokens and the user ID. If the user’s email is not verified, an appropriate message is returned. Authentication is required for this operation.",
        tags=['User'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username of the user'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password of the user'),
                'googleAccount': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Indicates if the user is logging in with a Google account'),
            },
            required=['username', 'password', 'googleAccount']
        ),
        responses={
            200: openapi.Response(
                description="Login successful",
                examples={
                    "application/json": {
                        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
                        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
                        "userId": "374e2243-6fbb-4c3b-9185-ca56cdcd81f3",
                        "message": "Login successful"
                    }
                }
            ),
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "email": "El email no ha sido verificado"
                    }
                }
            ),
            401: openapi.Response(
                description="Unauthorized",
                examples={
                    "application/json": {
                        "error": "Usuario o contraseña incorrectos"
                    }
                }
            )
        }
    )

def create_user_swagger():
    return swagger_auto_schema(
        operation_summary="Create a New User",
        operation_description="Register a new user by providing the necessary information. If the registration is successful, the user will receive a verification email.",
        tags=['User'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username of the user'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password of the user'),
                'password2': openapi.Schema(type=openapi.TYPE_STRING, description='Password confirmation'),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First name of the user'),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last name of the user'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email address of the user'),
            },
            required=['username', 'password', 'password2', 'email']
        ),
        responses={
            201: openapi.Response(
                description="User created successfully",
                examples={
                    "application/json": {
                        "id": "374e2243-6fbb-4c3b-9185-ca56cdcd81f3",
                        "username": "testuser",
                        "first_name": "John",
                        "last_name": "Doe",
                        "email": "johndoe@example.com",
                        "auth_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
                    }
                }
            ),
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "errors": {
                            "username": "This field is required.",
                            "password": "This field is required.",
                            "password2": "This field is required.",
                            "email": "This field is required."
                        }
                    }
                }
            )
        }
    )







