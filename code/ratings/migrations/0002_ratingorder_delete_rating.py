# Generated by Django 5.0.3 on 2024-04-21 16:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0008_remove_order_order_taken_remove_order_order_taken_at'),
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial', models.TextField(blank=True, null=True, verbose_name='Отзыв')),
                ('order_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_rating', to='freelance.orderrequest')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
