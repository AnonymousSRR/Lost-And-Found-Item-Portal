# Generated by Django 4.2.3 on 2023-12-04 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='choice1',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='choice2',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='choice3',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='choice4',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='correct_choice',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Choice 1'), (2, 'Choice 2'), (3, 'Choice 3'), (4, 'Choice 4')], default=1),
        ),
        migrations.AddField(
            model_name='item',
            name='verification_question',
            field=models.CharField(default=11, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Verification',
        ),
    ]
