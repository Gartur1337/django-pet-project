from myapp.models import *


menu = [{'title': "Добавить статью", 'url_name': 'add_post'},
        {'title': "О Сайте", 'url_name': 'about'},
        {'title': "Главная", 'url_name': 'home'},
        {'title': "Создать профиль", 'url_name': 'create_user_profile'},
        {'title': "Ваш профиль", 'url_name': 'user_profile' },
]

class DataMixin:
    
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(0)
            user_menu.pop(3)
            if UserProfile.slug:
                user_menu.pop(2)
        
        context['menu'] = user_menu
        context['cats'] = cats
        return context