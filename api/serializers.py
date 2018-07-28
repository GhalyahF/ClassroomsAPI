from rest_framework import serializers
from classes.models import Classroom



class ListSerializer(serializers.ModelSerializer):
	class Meta:
		model= Classroom 
		fields= ['subject', 'year', 'teacher']


class DetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields= ['teacher', 'subject', 'year']



class CreateSerializer(serializers.ModelSerializer):
	class Meta:
		model= Classroom
		fields= ['teacher', 'subject', 'year']
