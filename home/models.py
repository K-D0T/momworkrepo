from django.db import models


class SubmitModel(models.Model):
	id=models.AutoField(primary_key=True)
	author=models.CharField(max_length=100, null=True)
	pic=models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=100, null=True)
	objects=models.Manager()