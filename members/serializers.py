from rest_framework import serializers
from .models import Members
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ["firstname", "lastname","completed", "timestamp", "updated", "user"]