from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views


urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "user"
