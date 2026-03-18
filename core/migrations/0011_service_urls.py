from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_add_phone2_phone3'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='service1_url',
            field=models.CharField(blank=True, max_length=200, verbose_name='Usługa 1 – link'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='service2_url',
            field=models.CharField(blank=True, max_length=200, verbose_name='Usługa 2 – link'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='service3_url',
            field=models.CharField(blank=True, max_length=200, verbose_name='Usługa 3 – link'),
        ),
    ]
