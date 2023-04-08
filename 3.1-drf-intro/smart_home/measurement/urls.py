from django.urls import path

from measurement.views import SensorsView, UpdateView, MeasurementsView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', UpdateView.as_view()),
    path('measurements/', MeasurementsView.as_view())

]
