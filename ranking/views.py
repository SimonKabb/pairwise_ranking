from django.shortcuts import render
from django.shortcuts import redirect
from .models import Image
from django.shortcuts import render, redirect
from .models import Image, ComparisonResult
from .forms import ImageForm
from django.core.files.storage import FileSystemStorage
from django.utils.text import slugify
import os
from itertools import combinations
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


def upload_image(request):
    form = ImageForm()  # Создаем экземпляр формы за пределами условия
    if request.method == 'POST':
        image = request.FILES.get('image')
        if image:
            # Получаем имя файла без расширения и его расширение
            filename, ext = os.path.splitext(image.name)
            # Обрезаем имя файла до 100 символов и преобразуем его в slug
            new_filename = slugify(filename[:90]) + ext
            image.name = new_filename
            if len(new_filename) > 100:
                # Если новое имя файла больше 100 символов, возвращаем ошибку
                print('Filename too long. Maximum length is 100 characters.')
            else:
                form = ImageForm(request.POST, request.FILES)
                if form.is_valid():
                    # Применяем новое имя файла к изображению
                    image.name = new_filename
                    form.save()
                    return redirect('compare_images')
                else:
                    print('Form is not valid. Errors:', form.errors)
        else:
            print('No image file uploaded')
    return render(request, 'index.html', {'form': form})


def compare_images(request):
    # Получаем список всех изображений
    images = Image.objects.all()
    for image in images:
        print(image.image.url)
    return render(request, 'compare_images.html', {'images': images})


def sort_image(Image):
    images = Image.objects.all()
    pairs = list(combinations(images, 2))
    return pairs
