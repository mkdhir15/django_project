import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render


def home(request):
    if request.method != "GET":
        return JsonResponse(
            {"error": "Only GET method is allowed"},
            status=405
        )

    return HttpResponse("Welcome to My Django Backend!")


def about(request):
    if request.method != "GET":
        return JsonResponse(
            {"error": "Only GET method is allowed"},
            status=405
        )

    return HttpResponse("This is the About endpoint.")


def users(request):
    if request.method != "GET":
        return JsonResponse(
            {"error": "Only GET method is allowed"},
            status=405
        )

    data = {
        "users": ["Harshit", "Gitesh", "Mohit"]
    }

    return JsonResponse(data)


def products(request):
    if request.method != "GET":
        return JsonResponse(
            {"error": "Only GET method is allowed"},
            status=405
        )

    data = {
        "products": ["Laptop", "Mouse", "Keyboard"]
    }

    return JsonResponse(data)


def contact(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST method is allowed"},
            status=405
        )

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON"},
            status=400
        )

    name = data.get("name")
    message = data.get("message")

    if not name or not message:
        return JsonResponse(
            {"error": "name and message are required"},
            status=400
        )

    return JsonResponse(
        {
            "message": "Contact submitted successfully",
            "name": name,
            "content": message
        },
        status=201
    )


def go_about(request):
    if request.method != "GET":
        return JsonResponse(
            {"error": "Only GET method is allowed"},
            status=405
        )

    return redirect("about")


def page(request):
    if request.method != "GET":
        return JsonResponse(
            {"error": "Only GET method is allowed"},
            status=405
        )

    return render(request, "api/home.html")