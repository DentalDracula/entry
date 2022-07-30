import imp
from django.http import JsonResponse
from .models import Entry
from .serializers import EntrySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def table_list(request, format=None):

    if request.method == 'GET':
        entrys = Entry.objects.all()
        serializer = EntrySerializer(entrys, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])
def entry_detail(request, sno,format=None):
    try:
        entrys = Entry.objects.get(pk = sno)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = EntrySerializer(entrys)
        return Response(serializer.data)         
    elif request.method == 'PUT':
        serializer = EntrySerializer(entrys, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        entrys.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


