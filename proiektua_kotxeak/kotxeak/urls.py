from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('gehituBezeroa/', views.gehituBezeroa, name='gehituBezeroa'),
    path('gehituBezeroa/gehitutaBezeroa/', views.gehitutaBezeroa, name='gehitutaBezeroa'),
    path('gehituKotxea/', views.gehituKotxea, name='gehituKotxea'),
    path('gehituKotxea/gehitutaKotxea/', views.gehitutaKotxea, name='gehitutaKotxea'),
    path('ezabatuBezeroa/<int:id>', views.ezabatuBezeroa, name='ezabatuBezeroa'),
    path('alokatu/<int:id>', views.alokatu, name='alokatu'),
    path('alokatu/alokatuKotxea/', views.alokatuKotxea, name='alokatuKotxea'),
]