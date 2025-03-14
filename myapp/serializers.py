from rest_framework import serializers

from myapp.models import Users
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class AbstractUserSerializers(serializers.ModelSerializer):

    class Meta:
        model= User
        fields=['id','username','email','password']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
