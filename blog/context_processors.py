from blog import models

def get_categories(request):
    return {'categories': models.Category.objects.all()}