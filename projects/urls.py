from django.urls import path
from .views import(
    ProjectListCreateView,
    ProposalCreateView,
    ProjectProposalListView
)

urlpatterns = [
    path('',ProjectListCreateView.as_view(), name='project-list-create'),
    path('<int:pk>/proposal/', ProjectProposalListView.as_view(), name='project-proposal'),
    path('proposal/create/', ProposalCreateView.as_view(), name='proposal-create'),
]