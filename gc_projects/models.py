from distutils.command.upload import upload
from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200, null = False, blank = False)
    description = models.TextField(null=False, blank=False)
    cover_image = models.ImageField(upload_to = '3d_models_images')
    other_image1 = models.ImageField(upload_to = '3d_models_images', null = True, blank = True)
    other_image2 = models.ImageField(upload_to = '3d_models_images', null = True, blank = True)
    other_image3 = models.ImageField(upload_to = '3d_models_images', null = True, blank = True)
    other_image4 = models.ImageField(upload_to = '3d_models_images', null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_created']

    @property
    def ImageUrl1(self):
        try:
            url = self.other_image1.url
        except:
            url = ''
        return url
    @property
    def ImageUrl2(self):
        try:
            url = self.other_image2.url
        except:
            url = ''
        return url

    @property
    def ImageUrl3(self):
        try:
            url = self.other_image3.url
        except:
            url = ''
        return url

    @property
    def ImageUrl4(self):
        try:
            url = self.other_image4.url
        except:
            url = ''
        return url