
from django.contrib import admin
from django.urls import path
from women.views import WomenApiView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/women_list/', WomenApiView.as_view())
]
