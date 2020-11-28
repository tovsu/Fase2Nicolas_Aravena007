from django.test import TestCase
from comic.models import nombre_comic, codigo_comic, precio, editorial, autor, cantidad, ingreso_fechas

class GenreModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Comic.objects.create(name='Accion', summary='Prueba')
    
    def test_name_label(self):
        Comic=Comic.objects.get(id=1)
        field_label = Comic._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_summary_label(self):
        Comic=Comic.objects.get(id=1)
        field_label = Comic._meta.get_field('summary').verbose_name
        self.assertEquals(field_label,'summary')
    
    def test_name_max_length(self):
        Comic=Comic.objects.get(id=1)
        max_length = Comic._meta.get_field('name').max_length
        self.assertEquals(max_length,100)
    
    def test_summary_max_length(self):
        Comic=Comic.objects.get(id=1)
        max_length = Comic._meta.get_field('summary').max_length
        self.assertEquals(max_length,1000)
        
    def test_get_absolute_url(self):
        Comic=Comic.objects.get(id=1)
        self.assertEquals(Comic.get_absolute_url(), '/catalogos/comic/1')

