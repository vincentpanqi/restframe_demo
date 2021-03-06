from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

    def get_full_address(self):
        return "%s %s %s %s" % (self.address, self.city, self.state_province, self.country)


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        unique_together = ("first_name", "last_name")


class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    authors = models.ManyToManyField(Author, related_name="books")
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
