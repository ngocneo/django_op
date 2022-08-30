from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members
from .serializers import MemberSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Members
from .serializers import MemberSerializer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView




class MembersApiView(ListCreateAPIView):
    model = Members
    serializer_class = MemberSerializer

    def get_queryset(self):
        return Members.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = MemberSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Car successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Car unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class MembersDetailApiView(RetrieveUpdateDestroyAPIView):
    model = Members
    serializer_class = MemberSerializer

    def put(self, request, *args, **kwargs):
        car = get_object_or_404(Car, id=kwargs.get('pk'))
        serializer = MemberSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Car successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Car unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        car = MemberSerializer(Members, id=kwargs.get('pk'))
        car.delete()

        return JsonResponse({
            'message': 'Delete Car successful!'
        }, status=status.HTTP_200_OK)


def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))


def addrecord(request):
  x = request.POST['firstname']
  y = request.POST['lastname']
  member = Members(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))


def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['firstname']
  last = request.POST['lastname']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))