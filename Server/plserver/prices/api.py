from rest_framework import serializers, viewsets
from .models import Item
from django.contrib.auth.models import User

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        user = self.context['request'].user
        item = Item.objects.create(user=user, **validated_data)
        return item

    class Meta:
        model = Item
        fields = ('name', 'price', 'purchased', 'quantity', 'user')
    
    

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="prices:user-detail")

    class Meta:
        model = User
        fields = ('url', 'username')

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    

