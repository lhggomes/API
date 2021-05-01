
from django.contrib import admin
from django.urls import path
from escola.views import students

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students', students),
]
