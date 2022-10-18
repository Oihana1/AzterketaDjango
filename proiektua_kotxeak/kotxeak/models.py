from django.db import models

# Create your models here.
class Bezeroa(models.Model):
    id=models.AutoField(primary_key=True)
    izena=models.CharField(max_length=50)
    abizena=models.CharField(max_length=50)
    zb=models.CharField(max_length=9)
class KotxeaSortzekoModeloa(models.Model):
    id=models.AutoField(primary_key=True)
    matrikula=models.CharField(max_length=8)
    marka=models.CharField(max_length=100)
class Kotxea(models.Model):
    id=models.AutoField(primary_key=True)
    kotxea =  models.ForeignKey(KotxeaSortzekoModeloa, on_delete=models.CASCADE,null=True)
    bezeroa =  models.ForeignKey(Bezeroa, on_delete=models.CASCADE)
    alokatuHasiera=models.CharField(max_length=10,null=True)
    alokatuAmaiera=models.CharField(max_length=10,null=True)

    
    
    
    
    

