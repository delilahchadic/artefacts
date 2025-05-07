from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .utils import IIIFParser
from .models import DocumentType, Gallery, GalleryItem, Person, Work, Document, PersonData, PersonType, PersonDataType
from .serializers import GalleryItemSerializer, GallerySerializer, PersonDataSerializer, PersonSerializer, WorkSerializer, DocumentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
# Create your views here.

class PersonList(generics.ListCreateAPIView):
  queryset=Person.objects.all()
  serializer_class = PersonSerializer

class WorkList(generics.ListCreateAPIView):
  queryset=Work.objects.all()
  serializer_class = WorkSerializer

@api_view(['GET'])
def get_person(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
        serializer = PersonSerializer(person)
        

        return Response(serializer.data)

    except Person.DoesNotExist:
        return Response({'error': 'Deck not found'}, status=404)
    
@api_view(['GET'])
def get_image(request, person_id):
  try:
    imagetype = PersonDataType.objects.get(name="image")
    if imagetype:
        image = PersonData.objects.get(person=person_id, type=imagetype)
        serializer = PersonDataSerializer(image)
        return Response(serializer.data)
    image = PersonData.objects.get()
  except:
    return Response({'error':'error'})
# @api_view(['GET'])
# def get_work(request, work_id):

#     try:
#         person = Person.objects.get(pk=person_id)
#         serializer = PersonSerializer(person)
        

#         return Response(serializer.data)

#     except Person.DoesNotExist:
#         return Response({'error': 'Deck not found'}, status=404)

def credits(request):
  test = "<h1>Delilah Chadic</h1>"
  return HttpResponse(test)

@api_view(['GET'])
def get_works_by_person(request, person_id):
  try:
    works = Work.objects.filter(creators__id=person_id)
    serializer = WorkSerializer(works,many=True)
    return Response(serializer.data)
  except Work.DoesNotExist:
    return Response({'error': 'Deck not found'}, status=404) 
  

@api_view(['POST'])
def post_iiif(request):
  iiif_url = request.data.get('iiifUrl') 
  artist = request.data.get('artist') 
  iiif = IIIFParser(iiif_url)

  person, personCreated= Person.objects.get_or_create(name=artist)
  work, workCreated = Work.objects.get_or_create(name=iiif.getTitle)
  work.creators.add(person)
  
  iiifType = DocumentType.objects.get(name="IIIF")
  iiifDocument = Document.objects.create(link = iiif_url, work=work, type=iiifType)
  return Response({"message": "IIIF Document processed and created."}, status=201)

    
@api_view(['GET'])
def get_iiif(request, work_id):
   try:
      document = Document.objects.filter(work = work_id, type__name = "IIIF").first()
      work = get_object_or_404(Work, pk=work_id)
      creators = work.creators.all()
      work_serializer = WorkSerializer(work)
      creator_serializer = PersonSerializer(creators, many=True)  # Serialize the creators
      document_serializer = DocumentSerializer(document)  # Serialize the document

      if document:
         return Response({"work":work_serializer.data, "link": document_serializer.data.get('link'), "creators": creator_serializer.data})
      # # serializer = (document, many=True)
      # if document:
      #    return Response({"link": document.link, "creators":creator})
      else:
         return Response({'error': 'Deck not found'}, status=404) 
   except Document.DoesNotExist:
      return Response({'error': 'Deck not found'}, status=404) 
   
@api_view(['GET'])
def get_gallery(request, gallery_id):
   try:
      gallery =  Gallery.objects.prefetch_related('gallery_items__work').get(pk=gallery_id)
      # gallery_items = GalleryItem.objects.filter(gallery=gallery_id)
      gallery_serializer = GallerySerializer(gallery)
      # gallery_items_serializer = GalleryItemSerializer(gallery_items, many=True)
      
         
      return Response({"gallery": gallery_serializer.data})
   except Gallery.DoesNotExist:
      return Response({'error': 'Gallery not found'}, status=404) 

   
def persons(request):
  person_list = Person.objects.all()
  body = "<div>"
  if person_list:
    for person in person_list:
      body += f"<h1>{person.name}</h1>"
  else:
    body+= "<h1>no persons found</h1>"

  body +="</div>"
  return HttpResponse(body)
