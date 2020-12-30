from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import (ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	)
from . models import (
	Article,
	PublicProcurement,
	Vacancy,
	)
from .forms import (
	PublicProcurementCreateForm,
	VacancyCreateForm
)

def home(request):
	context = {
		'article': Article.objects.all()
	}
	return render(request, 'article/home.html', context)

class ArticleListView(ListView):
	model = Article
	template_name = 'article/home.html'
	context_object_name = 'article'
	ordering = ['-date_posted']
	paginate_by = 5

class UserPostListView(ListView):
	model = Article
	template_name = 'blog/user_post.html'
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Article.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Article

class ArticleCreateView(LoginRequiredMixin, CreateView):
	model = Article
	fields = ['title',
			  'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PublicProcurementCreateView(CreateView):
	form_class = PublicProcurementCreateForm
	template_name = 'screendisplay/publicprocurement_form.html'

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)

class PublicProcurementListView(ListView):
	model = PublicProcurement
	template_name = 'screendisplay/publicproocurement_list.html'
	context_object_name = 'publicprocurement-list'
	ordering = ['-date_posted']
	paginate_by = 5


## VACANCY VIEWS STARTS HERE

class VacancyCreateView(CreateView):
	form_class = VacancyCreateForm
	template_name = 'screendisplay/vacancy_form.html'

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)

class VacancyListView(ListView):
	model = Vacancy
	template_name = 'screendisplay/vacancy_list.html'
	context_object_name = 'vacancy-list'