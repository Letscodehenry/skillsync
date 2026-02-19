from rest_framework import serializers
from .models import Project, Proposal
from users.models import Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.username')
    required_skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProposalSerializer(serializers.ModelSerializer):
    freelancer = serializers.ReadOnlyField(source='freelancer.username')

    class Meta:
        model = Proposal
        fields = '__all__'
