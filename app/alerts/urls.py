from rest_framework.routers import SimpleRouter

from app.alerts.views import AlertListViewGov

router = SimpleRouter()
'''
ALERT
'''
router.register(r'alerts/list/gob', AlertListViewGov, basename="alert-list-gob")
