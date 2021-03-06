"""
    AUTHOR:         luis mora
    CREATION DATE:  09/06/2021
    DESCRIPTION:    Modelo de la tabla cliente del esquema public

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        DATE    ||  MODIFIED_BY ||  DESCRIPTION
    --------------------------------------------------------
                ||              ||  
                ||              ||  
"""

from django.db import models

class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    contraceña = models.CharField(max_length=40)
    direccion = models.CharField(max_length=80, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'

    def __str__(self):
        return (self.Nombre,)