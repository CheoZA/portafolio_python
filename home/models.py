from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50, null=False, primary_key=True)
    apellido = models.CharField(max_length=50, null=False)
    fecha_de_nacimiento = models.DateField(null=False)
    imagen = models.ImageField(upload_to='static/upload/profile_image/')
    def save(self, *args, **kwargs):
        if len(Persona.objects.all()) == 0:
            return super(Persona, self).save(*args, **kwargs)

class Proyecto(models.Model):
    proyecto_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=600, blank=True)
    link_en_vivo = models.URLField(max_length = 200, blank=True )
    link_en_codigo = models.URLField(max_length = 200, blank=True)
    
    def __str__(self) -> str:
        return self.titulo

class ProyectoImagen(models.Model):
    proyecto_imagen_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=250, blank=True)
    imagen = models.ImageField(upload_to='static/upload/images/')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="proyectoImagen")
    def __str__(self) -> str:
        return self.titulo