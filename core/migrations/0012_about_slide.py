from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_service_urls'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSlide',
            fields=[
                ('id',           models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag',          models.CharField(default='O nas', max_length=60, verbose_name='Etykieta')),
                ('title',        models.CharField(max_length=200, verbose_name='Tytuł')),
                ('lead',         models.CharField(blank=True, max_length=300, verbose_name='Lead (wyróżniony akapit)')),
                ('body',         models.TextField(blank=True, verbose_name='Treść')),
                ('check_items',  models.JSONField(blank=True, default=list, verbose_name='Lista punktów')),
                ('image',        models.ImageField(blank=True, null=True, upload_to='about/', verbose_name='Zdjęcie')),
                ('stat1_number', models.CharField(blank=True, max_length=20, verbose_name='Statystyka 1 – liczba')),
                ('stat1_label',  models.CharField(blank=True, max_length=60, verbose_name='Statystyka 1 – opis')),
                ('stat2_number', models.CharField(blank=True, max_length=20, verbose_name='Statystyka 2 – liczba')),
                ('stat2_label',  models.CharField(blank=True, max_length=60, verbose_name='Statystyka 2 – opis')),
                ('order',        models.PositiveSmallIntegerField(default=0, verbose_name='Kolejność')),
                ('is_active',    models.BooleanField(default=True, verbose_name='Aktywny')),
            ],
            options={
                'verbose_name':        'Slajd – O nas',
                'verbose_name_plural': 'Slajdy – O nas',
                'ordering':            ['order'],
            },
        ),
    ]
