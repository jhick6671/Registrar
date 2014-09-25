from django.views import generic

# Create your views here.
class StudentView(generic.TemplateView):
    """ Loads the main page"""
    template_name = 'students/main.html'

# class NextView(generic.TemplateView):
#     """ Loads the next page"""
#     template_name = 'units/next.html'


