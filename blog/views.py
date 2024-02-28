from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import BlogPost
from skystore import settings


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content', 'preview_image')
    success_url = reverse_lazy('blog:list')
    extra_context = {
        'title': 'Добавить новую запись:'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogPostListView(ListView):
    model = BlogPost
    extra_context = {
        'title': 'Последнии записи в блоге:'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = BlogPost.objects.filter(is_published=True)
        return queryset


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        if self.object.views_count == 100:
            send_mail(subject="Отправка письма",
                      message=f'Поздравляю! У Вас 100 просмотров по записи "{self.object.title}" в блоге!',
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=['mr1993@bk.ru'],
                      fail_silently=False
                      )
        self.object.save()
        return self.object


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'preview_image')
    extra_context = {
        'title': 'Редактировать запись:'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', args=[self.kwargs.get('slug')])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:list')
    extra_context = {
        'title': 'Удаление записи:'
    }