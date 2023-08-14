from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Choice, Submission, Question

class QuestionInline(admin.StackedInline):
    model = Question

class ChoiceInline(admin.StackedInline):
    model = Choice

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ["question_text"]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["choice_text", "question", "is_correct"]
    list_filter = ["is_correct", "question"]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
