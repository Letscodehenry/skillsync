from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile,Skill


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password','user_type']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            user_type=validated_data['user_type']
        )
        return user
    
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

class ProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many = True)

    class Meta: 
        model = Profile
        fields = ['bio', 'profile_picture', 'hourly_rate', 'availability', 'skills']