from django.db import models

# Create your models here.
class Course(models.Model):
    courseNumber = models.CharField(max_length=4)
    courseName = models.CharField(max_length=256)
    subject = models.CharField(max_length=10)
    prereqs = models.ManyToManyField('Course', related_name='pre', blank=True)
    coreqs = models.ManyToManyField('Course', related_name='co', blank=True)
    requiredForMajor = models.BooleanField(default=False)
    isElective = models.BooleanField(default=False)

    def __str__(self):
        return str(self.subject) + ' ' + str(self.courseNumber) + ': ' + str(self.courseName)

class User(models.Model):
    coursesTaken = models.ManyToManyField(Course)

    def takeCourse(self, course):
        # Add course to list of taken courses
        self.coursesTaken.add(course)

        # Add prereques to list of taken courses
        for c in course.prereqs.all:
            takeCourse(c)

        # Add coreqs to list of taken course
        for c in course.coreqs.all:
            takeCourse(c)
