from django.shortcuts import render
from django.db.models import Case, When, Value, IntegerField
from .models import TimeSlot

def timetable_view(request):

    timetable_records = TimeSlot.objects.annotate(
        day_order=Case(
            When(day='Monday', then=Value(1)),
            When(day='Tuesday', then=Value(2)),
            When(day='Wednesday', then=Value(3)),
            When(day='Thursday', then=Value(4)),
            When(day='Friday', then=Value(5)),
            When(day='Saturday', then=Value(6)),
            When(day='Sunday', then=Value(7)),
            default=Value(8),
            output_field=IntegerField()
        )
    ).order_by('day_order', 'start_time')

    return render(
        request,
        'timetable/timetable.html',
        {'timetable_records': timetable_records}
    )

