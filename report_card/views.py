from django.shortcuts import render
from django.http import HttpResponse
from report_card.models import *
from django.core.paginator import Paginator

# Create your views here.

from django.db.models import Q, Sum

def report(request):

    queryset = Student.objects.all()

    search_query = request.GET.get('search')  # Make sure the name matches your form
    if search_query:
        queryset = queryset.filter(
            Q(name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(roll_number__icontains=search_query) |
            Q(department__name__icontains=search_query)
        )

    paginator = Paginator(queryset, 15)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'marks_data.html', {'queryset': page_obj})


from report_card.models import Student_marks

def see_marks(request, roll_number):
    queryset = Student_marks.objects.filter(student__roll_number=roll_number).select_related('student', 'subject')
    s_rank = -1
    total_marks = queryset.aggregate( total_marks=Sum('marks'))
    rank = Student.objects.annotate(total_marks = Sum( 'student_marks__marks')).order_by('-total_marks')

    i = 1
    for r in rank:
        if roll_number == r.roll_number:
            s_rank = i
            break

        i += 1
    return render(request, 'result.html', {'queryset': queryset, 'total_marks': total_marks, 's_rank' :s_rank})

