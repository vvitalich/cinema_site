from rest_framework import viewsets, pagination
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.shortcuts import redirect
from .models import Film, Person, Role, TeamMember
from .serializers import FilmSerializer, PersonSerializer, RoleSerializer, TeamMemberSerializer
from .forms import FilmForm, TeamMemberForm, FilmUpdateForm, TeamMemberUpdateForm


class FilmListView(ListView):
    model = Film
    template_name = 'film_list.html'
    context_object_name = 'films'
    paginate_by = 25

    def get_queryset(self):
        queryset = super().get_queryset()
        year = self.request.GET.get('year')
        title = self.request.GET.get('title')
        actor = self.request.GET.get('actor')

        if year:
            queryset = queryset.filter(release_year=year)
        if title:
            queryset = queryset.filter(title__icontains=title)
        if actor:
            queryset = queryset.filter(team__name__icontains=actor)

        return queryset.distinct()


class FilmDetailView(DetailView):
    model = Film
    template_name = 'film_detail.html'
    context_object_name = 'film'


class FilmCreateView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'film_create.html'
    success_url = reverse_lazy('list-films')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['roles'] = Role.objects.all()
        context['team_member_form'] = TeamMemberForm()
        return context

    def form_valid(self, form):
        film = form.save()

        participants = self.request.POST.getlist('participant_name[]')
        roles = self.request.POST.getlist('participant_role[]')
        for participant, role_id in zip(participants, roles):
            person, created = Person.objects.get_or_create(name=participant)
            role = Role.objects.get(id=role_id)
            team_member = TeamMember.objects.create(person=person, film=film)
            team_member.roles.add(role)

        return super().form_valid(form)


class FilmUpdateView(UpdateView):
    model = Film
    template_name = 'film_update.html'
    form_class = FilmUpdateForm
    success_url = reverse_lazy('list-films')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        TeamMemberFormSet = inlineformset_factory(Film, TeamMember, form=TeamMemberUpdateForm, extra=1)
        if self.request.POST:
            context['team_member_formset'] = TeamMemberFormSet(self.request.POST, instance=self.object)
        else:
            context['team_member_formset'] = TeamMemberFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        team_member_formset = context['team_member_formset']
        if team_member_formset.is_valid():
            self.object = form.save()
            team_member_formset.instance = self.object
            team_member_formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class FilmDeleteView(DeleteView):
    model = Film
    template_name = 'film_confirm_delete.html'
    success_url = reverse_lazy('list-films')


class CustomPagination(pagination.PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 1000


class FilmListCreateViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    pagination_class = CustomPagination


class PersonListCreateViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = CustomPagination


class RoleListCreateViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    pagination_class = CustomPagination


class TeamMemberListCreateViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    pagination_class = CustomPagination

