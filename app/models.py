from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descuento = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete= models.PROTECT)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="productos", null=True)
    
    def __str__(self):
        return self.nombre    
    
class ImagenProduct0(models.Model):
    imagen = models.ImageField(upload_to="productos")
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE, related_name="imagenes")   
   
 
opciones_consultas = [
    [0,"consulta"],
    [1,"reclamo"],
    [2,"sugerencia"],
    [3,"felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()
    
    def __str__(self):
        return self.nombre
