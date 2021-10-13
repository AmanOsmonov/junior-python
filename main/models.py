from django.db import models

class UserRequest(models.Model):
    link=models.URLField(max_length=200)

class UserRequestRezult(models.Model):

    post = models.ForeignKey(UserRequest, on_delete=models.CASCADE)
    titile= models.CharField(max_length=100, verbose_name='названиме Pull Request')
    links=models.URLField(max_length=200)
    # Ceate your models here.
