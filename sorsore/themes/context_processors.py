from .models import TemplateSettings

def theme(request):
    theme = TemplateSettings.objects.first()
    return {'card_context': f'themes/defaults/{theme}/card.html',
            'card_list_context': f'themes/defaults/{theme}/card_list.html',
            'card_page_context': f'themes/defaults/{theme}/card_page.html',
            'carousel_context': f'themes/defaults/{theme}/carousel.html',
            'footer_context': f'themes/defaults/{theme}/footer.html',
            'navbar_context': f'themes/defaults/{theme}/navbar.html',
            'one_paragraph_context': f'themes/defaults/{theme}/one_paragraph.html',}