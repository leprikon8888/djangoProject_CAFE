from  django.urls import path
from .views import events,events_year,events_year_month, future_events

app_name = 'events'

urlpatterns = [
    path('', events, name='events'),
    path('future', future_events, name = 'future_events'),
    path('<int:year>', events_year, name='events_year'),
    path('<int:year>/<int:month>', events_year_month, name='events_year_month'),
]