from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id',          models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name',        models.CharField(max_length=100, verbose_name='Nazwa')),
                ('slug',        models.SlugField(unique=True, verbose_name='Slug')),
                ('description', models.CharField(blank=True, max_length=300, verbose_name='Opis')),
            ],
            options={
                'verbose_name':        'Kategoria bloga',
                'verbose_name_plural': 'Kategorie bloga',
                'ordering':            ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id',   models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Nazwa')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name':        'Tag',
                'verbose_name_plural': 'Tagi',
                'ordering':            ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id',               models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title',            models.CharField(max_length=200, verbose_name='Tytuł')),
                ('slug',             models.SlugField(blank=True, unique=True, verbose_name='Slug (URL)')),
                ('author',           models.CharField(default='Redakcja', max_length=100, verbose_name='Autor')),
                ('status',           models.CharField(choices=[('draft', 'Szkic'), ('published', 'Opublikowany')], default='draft', max_length=10, verbose_name='Status')),
                ('is_featured',      models.BooleanField(default=False, verbose_name='Wyróżniony')),
                ('excerpt',          models.CharField(blank=True, max_length=500, verbose_name='Zajawka')),
                ('content',          models.TextField(verbose_name='Treść (HTML)')),
                ('cover_image',      models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Zdjęcie główne')),
                ('cover_alt',        models.CharField(blank=True, max_length=200, verbose_name='Alt zdjęcia')),
                ('meta_title',       models.CharField(blank=True, max_length=70, verbose_name='Meta title')),
                ('meta_description', models.CharField(blank=True, max_length=160, verbose_name='Meta description')),
                ('og_image',         models.ImageField(blank=True, null=True, upload_to='blog/og/', verbose_name='OG Image (social media)')),
                ('published_at',     models.DateTimeField(blank=True, null=True, verbose_name='Data publikacji')),
                ('created_at',       models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')),
                ('updated_at',       models.DateTimeField(auto_now=True, verbose_name='Zaktualizowano')),
                ('reading_time',     models.PositiveSmallIntegerField(default=1, verbose_name='Czas czytania (min)')),
                ('category',         models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='blog.postcategory', verbose_name='Kategoria')),
                ('tags',             models.ManyToManyField(blank=True, to='blog.tag', verbose_name='Tagi')),
            ],
            options={
                'verbose_name':        'Wpis',
                'verbose_name_plural': 'Wpisy',
                'ordering':            ['-published_at', '-created_at'],
            },
        ),
    ]
