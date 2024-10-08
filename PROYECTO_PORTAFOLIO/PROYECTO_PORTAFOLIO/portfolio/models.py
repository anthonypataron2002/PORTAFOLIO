from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title
    
class Experiencia(models.Model):
    institucion_del_curso = models.CharField(max_length=100)
    descripcion_curso = models.TextField()
    fecha_curso = models.DateField()
    numero_horas = models.IntegerField()
    image = models.ImageField(upload_to='experiencias/images/', default='portfolio/images/IMG1.jpeg')  # Establece una imagen predeterminada aquí

    def __str__(self):
        return f"{self.institucion_del_curso} - {self.descripcion_curso}"
