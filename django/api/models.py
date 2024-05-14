from tastypie.resources import ModelResource
from shop.models import Category, Course
from .auth import CustomAuthentication
from tastypie.authorization import Authorization


# Create your models here.
class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name: str = 'categories'
        allowed_methods: list = ['get']


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name: str = 'courses'
        allowed_methods: list = ['get', 'post', 'delete']
        excludes: list = ['created_at', 'reviews_dty']
        authentication: CustomAuthentication = CustomAuthentication()
        authorization: Authorization = Authorization()

    # Эти манипуляции для того что бы добавить категорию к курсу, поскольку они связаны каскадно
    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle

    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category'] = bundle.obj.category
        return bundle

    # Сделать title заглавными, так можна пересчитывать цену к примеру
    def dehydrate_title(self, bundle):
        return bundle.data['title'].upper()
