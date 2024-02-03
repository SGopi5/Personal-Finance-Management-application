# Generated by Django 5.0 on 2024-02-01 19:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=140)),
                ('Date_of_Expence', models.DateField()),
                ('Description', models.TextField()),
                ('Amount', models.PositiveIntegerField()),
                ('Category', models.CharField(choices=[('health', 'Health'), ('electronics', 'Electronics'), ('travel', 'Travel'), ('education', 'Education'), ('books', 'Books'), ('others', 'Others')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
