from django.db import models
from users.models import IMUser, Cohort
import datetime


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length = 2000)
    description = models.TextField(default = 'N/A', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add= True, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now= True, blank=True, null=True)


    def __str__(self) -> str:
        return f"{self.name}" 



class ClassSchedule(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date_and_time = models.DateTimeField()
    end_date_and_time = models.DateTimeField()
    is_repeated = models.BooleanField(default=False)
    repeat_frequency = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    organizer = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='organized_classes')
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='class_schedules')
    venue = models.CharField(max_length=100)

class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE, related_name='attendances')
    attendee = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='attended_classes')
    is_present = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='authored_attendances')

class Query(models.Model):
    RESOLUTION_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('DECLINED', 'Declined'),
        ('RESOLVED', 'Resolved')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    submitted_by = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='submitted_queries')
    assigned_to = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='assigned_queries')
    resolution_status = models.CharField(max_length=20, choices=RESOLUTION_CHOICES, default='PENDING')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='authored_queries')

class QueryComment(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='authored_query_comments')
