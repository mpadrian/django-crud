import os
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

# Lista para almacenar los posts temporalmente
posts = []

def home(request):
    return render(request, 'home.html')

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

def post_list(request):
    global posts
    return render(request, 'post.html', {'posts': posts})