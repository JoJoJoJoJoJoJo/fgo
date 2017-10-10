from rest_framework import serializers
from .models import Servant


class ServantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servant
        fields = ('id','name','classes','stars','skills','phantasm')