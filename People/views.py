from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.contrib.auth.decorators import login_required

from People.models import Student

# Create your views here.

@login_required
def students(request):
	students = get_list_or_404(Student)
	return render(request, 'students.html', {'students': students, 'detail': False})

@login_required
def student_detail(request, student_id):
	student = get_object_or_404(Student, pk=student_id)
	return render(request, 'students.html', {'students': [student], 'detail': True})