from django.db import models
import os.path
#Photoのupload_toのpathを指定
def imagePath(instance,filename):

    fn, ext = os.path.splitext(filename)
    return "{presetname}/{id}{ext}".format(presetname=instance.preset,id=instance.pk, ext=ext)


class Preset(models.Model):
    title = models.CharField(max_length=32,primary_key=True,verbose_name='preset')

    def __str__(self):
        return self.title

class Photo(models.Model):
    preset = models.ForeignKey(Preset,on_delete=models.CASCADE)
    file = models.ImageField(upload_to='images/')
    upload_at = models.DateTimeField(auto_now_add=True)
