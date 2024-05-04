from blog import models

def get_social_links(request):
    return {'categories': models.Category.objects.all()}