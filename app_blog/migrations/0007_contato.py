# Generated by Django 2.1.7 on 2019-05-26 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0006_auto_20190512_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('mensagem', models.TextField(verbose_name='Mensagem')),
            ],
        ),
    ]