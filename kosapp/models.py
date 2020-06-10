from django.db import models

class Client(models.Model):
	date_creat = models.DateField(auto_now_add=True)
	claimant = models.CharField(max_length=200)
	date_of_birth = models.DateField()
	defendant = models.CharField(max_length=200)	
	email = models.EmailField(max_length=200)
	email_password = models.CharField(max_length=200)
	date_of_inspection = models.DateField()



