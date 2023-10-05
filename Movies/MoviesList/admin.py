from django.contrib import admin

from .models import Movies_Info, Publisher, Contributor, Review
# Register your models here.
admin.site.register(Movies_Info)
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Review)
