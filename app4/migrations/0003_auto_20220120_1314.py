# Generated by Django 3.0.8 on 2022-01-20 10:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0002_remove_friend_ad'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='friend',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='friend',
            name='date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now, verbose_name='Время создания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='friend',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app4.Rubric', verbose_name='Рубрика'),
        ),
    ]
