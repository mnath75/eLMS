from django.db import models

# Create your models here.
class Categorys(models.Model):
    category_id=models.AutoField(primary_key=True,db_column='category_id')
    category_title=models.CharField('Title',max_length=255)
    category_slug=models.SlugField('slug',max_length=255)
    category_short=models.TextField('short description',blank=True,null=True)
    category_createddate=models.DateTimeField('created',auto_now_add=True)
    class meta:
        verbose_name_plural='Categories'
    def __str__(self):
        return self.category_title
