from django.db import models


# Model to store daily timetable details
class TimeSlot(models.Model):

    # Choices for days of the week
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ]

    # Day of the class
    day = models.CharField(
        max_length=20,
        choices=DAY_CHOICES
    )

    # Starting time of the class
    start_time = models.TimeField()

    # Ending time of the class
    end_time = models.TimeField()

    # Subject name
    subject_name = models.CharField(max_length=100)

    # Faculty name
    faculty_name = models.CharField(max_length=100)

    # Classroom number (Additional Task)
    classroom = models.CharField(max_length=50)

    # Display subject and day in admin panel
    def __str__(self):
        return f"{self.day} - {self.subject_name}"

