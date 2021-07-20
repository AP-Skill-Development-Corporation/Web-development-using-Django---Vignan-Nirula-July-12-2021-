from django.db import models

# Create your models here.
class library(models.Model):
	branches = (
		("IT","it"),
		("CSE","cse"),
		("ECE","ece"),
		("CE","ce"),
		("MECH","mech")
		)

	book_no = models.IntegerField(unique = True)
	book_name = models.CharField(max_length=50)
	author = models.CharField(max_length=30)
	department = models.CharField(max_length = 15, choices=branches)
	published_in = models.DateField(null=True,blank=True,help_text = "format(yyyy-mm-dd)")


	def __str__(self):
		return self.book_name