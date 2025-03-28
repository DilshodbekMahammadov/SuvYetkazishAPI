from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models

class Suv(models.Model):
    brend = models.CharField(max_length=100)
    narx = models.FloatField(validators=[MinValueValidator(0.0)])
    miqdor = models.IntegerField()
    batafsil = models.TextField()

    def __str__(self):
        return self.brend

class Mijoz(models.Model):
    ism = models.CharField(max_length=255)
    tel = models.CharField(max_length=15, blank=True, null=True)
    manzil = models.TextField( blank=True, null=True)
    qarz = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return self.ism

class Administrator(AbstractUser):
    ism = models.CharField(max_length=255)
    yosh = models.SmallIntegerField(null=True, blank=True)
    ish_vaqti = models.CharField(max_length=100, choices=(('8:00-12:30', '8:00-12:30'), ('12:30-18:00', '12:30-18:00')))

    def __str__(self):
        return self.ism

class Haydovchi(models.Model):
    ism = models.CharField(max_length=255)
    tel = models.CharField(max_length=15, blank=True, null=True)
    smena = models.CharField(max_length=100, choices=(('1-smena', '1-smena'), ('2-smena', '2-smena'),))

    def __str__(self):
        return self.ism

class Buyurtma(models.Model):
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    suv = models.ForeignKey(Suv, on_delete=models.CASCADE)
    sana = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)
    miqdor = models.IntegerField()
    umumiy_narx = models.FloatField(validators=[MinValueValidator(0.0)])
    admin = models.ForeignKey(Administrator, on_delete=models.CASCADE)

    def __str__(self):
        return self.mijoz.ism + " " + self.suv.brend
