from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, "uploader/upload.html", {
            "image_url": image_url
        })
    return render(request, "uploader/upload.html")

class UploadFileView(FormView):
    form_class = UploadFileForm
    template_name = 'uploader/upload_cls.html'
    success_url = 'myapp:index'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            # save the file
            file = request.FILES["file"]
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            return redirect(self.success_url)
        return render(request, self.template_name, {'form':form})