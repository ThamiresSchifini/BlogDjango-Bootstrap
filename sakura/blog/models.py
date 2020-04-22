from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    resume = RichTextField()
    content = RichTextUploadingField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT)       #não deixa deletar se tiver usuário
    created_at = models.DateField(auto_now_add=True)        #quando adc o post gera a data

    def __str__(self):                              # transformar uma string
        return self.title