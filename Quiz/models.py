from django.db import models

# Create your models here.


# Create your models here.
class Qtype(models.Model):
    qt_id = models.AutoField(primary_key=True, db_column='qt_id')

    qt_title = models.CharField('Title', max_length=255)  
    def __str__(self):
        return self.qt_title