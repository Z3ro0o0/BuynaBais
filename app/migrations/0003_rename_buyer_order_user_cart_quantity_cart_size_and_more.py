# Generated by Django 5.0.2 on 2024-05-19 22:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='buyer',
            new_name='user',
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='size',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ewallet',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
