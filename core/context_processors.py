from .models import Page


def footer_pages(request):
    return {
        'footer_pages': Page.objects.filter(is_active=True, show_in_footer=True),
    }
