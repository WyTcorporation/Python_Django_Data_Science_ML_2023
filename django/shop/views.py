from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Course


# Create your views here.
def index(request) -> render:
    courses: Course = Course.objects.all()
    return render(request, 'shop/courses.html', {'courses': courses, 'title': 'All Courses'})


def course(request, course_id) -> render:
    # Option 1
    # try:
    #     course: Course = Course.objects.get(pk=course_id)
    #     return render(request, 'course.html', {'course': course, 'title': course.title})
    # except Course.DoesNotExist:
    #     raise Http404()

    # Option 2
    course: get_object_or_404 = get_object_or_404(Course, pk=course_id)
    return render(request, 'shop/course.html', {'course': course, 'title': course.title})
