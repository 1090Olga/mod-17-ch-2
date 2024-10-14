from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=500, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=1000, unique=True, blank=True,null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    descrfiptions = models.TextField(blank=True,null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=12, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('id',)

    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'


    # Метод который формирует id из 5 символов

    def display_id(self):
        return f'{self.id:05}'

    # Метод проверяющий есть ли скидка и возвращает нужную стоимость
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 0)

        return self.price