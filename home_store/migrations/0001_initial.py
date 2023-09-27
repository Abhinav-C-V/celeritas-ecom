# Generated by Django 4.2.2 on 2023-07-12 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('image', models.ImageField(default=None, upload_to='image_space/banner')),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_firstname', models.CharField(default='', max_length=50)),
                ('user_lastname', models.CharField(default='', max_length=50)),
                ('user_email', models.CharField(max_length=50, unique=True)),
                ('user_phone', models.CharField(max_length=50, null=True)),
                ('user_password', models.CharField(max_length=128)),
                ('user_cpassword', models.CharField(max_length=128)),
                ('user_is_active', models.BooleanField(default=True)),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='image_space/')),
            ],
        ),
    ]