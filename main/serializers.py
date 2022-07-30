from rest_framework import serializers
from .models import Entry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'
        extra_fields = ['sno', 'name', 'service', 'date', 'check_in', 'check_out', 'service_man', 'cost']

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(EntrySerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields
        

