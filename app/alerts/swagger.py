from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

def alert_details_swagger():
    return swagger_auto_schema(
        operation_summary="Retrieve an Alert",
        operation_description="This endpoint retrieves the details of an alert given its URL. No requires authentication.",
        tags=['Alert'],
        manual_parameters=[
            openapi.Parameter(
                name='link',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='URL of the alert',
                required=True,
                example='https://plagas.itacyl.es/-/252345-102?redirect=%2Falertas',
            )
        ],
        responses={
            200: openapi.Response(
                description="Alert details retrieved successfully",
                examples={
                    "application/json": {
                        "details": "The details of the alert"
                    }
                }
            ),
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "error": "Link not provided"
                    }
                }
            ),
            404: openapi.Response(
                description="Alert not found",
                examples={
                    "application/json": {
                        "error": "Alert not found for the provided URL"
                    }
                }
            )
        }
    )

def list_alerts_government_swagger():
    return swagger_auto_schema(
        operation_summary="List of Alerts for Government",
        operation_description="Retrieve a list of alerts specifically for government use.",
        tags=['Alert'],
        responses={
            200: openapi.Response(
                description="List of alerts retrieved successfully",
                examples={
                    "application/json": [
                        {
                            "title": "Agrilus anxius Gory.",
                            "image": "https://www.mapa.gob.es/es/agricultura/temas/sanidad-vegetal/1aglirusanxiusgory_tcm30-536017.jpg",
                            "family": "Buprestidae.",
                            "distribution": "EE.UU, Canadá.",
                            "host": "Betula albosinensis, Betula alleghaniensis, Betula dahurica, Betula ermanii, Betula lenta, Betula maximowicziana, Betula occidentalis, Betula papyrifera, Betula pendula, Betula platyphylla var. japonica, Betula platyphylla var. Szechuanica, Betula populifolia, Betula pubescens, Betula utilis, Betula utilis var. Jacquemontii",
                            "damage": "Polífago, la larva produce galerías, que interrumpen el transporte del floema. En altas densidades pueden matar a los árboles."
                        },
                        {
                            "title": "Sample Alert 2",
                            "image": "https://www.mapa.gob.es/sample_image2.jpg",
                            "family": "Sample Family 2",
                            "distribution": "Sample Distribution 2",
                            "host": "Sample Host 2",
                            "damage": "Sample Damage 2"
                        }
                    ]
                }
            ),
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "error": "Invalid request"
                    }
                }
            )
        }
    )


def list_alerts_swagger():
    return swagger_auto_schema(
        operation_summary="List of Alerts",
        operation_description="Retrieve a list of general alerts.",
        tags=['Alert'],
        responses={
            200: openapi.Response(
                description="List of alerts retrieved successfully",
                examples={
                    "application/json": [
                        {
                            "title": "Alert 1 Title",
                            "link": "https://example.com/alert1"
                        },
                        {
                            "title": "Alert 2 Title",
                            "link": "https://example.com/alert2"
                        }
                    ]
                }
            ),
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "error": "Invalid request"
                    }
                }
            )
        }
    )
