from django.urls import path
from .views import FileUploadView,FileListView

urlpatterns =[
    path('',FileListView.as_view(), name="product_list"),
    path('upload/', FileUploadView.as_view(), name="product_upload")
]