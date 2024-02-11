# models.py

from django.db import models

class IMUser(models.Model):
    USER_TYPES = [
        ('EIT', 'EIT'),
        ('TEACHING_FELLOW', 'Teaching Fellow'),
        ('ADMIN_STAFF', 'Admin Staff'),
        ('ADMIN', 'Admin')
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    date_created = models.DateTimeField(auto_now_add=True)
    # Add any extra fields here if needed

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Cohort(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='authored_cohorts')

    def __str__(self):
        return self.name

class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='cohorts')
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='members')
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='authored_cohort_members')

    def __str__(self):
        return f"{self.member.first_name} {self.member.last_name} - {self.cohort.name}"
