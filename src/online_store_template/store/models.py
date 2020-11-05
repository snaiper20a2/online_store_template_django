from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    quantity = models.IntegerField(verbose_name='Количество на складе')
    price = models.IntegerField(verbose_name='Цена')
    title = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Images(models.Model):
    image = models.ImageField(upload_to='uploads/', verbose_name='Изображение')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Customers(models.Model):
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=64)
    data = models.ForeignKey(to='BuyersData', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Авторизованый покупатель'
        verbose_name_plural = 'Авторизованные покупатели'


class BuyersData(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(max_length=70)

    class Meta:
        verbose_name = 'Данные покупателя'
        verbose_name_plural = 'Данные покупателей'


class Orders(models.Model):
    buyer_data = models.ForeignKey(to=BuyersData, on_delete=models.CASCADE, verbose_name='Данные покупателя')
    status = models.CharField(max_length=15, verbose_name='Статус заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductList(models.Model):
    product = models.ForeignKey(to=Products, on_delete=models.SET_NULL, null=True, verbose_name='Товар')
    quantity = models.IntegerField(verbose_name='Количество')
    order = models.ForeignKey(to=Orders, on_delete=models.CASCADE, verbose_name='Заказ')

    class Meta:
        verbose_name = 'Список товаров в заказах'
        verbose_name_plural = 'Списки товаров в заказах'
