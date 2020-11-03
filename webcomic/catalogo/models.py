from django.db import models
from django.urls import reverse
import uuid 

class Comic(models.Model):
    
	nombre_comic  = models.CharField    (max_length = 120)
	cod_comic     = models.CharField    (max_length = 12)
	precio        = models.CharField    (max_length = 7)
	editorial     = models.CharField    (max_length = 21)
	autor         = models.CharField    (max_length = 120)
	cantidad      = models.IntegerField (default=0)
	ingreso_fecha = models.DateField    (null=True, blank=True)


def _str_(self):
		return self.cod_comic


