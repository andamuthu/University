from django.db import models
from django_currentuser.middleware import (get_current_user,get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField



class StudentsMarks(models.Model):
    student_name = models.CharField(max_length=100, unique=True)
    tamil = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    socialscience = models.IntegerField()
    total_marks = models.IntegerField()
    created_by = CurrentUserField()

    def __unicode__(self):
        return self.student_name

    def save(self, *args, **kwargs):
        self.total_marks = self.tamil + self.english + self.maths + self.science + self.socialscience
        super(StudentsMarks, self).save(*args, **kwargs)


