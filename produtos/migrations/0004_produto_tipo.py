# Generated by Django 4.1.6 on 2023-02-15 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_produto_excluido'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('P', 'Produto'), ('S', 'Servico')], default='P', max_length=2),
        ),
    ]