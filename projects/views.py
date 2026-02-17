from rest_framework import generics, permissions
from .models import Project,Proposal
from .serializers import ProjectSerializer, ProposalSerializer
from rest_framework.permissions import IsAuthenticated

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

class ProposalCreateView(generics.CreateAPIView):
    serializer_class = ProposalSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(freelancer=self.request.user)

class ProjectProposalListView(generics.ListAPIView):
    serializer_class = ProposalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs['pk']
        return Proposal.objects.filter(project_id=project_id)