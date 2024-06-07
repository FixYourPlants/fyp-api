from drf_yasg import openapi
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from bs4 import BeautifulSoup
from rest_framework.views import APIView




# Create your views here.
'''
ALERTS
'''
base_url = "https://plagas.itacyl.es/alertas"

def getAlerts():
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    alerts = []

    alerts_divs = soup.select("div.textoInterior div.row.bb-10")
    for alert in alerts_divs:
        title_element = alert.select_one("p")
        link_element = alert.select_one("a")
        
        if title_element and link_element:
            title = title_element.get_text(strip=True)
            link = link_element['href']
            alerts.append({"title":title,"link":link})
    
    return alerts

def getAlert(url):
    response_element = requests.get(url)
    soup_element = BeautifulSoup(response_element.content, 'html.parser')
    text_element = soup_element.select_one("div.textoInterior")
    title = text_element.find('h3').get_text()
    content = text_element.find_all('p')
    details = ''.join([p.get_text().strip() for p in content])
    
    return {"title": title, "details": details}

class AlertListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="List of Alerts",
        tags=['Alert']
    )
    def list(self, request, *args, **kwargs):
        return Response(getAlerts())


 

class AlertDetailsView(APIView):
    # Obtén el valor de los parámetros de consulta
    @swagger_auto_schema(
    operation_summary="Retrieving an Alerts",
    tags=['Alert'],
    manual_parameters=[
        openapi.Parameter(
            name='link',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description='URL of the alert'
        )
    ]
    )
    def get(self, request, *args, **kwargs):
        link = request.query_params.get('link', None)
        
        if link is None:
            return Response({"error": "No se proporcionó ningún valor para 'link'"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Lógica para procesar el valor y generar una respuesta
        alert_details = getAlert(link)
        
        return Response(alert_details, status=status.HTTP_200_OK)