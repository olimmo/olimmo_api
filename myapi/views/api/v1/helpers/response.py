from rest_framework.response import Response
from rest_framework import status


def render_serialized_data(serializer, save_kwargs={}):
    if serializer.is_valid():
        serializer.save(**save_kwargs)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
