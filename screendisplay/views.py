from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
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
	Official,
	OfficeInfo,
	)
from .forms import (
	PublicProcurementCreateForm,
	VacancyCreateForm,
	OfficialCreateForm,
	OfficeCreateForm,
)

class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if(not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
        if not self.has_permission():
            return redirect('/')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)


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
	context_object_name = 'publicprocurement_list'

class PublicProcurementDetailView(DetailView):
	model = PublicProcurement

class PublicProcurementUpdateView(UserAccessMixin, UpdateView):
    raise_exception = False
    permission_required = 'screendisplay.change_publicprocurement'
    permission_denied_message = ""
    login_url = 'procurement/list/'
    redirect_field_name = 'next'

    model = PublicProcurement
    fields = ['publicprocurement_title', 'publicprocurement_image', 'published_status', 'website_link']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class PublicProcurementDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    permission_required = 'screendisplay.delete_publicprocurement'
    model = PublicProcurement
    success_url = '/publicprocurement/list/'

## VACANCY VIEWS STARTS HERE

class VacancyCreateView(LoginRequiredMixin, CreateView):
	form_class = VacancyCreateForm
	template_name = 'screendisplay/vacancy_form.html'

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)

class VacancyListView(ListView):
	model = Vacancy
	template_name = 'screendisplay/vacancy_list.html'
	context_object_name = 'vacancy_list'

class VacancyDetailView(DetailView):
	model = Vacancy


class VacancyUpdateView(UserAccessMixin, UpdateView):
	raise_exception = False
	permission_required = 'screendisplay.change_vacancy'
	permission_denied_message = ""
	login_url = '/vacancy/list/'
	redirect_field_name = 'next'

	model = Vacancy
	fields = ['vacancy_title', 'vacancy_image', 'vacancy_published_status', 'vacancy_website_link']

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)

class VacancyDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
	permission_required = 'screendisplay.delete_vacancy'
	model = Vacancy
	success_url = '/vacancy/list/'

## OFFICIAL VIEWS STARTS HERE

class OfficialCreateView(LoginRequiredMixin, CreateView):
	form_class = OfficialCreateForm
	template_name = 'screendisplay/official_form.html'

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)

# class OfficialListView(ListView):
# 	model = Official
# 	template_name = 'screendisplay/official_list.html'
# 	context_object_name = 'official_list'

class OfficialListView(ListView):
	model = Official
	template_name = 'screendisplay/official_list.html'
	context_object_name = 'official_list'

class OfficialDetailView(DetailView):
	model = Official


class OfficialUpdateView(UserAccessMixin, UpdateView):
	raise_exception = False
	permission_required = 'screendisplay.change_official'
	permission_denied_message = ""
	login_url = '/official/list/'
	redirect_field_name = 'next'

	model = Official
	fields = ['official_name', 'official_designation', 'official_phoneno', 'official_roomno', 'official_published_status', 'official_image']

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)


class OfficialDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
	permission_required = 'screendisplay.delete_official'
	model = Official
	success_url = '/official/list/'





## Office Information VIEWS STARTS HERE

class OfficeCreateView(LoginRequiredMixin, CreateView):
	form_class = OfficeCreateForm
	template_name = 'screendisplay/office_form.html'

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)

class OfficeListView(ListView):
	model = OfficeInfo
	template_name = 'screendisplay/office_list.html'
	context_object_name = 'office_list'

class OfficeListView(ListView):
	model = OfficeInfo
	template_name = 'screendisplay/office_list.html'
	context_object_name = 'office_list'
#
class OfficeDetailView(DetailView):
	model = OfficeInfo
#
#
# class OfficialUpdateView(UserAccessMixin, UpdateView):
# 	raise_exception = False
# 	permission_required = 'screendisplay.change_official'
# 	permission_denied_message = ""
# 	login_url = '/official/list/'
# 	redirect_field_name = 'next'
#
# 	model = Official
# 	fields = ['official_name', 'official_designation', 'official_phoneno', 'official_roomno', 'official_published_status', 'official_image']
#
# 	def form_valid(self, form):
# 		form.instance.created_by = self.request.user
# 		return super().form_valid(form)
#
#
# class OfficialDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
# 	permission_required = 'screendisplay.delete_official'
# 	model = Official
# 	success_url = '/official/list/'

# GET MORE THAN ONE VIEW TO RENDER IN SINGLE PAGE,

# class AlldataView(LoginRequiredMixin, ListView):
# 	template_name = 'screendisplay/article_list.html'
# 	queryset = Official.objects.all()
#
# 	def get_context_data(self, **kwargs):
# 		context = super(AlldataView, self).get_context_data(**kwargs)
# 		context['vacancy_list'] = Vacancy.objects.all()
# 		context['official_list'] = self.queryset
# 		return context

# class AlldataListView(LoginRequiredMixin, ListView):
#     template_name = 'officialdata/allofficialdata_list.html'
#     queryset = Servicegroup.objects.all()
#
#     def get_context_data(self, **kwargs):
#         context = super(AllOfficialdataListView, self).get_context_data(**kwargs)
#         context['designation_list'] = Designation.objects.all()
#         context['sectiontype_list'] = Sectiontype.objects.all()
#         context['employeetype_list'] = Employeetype.objects.all()
#         context['servicegroup_list'] = self.queryset
#         return context


class AlldisplaydataListView(ListView):
	template_name = 'screendisplay/data_list.html'
	queryset = Vacancy.objects.all()

	def get_context_data(self, **kwargs):
		context = super(AlldisplaydataListView, self).get_context_data(**kwargs)
		context['official_list'] = Official.objects.all()
		context['publicprocurement_list'] = PublicProcurement.objects.all()
		context['officeinfo_list'] = OfficeInfo.objects.all()
		context['vacancy_list'] = self.queryset
		return context