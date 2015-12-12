from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	autore=models.ForeignKey('auth.User')
	titolo=models.CharField(max_length=200)
	testo=models.TextField()
	data_creazione=models.DateTimeField(default=timezone.now)
	data_pubblicazione=models.DateTimeField(blank=True, null=True)

	def pubblica(self):
		self.data_pubblicazione=timezone.now()
		self.save()

	def __str__(self):
		return self.titolo


