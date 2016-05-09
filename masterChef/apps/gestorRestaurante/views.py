from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from models import userForm, perfilForm, usuario, User, formularioEditarCuenta, inventario, formularioEditarInventario
from models import menu, menu_platos, plato, orden, descripcion_orden, ingrediente



# Create your views here.

def principal(request):
    user = request.user.usuario
    if user.tipoUsuario == 'C':
        inv = inventario.objects.filter(alerta=True)
        return render(request, "paginaChef.html", {'inv':inv})
    else:
        if user.tipoUsuario =='M': return render(request,"paginaMesero.html",{})





def gestion_cuentas(request):
    user = request.user.usuario
    if user.tipoUsuario =='C':
        return render(request,"gestionCuentas.html",{})



def nuevo_mesero(request):
    u = request.user.usuario

    if request.method == 'POST':
        form = userForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect('/crear_perfil/')
    else:
        form = userForm() # Unbound form

    return render(request,"nuevoMesero.html",{'form' : form})


def crear_perfil(request):
    u = request.user.usuario
    if request.method == 'POST':
        form = perfilForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            new_user.tipoUsuario='M'
            new_user.save()
            return HttpResponseRedirect('/gestion_cuentas/')
    else:
        form = perfilForm() # Unbound form
    return render(request,"crearPerfil.html",{'form' : form})

def consultar_cuentas(request):
    u = request.user.usuario
    cuentas= usuario.objects.filter(tipoUsuario  = 'M')
    return render(request,'consultar_cuentas.html', {'cuentas': cuentas})


def ver_cuenta(request,id_user):
    u = request.user.usuario
    cuenta= usuario.objects.get(user__username=id_user)
    return render(request,'ver_cuenta.html', {'cuenta': cuenta})



def editar_cuentas(request):
    u = request.user.usuario
    cuentas= usuario.objects.filter(tipoUsuario  = 'M')
    return render(request,'editarCuentas.html', {'cuentas': cuentas})


def editar_cuenta(request,id_user):
    u = request.user.usuario

    c= User.objects.get(username=id_user)
    if request.method == 'POST':
        form = formularioEditarCuenta(request.POST, request.FILES)
        if form.is_valid():
            Nombre = form.cleaned_data['first_name']
            Apellidos = form.cleaned_data['last_name']
            Email = form.cleaned_data['email']
            c.first_name = Nombre
            c.last_name = Apellidos
            c.email = Email
            c.save()
            datos = {'cuenta': c}
            return HttpResponseRedirect('/principal/')

    if request.method == 'GET':
        form = formularioEditarCuenta(initial={
                            'Nombre': c.first_name,
                            'Apellidos': c.last_name,
                            'Email': c.email,
        }, instance= c)

    ctx = {
        'form': form,
        'cuenta': c
    }
    return render_to_response('editarCuenta.html', ctx, context_instance=RequestContext(request))

def borrar_mesero(request):
    u = request.user.usuario
    cuentas= usuario.objects.filter(tipoUsuario  = 'M')
    return render(request,'borrarMesero.html', {'cuentas': cuentas})

def borrar_cuenta(request,id_user):
    u = request.user.usuario
    c= User.objects.get(username=id_user)

    if request.method == 'POST':
        form = formularioEditarCuenta(request.POST, request.FILES)
        if form.is_valid():
            Nombre = form.cleaned_data['first_name']
            Apellidos = form.cleaned_data['last_name']
            Email = form.cleaned_data['email']
            c.first_name = Nombre
            c.last_name = Apellidos
            c.email = Email
            c.delete()
            datos = {'cuenta': c}
            return  HttpResponseRedirect('/principal/')
    if request.method == 'GET':
        form = formularioEditarCuenta(initial={
                            'Nombre': c.first_name,
                            'Apellidos': c.last_name,
                            'Email': c.email,
        }, instance= c)

    ctx = {
        'form': form,
        'cuenta': c
    }
    return render_to_response('borrarCuenta.html', ctx, context_instance=RequestContext(request))


def bodega(request):
    user = request.user.usuario
    return render(request,"inventario.html",{})


def buscar(request):
    u = request.user.usuario
    query = request.GET.get('q', '')
    inv = inventario.objects.all()
    if query:
        qset = (
            Q(nombre__icontains=query) |
            Q(alerta__icontains=query)
        )
        results = inventario.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response('consultar.html', {"results": results,"query": query,"inv":inv}, context_instance=RequestContext(request))


def editar_inventario(request,id_elemento):
    u = request.user.usuario

    c= inventario.objects.get(idIngrediente=id_elemento)
    if request.method == 'POST':
        form = formularioEditarInventario(request.POST, request.FILES)
        if form.is_valid():
            Nombre = form.cleaned_data['nombre']
            Descripcion = form.cleaned_data['descripcion']
            uMedida = form.cleaned_data['unidadMedida']
            cDisponible = form.cleaned_data['cantidadDisponible']
            pUnitario = form.cleaned_data['precioUnitario']
            cMin = form.cleaned_data['cantidadMinima']
            c.nombre = Nombre
            c.descripcion = Descripcion
            c.unidadMedida = uMedida
            c.cantidadDisponible = cDisponible
            c.precioUnitario = pUnitario
            c.cantidadMinima = cMin
            c.save()
            datos = {'elemento': c}
            return HttpResponseRedirect('/inventario/buscar/')

    if request.method == 'GET':
        form = formularioEditarInventario(initial={
                            'Nombre': c.nombre,
                            'Descripcion': c.descripcion,
                            'Unidad de medida': c.unidadMedida,
                            'Cantidad disponible': c.cantidadDisponible,
                            'Precio x unidad' : c.precioUnitario,
                            'Cantidad minima para generar alerta': c.cantidadMinima,
        }, instance= c)

    ctx = {
        'form': form,
        'elemento': c
    }
    return render_to_response('editarInventario.html', ctx, context_instance=RequestContext(request))



def gestion_menus(request):
    user = request.user.usuario
    if user.tipoUsuario =='C':
        return render(request,"gestionMenus.html",{})

def crear_menu(request):
    platos = plato.objects.all()
    if request.method == 'POST':
        listaPlatos = request.POST.getlist('plato[]')
        if len(listaPlatos) == 0:
            return render(request,"crearMenu.html",{'platos' : platos})

        nuevoMenu = menu()
        nuevoMenu.precio = request.POST['precio']
        nuevoMenu.estado = False
        nuevoMenu.save()
        i=0
        while i<len(listaPlatos):
            aux = plato.objects.get(nombre=listaPlatos[i])
            a = menu_platos()
            a.plato = listaPlatos[i]
            a.menu = nuevoMenu.id
            a.tipoPlato = aux.tipo
            a.save()
            i+=1
        return HttpResponseRedirect('/gestion_menus/')

    return render(request,"crearMenu.html",{'platos' : platos})


def tomar_orden(request):
    return render(request,"mesas.html",{})

def crear_orden(request, mesa):
    menuDia = menu.objects.get(estado = True)
    datosMenu = menu_platos.objects.filter(menu = menuDia.id)
    user = request.user
    if request.method == 'POST':
        datosOrden = request.POST.getlist('cantidad[]')
        numeroMenus = len(menu.objects.all())
        nuevaOrden = orden()
        nuevaOrden.mesa = mesa
        nuevaOrden.mesero = user.first_name
        nuevaOrden.estado = 'NF'
        nuevaOrden.save()

        i=0;
        while i<len(datosMenu):
            if datosOrden[i] != '':
                a = descripcion_orden()
                a.idOrden = nuevaOrden.idOrden
                a.idPlato = datosMenu[i].plato
                a.cantidad = datosOrden[i]
                a.save()
            i+=1
        return HttpResponseRedirect('/principal/')

    return render(request,"crearOrden.html",{'datosMenu': datosMenu, 'mesa': mesa})


def eliminar_menu(request):
    menus = menu.objects.filter(estado=False)

    if request.method == 'POST':
        men = request.POST.get('menu')
        a = menu.objects.get(id=men)
        a.delete()
        aux = menu_platos.objects.filter(menu=men)
        aux.delete()

        return HttpResponseRedirect('/principal/')

    return render(request, "eliminarMenu.html", {'menus': menus})


def establecer_menu_dia(request):

    if request.method == 'POST':
        actual_menu_dia = menu.objects.get(estado=True)
        actual_menu_dia.estado = False
        actual_menu_dia.save()

        men = request.POST.get('menu')
        nuevo_menu_dia = menu.objects.get(id=men)
        nuevo_menu_dia.estado = True
        nuevo_menu_dia.save()

        return HttpResponseRedirect('/gestion_menus/')
    menus = menu.objects.filter(estado=False)

    return render(request, "establecerMenuDia.html", {'menus': menus})


def seleccionar_plato(request):
    menuDia = menu.objects.get(estado=True)
    datosMenu = menu_platos.objects.filter(menu=menuDia.id)

    return render(request, "seleccionarPlato.html", {'datosMenu': datosMenu})


def preparar_plato(request, plato):
    ingredientes = ingrediente.objects.filter(plato=plato)
    validador = []
    excede = []
    if request.method == 'POST':
        class ingredientePlato:
            def __init__(self, ingrediente, cantidad, uMedida):
                self.ingrediente = ingrediente
                self.cantidad = cantidad
                self.uMedida = uMedida
        cantidad = request.POST.get('cantidad')
        receta = []
        i = 0

        while i < len(ingredientes):
            w = inventario.objects.get(nombre=ingredientes[i].ingrediente)
            aux = ingredientes[i].cantidad
            c = aux * float(cantidad)

            if w.cantidadDisponible-c < 0:
                excede.append(1)
                break
            i += 1

        if i == len(ingredientes):
            r = 0
            while r < len(ingredientes):
                a = inventario.objects.get(nombre=ingredientes[r].ingrediente)
                unidadMedida = a.unidadMedida
                aux = ingredientes[r].cantidad
                c = aux * float(cantidad)
                if a.nombre == "agua":
                    a.save()
                    t = ingredientePlato(ingredientes[r].ingrediente, c, unidadMedida)
                    receta.append(t)
                else:
                    a.cantidadDisponible -= c
                    a.save()
                    t = ingredientePlato(ingredientes[r].ingrediente, c, unidadMedida)
                    receta.append(t)
                r += 1
        validador.append(1)
        return render(request,"prepararPlato.html", {'validador': validador,  'receta': receta, 'excede': excede})

    else:
        return render(request,"prepararPlato.html",{'plato': plato, 'validador': validador})


def anadir_platos(request):
    ordenes = orden.objects.filter(estado='NF')
    return render(request, "anadirPlatos.html", {'ordenes': ordenes})


def mas(request, idOrden):
    menuDia = menu.objects.get(estado=True)
    datosMenu = menu_platos.objects.filter(menu=menuDia.id)
    if request.method == 'POST':
        datosOrden = request.POST.getlist('cantidad[]')
        i=0;
        while i<len(datosMenu):
            if datosOrden[i] != '':
                a = descripcion_orden()
                a.idOrden = idOrden
                a.idPlato = datosMenu[i].plato
                a.cantidad = datosOrden[i]
                a.save()
            i+=1
        return HttpResponseRedirect('/principal/')

    return render(request,"mas.html",{'datosMenu': datosMenu, 'idOrden': idOrden})


def menu_dia(request):
    menuDia = menu.objects.get(estado=True)
    datosMenu = menu_platos.objects.filter(menu=menuDia.id)

    return render(request,"menuDia.html",{'datosMenu': datosMenu})

def ordenes_en_cola(request):
    colaOrdenes = orden.objects.filter(estado="NF")

    return render(request,"ordenesEnCola.html",{'ordenes': colaOrdenes})

def detalle_orden(request, idOrden):
    ord = orden.objects.get(idOrden=idOrden)
    detalle = descripcion_orden.objects.filter(idOrden=idOrden)

    return render(request,"detalleOrden.html",{'orden': ord, 'detalle': detalle})

def facturar(request, Orden):
    ord = orden.objects.get(idOrden=Orden)
    ord.estado = 'FA'
    ord.save()
    detalle = descripcion_orden.objects.filter(idOrden=Orden)
    lista = []

    class factura:
            def __init__(self, plato, precioUnitario, cantidad, subtotal):
                self.plato = plato
                self.precioUnitario = precioUnitario
                self.cantidad = cantidad
                self.subtotal = subtotal

    i = 0
    total = 0
    while (i<len(detalle)):
        precioUnitario = plato.objects.get(nombre=detalle[i].idPlato)
        subtotal = precioUnitario.precio * detalle[i].cantidad
        f = factura(detalle[i].idPlato, precioUnitario.precio, detalle[i].cantidad, subtotal)
        total = total + subtotal
        lista.append(f)
        i += 1

    return render(request, "facturar.html", {'orden': ord, 'detalle': lista, 'total': total})






