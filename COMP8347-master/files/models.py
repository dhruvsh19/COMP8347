from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, null=False, blank=False, default='Category001')

    def __str__(self):
        return self.name + " , " + self.category


class Course(models.Model):
    topic = models.ForeignKey(Topic, related_name='courses', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    for_everyone = models.BooleanField(default=True)
    description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name


class Student(User):
    CITY_CHOICES = [('WS', 'Windsor'),
                    ('CG', 'Calgary'),
                    ('MR', 'Montreal'),
                    ('VC', 'Vancouver')]
    school = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='WS')
    interested_in = models.ManyToManyField(Topic)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Order(models.Model):
    VALID_CHOICES = [
        (0, 'Cancelled'),
        (1, 'Confirmed'),
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    levels = models.PositiveIntegerField(default=1)
    order_status = models.IntegerField(choices=VALID_CHOICES, default=1)
    order_date = models.DateField(default=timezone.now)

    def total_cost(self):
        # returns total cost of all courses in order;
        return sum([course_item.price for course_item in self.course.all()])

    def __str__(self):
        return "order#" + str(self.id) + " courseName: " + str(self.course.name) + " StudentId: " + str(self.student)
