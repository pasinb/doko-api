from django.db import models

# Create your models here.

class FirebaseUser(models.Model):
    id = models.CharField(max_length=64, primary_key=True)

class Course(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=50000)

class CourseSection(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=50000)

class CourseSubSection(models.Model):
    course_section_id = models.ForeignKey(CourseSection, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=50000)
    boilerplate = models.CharField(max_length=50000)

class UserCourse(models.Model):
    user_id = models.ForeignKey(FirebaseUser, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    complete_percent = models.FloatField(default=0.0)

class UserCourseSection(models.Model):
    user_id = models.ForeignKey(FirebaseUser, on_delete=models.CASCADE)
    course_id = models.ForeignKey(CourseSection, on_delete=models.CASCADE)
    complete_percent = models.FloatField(default=0.0)

class UserCourseSubSection(models.Model):
    user_id = models.ForeignKey(FirebaseUser, on_delete=models.CASCADE)
    course_id = models.ForeignKey(CourseSection, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)