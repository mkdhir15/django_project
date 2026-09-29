from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("users/", views.users, name="users"),
    path("products/", views.products, name="products"),
    path("contact/", views.contact, name="contact"),
    path("go-about/", views.go_about, name="go_about"),
    path("page/", views.page, name="page"),
]