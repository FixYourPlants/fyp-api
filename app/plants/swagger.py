from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

'''
PLANT
'''
def list_plants_swagger():
    return swagger_auto_schema(
        operation_summary="List of Plants",
        operation_description="Retrieve a list of all plants. No authentication required.",
        tags=['Plant'],
        responses={
            200: openapi.Response(
                description="A list of plants",
                examples={
                    "application/json": [
                        {
                            "id": "123e4567-e89b-12d3-a456-426614174000",
                            "name": "Rose",
                            "scientific_name": "Rosa",
                            "description": "A beautiful flower",
                            "image": "https://example.com/plants/rose.jpg",
                            "difficulty": "FÁCIL",
                            "treatment": "Regular watering",
                            "sicknesses": [],
                            "characteristics": [],
                            "notifications": []
                        },
                        {
                            "id": "123e4567-e89b-12d3-a456-426614174001",
                            "name": "Tulip",
                            "scientific_name": "Tulipa",
                            "description": "A vibrant flower",
                            "image": "https://example.com/plants/tulip.jpg",
                            "difficulty": "MEDIO",
                            "treatment": "Moderate watering",
                            "sicknesses": [],
                            "characteristics": [],
                            "notifications": []
                        }
                    ]
                }
            ),
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "detail": "Invalid parameters provided."
                    }
                }
            ),
        }
    )

def retrieve_plant_swagger():
    return swagger_auto_schema(
        operation_summary="Retrieve a Plant",
        operation_description="Retrieve detailed information about a specific plant by its ID. No authentication required.",
        tags=['Plant'],
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description="ID of the plant to retrieve",
                type=openapi.TYPE_STRING
            )
        ],
        responses={
            200: openapi.Response(
                description="A plant object",
                examples={
                    "application/json": {
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "name": "Rose",
                        "scientific_name": "Rosa",
                        "description": "A beautiful flower",
                        "image": "https://example.com/plants/rose.jpg",
                        "difficulty": "FÁCIL",
                        "treatment": "Regular watering",
                        "sicknesses": [],
                        "characteristics": [],
                        "notifications": []
                    }
                }
            ),
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "detail": "Invalid ID provided."
                    }
                }
            ),
            404: openapi.Response(
                description="Not Found",
                examples={
                    "application/json": {
                        "detail": "Plant not found."
                    }
                }
            )
        }
    )

def list_favourite_plants_swagger():
    return swagger_auto_schema(
        operation_summary="List of Favorite Plants",
        operation_description="Retrieve a list of the logged-in user's favourite plants. Requires authentication.",
        tags=['Plant'],
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description="Token used for authentication. Format: Bearer <token>",
                type=openapi.TYPE_STRING
            )
        ],
        responses={
            200: openapi.Response(
                description="A list of favorite plant objects",
                examples={
                    "application/json": [
                        {
                            "id": "123e4567-e89b-12d3-a456-426614174000",
                            "name": "Rose",
                            "scientific_name": "Rosa",
                            "description": "A beautiful flower",
                            "image": "https://example.com/plants/rose.jpg",
                            "difficulty": "FÁCIL",
                            "treatment": "Regular watering",
                            "sicknesses": [],
                            "characteristics": [],
                            "notifications": []
                        }
                    ]
                }
            ),
            401: openapi.Response(
                description="Unauthorized",
                examples={
                    "application/json": {
                        "detail": "Authentication credentials were not provided."
                    }
                }
            ),
            403: openapi.Response(
                description="Forbidden",
                examples={
                    "application/json": {
                        "detail": "You do not have permission to perform this action."
                    }
                }
            )
        }
    )

def update_favourite_plant_swagger():
    return swagger_auto_schema(
        operation_summary="Add or Remove a Favorite Plant",
        operation_description="Toggle the favourite status of a plant for the logged-in user. Requires authentication. The plant ID must be provided in the URL.",
        tags=['Plant'],
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description="Token used for authentication. Format: Bearer <token>",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'pk',
                openapi.IN_PATH,
                description="ID of the plant to be added or removed from favorites",
                type=openapi.TYPE_STRING
            ),
        ],
        responses={
            200: openapi.Response(
                description="Favorite status toggled successfully",
                examples={
                    "application/json": {
                        "favorite": True
                    }
                }
            ),
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "detail": "Invalid data provided."
                    }
                }
            ),
            401: openapi.Response(
                description="Unauthorized",
                examples={
                    "application/json": {
                        "detail": "Authentication credentials were not provided."
                    }
                }
            ),
            403: openapi.Response(
                description="Forbidden",
                examples={
                    "application/json": {
                        "detail": "You do not have permission to perform this action."
                    }
                }
            ),
            404: openapi.Response(
                description="Not Found",
                examples={
                    "application/json": {
                        "detail": "Plant not found."
                    }
                }
            )
        }
    )

def retrieve_favourite_plant_swagger():
    return swagger_auto_schema(
        operation_summary="Retrieve Favorite Plant Status",
        operation_description="Check if a specific plant is in the user's list of favourite plants. Requires authentication. The plant ID must be provided in the URL.",
        tags=['Plant'],
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description="Token used for authentication. Format: Bearer <token>",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'pk',
                openapi.IN_PATH,
                description="ID of the plant to check in the favorites list",
                type=openapi.TYPE_STRING
            ),
        ],
        responses={
            200: openapi.Response(
                description="Favorite plant status retrieved successfully",
                examples={
                    "application/json": {
                        "favorite": True
                    }
                }
            ),
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "detail": "Invalid data provided."
                    }
                }
            ),
            401: openapi.Response(
                description="Unauthorized",
                examples={
                    "application/json": {
                        "detail": "Authentication credentials were not provided."
                    }
                }
            ),
            403: openapi.Response(
                description="Forbidden",
                examples={
                    "application/json": {
                        "detail": "You do not have permission to perform this action."
                    }
                }
            ),
            404: openapi.Response(
                description="Not Found",
                examples={
                    "application/json": {
                        "detail": "Plant not found."
                    }
                }
            )
        }
    )

'''
OPINION
'''
def list_opinions_swagger():
    return swagger_auto_schema(
        operation_summary="List of Opinions",
        operation_description="Retrieve a list of opinions for a specific plant. Requires authentication. The plant ID must be provided in the query parameters.",
        tags=['Opinion'],
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token used for authentication. Format: Bearer <token>'
            ),
            openapi.Parameter(
                name='plant_id',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description='ID of the plant to filter opinions'
            )
        ],
        responses={
            200: openapi.Response(
                description="List of opinions retrieved successfully",
                examples={
                    "application/json": [
                        {
                            "id": "2926d45c-b7bf-4b21-8752-0f6aebf9c8b3",
                            "user": {
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
                            },
                            "title": "Patata",
                            "description": "Con papas mejor todava",
                            "created_at": "2024-07-21T16:52:38+0000",
                            "plant": "15fe39ec-5071-4940-9d14-cb80bdc8bc27"
                        }
                    ]
                }
            ),
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "detail": "Invalid plant ID provided."
                    }
                }
            ),
            401: openapi.Response(
                description="Unauthorized",
                examples={
                    "application/json": {
                        "detail": "Authentication credentials were not provided."
                    }
                }
            ),
            403: openapi.Response(
                description="Forbidden",
                examples={
                    "application/json": {
                        "detail": "You do not have permission to perform this action."
                    }
                }
            ),
            404: openapi.Response(
                description="Not Found",
                examples={
                    "application/json": {
                        "detail": "Plant not found."
                    }
                }
            )
        }
    )

def opinion_create_swagger():
    return swagger_auto_schema(
        operation_summary="Create an Opinion",
        operation_description="Create a new opinion related to a specific plant. Requires authentication. The plant ID and user ID must be provided in the request body.",
        tags=['Opinion'],
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token used for authentication. Format: Bearer <token>'
            )
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="The title of the opinion"
                ),
                'description': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Detailed description of the opinion"
                ),
                'plant_id': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="ID of the plant the opinion is related to"
                ),
                'user_id': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="ID of the user creating the opinion"
                ),
            },
            required=['title', 'description', 'plant_id', 'user_id']
        ),
        responses={
            201: openapi.Response(
                description="Opinion successfully created",
                examples={
                    "application/json": {
                        "id": "2926d45c-b7bf-4b21-8752-0f6aebf9c8b3",
                        "user": {
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
                        },
                        "title": "Patata",
                        "description": "Con papas mejor todava",
                        "created_at": "2024-07-21T16:52:38+0000",
                        "plant": "15fe39ec-5071-4940-9d14-cb80bdc8bc27"
                    }
                }
            ),
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "detail": "Invalid data provided, or the specified plant or user does not exist."
                    }
                }
            ),
            401: openapi.Response(
                description="Unauthorized",
                examples={
                    "application/json": {
                        "detail": "Authentication credentials were not provided."
                    }
                }
            ),
            403: openapi.Response(
                description="Forbidden",
                examples={
                    "application/json": {
                        "detail": "You do not have permission to perform this action."
                    }
                }
            ),
            404: openapi.Response(
                description="Not Found",
                examples={
                    "application/json": {
                        "detail": "Plant or user not found."
                    }
                }
            )
        }
    )




