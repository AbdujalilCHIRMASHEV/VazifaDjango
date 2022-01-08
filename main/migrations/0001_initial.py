# Generated by Django 3.2.9 on 2022-01-07 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yonalish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ismi', models.CharField(max_length=255)),
                ('yoshi', models.IntegerField()),
                ('rasmi', models.ImageField(upload_to='Rasmlar/')),
                ('yonalish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.yonalish')),
            ],
        ),
    ]
