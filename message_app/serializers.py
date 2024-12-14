from rest_framework import serializers
from .models import messages_data

class MessagesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = messages_data
        fields = '__all__'