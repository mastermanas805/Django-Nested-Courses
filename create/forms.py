from django.forms import ModelForm
from django.forms import formset_factory, inlineformset_factory,modelformset_factory
from .models import courses, topics, sub_topics, course_to_topics, topics_to_subtopics

class CourseForm(ModelForm):
    class Meta:
        model = courses
        fields = ['name',]
        exclude = ()


class TopicForm(ModelForm):
    class Meta:
        model = topics
        fields = ['name',]
        exclude = ('course',)


class Sub_TopicForm(ModelForm):
    class Meta:
        model = sub_topics
        fields = ['name',]
        exclude = ('topic',)

# courseform = modelformset_factory(courses,form = CourseForm,min_num = 1)
# topicform = modelformset_factory(topics,form = TopicForm,min_num = 1)
# sub_topicsform = modelformset_factory(sub_topics,form = Sub_TopicForm,min_num = 1)

TopicFormset = inlineformset_factory(courses, topics, fields=('name',),extra =1)
Sub_TopicFormset = inlineformset_factory(topics, sub_topics, fields=('name',),extra = 1)
