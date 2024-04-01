from django.db import models

# Create your models here.
class University(models.Model):
    BY_CARD = "CARD"
    BY_CASH = "CASH"
    PAYMENT_STATUS_CHOICES = [
        (BY_CARD, 'CARD'),
        (BY_CASH, 'CASH'),
    ]
    name = models.CharField(max_length=100)
    bio = models.TextField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    payment = models.CharField(
        max_length=50, choices=PAYMENT_STATUS_CHOICES, default=BY_CASH)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='feedback/', null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Faculties(models.Model):
    university_id = models.ForeignKey(University, on_delete=models.CASCADE, related_name='faculties')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Sertificate(models.Model):
    university_id = models.ForeignKey(University, on_delete=models.CASCADE, related_name='sertificate')
    img = models.ImageField(upload_to='img/', default='', null=True, blank=True)

    def __str__(self):
        return str(self.university_id)

