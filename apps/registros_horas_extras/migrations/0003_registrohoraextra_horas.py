# Generated by Django 4.1.2 on 2022-10-23 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros_horas_extras', '0002_registrohoraextra_funcionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='horas',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
    ]
