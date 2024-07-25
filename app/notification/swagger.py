from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


def list_notifications_swagger():
    return swagger_auto_schema(
        operation_summary="List of Notifications for the Logged-in User",
        operation_description="Retrieve a list of notifications for the logged-in user. Requires authentication. Optionally, filter notifications by start and end times.",
        tags=['Notification'],
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description="Token used for authentication. Format: Bearer <token>",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'start_time',
                openapi.IN_QUERY,
                description="Start time for filtering notifications (HH:MM:SS)",
                type=openapi.TYPE_STRING,
                format='time'
            ),
            openapi.Parameter(
                'end_time',
                openapi.IN_QUERY,
                description="End time for filtering notifications (HH:MM:SS)",
                type=openapi.TYPE_STRING,
                format='time'
            ),
        ],
        responses={
            200: openapi.Response(
                description="A list of notifications for the logged-in user",
                examples={
                    "application/json": [
                        {
                            "id": "123e4567-e89b-12d3-a456-426614174000",
                            "title": "Notification 1",
                            "timestamp": "2024-01-01T12:00:00Z",
                            "description": "Description of notification 1"
                        },
                        {
                            "id": "123e4567-e89b-12d3-a456-426614174001",
                            "title": "Notification 2",
                            "timestamp": "2024-01-01T12:30:00Z",
                            "description": "Description of notification 2"
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

