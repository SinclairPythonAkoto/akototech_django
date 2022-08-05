from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# landing page (first page)
def landing_page(request):
    return HttpResponse("Hello World")


# main home page
def homepage(request):
    return HttpResponse("Welcome to the Homepage.")


# about page
def about_page(request):
    return HttpResponse("About page - brief description of my passion and my goals")


# AT tuition page
def akototech_tuition(request):
    return HttpResponse(
        "Akoto Tech Tuition - classes available for anyone who wants to learn!"
    )


# projects page (EASYChef, Miri model, digital cv, dj fire)
def akototech_projects(request):
    return HttpResponse(
        "Browse through some projects - EASY Chef, Miri the model, DJ Fyre"
    )


# reference page (modenised cv with download)
def references(request):
    return HttpResponse(
        "References Page - insights from previous work and CV available to download!"
    )


# contact me page
def contact_me(request):
    return HttpResponse(
        "Contact Me Page - users can send me an email to get in contact."
    )
