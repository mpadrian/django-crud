import os
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Publicacion
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import PublicacionForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView

# Lista para almacenar los posts temporalmente
posts = []

def home(request):
    posts = Publicacion.objects.all()  # Obtener todos los posts
    return render(request, 'home.html', {'posts': posts})

def upload_image(request):
    global posts
    image_url = None
    if request.method == 'POST':
        # Manejar eliminación de imagen
        if 'delete_image' in request.POST:
            image_path = request.POST.get('image_path')
            if image_path and os.path.exists(image_path.replace('/static/', 'static/')):
                os.remove(image_path.replace('/static/', 'static/'))  # Eliminar imagen del servidor
            return redirect('upload_image')  # Redirigir a la misma página después de eliminar

        # Manejar subida de imagen
        elif 'image' in request.FILES:
            title = request.POST.get('title')  # Obtener el título del formulario
            content = request.POST.get('content')  # Obtener el contenido del formulario
            image = request.FILES['image']

            # Guardar la imagen en la carpeta 'static/upload_image'
            fs = FileSystemStorage(location='static/upload_image')
            filename = fs.save(image.name, image)
            image_url = fs.url(filename)

            # Agregar el post a la lista de posts
            posts.append({
                'title': title,
                'content': content,
                'image_url': image_url
            })

            # Renderizar la página con la imagen subida
            return render(request, 'post_create.html', {
                'image_url': image_url,
                'title': title,
                'content': content
            })

    # Si no es POST, simplemente renderizar la página
    return render(request, 'post_create.html', {'image_url': image_url})

class PostListView(ListView):
    model = Publicacion
    template_name ='post.html'
    context_object_name = 'posts' 

class PostUpdate(UpdateView):
    model = Publicacion
    fields = ['titulo', 'descripcion', 'imagen']
    template_name = 'post_update.html'
    succces_url = reverse_lazy('post_list')

class PostDetail(DetailView):
    model = Publicacion
    template_name = 'post_detail.html'  # Nombre de la plantilla que se usará
    context_object_name = 'post' 