    python -m django startproject base . (installation)
    
    python .\manage.py runserver (run server)

    python manage.py migrate (migration)

    python manage.py startapp shop (create app)

    python manage.py createsuperuser (create superuser)

    python manage.py makemigrations (create migrations all apps)

    python manage.py shell (open virtual shell)

        Examples:
        from shop.models import Category, Course
        Category.objects.all()

        new_category = Category(title='Programming')
        new_category.save()

        Category.objects.get(pk=1) - pk(primary key) = id
        Category.objects.get(id=1)
        Category.objects.get(id=1).title - etc
        Category.objects.filter(title='Programming')

        category = Category.objects.get(id=1)
        category.course_set.all()

        category.course_set.create(title='Complete Python Guide',description='Complete Python Guide Description',price=99.99,students_qty=100,reviews_dty=50)
        
        Course.objects.all()
        Course.objects.get(id=1)

    pip install django-tastypie

    python manage.py startapp api
