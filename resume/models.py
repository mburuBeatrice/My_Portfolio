from django.db import models



# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'media/')
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
    
    def save_image(self):
        self.save()