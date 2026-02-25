from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(
         User,
         on_delete=models.CASCADE,
         null=True,
         blank=True
    )

    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science'),
        ('ECE', 'Electronics'),
        ('EEE', 'Electrical'),
        ('ME', 'Mechanical'),
        ('CE', 'Civil'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(
        validators=[MinValueValidator(1)]
    )
    roll_number = models.CharField(max_length=20)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    year = models.IntegerField()
    image = models.ImageField(upload_to='students/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def total_marks_obtained(self):
        return sum(mark.marks_obtained for mark in self.marks.all())

    def total_max_marks(self):
        return sum(mark.subject.max_marks for mark in self.marks.all())

    def percentage(self):
        max_marks = self.total_max_marks()
        if max_marks == 0:
            return 0
        return round((self.total_marks_obtained() / max_marks) * 100, 2)

    def has_failed_any_subject(self):
        for mark in self.marks.all():
            if mark.marks_obtained < 35:
                return True
        return False

    def result(self):
        if self.has_failed_any_subject():
            return "FAIL"
        return "PASS"
    
    def total_attendance_days(self):
        return self.attendance.count()

    def present_days(self):
        return self.attendance.filter(status='P').count()

    def attendance_percentage(self):
        total_days = self.total_attendance_days()
        if total_days == 0:
            return 0
        return round((self.present_days() / total_days) * 100, 2)
    
    def monthly_attendance_queryset(self, year, month):
        return self.attendance.filter(
            date__year=year,
            date__month=month
        )

    def monthly_total_days(self, year, month):
        return self.monthly_attendance_queryset(year, month).count()

    def monthly_present_days(self, year, month):
        return self.monthly_attendance_queryset(year, month).filter(status='P').count()

    def monthly_absent_days(self, year, month):
        return self.monthly_attendance_queryset(year, month).filter(status='A').count()

    def monthly_attendance_percentage(self, year, month):
        total = self.monthly_total_days(year, month)
        if total == 0:
            return 0
        return round((self.monthly_present_days(year, month) / total) * 100, 2)

    def __str__(self):
        return self.name

class Subject(models.Model):
    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science'),
        ('ECE', 'Electronics'),
        ('EEE', 'Electrical'),
        ('ME', 'Mechanical'),
        ('CE', 'Civil'),
    ]
    name = models.CharField(max_length=100)
    department = models.CharField(
        max_length=50,
        choices=DEPARTMENT_CHOICES
    )
    max_marks = models.PositiveIntegerField(default=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
            return f"{self.name} ({self.get_department_display()})"

    
class Marks(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='marks'
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='marks'
    )

    marks_obtained = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student','subject')

    def __str__(self):
                return f"{self.student.name} - {self.subject.name}: {self.marks_obtained}"
    
class Attendance(models.Model):
     STATUS_CHOICES = (
          ('P','Present'),
          ('A', 'Absent'),
     )

     student = models.ForeignKey(
          Student,
          on_delete=models.CASCADE,
          related_name='attendance'
          )
     date = models.DateField()
     status = models.CharField(
        max_length=1,
        choices= STATUS_CHOICES
     )
     created_at = models.DateTimeField(auto_now_add=True)

     class Meta:
          unique_together = ('student', 'date')
          ordering = ['-date']

     def __str__(self):
         return f"{self.student.name} - {self.date} - {self.get_status_display()}"


    
