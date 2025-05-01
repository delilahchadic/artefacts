from django.contrib import admin
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
)

@admin.register(PersonType)
class PersonTypeAdmin(admin.ModelAdmin):
    list_display = ('description',)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date', 'display_person_types')
    filter_horizontal = ('types',)

    def display_person_types(self, obj):
        return ", ".join([type.description for type in obj.types.all()])
    display_person_types.short_description = 'Person Types'

@admin.register(PersonDataType)
class PersonDataTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(PersonData)
class PersonDataAdmin(admin.ModelAdmin):
    list_display = ('person', 'type', 'value')
    list_filter = ('person', 'type')

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'display_creators')
    filter_horizontal = ('creators',)

    def display_creators(self, obj):
        return ", ".join([f"{creator.first_name} {creator.last_name}" for creator in obj.creators.all()])
    display_creators.short_description = 'Creators'

@admin.register(WorkType)
class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ('description',)

@admin.register(WorkDataType)
class WorkDataTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(WorkData)
class WorkDataAdmin(admin.ModelAdmin):
    list_display = ('work', 'type', 'value')
    list_filter = ('work', 'type')

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('work', 'type', 'link')
    list_filter = ('work', 'type')