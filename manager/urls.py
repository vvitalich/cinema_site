from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import FilmListView, FilmDetailView, FilmCreateView, FilmUpdateView, FilmDeleteView
from .views import FilmListCreateViewSet, PersonListCreateViewSet, RoleListCreateViewSet, TeamMemberListCreateViewSet


router = DefaultRouter()
router.register(r'films', FilmListCreateViewSet)
router.register(r'persons', PersonListCreateViewSet)
router.register(r'roles', RoleListCreateViewSet)
router.register(r'team-members', TeamMemberListCreateViewSet)

urlpatterns = [
    path('', FilmListView.as_view(), name='list-films'),
    path('<int:pk>/', FilmDetailView.as_view(), name='film-details'),
    path('create/', FilmCreateView.as_view(), name='film-create'),
    path('<int:pk>/update/', FilmUpdateView.as_view(), name='film-update'),
    path('<int:pk>/delete/', FilmDeleteView.as_view(), name='film-delete'),
    path('search/',  FilmListView.as_view(), name='film-search'),

    path('api/', include(router.urls)),

]

