from rest_framework import serializers

from .models import Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        #fields = '__all__'
        fields = ('id', 'name', 'color', 'birth_year')
