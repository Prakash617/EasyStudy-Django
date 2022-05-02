
from django.db import models

# Create your models here.
SCHOOL_LEVEL = (
    ("one", "one"),
    ("two", "two"),
    ("Four", "Four"),
    ("Five", "Five"),
    ("Six", "Six"),
    ("Seven", "Seven"),
    ("Eight", "Eight"),
    ("Nine", "Nine"),
    ("Ten", "Ten"),
    ("Eleven", "Eleven"),
    ("Twelve", "Twelve"),
  
)

BACHELOR_LEVEL = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)

MASTER_LEVEL = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)

class School(models.Model):
    level = models.CharField(max_length=50, choices= SCHOOL_LEVEL)
    
    def __str__(self):
        return self.level
    
class Bachelor(models.Model):
    level = models.CharField(max_length=50, choices= SCHOOL_LEVEL)
    
    def __str__(self):
        return self.level
    
class Master(models.Model):
    level = models.CharField(max_length=50, choices= SCHOOL_LEVEL)
    
    def __str__(self):
        return self.level
class Faculty(models.Model):
    level = models.CharField(max_length=50, choices= SCHOOL_LEVEL)
    
    def __str__(self):
        return self.level
class Semister(models.Model):
    level = models.CharField(max_length=50, choices= SCHOOL_LEVEL)
    
    def __str__(self):
        return self.level
class Subjects(models.Model):
    
    schoolLEVEL = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, blank=True)
    schoolSubjects = models.CharField(max_length=100)
    # Master_subjects = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.schoolSubjects
    
    
class Syllabus(models.Model):
    SyllabusSubjects = models.OneToOneField(Subjects,on_delete=models.SET_NULL, null=True, blank=True)
    syllabus_Name = models.CharField( max_length=50)
    syllabus_pic = models.ImageField(upload_to = 'syllabus_pic')

    
    def __str__(self):
        return self.syllabus
    
class Master(models.Model):
    level = models.CharField(max_length=50, choices= SCHOOL_LEVEL)
    
    def __str__(self):
        return self.level
class QuestionBank(models.Model):
    Subjects = models.OneToOneField(Subjects,on_delete=models.SET_NULL, null=True, blank=True)
    questionBank = models.CharField( max_length=50)
    
    def __str__(self):
        return self.questionBank
class Other_Notes(models.Model):
    Subjects = models.ForeignKey(Subjects,on_delete=models.CASCADE, null=True, blank=True)
    note_name = models.CharField(max_length=50)
    note_urls = models.URLField(max_length=200)
    
    def __str__(self):
        return self.note_name
    
class Official_Note(models.Model):
    level = models.CharField(max_length=50, choices= SCHOOL_LEVEL)
    
    def __str__(self):
        return self.level
class Chapter(models.Model):
    level = models.CharField(max_length=50, choices= SCHOOL_LEVEL)
    
    def __str__(self):
        return self.level
class Topic(models.Model):
    level = models.CharField(max_length=50, choices= SCHOOL_LEVEL)
    
    def __str__(self):
        return self.level
class Discriptions(models.Model):
    level = models.CharField(max_length=50, choices= SCHOOL_LEVEL)
    
    def __str__(self):
        return self.level
class Table(models.Model):
    level = models.CharField(max_length=50, choices= SCHOOL_LEVEL)
    
    def __str__(self):
        return self.level
class Note_Video(models.Model):
    level = models.CharField(max_length=50, choices= SCHOOL_LEVEL)
    
    def __str__(self):
        return self.level
class Diagram(models.Model):
    level = models.CharField(max_length=50, choices= SCHOOL_LEVEL)
    
    def __str__(self):
        return self.level
class Official_Comments(models.Model):
    level = models.CharField(max_length=50, choices= SCHOOL_LEVEL)
    
    def __str__(self):
        return self.level
class Other_Notes(models.Model):
    level = models.CharField(max_length=50, choices= SCHOOL_LEVEL)
    
    def __str__(self):
        return self.level
class Files(models.Model):
    level = models.CharField(max_length=50, choices= SCHOOL_LEVEL)
    
    def __str__(self):
        return self.level
class Comments(models.Model):
    level = models.CharField(max_length=50, choices= SCHOOL_LEVEL)
    
    def __str__(self):
        return self.level
# class Other_Notes(models.Model):
#     level = models.CharField(max_length=50, choices= SCHOOL_LEVEL)
    
#     def __str__(self):
#         return self.level
    
