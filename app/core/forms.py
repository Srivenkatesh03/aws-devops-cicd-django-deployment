from django import forms
from .models import Student, Marks, Attendance

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'age','department', 'roll_number', 'year' ,'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'roll_number': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),    
        }

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18 or age > 30:
            raise forms.ValidationError("Age must be between 10 to 30")
        return age
        
    def clean_roll_number(self):
        roll = self.cleaned_data.get('roll_number')
        if not roll.isdigit():
            raise forms.ValidationError("Roll number must contain only digits.")
        return roll
    
class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student','subject','marks_obtained']
        widgets =  {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'marks_obtained': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        def clean_marks_obtained(self):
            marks = self.cleaned_data.get('marks_obtained')
            subject = self.cleaned_data.get('subject')

            if subject and marks > subject.max_marks:
                raise forms.ValidationError(
                f"Marks cannot exceed {subject.max_marks} for this subject")
            
            return marks
        
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']
        widgets = {
            'student': forms.HiddenInput,
            'date': forms.HiddenInput,
            'status': forms.RadioSelect(choices=Attendance.STATUS_CHOICES)
        }