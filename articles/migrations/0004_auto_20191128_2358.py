# Generated by Django 2.2.7 on 2019-11-28 15:58

from django.db import migrations, models
import profanity.validators


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20191128_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(validators=[profanity.validators.validate_is_profane]),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255, validators=[profanity.validators.validate_is_profane]),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=140, validators=[profanity.validators.validate_is_profane]),
        ),
    ]
