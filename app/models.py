from django.db import models

# Create your models here.


class bankaccount(models.Model):
	create_at = models.DateTimeField(auto_now_add=True)	
	account_no = models.CharField(max_length = 20)
	owner_name = models.CharField(max_length = 15)
	owner_lastname = models.CharField(max_length = 25)
	email = models.CharField(max_length = 20)
	accountType=models.CharField(max_length = 15)
	securitycode = models.CharField(max_length = 10)
	balance = models.CharField(max_length = 100)

	def __str__(self):
			return(f"{self.account_no}{self.owner_name}{self.owner_lastname}")
