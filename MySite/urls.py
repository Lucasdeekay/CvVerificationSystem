from django.urls import path

from MySite.views import HomeView, ContactView, AboutView, AuthLoginView, LogoutView

app_name = "MySite"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about", AboutView.as_view(), name="about"),
    path("contact", ContactView.as_view(), name="contact"),
    path("login", AuthLoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
]