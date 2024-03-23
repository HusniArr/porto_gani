from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from mimetypes import guess_type

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    
class Project(models.Model):
    project_name = models.CharField(max_length=300)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(null=True,blank=True)

class Gallery(models.Model):
    gallery_name = models.CharField(max_length=200)
    file = models.FileField(upload_to="gallery",null=True, verbose_name="")

    def file_type(self):
        type_tuple = guess_type(self.file.url, strict=True)
        if(type_tuple[0]).__contains__("image"):
            return "image"
        elif(type_tuple[0]).__contains__("video"):
            return "video"
    

    