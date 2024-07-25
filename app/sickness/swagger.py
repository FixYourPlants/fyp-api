from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

def sickness_list_swagger():
    return swagger_auto_schema(
        operation_summary="List of Sicknesses",
        operation_description="Retrieve a list of all sicknesses. This endpoint does not require authentication and returns a paginated list of sicknesses.",
        tags=['Sickness'],
        responses={
            200: openapi.Response(
                description="List of sicknesses",
                examples={
                    "application/json": [
                        {
                            "id": "a5dcb5a2-3b0e-4f12-b21f-b27efdb6e4ee",
                            "name": "Oídio",
                            "description": "Enfermedad fúngica que afecta a muchas plantas.",
                            "treatment": "Aplicar fungicida.",
                            "image": "http://example.com/media/sicknesses/oidio.jpg",
                            "notifications": [
                                "a1b2c3d4-5678-90ab-cdef-1234567890ab",
                                "b2c3d4e5-6789-01ab-cdef-234567890abc"
                            ]
                        },
                        {
                            "id": "a6f3f5b9-d5bb-4d7a-9d12-f8a88a9a9ed5",
                            "name": "Podredumbre negra",
                            "description": "Enfermedad que provoca la descomposición de los tejidos.",
                            "treatment": "Eliminar las partes afectadas y aplicar tratamiento antifúngico.",
                            "image": "http://example.com/media/sicknesses/podredumbre_negra.jpg",
                            "notifications": [
                                "c3d4e5f6-7890-12ab-cdef-345678901bcd"
                            ]
                        }
                    ]
                }
            ),
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "detail": "Invalid request parameters."
                    }
                }
            ),
            500: openapi.Response(
                description="Internal Server Error",
                examples={
                    "application/json": {
                        "error": "An error occurred while retrieving the list of sicknesses."
                    }
                }
            )
        }
    )

def sickness_create_swagger():
    return swagger_auto_schema(
        operation_summary="Create a Sickness",
        operation_description="Create a new sickness with the provided details. Requires authentication and appropriate permissions. The request must include the sickness's name, description, treatment, and optionally an image.",
        tags=['Sickness'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="The name of the sickness"
                ),
                'description': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="A detailed description of the sickness"
                ),
                'treatment': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Recommended treatment for the sickness"
                ),
                'image': openapi.Schema(
                    type=openapi.TYPE_FILE,
                    description="Optional image associated with the sickness"
                )
            },
            required=['name', 'description', 'treatment']
        ),
        responses={
            201: openapi.Response(
                description="Sickness successfully created",
                examples={
                    "application/json": {
                        "id": "b6e1f1d2-3a56-4b32-94a5-4cfa5b839cc1",
                        "name": "Oídio",
                        "description": "Enfermedad fúngica que afecta a muchas plantas.",
                        "treatment": "Aplicar fungicida.",
                        "image": "http://example.com/media/sicknesses/oidio.jpg",
                        "notifications": []
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
            500: openapi.Response(
                description="Internal Server Error",
                examples={
                    "application/json": {
                        "error": "An error occurred while creating the sickness."
                    }
                }
            )
        }
    )

def sickness_detail_swagger():
    return swagger_auto_schema(
        operation_summary="Retrieve a Sickness",
        operation_description="Retrieve detailed information about a specific sickness by its ID. The response includes the sickness's name, description, treatment, and an optional image.",
        tags=['Sickness'],
        responses={
            200: openapi.Response(
                description="Sickness details retrieved successfully",
                examples={
                    "application/json": {
                        "id": "b6e1f1d2-3a56-4b32-94a5-4cfa5b839cc1",
                        "name": "Oídio",
                        "description": "Enfermedad fúngica que afecta a muchas plantas.",
                        "treatment": "Aplicar fungicida.",
                        "image": "http://example.com/media/sicknesses/oidio.jpg",
                        "notifications": []
                    }
                }
            ),
            404: openapi.Response(
                description="Sickness not found",
                examples={
                    "application/json": {
                        "detail": "Not found."
                    }
                }
            ),
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "detail": "Invalid request format."
                    }
                }
            )
        }
    )

def plants_with_sickness_swagger():
    return swagger_auto_schema(
        operation_summary="List of Plants with a Sickness",
        operation_description="Retrieve a list of plants that are related to a specific sickness identified by its ID. This endpoint filters the plants based on the given sickness ID.",
        tags=['Sickness'],
        manual_parameters=[
            openapi.Parameter(
                name='sickness_id',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_STRING,
                required=True,
                description='ID of the sickness to filter plants'
            )
        ],
        responses={
            200: openapi.Response(
                description="List of plants related to the specified sickness",
                examples={
                    "application/json": [
                        {
                            "id": "15fe39ec-5071-4940-9d14-cb80bdc8bc27",
                            "name": "Tomate",
                            "description": "Planta de tomate.",
                            "image": "http://example.com/media/plants/tomate.jpg"
                        },
                        {
                            "id": "5e1c6c4b-6c2f-4d4a-bc47-0e930a4e1c60",
                            "name": "Pimiento",
                            "description": "Planta de pimiento.",
                            "image": "http://example.com/media/plants/pimiento.jpg"
                        }
                    ]
                }
            ),
            404: openapi.Response(
                description="Sickness not found",
                examples={
                    "application/json": {
                        "detail": "Sickness with the given ID not found."
                    }
                }
            )
        }
    )


def sickness_affected_change_swagger():
    return swagger_auto_schema(
        operation_summary="Add or Remove an Affected Sickness",
        operation_description= "This endpoint allows the authenticated user to add or remove a sickness from their list of affected sicknesses. Specify the sickness ID in the URL path to either add it if it's not present or remove it if it's already added. Authentication is required for this operation.",
        tags=['Sickness'],
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                description="Token used for authentication. Format: Bearer <token>",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                name='sickness_id',
                in_=openapi.IN_PATH,
                description="ID of the sickness to add or remove.",
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={
            200: openapi.Response(
                description="Sickness successfully added or removed",
                examples={
                    "application/json": True  # True if sickness was added, False if removed
                }
            ),
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "detail": "Invalid data provided or operation could not be completed."
                    }
                }
            ),
            404: openapi.Response(
                description="Sickness not found",
                examples={
                    "application/json": {
                        "detail": "Sickness with the specified ID does not exist."
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

def sickness_affected_status_swagger():
    return swagger_auto_schema(
        operation_summary="Retrieve Affected Sickness Status",
        operation_description= "Check if a specific sickness is affecting the currently authenticated user. This endpoint returns a boolean value indicating whether the specified sickness is present in the user's list of affected sicknesses. Authentication is required for this operation.",
        tags=['Sickness'],
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                description="Token used for authentication. Format: Bearer <token>",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                name='sickness_id',
                in_=openapi.IN_PATH,
                description="ID of the sickness to check if it is affecting the user",
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={
            200: openapi.Response(
                description="Status of the sickness affecting the user",
                examples={
                    "application/json": True  # If the sickness is affecting the user
                }
            ),
            401: openapi.Response(
                description="Unauthorized",
                examples={
                    "application/json": {
                        "detail": "Authentication credentials were not provided or are invalid."
                    }
                }
            ),
            404: openapi.Response(
                description="Sickness Not Found",
                examples={
                    "application/json": {
                        "detail": "The specified sickness was not found in the user's list of affected sicknesses."
                    }
                }
            )
        }
    )

def retrieve_sickness_affected_status_swagger():
    return swagger_auto_schema(
        operation_summary="Retrieve Affected Sickness Status",
        operation_description="Check if a specific sickness is in the user's affected sicknesses list by providing the sickness ID.",
        tags=['Sickness'],
        responses={
            200: openapi.Response(
                description="Sickness status retrieved successfully",
                examples={
                    "application/json": True
                }
            ),
            404: openapi.Response(
                description="Sickness not found",
                examples={
                    "application/json": {
                        "detail": "Not found."
                    }
                }
            )
        }
    )

def sickness_affected_change_swagger():
    return swagger_auto_schema(
        operation_summary="Add or Remove an Affected Sickness",
        operation_description="Add or remove a sickness from the user's affected sicknesses list by providing the sickness ID in the URL.",
        tags=['Sickness'],
        responses={
            200: openapi.Response(
                description="Sickness affected status changed successfully",
                examples={
                    "application/json": True  # or False depending on the action performed
                }
            ),
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "detail": "Sickness ID is required"
                    }
                }
            ),
            404: openapi.Response(
                description="Not Found",
                examples={
                    "application/json": {
                        "detail": "Sickness not found"
                    }
                }
            )
        }
    )

