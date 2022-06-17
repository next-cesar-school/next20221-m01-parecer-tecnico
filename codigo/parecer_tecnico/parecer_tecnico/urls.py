"""parecer_tecnico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),

    # somente pra exemplo
    path("api/exemplos/", views.ExemploAPI.as_view(), name="exemplos"),
    path("api/exemplos/<int:exemplo_id>", views.ExemploAPI.as_view(), name="exemplos_com_parametro"),
    
    path("api/clientes/", views.ClienteAPI.as_view(), name="clientes"),
    path("api/clientes/<int:cliente_id>", views.ClienteAPI.as_view(), name="clientes_com_parametro"),
    
    path("api/equipamentos/", views.EquipamentoAPI.as_view(), name="equipamentos"),
    path("api/equipamentos/<int:equipamentos_id>", views.EquipamentoAPI.as_view(), name="equipamentos_com_parametro"),
    
    path("api/parecerdotecnicos/", views.ParecerDoTecnicoAPI.as_view(), name="parecerdotecnicos"),
    path("api/parecerdotecnicos/<int:parecerdotecnicos_id>", views.ParecerDoTecnicoAPI.as_view(), name="eparecerdotecnicos_com_parametro"),
    
]
