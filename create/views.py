from .forms import CourseForm,TopicFormset,Sub_TopicFormset, Upload
from .models import courses,topics,sub_topics, image
from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponse

class Create_Course_View(CreateView):
    model = courses
    form_class = CourseForm
    template_name = 'create/add.html'
    success_url = 'create/add.html'

    def form_valid(self, form):
        result = super(Create_Course_View, self).form_valid(form)

        topic_formset = TopicFormset(form.data, instance=self.object, prefix='topic_formset')

        if topic_formset.is_valid():
            topics = topic_formset.save()

        topics_count = 0

        for topic in topics:
            sub_topic_formset = Sub_TopicFormset(form.data, instance = topic, prefix='sub_topic_formset_%s'% topics_count)
            # x = sub_topic_formset.cleaned_data
            # print(x[0])
            print(sub_topic_formset.image())
            if sub_topic_formset.is_valid():
                sub_topic_formset.save()

            # if image.is_valid():
            #     image.save()
            # topics_count += 1

        return result

    def get_context_data(self, **kwargs):
        context = super(Create_Course_View, self).get_context_data(**kwargs)
        context['topic_formset'] = TopicFormset(prefix='topic_formset')
        context['sub_topic_formset'] = Sub_TopicFormset(prefix='sub_topic_formset_0')
        # context['image'] = upload_image
        # print(upload_image)
        return context


class upload_image(CreateView):
    model = image
    form_class = Upload
    template_name = 'create/upload.html'

    def form_valid(self, form):
        result = super(upload_image, self).form_valid(form)
        return result

    def get_context_data(self, **kwargs):
        context = super(upload_image, self).get_context_data(**kwargs)
        return context
