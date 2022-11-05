from rest_framework import serializers
from home.models import Contact
import re


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        # fields='__all__'
        exclude = ['id', 'date']

    def validate(self, validated_data):
        if validated_data.get('name'):
            name = validated_data['name']
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if not regex.search(name) == None:
                raise serializers.ValidationError('Special characters are not allowed')

        return validated_data
