# Create your views here.
import requests
from bs4 import BeautifulSoup
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

'''
ALERTS
'''
# Constants
BASE_URL = "https://plagas.itacyl.es/alertas"
BASE_URL_GOB = "https://www.mapa.gob.es/es/agricultura/temas/sanidad-vegetal/organismos-nocivos/plagas-prioritarias/"

# Helper functions
def fetch_and_parse(url):
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses
    return BeautifulSoup(response.content, 'html.parser')

def extract_info_paragraphs(info_div):
    paragraphs = info_div.find_all('p') if info_div else []
    info_dict = {}
    for p in paragraphs:
        text = p.get_text(strip=True)
        if ':' in text:
            category, content = text.split(':', 1)
            info_dict[category.strip()] = content.strip()
        else:
            info_dict['Other'] = text.strip()
    return info_dict

def get_alerts_gob():
    soup = fetch_and_parse(BASE_URL_GOB)
    alerts = []
    container = soup.find('div', class_='col-md-9').find('div', class_='anclas-enlaces')
    divs_alert = container.find_all('div', class_='panel')

    for div in divs_alert:
        title = div.find('h3').get_text(strip=True) if div.find('h3') else 'No title'
        panel_body = div.find('div', class_='panel-body')

        if panel_body:
            image_div = panel_body.find('div', class_='panel-imagen-izq')
            image_url = f"https://www.mapa.gob.es{image_div.find('img')['src']}" if image_div and image_div.find('img') else 'No image'
            info_div = panel_body.find('div', class_='panel-info')
            info_dict = extract_info_paragraphs(info_div)
            alerts.append({"title": title, "image": image_url, "family": info_dict["Familia"], "distribution": info_dict["Distribución"], "host": info_dict["Hospedantes"], "damage": info_dict["Daños"]})
        else:
            alerts.append({"title": title, "image": 'No image', "family": 'No family', "distribution": 'No distribution', "host": 'No host', "damage": 'No damage'})

    return alerts

def get_alerts():
    soup = fetch_and_parse(BASE_URL)
    alerts = []
    alerts_divs = soup.select("div.textoInterior div.row.bb-10")

    for alert in alerts_divs:
        title_element = alert.select_one("p")
        link_element = alert.select_one("a")

        if title_element and link_element:
            title = title_element.get_text(strip=True)
            link = link_element['href']
            alerts.append({"title": title, "link": link})

    return alerts

def getAlert(url):
    soup_element = fetch_and_parse(url)
    text_element = soup_element.select_one("div.textoInterior")
    return {"details": text_element.get_text(strip=True)}

# Views
class AlertListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="List of Alerts",
        tags=['Alert']
    )
    def list(self, request, *args, **kwargs):
        return Response(get_alerts())

class AlertListViewGob(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="List of Alerts for Government",
        tags=['Alert']
    )
    def list(self, request, *args, **kwargs):
        return Response(get_alerts_gob())

class AlertDetailsView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_summary="Retrieving an Alert",
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
        link = request.query_params.get('link')

        if not link:
            return Response({"error": "No se proporcionó ningún valor para 'link'"}, status=status.HTTP_400_BAD_REQUEST)

        alert_details = getAlert(link)

        return Response(alert_details, status=status.HTTP_200_OK)
