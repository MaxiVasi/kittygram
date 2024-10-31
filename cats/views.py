from rest_framework.views import APIView  # Низкоуровневый.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics  # Дженерики, высокоуровневый.
from rest_framework import viewsets  # Вьюсеты и роутеры.

from .models import Cat
from .serializers import CatSerializer


# Реализация на ViewSet. Класс, который обработает все шесть типичных действий.
class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


# реализация на DFI:
class APICat(APIView):
    def get(self, request):
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CatList(generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


@api_view(['GET', 'POST'])
def cat_list(request):
    if request.method == 'POST':
        serializer = CatSerializer(data=request.data)
        # чтобы подавать списком на добавление. Т.е. несколько котов.
        # serializer = CatSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    cats = Cat.objects.all()
    serializer = CatSerializer(cats, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])  # Применили декоратор и указали разрешённые методы
def hello(request):
    # По задумке, в ответ на POST-запрос нужно вернуть JSON с теми данными,
    # которые получены в запросе.
    # Для этого в объект Response() передаём словарь request.data.
    if request.method == 'POST':
        return Response({'message': 'Получены данные', 'data': request.data})

    # В ответ на GET-запрос нужно вернуть JSON
    # Он тоже будет создан из словаря, переданного в Response()
    return Response({'message': 'Это был GET-запрос!'})


# Расшифровка
#@api_view(['GET', 'POST'])
#def cat_list(request):
#    if request.method == 'POST':
#        # Создаём объект сериализатора и передаём в него данные из POST-запроса
#        serializer = CatSerializer(data=request.data)
#        if serializer.is_valid():
#            # Если полученные данные валидны —
#            # сохраняем данные в базу через save().
#            serializer.save()
#            # Возвращаем JSON со всеми данными нового объекта
#            # и статус-код 201
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        # Если данные не прошли валидацию — 
#        # возвращаем информацию об ошибках и соответствующий статус-код:
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
#     В случае GET-запроса возвращаем список всех котиков
#     cats = Cat.objects.all()
#     Передаём queryset в конструктор сериализатора
#     serializer = CatSerializer(cats, many=True)
#     return Response(serializer.data)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def cat_detail(request, pk):
    cat = Cat.objects.get(pk=pk)
    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = CatSerializer(cat)
    return Response(serializer.data, status=status.HTTP_200_OK)
