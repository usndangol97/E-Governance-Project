# Generated by Django 3.2 on 2021-04-10 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='', max_length=6)),
                ('birthdate', models.DateField()),
                ('birthplace', models.CharField(default='', max_length=50)),
                ('father', models.CharField(default='', max_length=50)),
                ('mother', models.CharField(default='', max_length=50)),
                ('birthplace_f', models.CharField(default='', max_length=50)),
                ('birthplace_m', models.CharField(default='', max_length=50)),
                ('registration_number', models.IntegerField(default='')),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('issue_date', models.DateField(default='')),
            ],
        ),
    ]
