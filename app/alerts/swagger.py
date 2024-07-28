from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

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
