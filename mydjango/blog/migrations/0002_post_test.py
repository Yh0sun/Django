# Generated by Django 3.1.13 on 2022-02-11 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='test',
            field=models.TextField(default='테스트'),
            preserve_default=False,
        ),
    ]
