from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_sitesettings_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='favicon',
            field=models.ImageField(
                blank=True, null=True,
                upload_to='favicon/',
                verbose_name='Favicon',
                help_text='Ikona zakładki przeglądarki. Zalecany rozmiar: 32×32 lub 64×64 px (PNG/ICO).',
            ),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='meta_description',
            field=models.CharField(
                blank=True, max_length=300,
                verbose_name='Meta description (strona główna)',
                help_text='Opis strony widoczny w wynikach wyszukiwarki. Maks. 160 znaków.',
            ),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='og_image',
            field=models.ImageField(
                blank=True, null=True,
                upload_to='og/',
                verbose_name='OG Image (udostępnianie)',
                help_text='Grafika widoczna przy udostępnianiu strony w social media. Zalecany rozmiar: 1200×630 px.',
            ),
        ),
    ]
