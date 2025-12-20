from django.shortcuts import render, redirect
from .models import SportsCategory, City, Area, SportsEvent
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def home(request):
    events = SportsEvent.objects.all()
    return render(request, "index.html", {"events": events})


def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if email exists
        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username   # Django still needs username to authenticate
        except User.DoesNotExist:
            return render(request, "login.html", {"error": "Email not found"})

        # Authenticate using username + password
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Incorrect password"})

    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("home")


def add_event(request):
    categories = SportsCategory.objects.all()
    cities = City.objects.all()
    areas = Area.objects.all()

    if request.method == "POST":
        SportsEvent.objects.create(
            category_id=request.POST["category"],
            title=request.POST["title"],
            description=request.POST["description"],
            date=request.POST["date"],
            time=request.POST["time"],
            city_id=request.POST["city"],
            area_id=request.POST["area"],
            created_by=request.user
        )
        return redirect("home")

    return render(request, "add_event.html", {
        "categories": categories,
        "cities": cities,
        "areas": areas,
    })


def delete_event(request, id):
    event = SportsEvent.objects.get(id=id)
    event.delete()
    return redirect("home")

