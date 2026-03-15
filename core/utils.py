from PIL import Image


def compress_image(field, max_width=1920, quality=85):
    """Kompresuje obraz ImageField w miejscu. Zachowuje format (JPEG/PNG/WEBP)."""
    if not field:
        return
    try:
        path = field.path
        with Image.open(path) as img:
            fmt = img.format or 'JPEG'
            if fmt not in ('JPEG', 'PNG', 'WEBP'):
                fmt = 'JPEG'
            if fmt == 'JPEG' and img.mode != 'RGB':
                img = img.convert('RGB')
            if img.width > max_width:
                h = int(img.height * max_width / img.width)
                img = img.resize((max_width, h), Image.LANCZOS)
            save_kwargs = {'format': fmt, 'optimize': True}
            if fmt == 'JPEG':
                save_kwargs['quality'] = quality
            elif fmt == 'PNG':
                save_kwargs['compress_level'] = 7
            img.save(path, **save_kwargs)
    except Exception:
        pass
