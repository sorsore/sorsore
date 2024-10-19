from .models import TemplateSettings

class ThemeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        theme = TemplateSettings.objects.first()
        request.theme = theme
        response = self.get_response(request)
        return response