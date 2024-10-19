from django.shortcuts import render, redirect, get_object_or_404
from wagtail.admin.viewsets.model import ModelViewSet

from .models import Index
from .model_theme import TemplateSettings
from .forms import GetTemplatesForm
# from wagtail.images import get_image_model
# from django.core.files import File
# from django.core.files.base import ContentFile
import os

# admin views
class ThemeViewSet(ModelViewSet):
    model = TemplateSettings
    form_fields = ["name"]
    icon = "user"
    add_to_admin_menu = True
    copy_view_enabled = False
    inspect_view_enabled = True

theme_viewset = ThemeViewSet("Theme")


def find(my_dict,string):
    num = 0
    for i in my_dict:
        if string in i:
            num += 1
    return num
# settings of themes
def settings(request):
    template_instance = TemplateSettings.objects.first()
    all_indexes = Index.objects.all()
    queryset = Index.objects.all()

    if request.method == 'POST':
        
        index_name = request.POST.get("indexes")
        template_form = GetTemplatesForm(request.POST)


        if  template_form.is_valid():
            if all_indexes and template_instance.name != 'None':
                active = Index.objects.filter(in_use=True).first()
                if active:
                    active.in_use = False
                    active.save()
                if index_name != 'None':
                    ready_to_active = get_object_or_404(Index, name=index_name)
                    ready_to_active.in_use = True
                    ready_to_active.save()

            data = template_form.cleaned_data
            if template_instance:
                template_instance.name = data["template_name"]
                template_instance.save()
            else:
                if data["template_name"] != 'None':
                    TemplateSettings.objects.create(name=data["template_name"])

            return redirect("/admin")
    else:
        if  template_instance:
            template_form = GetTemplatesForm(initial={'template_name': template_instance.name})
        else:
            template_form = GetTemplatesForm(initial={'template_name': 'None'})

    
    context = {
        'template_form' : template_form,
        'indexes': queryset,
        'theme_type': template_instance,
    }
    
        
    
    return render(request, "themes/admin/settings.html", context)


# download new themes
def new_themes(request):
    return render(request, "themes/admin/new.html")





# Image = get_image_model()

    # path = r'/home/reza/programs/python/django/wagtail/crx/sorsore/themes/crx-themes/ara_shop/themes/static/themes/theme1/images/banner-img-1.jpg'
    # with open(path, 'rb') as f:
    #     img_name = os.path.basename(path)
    #     image = Image.objects.create(title='about', file=ContentFile(f.read(), name=img_name))
    #     image.uploaded_by_user = request.user
    #     image.save()


# if request.method == 'POST':
    #     template_form = GetTemplatesForm(request.POST)
    #     if template_form.is_valid():
    #         index_names = request.POST.getlist('index_name')
    #         in_uses = request.POST.getlist('in_use')
    #         print(f"Number of index_names: {len(index_names)}")
    #         print(f"Number of in_uses: {len(in_uses)}")
    #         for i in range(len(index_names)):
    #             form_data = {
    #                 'id': request.POST.getlist('id')[i],
    #                 'index_name': index_names[i],
    #                 'in_use': in_uses[i]
    #             }
    #             index_form = IndexesForm(form_data, prefix=str(i))
    #             if index_form.is_valid():
    #                 data = index_form.cleaned_data
    #                 try:
    #                     instance = Index.objects.get(id=data['id'])
    #                     instance.name = data['index_name']
    #                     instance.in_use = data['in_use'].lower() == 'active'
    #                     instance.save()
    #                 except Index.DoesNotExist:
    #                     pass
    #         return redirect("/admin")
    # else:
    #     indexes = Index.objects.all()
    #     index_forms = []
    #     index_forms = [IndexesForm(initial={'id': index.id, 'index_name': index.name, 'in_use': index.in_use}, prefix=str(i)) for i, index in enumerate(indexes)]
    #     template_form = GetTemplatesForm(initial={'template_name': template_instance.name})

    # context = {
    #     'template_form' : template_form,
    #     'index_forms': index_forms
    # }