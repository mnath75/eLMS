from django.db import models

# Create your models here.
class CourseCategory(models.Model):
    category_id=models.AutoField(primary_key=True,db_column='category_id')
    category_title=models.CharField('Title',max_length=255)
    category_slug=models.SlugField('slug',max_length=255,null=True)
    category_short=models.TextField('short description',blank=True,null=True)
    category_createddate=models.DateTimeField('created',auto_now_add=True)
    class meta:
        verbose_name_plural='Categories'
    def __str__(self):
        return self.category_title

class Course(models.Model):
    cr_id = models.AutoField(primary_key=True, db_column='cr_id')
    cr_categ = models.ManyToManyField(CourseCategory,
                            verbose_name='Category',
                            db_column = 'cr_categ',
                            related_name='courses')
    cr_title = models.CharField('Title', max_length=255)
    cr_slug = models.SlugField('Slug', max_length=255)
    cr_short = models.TextField('Short description', blank=True, null=True)
    cr_long = models.TextField('Long description', blank=True, null=True)
    cr_created_at = models.DateTimeField('Created at', auto_now_add=True)