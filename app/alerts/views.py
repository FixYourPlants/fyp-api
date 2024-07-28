# Create your views.py here.
import requests
from bs4 import BeautifulSoup
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from app.alerts.swagger import alert_details_swagger, list_alerts_government_swagger, list_alerts_swagger

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


class AlertListViewGov(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = (AllowAny,)
    pagination_class = None

    @list_alerts_government_swagger()
    def list(self, request, *args, **kwargs):
        return Response(get_alerts_gob())

