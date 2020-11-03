from django.shortcuts import render
from . models import Comic
from django.views import generic 


def index(request):
     
    return render(
        request,
        'index.html',
        
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


class ComicCreate(CreateView):
    model  = Comic
    fields = '__all__'
    initil ={'' : '25/12/2020'}

class ComicUpdate(UpdateView):
    model = Comic
    field = ['nombre_comic',
            'cod_comic',
            'precio',
            'editorial',
            'autor',
            'cantidad',
            'ingreso_fecha']

class ComicDelete(DelateView):
    model = Comic
    sucess_url = reverse_lazy('index')

class GenreDetailView(generic.DetailView):
    model = Comic

class GenreListView(generic.ListView):
    model = comic
    template_name = 'templates/catalogo/comic_list.html'
    queryset = comic.objects.all()

    paginate_by = 10

def genre_new(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('genre-detail', pk=post.pk)
    else:
        form = GenreForm()
        return render(request, 'peliculas/comic_form.html', {'form': form})

def comic_new(request):
    if request.method == "POST":
        form = ComicForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('comic-detail', pk=post.pk)
    else:
        form = ComicForm()
        return render(request, 'catalogo/comic_form.html', {'form': form})

