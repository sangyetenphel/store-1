# Generated by Django 3.2.3 on 2021-06-05 21:50

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name_plural': 'Images'},
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='review',
            name='subject',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(blank=True),
        ),
    ]