from django.db import models

# Create your models here.
class CreateUpdateDate(models.Model):

	Create_at=models.DateTimeField(auto_now_add=True)

	update_at=models.DateTimeField(auto_now=True)

	"""creation d'une classe d'abstraction"""

	class Meta(object):
		abstract=True
			

class Post(CreateUpdateDate):

	title=models.CharField(max_length=200)
	
	body=models.TextField()
	

	def __str__(self):
		return self.title


		