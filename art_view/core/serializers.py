from rest_framework import serializers
from .models import (
    PersonType,
    Person,
    PersonDataType,
    PersonData,
    Work,
    WorkType,
    WorkDataType,
    WorkData,
    DocumentType,
    Document,
    Gallery,
    GalleryItem,
)

class PersonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonType
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class PersonDataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonDataType
        fields = '__all__'

class PersonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonData
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class WorkSerializer(serializers.ModelSerializer):
    documents = DocumentSerializer(many=True,read_only=True)
    class Meta:
        model = Work
        fields = '__all__'

class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkType
        fields = '__all__'

class WorkDataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkDataType
        fields = '__all__'

class WorkDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkData
        fields = '__all__'

class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = '__all__'




class GalleryItemSerializer(serializers.ModelSerializer):
    work = WorkSerializer(read_only=True)

    class Meta:
        model = GalleryItem
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
    gallery_items = GalleryItemSerializer(many=True, read_only=True)
    class Meta:
        model = Gallery
        fields = '__all__'