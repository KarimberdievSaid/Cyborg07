from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import DateTimeField


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Image(models.Model):
    file = models.ImageField(
        upload_to='media/product_file',
        verbose_name='Файл'
    )
    def __str__(self):
        return str(self.file)

    class Meta:
        verbose_name = 'Изображение продукта'
        verbose_name_plural = 'Изображения продуктов'


# TODO: Сделать связь на таблицу User
class Product(models.Model):
    # user = models.ForeignKey()
    title = models.CharField(
        max_length=123,
        verbose_name="Название"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name = 'Катогория'
    )
    images = models.ManyToManyField(
        Image,
        verbose_name='Изображения'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активен'
    )

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

# TODO: Сделать связь на таблицу User
class Rating(models.Model):
    # user = models.ForeignKey()
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    count = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(15)
        ],
        verbose_name='Оценка'
    )
    comment = models.TextField(
        max_length=200,
        verbose_name='Комментарий'
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    # def __str__(self):
    #     return str(sel)
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

# TODO: Сделать связь на таблицу User
class RatingAnswer(models.Model):
    # user = models.ForeignKey()
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name= 'Отзыв'
    )
    comment = models.TextField(
        max_length=500,
        verbose_name='Комментарий'
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения'
    )
    time_limit = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Ограничения по времени'
    )
    class Meta:
        verbose_name = 'Ответ на отзыв'
        verbose_name_plural = 'Ответы на отзывы'

# # TODO: Сделать связь на таблицу User
# class Order(models.Model):
#     # user = models.ForeignKey()
#     product = models.ForeignKey(
#         Product,
#         on_delete=models.CASCADE,
#         verbose_name='Заказ'
#     )
#     created_date = models.DateTimeField(
#         auto_now_add=True,
#         verbose_name='Дата заказа'
#     )
#     is_paid = models.BooleanField(
#         default=True,
#         verbose_name='Оплачен'
#     )
#     quantity = models.PositiveIntegerField(
#         validators=[
#             MinValueValidator(1),
#             MaxValueValidator(15)
#         ],
#         verbose_name='Цена'
#     )
#     check = models.DecimalField(
#         max_digits=10,
#         decimal_places=2,
#         verbose_name='Проверка'
#     )
#
#     class Meta:
#         verbose_name = 'Заказ'
#         verbose_name_plural = 'Заказы'
