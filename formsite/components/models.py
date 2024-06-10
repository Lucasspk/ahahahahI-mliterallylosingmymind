from django.db import models
from django.urls import reverse


# Create your models here.
class Component(models.Model):
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length='300', default='null', null=True, blank=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    fps1080 = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    fps1440 = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    fps4k = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    AvgPower = models.IntegerField(default=0)
    itemDescription = models.CharField(max_length=4000000)
    point_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.00)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('component_detail', kwargs={'component_type': self.__class__.__name__.lower(), 'pk': self.pk})
    
    def raw_gaming_performance(self):
        return (self.fps1080 + self.fps1440 + self.fps4k) / 3
class GPU(Component):
    avgTemp = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    memory_size = models.IntegerField(default=0)
    core_clock = models.IntegerField(default=0)
class CPU(Component):
    cores = models.IntegerField()
    clock_speed = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    threads = models.IntegerField(default=0)
    avgTemp = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    socket = models.CharField(max_length=80)
class PSU(Component):
    wattage = models.IntegerField(default=0)
    modular = models.CharField(max_length=200)
    efficiency_rating = models.CharField(max_length=280)
    pstier = models.CharField(max_length=200)
class Motherboard(Component):
    formFactor = models.CharField(max_length=20)