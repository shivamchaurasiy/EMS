# Generated by Django 4.1.6 on 2023-08-13 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_enquiry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminSingUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('confirm_password', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='AdminDataBase',
        ),
    ]
