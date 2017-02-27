from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.contrib.auth.decorators import login_required

from Courses.models import Course

####################
### COURSE VIEWS ###
####################