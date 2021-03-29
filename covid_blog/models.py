from django.db import models

# class Author(models.Model):
# 	first_name = models.CharField(max_length=50)
# 	last_name = models.CharField(max_length=50)


class Article(models.Model):
	title = models.CharField(max_length=100)
	details = models.TextField()
	pub_date = models.DateTimeField('date published')
	#author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Image(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='images')

	def __str__(self):
		return self.title