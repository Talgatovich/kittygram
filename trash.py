# View функции API
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from .models import Cat
# from .serializers import CatSerializer


@api_view(["GET", "POST"])
def cat_list(request):
    if request.method == "POST":
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    cats = Cat.objects.all()
    serializer = CatSerializer(cats, many=True)
    return Response(serializer.data)


# View-классы API
# from django.shortcuts import get_object_or_404
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from .models import Cat
# from .serializers import CatSerializer


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


class APICatDetail(APIView):
    def delete(self, request, pk):
        cat = get_object_or_404(Cat, id=pk)
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk):
        cat = get_object_or_404(Cat, id=pk)
        serializer = CatSerializer(cat)
        return Response(serializer.data)

    def put(self, request, pk):
        cat = get_object_or_404(Cat, id=pk)
        serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Дженерики

#from rest_framework import generics
#
#from .models import Cat
#from .serializers import CatSerializer


class CatList(generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

