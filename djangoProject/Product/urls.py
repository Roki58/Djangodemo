from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name = "home"),
    path("product/",views.ProductView.as_view(),name="product")
]