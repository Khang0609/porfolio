# Generated by Django 5.0.7 on 2024-08-23 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Infor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('residence', models.CharField(max_length=200)),
                ('school', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('facebook', models.URLField()),
                ('logo', models.CharField(max_length=20)),
                ('call_description', models.TextField()),
                ('hobby1', models.CharField(max_length=250)),
                ('hobby1_description', models.TextField()),
                ('hobby2', models.CharField(max_length=250)),
                ('hobby2_description', models.TextField()),
                ('hobby3', models.CharField(max_length=250)),
                ('hobby3_description', models.TextField()),
                ('work1', models.CharField(max_length=250)),
                ('work1_description', models.TextField()),
                ('work2', models.CharField(max_length=250)),
                ('work2_description', models.TextField()),
                ('work3', models.CharField(max_length=250)),
                ('work3_description', models.TextField()),
                ('work1_img', models.ImageField(upload_to='images/')),
                ('work2_img', models.ImageField(upload_to='images/')),
                ('work3_img', models.ImageField(upload_to='images/')),
                ('about_description', models.TextField()),  
            ],
        ),
    ]   