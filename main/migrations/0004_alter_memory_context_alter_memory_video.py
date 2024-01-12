# Generated by Django 5.0 on 2024-01-11 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_memory_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='context',
            field=models.CharField(blank=True, choices=[('M', 'Maryama'), ('A', 'Arya'), ('T', 'Together'), ('F', 'Family')], default='T', max_length=2),
        ),
        migrations.AlterField(
            model_name='memory',
            name='video',
            field=models.FileField(blank=True, default=None, upload_to='videos/'),
        ),
    ]
