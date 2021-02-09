from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    template_name = 'myapp/index.html'

    def get(self, request):
        return render(request, self.template_name)