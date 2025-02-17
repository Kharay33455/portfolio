from django.db import models

# Create your models here.

class PageData(models.Model):
    project = models.CharField(max_length=100)
    page = models.CharField(max_length=100)
    screenshotPhone = models.ImageField(upload_to='screenshot/')
    screenshotiPad = models.ImageField(upload_to='screenshot/')
    screenshotLaptop = models.ImageField(upload_to='screenshot/')
    

    def __str__(self):
        return f'Project {self.project}'
    
class Image(models.Model):
    page = models.ForeignKey(PageData, on_delete= models.CASCADE)
    file = models.FileField(upload_to='file', null=True, blank=True)
    image = models.ImageField(upload_to='projectImages')
    associatedText = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.page} picture'
    
class Text(models.Model):
    page = models.ForeignKey(PageData, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'Text for {self.page}'

