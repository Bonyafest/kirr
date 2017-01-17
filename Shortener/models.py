from django.db import models
from .utils import urlGenerator,shortcodeGenerator

class KirrURL(models.Model):
    url         = models.CharField(max_length=220,)
    shortenurl  = models.CharField(max_length=15,default='defaultvalue',unique=True,blank=True,null=False)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    
    def save(self,*args,**kwargs):
        if self.shortenurl is None or self.shortenurl == '':
            self.shortenurl = shortcodeGenerator(self)
        super(KirrURL,self).save(*args,**kwargs)
    def __str__(self):
        return str(self.url)

    