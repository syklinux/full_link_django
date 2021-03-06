# Generated by Django 2.1.7 on 2019-03-11 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('full_test', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='api',
            options={'verbose_name': 'api接口', 'verbose_name_plural': 'api接口'},
        ),
        migrations.AlterModelOptions(
            name='history',
            options={'verbose_name': '历史数据', 'verbose_name_plural': '历史数据'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': '应用', 'verbose_name_plural': '应用'},
        ),
        migrations.AlterField(
            model_name='history',
            name='rt',
            field=models.FloatField(verbose_name='rt值'),
        ),
    ]
