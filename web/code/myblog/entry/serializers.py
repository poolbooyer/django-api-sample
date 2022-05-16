from rest_framework import serializers
from entry.models import Entry

class EntrySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False,allow_blank=False,max_length=100)
    body = serializers.CharField()

    def create(self, validated_data):
        return Entry.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data('title',instance.title)
        instance.body = validated_data('body', instance.body)
        instance.save() 
        return instance
