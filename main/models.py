from django.db import models

# Create your models here.

class Query(models.Model):
    text = models.TextField()
    contact = models.CharField(max_length=200, null=True)

    def __str__(self):
        return 'Query ' + str(self.id)

class Mark(models.Model):
    line_no = models.IntegerField()
    line_id = models.IntegerField()
    line_mark = models.IntegerField()
    query = models.ForeignKey('Query', null=False, on_delete=models.CASCADE)
