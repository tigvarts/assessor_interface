from django.db import models

# Create your models here.

class Query(models.Model):
    text = models.TextField()
    contact = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    version = models.ForeignKey('Version', null=True)

    def __str__(self):
        return 'Query ' + str(self.id)

class Mark(models.Model):
    line_no = models.IntegerField()
    line_id = models.IntegerField()
    line_mark = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    version = models.ForeignKey('Version', null=True)
    query = models.ForeignKey('Query', null=False, on_delete=models.CASCADE)

class CatImage(models.Model):
    url = models.CharField(max_length=400)

    def __str__(self):
        return self.url

class Version(models.Model):
    occured_at = models.DateTimeField(auto_now_add = True)
    short_description = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return str(self.occured_at) + ' ' + self.short_description

    def get_current_version():
        if Version.objects.count() == 0:
            return None
        else:
            return Version.objects.all()[Version.objects.count() - 1]
