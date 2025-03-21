# Generated by Django 5.1.6 on 2025-03-01 11:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_user_rating_user_ratinganswer_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.ImageField(default=1, help_text='Фото которое будет отабражаться на обложке объявлении', upload_to='media/main_covers', verbose_name='Главное фото'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ratinganswer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
