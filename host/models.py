from django.db import models


# Create your models here.


class Bussiness(models.Model):
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32, default='sa')


class Host(models.Model):
    hid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32, db_index=True)
    ip = models.GenericIPAddressField(protocol="both", db_index=True)
    port = models.IntegerField()
    b = models.ForeignKey("Bussiness", to_field="id", related_name='hosts', on_delete=models.CASCADE)


class Application(models.Model):
    name = models.CharField(max_length=32)
    r = models.ManyToManyField("Host", related_name="apps")
