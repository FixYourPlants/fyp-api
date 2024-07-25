from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

'''
DIARY
'''
def list_diaries_swagger():
    return swagger_auto_schema(
        operation_summary="List of Diaries",
        operation_description="Retrieve a list of diaries for the authenticated user. Requires authentication. Each diary includes details such as title, last updated date, associated plant, and user.",
        tags=['Diary'],
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
                description="List of diaries retrieved successfully",
                examples={
                    "application/json": [
                        {
                            "id": "123e4567-e89b-12d3-a456-426614174000",
                            "title": "My First Diary",
                            "updated_at": "2024-01-01T12:00:00Z",
                            "plant": 1,
                            "user": 1
                        },
                        {
                            "id": "123e4567-e89b-12d3-a456-426614174001",
                            "title": "My Second Diary",
                            "updated_at": "2024-01-03T12:00:00Z",
                            "plant": 2,
                            "user": 1
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
        }
    )


'''
PAGE
'''
def list_pages_swagger():
    return swagger_auto_schema(
        operation_summary="List of Pages",
        operation_description="Retrieve a list of pages. Requires authentication. Optionally filter by `diary_id`. Each page includes details such as title, content, creation date, and associated image.",
        tags=['Page'],
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description="Token used for authentication. Format: Bearer <token>",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'diary_id',
                openapi.IN_QUERY,
                description="Optional filter by diary ID. If provided, only pages associated with this diary will be returned.",
                type=openapi.TYPE_STRING
            )
        ],
        responses={
            200: openapi.Response(
                description="List of pages successfully retrieved",
                examples={
                    "application/json": [
                        {
                            "id": "123e4567-e89b-12d3-a456-426614174000",
                            "title": "Page 1",
                            "content": "Content of page 1",
                            "created_at": "2024-01-01T12:00:00Z",
                            "image": "https://example.com/pages/page1.jpg",
                            "diary": "123e4567-e89b-12d3-a456-426614174000"
                        },
                        {
                            "id": "123e4567-e89b-12d3-a456-426614174001",
                            "title": "Page 2",
                            "content": "Content of page 2",
                            "created_at": "2024-01-02T12:00:00Z",
                            "image": "https://example.com/pages/page2.jpg",
                            "diary": "123e4567-e89b-12d3-a456-426614174001"
                        }
                    ]
                }
            ),
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "detail": "Invalid parameters."
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
            )
        }
    )


def create_page_swagger():
    return swagger_auto_schema(
        operation_summary="Create a Page",
        operation_description="Create a new page with the provided details. Requires authentication. The request must include a title, content, and diary ID. An optional image can be uploaded.",
        tags=['Page'],
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description="Token used for authentication. Format: Bearer <token>",
                type=openapi.TYPE_STRING
            )
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="The title of the page"
                ),
                'content': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="The content of the page"
                ),
                'image': openapi.Schema(
                    type=openapi.TYPE_FILE,
                    description="Optional image associated with the page"
                ),
                'diary': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="ID of the diary to which the page belongs"
                ),
            },
            required=['title', 'content', 'diary']
        ),
        responses={
            201: openapi.Response(
                description="Page successfully created",
                examples={
                    "application/json": {
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "title": "New Page",
                        "content": "Content of the new page",
                        "created_at": "2024-01-01T12:00:00Z",
                        "image": "https://example.com/pages/new_page.jpg",
                        "diary": "123e4567-e89b-12d3-a456-426614174000"
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
            )
        }
    )
