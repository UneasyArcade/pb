# Generated by Django 4.2.10 on 2024-02-22 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phoneboo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, verbose_name='Phone')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='phoneboo.persone')),
            ],
        ),
    ]