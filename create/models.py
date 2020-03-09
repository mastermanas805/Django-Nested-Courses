from django.db import models

# Create your models here.
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class courses(models.Model):
    name  = models.CharField(max_length = 50)


class topics(models.Model):
    name  = models.CharField(max_length = 50)
    sno   = models.PositiveIntegerField(default = 0)
    course = models.ForeignKey(courses,on_delete = models.CASCADE,null = True)

class sub_topics(models.Model):
    name  = models.CharField(max_length = 50)
    content = models.TextField(null = True)
    sno   = models.PositiveIntegerField(default = 0)
    image = models.ImageField(upload_to="images/")
    #pdf = models.FileField(null = True)
    topic = models.ForeignKey(topics,on_delete = models.CASCADE,null = True)

class image(models.Model):
    image = models.ImageField(upload_to=('images/'),blank=  True,null = True)
    #sub_topic = models.OneToOneField(sub_topics,on_delete = models.CASCADE,null = True)


class course_to_topics(models.Model):
    serial_no = models.IntegerField()
    course =  models.ForeignKey(courses ,related_name="course",
                                        on_delete = models.CASCADE,null = True)
    topic =  models.ForeignKey(topics ,related_name="topics",
                                        on_delete = models.CASCADE,null = True)

class topics_to_subtopics(models.Model):
        serial_no = models.IntegerField()
        topic =  models.ForeignKey(topics ,related_name="topic",
                                            on_delete = models.CASCADE,null = True)
        subtopic =  models.ForeignKey(sub_topics ,related_name="subtopics",
                                            on_delete = models.CASCADE,null = True)
