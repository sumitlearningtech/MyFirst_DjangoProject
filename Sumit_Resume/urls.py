from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("resume/", include("Personal_Information.urls")),
    path("admin/", admin.site.urls),
]