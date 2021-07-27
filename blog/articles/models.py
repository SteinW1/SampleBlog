from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from main.models import TimeStampMixin

# Create your models here.
class Article(TimeStampMixin):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    visible = [('True', 'False')] #this line needs fixed