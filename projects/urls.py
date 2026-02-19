from django.urls import path
from .views import (
    ProjectListCreateView,
    ProposalCreateView,
    ProjectProposalListView
)

urlpatterns = [
    path('', ProjectListCreateView.as_view(), name='project-list-create'),
    path('<int:pk>/proposals/', ProjectProposalListView.as_view(), name='project-proposals'),
    path('proposals/create/', ProposalCreateView.as_view(), name='proposal-create'),
]
