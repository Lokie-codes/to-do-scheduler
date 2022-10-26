from rest_framework import serializers

class taskSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'status', 'time', 'due_date']
