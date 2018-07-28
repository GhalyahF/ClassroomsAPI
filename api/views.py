from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from classes.models import Classroom 
from .serializers import CreateSerializer, DetailsSerializer,ListSerializer

# Create your views here.
class ClassroomList(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ListSerializer


class DetailsView(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = DetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class CreateView(CreateAPIView):
	serializer_class = CreateSerializer

	def perform_create(self, serializer):
		 serializer.save(teacher=self.request.user)

class UpdateView(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = CreateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'



class DeleteView(DestroyAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'