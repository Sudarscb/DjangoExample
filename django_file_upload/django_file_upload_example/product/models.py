from django.db import models

# Create your models here.
class FileUpload(models.Model):
    title = models.CharField(max_length=100)
    doc_file = models.FileField(upload_to="documents/")
    image_file = models.ImageField(upload_to="images/")


