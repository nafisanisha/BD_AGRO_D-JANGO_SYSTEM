# Generated by Django 3.2.9 on 2021-12-04 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desciptions', models.TextField()),
                ('location', models.TextField(blank=True, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='blog-image')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='blog-image')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='blog-image')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='blog-image')),
                ('add_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('add_on', models.DateField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blogpost')),
            ],
        ),
    ]
