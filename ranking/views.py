from django.shortcuts import render
from django.shortcuts import redirect
from .models import Image
from django.shortcuts import render, redirect
from .models import Image, ComparisonResult
from .forms import MultipleImageForm
from django.core.files.storage import FileSystemStorage
from django.utils.text import slugify
import os
from itertools import combinations
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import random


def upload_image(request):
    form = MultipleImageForm()  # Создаем экземпляр формы за пределами условия
    if request.method == 'POST':
        form = MultipleImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('compare_images')
        else:
            print('Form is not valid. Errors:', form.errors)
    return render(request, 'index.html', {'form': form})


def compare_images(request):
    images = Image.objects.all()
    img1_index = request.session.get('img1_index', 0)
    img2_index = request.session.get('img2_index', 1)
    print('indexs', img1_index, img2_index)
    try:
        img1 = images[img1_index]
        img2 = images[img2_index]
    except IndexError:
        print('Error')
        winner = img1
        request.session.flush()
        return render(request, 'winner.html', {'winner': winner})

    if request.method == 'POST':
        # Обработка формы выбора победителя
        winner_id = int(request.POST.get('winner_id'))
        if img1_index == winner_id - 1:
            request.session['img1_index'] = img1_index
            request.session['img2_index'] = img2_index + 1
        elif img2_index == winner_id - 1:
            request.session['img1_index'] = img2_index
            request.session['img2_index'] = img2_index + 1
        else:
            print('finita')
            winner = img1
            request.session.flush()
            return render(request, 'winner.html', {'winner': winner})
        return redirect('compare_images')
    return render(request, 'compare_images.html',
                  {'image1': img1, 'image2': img2})
