from django.urls import path
from akototech_home import views

urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("home/", views.homepage, name="homepage"),
    path("about/", views.about_page, name="about_page"),
    path("tuition/", views.akototech_tuition, name="akototech_tuition"),
    path("projects/", views.akototech_projects, name="akototech_projects"),
    path("ref/", views.references, name="references"),
    path("contact/", views.contact_me, name="contact_me"),
]
