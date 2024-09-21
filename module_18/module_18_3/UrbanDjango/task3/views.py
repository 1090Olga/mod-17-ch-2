from urllib import request

from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def func_template(request):
    return render(request, 'func_template.html')

def platform(request):
    return render(request, "platform.html")

def games(request):
    page_name = "Игры"
    game_1 = "Atomic Heart"
    game_2 = "Cyberpunk 2077"
    game_3 = "PayDay 2"
    buy = "Купить"
    context = {
        'Title': page_name,
        'game_1': game_1,
        'game_2': game_2,
        'game_3': game_3,
        'buy': buy,
    }
    return render(request, 'games.html', context)

def cart(request):
    page_name = "Корзина"
    img = "/static/Корзина.jpg"
    text_1 = "Ваша"
    text_2 = "корзина"
    text_3 = "ПУСТА!"
    context = {
        'Title': page_name,
        'img': img,
        'text_1': text_1,
        'text_2': text_2,
        'text_3': text_3,
    }
    return render(request, 'cart.html', context)

class ClassTemplate(TemplateView):
    template_name = "class_template.html"
# Create your views here.
