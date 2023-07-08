from django.contrib import admin
from django.urls import path
from pages import views
from django.conf.urls import handler404

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("service/", views.class11, name="service"),
    path("contact/", views.class12, name="contact"),
    path("shop/", views.result, name="shop"),
]
handler404 = 'pages.views.error_404'