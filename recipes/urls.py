# from django.http import HttpResponse
from django.urls import path
from recipes.views import home

# I created this "urls.py" file to separate the URLs from the "projeto/urls.py" file, because it is more organized
# and easier to understand the code.


urlpatterns = [
    # Here we dont need to import the "admin" module, because we are not using it
    path("", home), # because i put "my_view" here, the page will run the def my_view(request) function
]