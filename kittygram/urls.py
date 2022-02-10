# urls.py
from cats.views import CatViewSet
from django.urls import include, path
from rest_framework.routers import SimpleRouter

# Создаётся роутер
router = SimpleRouter()
# Вызываем метод .register с нужными параметрами
router.register("cats", CatViewSet)
# В роутере можно зарегистрировать любое количество пар "URL, viewset":
# например
# router.register('owners', OwnerViewSet)
# Но нам это пока не нужно

urlpatterns = [
    # Все зарегистрированные в router пути доступны в router.urls
    # Включим их в головной urls.py
    path("", include(router.urls)),
]
