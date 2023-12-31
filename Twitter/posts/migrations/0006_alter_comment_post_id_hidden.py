# Generated by Django 4.2.5 on 2023-09-23 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_id_hidden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_detail', to='posts.post'),
        ),
    ]
