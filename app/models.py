#coding=utf-8
from django.db import models

class UserFeedback(models.Model):
    name = models.CharField(u"姓名", max_length=50)
    email = models.EmailField(u"邮箱")
    title = models.CharField(u"主题", max_length=100)
    content = models.TextField(u"内容")
    
    class Meta:
        verbose_name = u"用户反馈"
        verbose_name_plural = u"用户反馈"
        
    def __unicode__(self):
        return self.title