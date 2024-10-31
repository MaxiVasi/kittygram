from django.urls import include, path

# Импорт Роутер - для заданных вьюсетов создаются эндпоинты по маске адреса
from rest_framework.routers import SimpleRouter, DefaultRouter

from cats.views import cat_list, hello, cat_detail
from cats.views import APICat
from cats.views import CatList, CatDetail, CatViewSet

# Простой Роутер
router = SimpleRouter()
router.register('cats/v3', CatViewSet)

# Дефоулт роутер
#router = DefaultRouter()
#router.register('cats/v4', CatViewSet)
# urlpatterns = [
#    path('', include(router.urls), name='api-root'),
#]


urlpatterns = [
   path('cats/', cat_list),
   path('cats/<int:pk>/', cat_detail),
   path('cats/v1/', APICat.as_view()),
   path('cats/v2/', CatList.as_view()),
   path('cats/v2/<int:pk>/', CatDetail.as_view()),
   path('hello/', hello),
   path('', include(router.urls)),
]


# Создание и использование Роутера.
# Создаётся роутер
#router = SimpleRouter()
# Вызываем метод .register с нужными параметрами
#router.register('cats', CatViewSet)
# В роутере можно зарегистрировать любое количество пар "URL, viewset":
# например
# router.register('owners', OwnerViewSet)
# Но нам это пока не нужно

#urlpatterns = [
#    # Все зарегистрированные в router пути доступны в router.urls
#    # Включим их в головной urls.py
#    path('', include(router.urls)),
#]
#Только что созданный роутер сгенерирует два эндпоинта:
#cats/,
#cats/<int:pk>/.
