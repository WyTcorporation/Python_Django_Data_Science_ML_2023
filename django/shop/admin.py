from django.contrib import admin
from .models import Course, Category

admin.site.site_header = 'Courses Admin'
admin.site.site_title = 'My Courses'
admin.site.index_title = 'Welcome to Courses Admin panel'


class CoursesAdmin(admin.ModelAdmin):
    list_display: tuple = ('id', 'title', 'price', 'category')


class CoursesInline(admin.TabularInline):
    model = Course
    exclude = ['created_at']
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display: tuple = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapse']
        })
    ]
    inlines = [CoursesInline]


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CoursesAdmin)
