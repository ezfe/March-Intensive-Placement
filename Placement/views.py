from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, HttpResponse
from People.models import Student
from Courses.models import Course
from Registrations.models import Request, Placement
from django.contrib.auth.decorators import login_required
import json
import csv

# Create your views here.
@login_required
def view_requests(request):
    q = Student.objects.filter(should_ignore=False).order_by('-grade','no_participate_previous','?')

    #Filter out students that have courses
    studentsRandom = [o for o in q if not o.has_course()]#[:1]

    printData = []

    MAX_RANK = 10;

    for student in studentsRandom:
        sRequest = {"student": student, "requests": []}
        for i in range(0,10):
            requestObject = {"FULL": None, "AM": None, "PM": None}
            requests = Request.objects.filter(request_rank=i,student=student);
            if len(requests) == 0:
                continue
            else:
                for req in requests:
                    requestObject[req.course.course_type] = req.course;
            sRequest["requests"].append(requestObject)
        printData.append(sRequest)


    return render(request, 'requests.html', {"printData": printData})

@login_required
def view_no_requests(request):
    return render(request, 'no_requests_cg.html', {"students": Student.objects.filter()})

@login_required
def view_results_detail(request, course_id=None):
    return render(request, 'placement.html', {"courses":Course.objects.filter(pk=course_id)})

@login_required
def view_results(request):
    return render(request, 'placement_lite.html', {"placements":Placement.objects.filter(),"courses":Course.objects.filter()})

@login_required
def manage_student(request):
    return render(request, 'manage_student.html', {"students":Student.objects.filter(),"courses":Course.objects.filter()})

@login_required
def configure_placement(request):
    return render(request, 'pre_placement.html', {"placements":Placement.objects.filter(),"courses":Course.objects.filter()})

@login_required
def verify_missing_students(request):
    students = get_list_or_404(Student)
    not_signed_up = []
    missing_students_ignored = []

    for student in students:
        if student.should_ignore:
            missing_students_ignored.append(student)
        elif not student.has_course():
            not_signed_up.append(student)
    return render(request, 'verify_missing_students.html', {"missing_students": not_signed_up, "ignored_students": missing_students_ignored, "allow_place": True})

@login_required
def import_students(request):
    if request.method == "GET":
        return render(request, 'import_students.html', {"imported":"no"});
    elif request.method == "POST":
        student_data = request.POST.get('student_data', None);
        if student_data is not None:
            failures = False;
            reader = csv.reader(student_data.split('\n'), delimiter=','); # split newlines because csvreader expects that
            for row in reader:
                try:
                    p, created = Student.objects.get_or_create(first_name=row[0],last_name=row[1],email=row[2],grade=row[3],common_ground=row[4],gender=row[5])
                    if not created:
                        failures = True
                except:
                    print("An error occured for %s %s" % (row[0], row[1]))
            if not failures:
                return render(request, 'import_students.html', {"imported":"yes"});
            else:
                return render(request, 'import_students.html', {"imported":"error"});
        else:
            return render(request, 'import_students.html', {"imported":"error"});

@login_required
def settings(request):
    all_configurations = PlaceConf.objects.all()
    if len(all_configurations) == 0:
        conf = PlaceConf(grade=9)
        conf.save();
        return redirect('/admin-django/Placement/placeconf/%s' % conf.pk);
    else:
        for conf in all_configurations[1:]:
            conf.delete();
        return redirect('/admin-django/Placement/placeconf/%s' % all_configurations[0].pk)
