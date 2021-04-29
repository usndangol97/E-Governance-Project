from django.urls import path
from . import views

app_name="core2_app"

urlpatterns = [
    path("create/",views.CvCreate, name='create'),
    path('render/pdf2/',views.Pdf.as_view(),name='pdf'),
]