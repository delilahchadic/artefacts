from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PersonType(models.Model):
  description = models.CharField(max_length=50)

  def __str__(self):
    return self.description

class Person(models.Model):
  first_name = models.CharField(max_length=50, blank=True)
  last_name = models.CharField(max_length=50)
  birth_date = models.DateField(null=True, blank=True)
  types = models.ManyToManyField(PersonType, related_name="persons")

  def __str__(self):
    if self.first_name:
      return f"{self.first_name} {self.last_name}"
    else:
      return self.last_name

class PersonDataType(models.Model):
  name = models.CharField()

  def __str__(self):
    return self.name

class PersonData(models.Model):
  person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="person_data")
  type = models.ForeignKey(PersonDataType, on_delete=models.CASCADE, related_name="person_data_types")
  value = models.CharField()

  def __str__(self):
    return f"{self.person} - {self.type}: {self.value}"

class Work(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField()
  creators = models.ManyToManyField(Person, related_name="works")

  def __str__(self):
    return self.name

class WorkType(models.Model):
  description = models.CharField()

  def __str__(self):
    return self.description

class WorkDataType(models.Model):
  name= models.CharField()

  def __str__(self):
    return self.name

class WorkData(models.Model):
  work = models.ForeignKey(Work, on_delete=models.CASCADE,related_name="work_data")
  type = models.ForeignKey(WorkDataType, on_delete=models.CASCADE, related_name="work_data_types")
  value = models.CharField()

  def __str__(self):
    return f"{self.work} - {self.type}: {self.value}"

class DocumentType(models.Model):
  name = models.CharField()

  def __str__(self):
    return self.name

class Document(models.Model):
  work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name="documents")
  type = models.ForeignKey(DocumentType, on_delete=models.CASCADE, related_name="document_types")
  link = models.URLField()

  def __str__(self):
    return f"{self.work} - {self.type}"

class Gallery(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField()
  description = models.TextField(null=True, blank=True)

class GalleryItem(models.Model):
  gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE,related_name='gallery_items')
  work = models.ForeignKey(Work, on_delete=models.CASCADE)
  index = models.IntegerField(default=0)