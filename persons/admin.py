from django.contrib import admin

# Register your models here.
#from persons.models import  Nome_Popular, City, Person
#from persons.models import City, Person, Nome_Popular
from .models import *

admin.site.register([Nome_Popular, Madeira, Person])

#admin.site.register(City)
#admin.site.register(Person)
#admin.site.register(Nome_Popular)
