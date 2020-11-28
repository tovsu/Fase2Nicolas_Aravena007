from django.shortcuts import render
from . models import comic
from django.views import generic

# from . models import nombre_comic, codigo_comic, precio, editorial, autor, cantidad, ingreso_fecha


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def index(request):
    num_comic = comic.objects.all().count()  

    return render(
        request,
        'index.html',
        context={'num_comic': num_comic},   
    )

def estante(request):
    
    return render (
        request,
        'estante.html',
    )
    
def compra(request):

    return render (
        request,
        'compra.html',
    )

def vendidos(request):

    return render (
        request,
        'vendidos.html',
    )

class comicCreate(CreateView):
    model  = comic
    fields = '__all__'

class comicUpdate(UpdateView):
    model = comic
    field = ['nombre_comic',
             'codigo_comic',
             'precio',
             'editorial',
             'autor',
             'cantidad',
             'ingreso_fecha']

class comicDelete(DeleteView):
    model = comic
    sucess_url = reverse_lazy('index')
  
class comicDetailView(generic.DetailView):
    model = comic
    
class comicListView(generic.ListView):
    model = comic
    paginate_by = 10

