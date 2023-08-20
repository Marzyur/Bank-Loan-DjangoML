from rest_framework import serializers
from .models import Approval
class approvalSerializers(serializers.ModelSerializer):
    class Meta:
        model=Approval
        fields='__all__'
        
