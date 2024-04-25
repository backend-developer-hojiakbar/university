from django.db import models

# Create your models here.


class Feedback(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='feedback/', null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Faculties(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Payment(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Sertificate(models.Model):
    img = models.ImageField(upload_to='img/', default='', null=True, blank=True)


class University(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    facultities = models.ForeignKey(Faculties, on_delete=models.CASCADE)
    sertificate = models.ForeignKey(Sertificate, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

