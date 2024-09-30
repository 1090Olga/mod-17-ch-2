from django.shortcuts import render

# Create your views here.
def catalog(request):
    context = {
        'title': "Home - Каталог"
        'goods'[
            {
                'image': 'deps/images/goods/tree1.jpg',
                'name': 'Дерево h 30 cm',
                'description': 'Дерево из стабилизированного мха высотой около 30 см, в комплекте кашпо ручной работы.',
                'price': 3500.00
            },
       ]
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    return render(request, 'goods/product.html')
