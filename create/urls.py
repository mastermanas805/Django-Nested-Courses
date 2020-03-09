from django.urls import path
from .views import Create_Course_View,upload_image


urlpatterns = [
    path('add/',Create_Course_View.as_view(),name = 'add'),
    path('upload/',upload_image.as_view(),name = 'upload'),
]
