from django.shortcuts import render, get_object_or_404
from Courses.models import Course
import json
from django.core import serializers
from django.http import HttpResponse

from People.models import Student
from Courses.models import Course
from Registrations.models import Request, Placement

from django.views.decorators.csrf import csrf_exempt

import sys

from subprocess import call

# Create your views here.

def register_success(request):
	sid = request.GET.get('person', None)
	student = get_object_or_404(Student, pk=sid)

	return render(request, 'success.html', {'student': student})

@csrf_exempt
def register(request):
	if request.method == "GET":
		courses = Course.objects.all().order_by('course_type','display_name')
		userpk = request.GET.get('student', None)
		print(userpk)
		is_student = False
		student = None
		try:
			student = Student.objects.get(pk=userpk)
			is_student = True
		except:
			is_student = False
		return render(request, 'register.html', {'courses': courses,'courses_json': serializers.serialize('json', courses), 'is_student': is_student, 'student': student})
	elif request.method == "POST":
		EMPTY_INPUT = "empty_inpt"
		INPUT_TOO_LONG = "tl_inpt"
		ACCEPTED_FOUND = "acc_fnd"
		ACCEPTED_NOTFOUND = "acc_nf"
		DUPLICATE_INPUT = "dup_in"

		response_errors = {}

		first_name = request.POST.get('attributes[first_name]', None)
		last_name = request.POST.get('attributes[last_name]', None)

		personKey = None

		user_found_status = "NotFound"

		user = None
		user_fn = None
		user_ln = None

		try:
			user = Student.objects.get(first_name__iexact=first_name, last_name__iexact=last_name)
		except:
			user = None
			try:
				user_fn = Student.objects.get(first_name__iexact=first_name)
			except:
				try:
					user_ln = Student.objects.get(last_name__iexact=last_name)
				except:
					pass
				else:
					user_found_status = "LastName"
			else:
				user_found_status = "FirstName"
		else:
			personKey = user.pk
			user_found_status = "Found"

		if first_name == "":
			response_errors["first_name"] = {"status": EMPTY_INPUT, "message": "First name needs to be filled out"}
		elif len(first_name) > 100:
			response_errors["first_name"] = {"status": INPUT_TOO_LONG, "message": "First name is too long"}
		elif user_found_status == "Found" or user_found_status == "FirstName":
			# response_errors["first_name"] = {"status": ACCEPTED_FOUND, "message": "Found a student with the first name %s" % first_name}
			pass
		else:
			response_errors["first_name"] = {"status": ACCEPTED_NOTFOUND, "message": "Couldn't find %s" % first_name}

		if last_name == "":
			response_errors["last_name"] = {"status": EMPTY_INPUT, "message": "Last name needs to be filled out"}
		elif len(last_name) > 100:
			response_errors["last_name"] = {"status": INPUT_TOO_LONG, "message": "Last name is too long"}
		elif user_found_status == "Found" or user_found_status == "LastName":
			# response_errors["last_name"] = {"status": ACCEPTED_FOUND, "message": "Found a student with the last name %s" % last_name}
			pass
		else:
			response_errors["last_name"] = {"status": ACCEPTED_NOTFOUND, "message": "Couldn't find %s %s" % (first_name, last_name)}

		try:
			request_list = json.loads(request.POST.get('request_list', None))
			print(request_list)
		except:
			response_errors["global_error"] = {"status": EMPTY_INPUT, "message": "No request object sent, or malformed request object sent."}
		else:
			if not user == None and request.POST.get('type', None) == 'submission_request' and len(response_errors) == 0:
				found_requests = Request.objects.filter(student=user)
				found_placements = Placement.objects.filter(student=user)
				if len(found_requests) > 0 or (len(found_placements) > 0 and not (user.student_leader == "AM" or user.student_leader == "PM")):
					response_errors["global_error"] = {"status": DUPLICATE_INPUT, "message": "Unable to register twice, or already has placements"}
				else:
					# print("Unable to find requests for %s" % users)
					email_subject = "Request for %s" % user
					email_string = "Requests:\n"
					for (i, sr) in enumerate(request_list):
						if "FULL" in sr and sr["FULL"] is not None:
							request_class = Course.objects.get(pk=sr["FULL"])

							email_string = "%s\nRequested %s for %s at level: %s" % (email_string, request_class, user, i)

							req = Request(student=user, course=request_class, request_rank=sr["rank"])
							req.save()
						if "AM" in sr and sr["AM"] is not None:
							request_class = Course.objects.get(pk=sr["AM"])

							email_string = "%s\nRequested %s for %s at level: %s" % (email_string, request_class, user, i)

							req = Request(student=user, course=request_class, request_rank=sr["rank"])
							req.save()
						if "PM" in sr and sr["PM"] is not None:
							request_class = Course.objects.get(pk=sr["PM"])

							email_string = "%s\nRequested %s for %s at level: %s" % (email_string, request_class, user, i)

							req = Request(student=user, course=request_class, request_rank=sr["rank"])
							req.save()
					call("echo \"%s\" | mail -s \"%s\" example@domain.com" % (email_string, email_subject),shell=True)

		return HttpResponse(json.dumps({"errors":response_errors, "sent":request_list, "personKey": personKey}), content_type="application/json")
