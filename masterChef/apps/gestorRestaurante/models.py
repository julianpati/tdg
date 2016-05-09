from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.core.validators import MaxLengthValidator


# Create your models here.
class usuario(models.Model):
    TIPOS_DE_USUARIO = (
        ('R','Root'),
        ('C','Chef'),
        ('M','Mesero'),
    )

    TIPOS_DE_DOCUMENTO = (
        ('C.C','Cedula de ciudadania'),
        ('T.I','Tarjeta de identidad'),
    )

    TIPOS_GENERO = (
        ('M','Masculino'),
        ('F','Femenino'),
    )
    user = models.OneToOneField(User)
    tipoUsuario = models.CharField(max_length=10, choices=TIPOS_DE_USUARIO)
    genero=models.CharField(max_length=10, choices=TIPOS_GENERO)
    tipoDocumento = models.CharField(max_length=20, choices= TIPOS_DE_DOCUMENTO)
    documento=models.CharField(max_length=20)
    direccion=models.CharField(max_length=50)
    telefono=models.BigIntegerField()
    fechaDeNacimiento = models.DateField()

    def __unicode__(self):
              return self.user.first_name

class userForm(ModelForm):
    class Meta:
        model = User
        fields = ('password', 'username','first_name','last_name','email')

class perfilForm(ModelForm):
    class Meta:
        model = usuario
        fields = ('user','genero','tipoDocumento','documento','direccion','telefono','fechaDeNacimiento')

class formularioEditarCuenta(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class formularioEditarPerfil(ModelForm):
    class Meta:
        model = usuario
        fields = ('tipoDocumento','documento','direccion','telefono','fechaDeNacimiento')


class inventario(models.Model):
    TIPOS_DE_MEDIDA = (
        ('gr','gramo'),
        ('ml','mililitro'),
        ('un','unidad'),
        ('po','porcion'),
    )
    idIngrediente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=40)
    unidadMedida = models.CharField(max_length=20, choices= TIPOS_DE_MEDIDA)
    cantidadDisponible = models.FloatField()
    precioUnitario = models.PositiveIntegerField()
    cantidadMinima = models.IntegerField()
    alerta = models.BooleanField()

    def __unicode__(self):
              return self.nombre

class formularioEditarInventario(ModelForm):
    class Meta:
        model = inventario
        fields = ('nombre', 'descripcion','unidadMedida', 'cantidadDisponible','precioUnitario', 'cantidadMinima')


class plato(models.Model):
    TIPOS_PLATO =(
        ('PR', 'primario'),
        ('SE', 'secundario'),
        ('JU','jugo'),
        ('SO', 'soda'),
    )
    idPlato = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20, choices=TIPOS_PLATO)
    receta = models.TextField(validators=[MaxLengthValidator(300)])
    precio = models.PositiveIntegerField(blank=True, null=True)

    def __unicode__(self):
              return self.nombre



class formularioNuevoPlato(ModelForm):
    class Meta:
        model = plato
        fields = ('nombre', 'receta', 'precio')

class ingrediente(models.Model):
    plato = models.CharField(max_length=20)
    ingrediente = models.CharField(max_length=20)
    cantidad = models.FloatField()
    def __unicode__(self):
              return self.ingrediente

class menu(models.Model):
    id = models.AutoField(primary_key=True)
    precio = models.PositiveIntegerField()
    estado = models.BooleanField()
    def __unicode__(self):
              return str(self.id)


class menu_platos(models.Model):
    menu = models.IntegerField()
    plato = models.CharField(max_length=20)
    tipoPlato = models.CharField(max_length=20)
    def __unicode__(self):
              return str(self.menu)


class orden(models.Model):
    ESTADOS =(
        ('FA', 'facturada'),
        ('NF','sin_facturar'),
    )

    idOrden = models.AutoField(primary_key=True)
    mesa = models.PositiveIntegerField()
    mesero = models.CharField(max_length=30)
    estado = models.CharField(max_length=20, choices=ESTADOS)

    def __unicode__(self):
              return str(self.idOrden)

class descripcion_orden(models.Model):
    id = models.AutoField(primary_key=True)
    idOrden = models.PositiveIntegerField()
    idPlato = models.CharField(max_length=20)
    cantidad = models.PositiveIntegerField()

    def __unicode__(self):
              return str(self.idOrden)



