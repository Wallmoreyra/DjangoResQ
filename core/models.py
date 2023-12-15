from django.db import models

class Adoptantes(models.Model):
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    DNI = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)

    class Meta:
        db_table = "adoptantes"
        verbose_name = "adoptante"
        verbose_name_plural = "adoptantes"
        ordering = ["lastName", "name"]

    def __str__(self):
        return self.userName