from django.views.generic import DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Post

    
class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostUpdateView(UpdateView):
    model = Post
    fields = (
        "title",
        "body",
    )
    template_name = "post_edit.html"
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
    
class PostCreateView(CreateView):
    model = Post
    template_name = "post_create.html"
    success_url = reverse_lazy("home")
    fields = ("body", "author")