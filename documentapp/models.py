from django.db import models

# Create your models here.

class document(models.Model):
    cClassName = models.CharField(max_length=100, null=False)
    cClassDescription = models.CharField(max_length=300, null=False)
    cClassOverview = models.CharField(max_length=1000, null=False)
    cAuthor = models.CharField(max_length=50, null=True)
    cCreateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cClassName

class functionModel(models.Model):
    fdocument = models.ForeignKey('document', on_delete=models.CASCADE)
    functionName = models.CharField(max_length=300, null=False)
    functionDescription = models.CharField(max_length=500, null=False)
    
    def __str__(self):
        return self.functionName