from django.db import models

# Create your models here.
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class courses(models.Model):
    name  = models.CharField(max_length = 50)


class topics(models.Model):
    name  = models.CharField(max_length = 50)
    course = models.ForeignKey(courses,on_delete = models.CASCADE,null = True)

class sub_topics(models.Model):
    name  = models.CharField(max_length = 50)
    content = models.TextField(null = True)
    # pdf = models.FileField(null = True)
    # image = models.ImageField(null = True)
    topic = models.ForeignKey(topics,on_delete = models.CASCADE,null = True)

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
