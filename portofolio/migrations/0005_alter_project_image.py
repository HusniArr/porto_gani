# Generated by Django 5.0.3 on 2024-03-15 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0004_alter_project_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
