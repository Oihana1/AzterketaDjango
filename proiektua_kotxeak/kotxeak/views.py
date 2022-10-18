
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Bezeroa, Kotxea, KotxeaSortzekoModeloa

# Create your views here.def index(request):

def index(request):
    bezeroa=Bezeroa.objects.all
    kotxea=KotxeaSortzekoModeloa.objects.all
    return render(request,'index.html', {'bezeroa': bezeroa, 'kotxea':kotxea})
def gehituBezeroa(request):
    return render(request,'gehituBezeroa.html')
def gehitutaBezeroa(request):
    izena = request.POST['izena']
    abizena = request.POST['abizena']
    zb= request.POST['zb']
    bezeroa = Bezeroa(izena=izena, abizena=abizena, zb=zb)
    bezeroa.save()
    return HttpResponseRedirect(reverse('index'))
def gehituKotxea(request):
     return render(request,'gehituKotxea.html')
def gehitutaKotxea(request):
    matrikula = request.POST['matrikula']
    marka = request.POST['marka']
    kotxea = KotxeaSortzekoModeloa(matrikula=matrikula, marka=marka)
    kotxea.save()
    return HttpResponseRedirect(reverse('index'))
def ezabatuBezeroa(request,id):
    bezeroa = Bezeroa.objects.get(id=id)
    bezeroa.delete()
    return HttpResponseRedirect(reverse('index'))

def alokatu(request,id):
    kotxea=KotxeaSortzekoModeloa.objects.all
    bezeroa=Bezeroa.objects.all
    return render(request,'alokatuKotxea.html',{'kotxea': kotxea, 'bezeroa': bezeroa})

def alokatuKotxea(request):
    kotxea=request.POST['kotxea']
    bezeroa = request.POST['bezeroa']
    alokatuHasiera=request.POST['alokatuHasiera']
    alokatuAmaiera=request.POST['alokatuAmaiera']
    #Ekarri kotxe guztiak for baten bidez kotxearen id berdina bada id hori gorde eta gero kotxe objetua sortu eta alokatu objetuan gorde
    #Ekarri kotxe guztiak for baten bidez kotxearen id berdina bada id hori gorde eta gero kotxe objetua sortu eta bezeroan berdina objetuan gorde
    alokatu = Kotxea(kotxea=kotxea, bezeroa=bezeroa, alokatuHasiera=alokatuHasiera,alokatuAmaiera=alokatuAmaiera)
    alokatu.save()
    return HttpResponseRedirect(reverse('index'))




    



 
    
    