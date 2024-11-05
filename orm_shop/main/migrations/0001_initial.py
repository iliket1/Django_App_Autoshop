# Generated by Django 4.2.7 on 2024-11-05 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=20)),
                ('mileage', models.PositiveIntegerField()),
                ('volume', models.DecimalField(decimal_places=1, max_digits=4)),
                ('body_type', models.CharField(choices=[('sedan', 'Седан'), ('hatchback', 'Хэтчбек'), ('SUV', 'Внедорожник'), ('wagon', 'Универсал'), ('minivan', 'Минивэн'), ('pickup', 'Пикап'), ('coupe', 'Купе'), ('cabrio', 'Кабриолет')], max_length=10)),
                ('drive_unit', models.CharField(choices=[('rear', 'Задний'), ('front', 'Передний'), ('full', 'Полный')], max_length=10)),
                ('gearbox', models.CharField(choices=[('manual', 'Механика'), ('automatic', 'Автомат'), ('вариатор', 'CVT'), ('robot', 'Робот')], max_length=10)),
                ('fuel_type', models.CharField(choices=[('gasoline', 'Бензин'), ('diesel', 'Дизель'), ('hybrid', 'Гибрид'), ('electro', 'Электро')], max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='cars/')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.car')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client')),
            ],
        ),
    ]
