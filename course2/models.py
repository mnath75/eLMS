from django.db import models

# Create your models here.

class batchCategory(models.Model):
    cat_id=models.AutoField(primary_key=True,db_column='cat_id')
    cat_title=models.CharField('Title',max_length=255)
    cat_slug=models.SlugField('slug',max_length=255,null=True)
    cat_short=models.TextField('short description',blank=True,null=True)
    cat_createddate=models.DateTimeField('created',auto_now_add=True)
    class meta:
        verbose_name_plural='Batch-Categories'
    def __str__(self):
        return self.cat_title

class batchCourse(models.Model):
    bcr_id = models.AutoField(primary_key=True, db_column='bcr_id')
    bcr_categ = models.ManyToManyField(batchCategory,
                            verbose_name='Category',
                            db_column = 'bcr_categ',
                            related_name='courses',
                            
                            )
    bcr_title = models.CharField('Title', max_length=255)
    bcr_slug = models.SlugField('Slug', max_length=255)
    bcr_short = models.TextField('Short description', blank=True, null=True)
    bcr_long = models.TextField('Long description', blank=True, null=True)
    bcr_created_at = models.DateTimeField('Created at', auto_now_add=True)
    def __str__(self):
        return self.bcr_title        