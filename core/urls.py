from django.urls import path
from . import views

app_name="core_app"

urlpatterns = [
    path('', views.index, name='home'),
    path('license-registration/', views.FormView, name="License_Registration"),
    path('result/',views.FormData,name='result'),
    path('render/pdf/', views.Pdf.as_view(), name='resultPdf'),
]