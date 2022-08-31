from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Profile
from api.serializers import ProfileSerializer


class ProfileView(APIView):
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Resume Uploaded Successfully', 'status': 'success', 'candidate': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            candidates = Profile.objects.get(id=id)
            serializer = ProfileSerializer(candidates)
            return Response(serializer.data)
        candidates = Profile.objects.all()
        serializer = ProfileSerializer(candidates, many=True)
        return Response({'status': 'success', 'candidates': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        id = pk
        candidates = Profile.objects.get(pk=id)
        serializer = ProfileSerializer(candidates, data=request.body)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Resume Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id = pk
        candidate = Profile.objects.get(pk=id)
        candidate.delete()
        return Response({'msg': 'Resume Deleted'}, status=status.HTTP_204_NO_CONTENT)
