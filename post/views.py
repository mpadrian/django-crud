from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import os

def home(request):
    return render(request, 'post_create.html')

def upload_image(request):
    image_url = None
    if request.method == 'POST':
        # Manejar subida de imagen
        if 'image' in request.FILES:
            image = request.FILES['image']
            fs = FileSystemStorage(location='static/upload_image')
            filename = fs.save(image.name, image)
            image_url = fs.url(filename)

        if 'delete_image' in request.POST:
            image_path = request.POST.get('image_path')
            if image_path and os.path.exists(image_path.replace('/static/', 'static/')):
                os.remove(image_path.replace('/static/', 'static/'))
            return redirect('upload_image')

    return render(request, 'post_create.html', {'image_url': image_url})