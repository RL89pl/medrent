from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_sitesettings_about_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='logo',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='logo/',
                verbose_name='Logo firmy',
                help_text='Wyświetlane w nagłówku i stopce. Zalecana wysokość: 40–60 px.',
            ),
        ),
    ]
