# Generated by Django 5.1.3 on 2024-11-09 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='surname',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
