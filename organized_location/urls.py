from django.urls import path
from .views import UploadCSVView, OrganizedLocationListView

urlpatterns = [
    path('upload-csv/', UploadCSVView.as_view(), name='upload-csv'),
    path('locations/', OrganizedLocationListView.as_view(), name='location-list'),
]
