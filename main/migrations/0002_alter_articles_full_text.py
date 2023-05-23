# Generated by Django 4.2.1 on 2023-05-23 13:13
from django.core.validators import MinLengthValidator
from django.db import migrations, models

def validate_min_length(apps, schema_editor):
    Articles = apps.get_model('main', 'Articles')
    for article in Articles.objects.all():
        if len(article.full_text) < 100:
            raise ValueError('Минимальное количество символов - 100.')

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(validate_min_length),
        migrations.AlterField(
            model_name='articles',
            name='full_text',
            field=models.TextField(verbose_name='Статья'),
        ),
    ]
