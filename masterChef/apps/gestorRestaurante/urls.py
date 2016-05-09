"""masterChef URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin



admin.autodiscover()

from django.contrib.auth.views import login

urlpatterns = patterns('',
                       url(r'^$' , 'django.contrib.auth.views.login',{'template_name':'inicio.html'}, name='login'),
                       url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
                       url(r'^principal/$', 'masterChef.apps.gestorRestaurante.views.principal', name='principal'),

                       url(r'^gestion_cuentas/$', 'masterChef.apps.gestorRestaurante.views.gestion_cuentas', name='gestion_cuentas'),
                       url(r'^gestion_menus/$', 'masterChef.apps.gestorRestaurante.views.gestion_menus', name='gestion_menus'),
                       url(r'^nuevo_mesero/$', 'masterChef.apps.gestorRestaurante.views.nuevo_mesero', name='nuevo_mesero'),
                       url(r'^crear_perfil/$', 'masterChef.apps.gestorRestaurante.views.crear_perfil', name='crear_perfil'),
                       url(r'^gestion_cuentas/consultar_cuentas/$', 'masterChef.apps.gestorRestaurante.views.consultar_cuentas', name='consultar_cuentas'),
                       url(r'^gestion_cuentas/consultar_cuentas/(?P<id_user>.*)/$', 'masterChef.apps.gestorRestaurante.views.ver_cuenta', name='ver_cuenta'),
                       url(r'^gestion_cuentas/editar_cuentas/$', 'masterChef.apps.gestorRestaurante.views.editar_cuentas', name='editar_cuentas'),
                       url(r'^gestion_cuentas/editar_cuentas/(?P<id_user>.*)/$', 'masterChef.apps.gestorRestaurante.views.editar_cuenta', name='editar_cuenta'),
                       url(r'^gestion_cuentas/borrar_mesero/$', 'masterChef.apps.gestorRestaurante.views.borrar_mesero', name='borrar_mesero'),
                       url(r'^gestion_cuentas/borrar_mesero/(?P<id_user>.*)/$', 'masterChef.apps.gestorRestaurante.views.borrar_cuenta', name='borrar_cuenta'),

                       url(r'^inventario/$', 'masterChef.apps.gestorRestaurante.views.bodega', name='inventario'),
                       url(r'^inventario/buscar/$', 'masterChef.apps.gestorRestaurante.views.buscar', name='buscar'),
                       url(r'^inventario/buscar/editar/(?P<id_elemento>.*)/$', 'masterChef.apps.gestorRestaurante.views.editar_inventario', name='editar_inventario'),
                       url(r'^gestion_menus/crear_menu/$', 'masterChef.apps.gestorRestaurante.views.crear_menu', name='crear_menu'),
                       url(r'^gestion_menus/eliminar_menu/$', 'masterChef.apps.gestorRestaurante.views.eliminar_menu', name='eliminar_menu'),
                       url(r'^gestion_menus/establecer_menu_dia/$', 'masterChef.apps.gestorRestaurante.views.establecer_menu_dia', name='establecer_menu_dia'),

                       url(r'^tomar_orden/$', 'masterChef.apps.gestorRestaurante.views.tomar_orden', name='tomar_orden'),
                       url(r'^tomar_orden/crear_orden/(?P<mesa>.*)/$', 'masterChef.apps.gestorRestaurante.views.crear_orden', name='crear_orden'),
                       url(r'^seleccionar_plato/$', 'masterChef.apps.gestorRestaurante.views.seleccionar_plato', name='seleccionar_plato'),
                       url(r'^seleccionar_plato/preparar_plato/(?P<plato>.*)/$', 'masterChef.apps.gestorRestaurante.views.preparar_plato', name='preparar_plato'),
                       url(r'^anadir_platos/$', 'masterChef.apps.gestorRestaurante.views.anadir_platos', name='anadir_platos'),
                       url(r'^anadir_platos/mas/(?P<idOrden>.*)/$', 'masterChef.apps.gestorRestaurante.views.mas', name='mas'),
                       url(r'^menu_dia/$', 'masterChef.apps.gestorRestaurante.views.menu_dia', name='menu_dia'),
                       url(r'^ordenes_en_cola/$', 'masterChef.apps.gestorRestaurante.views.ordenes_en_cola', name='ordenes_en_cola'),
                       url(r'^ordenes_en_cola/(?P<idOrden>.*)/$', 'masterChef.apps.gestorRestaurante.views.detalle_orden', name='detalle_orden'),
                       url(r'^facturar/(?P<Orden>.*)/$', 'masterChef.apps.gestorRestaurante.views.facturar', name='facturar'),
                       )




