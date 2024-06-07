import re
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

def get_Alerts_Gob():
    base_url_gob="https://www.mapa.gob.es/es/agricultura/temas/sanidad-vegetal/organismos-nocivos/plagas-prioritarias/"
    response = requests.get(base_url_gob)
    soup = BeautifulSoup(response.content, 'html.parser')
    alerts = []
    container = soup.find('div', class_='col-md-9').find('div', class_='anclas-enlaces')
    divs_alert = container.find_all('div', class_='panel')
    for div in divs_alert:
        h3 = div.find('h3')
        title = h3.get_text(strip=True) if h3 else 'No title'
        panel_body = div.find('div', class_='panel-body')
        if panel_body:
            image_div = panel_body.find('div', class_='panel-imagen-izq')
            image_url = "https://www.mapa.gob.es"+image_div.find('img')['src'] if image_div and image_div.find('img') else 'No image'

            info_div = panel_body.find('div', class_='panel-info')
            info_paragraphs = info_div.find_all('p') if info_div else []
            
            info_dict = {}
            for p in info_paragraphs:
                text = p.get_text(strip=True)
                if ':' in text:
                    category, content = text.split(':', 1)
                    info_dict[category.strip()] = content.strip()
                else:
                    info_dict['Other'] = text.strip()
            alerts.append({"title":title,"image":image_url,"info":info_dict})

        else:
            image_url = 'No image'
            info_text = 'No data'
            alerts.append({"title":title,"image":image_url,"info":info_text})
        
    return alerts
        

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
    '''
    title = text_element.find('h3').get_text().replace("\n", " ")
    title_element = text_element.find('h3')
    title_element.decompose()
    
    content = text_element.get_text(separator="\n").strip()
    
    def replace_newlines_except_lists(match):
        text = match.group(0)
        if '<li>' in text or '</ul>' in text:
            return text
        return text.replace('\n', ' ')
    
    html_content = str(text_element)
    details = re.sub(r'(<[^>]+>|\n)', replace_newlines_except_lists, html_content)

    details_soup = BeautifulSoup(details, 'html.parser')
    details_text = details_soup.get_text(separator="\n").strip()
    '''
        
    return {"details": text_element.get_text()}

class AlertListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="List of Alerts",
        tags=['Alert']
    )
    def list(self, request, *args, **kwargs):
        return Response(getAlerts())

class AlertListViewGob(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="List of Alerts for Goberment",
        tags=['Alert']
    )
    def list(self, request, *args, **kwargs):
        return Response(get_Alerts_Gob())
 

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