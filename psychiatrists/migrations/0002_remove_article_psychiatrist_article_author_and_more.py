# Generated by Django 4.1.7 on 2023-05-03 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_client_user'),
        ('psychiatrists', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='Psychiatrist',
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='psychiatrists.psychiatrist'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prescription',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='psychiatrist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='psychiatrists.psychiatrist'),
        ),
    ]
