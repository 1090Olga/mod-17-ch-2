from django.shortcuts import render
from django.http import HttpResponse
from models import Categories

# Create your views here.o0
def index(request):

    categories: Categories.object.all()

    context: dict[str, str] = {
        'title': 'ECOSIST- Главная',
        'content': 'ОЗЕЛЕНЕНИЕ БЕЗ УХОДА',
        'categories': categories
    }
    return render(request, "ECO/index.html", context)


def about(request):
    context: dict[str, str] = {
        'title': 'ECOSIST - О нас',
        'content': 'О нас',
        'text_on_page':
                        'Мы предлагаем широкий спектр услуг по озеленению помещений, которые не требуют ухода. '
                        'Наши специалисты используют только высококачественные материалы и современные технологии, '
                        'чтобы создать долговечные и эстетически привлекательные композиции.'
                        'Преимущества нашего искусственного озеленения:экологичность и безопасность для здоровья;'
                        'устойчивость к воздействию влаги, света и температуры;'
                        'долговечность и сохранение первоначального вида на протяжении нескольких лет;'
                        'возможность создания уникальных дизайнерских решений;экономия времени и средств на уходе за растениями.'
                        'Наши клиенты получают индивидуальный подход, профессиональные консультации и гарантию качества выполненных работ.'
                        'Мы всегда рады предложить вам лучшие решения для вашего интерьера и сделать его более уютным и привлекательным.'

    }
    return render(request, "ECO/about.html", context)

def contact(request):
    context = {
        'title': "Контактная информация",
        'content': "Контакты",
        'text_on_page': 'адрес: Погодина 45,г.Ростов-на-Дону, '
                        'тел.: 8918-876-54-32',
    }

    return render(request, 'ECO/contact.html', context)