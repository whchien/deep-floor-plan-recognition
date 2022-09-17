from django.urls import path

from api.views import ImageUploadView, ResultsView, CsvView, IndexView

urlpatterns = [
    # Homepage
    path('', IndexView.as_view()),

    # POST
    # Input: list of floor-plan images
    # Returns: 200
    path('images/upload', ImageUploadView.as_view(), name='image-list'),

    # GET
    # Returns: processed images
    path('images/process', ResultsView.as_view()),

    # GET
    # Returns: CSV file
    path('images/results', CsvView.as_view())
]
