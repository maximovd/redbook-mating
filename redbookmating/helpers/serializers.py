from rest_framework import serializers


class FilterSerializer(serializers.ModelSerializer):
    """Excluded for created_at, created_by, updated_at, updated_by,"""
    def __new__(cls, *args, **kwargs):
        meta = getattr(cls, 'Meta', None)
        # TODO Optimize this "if" condition
        exclude = getattr(meta, 'exclude', None)
        if isinstance(exclude, list) or isinstance(exclude, tuple):
            exclude = list(exclude) # noqa
            if 'created_at' not in exclude:
                exclude.append('created_at')
            if 'created_by' not in exclude:
                exclude.append('created_by')
            if 'updated_at' not in exclude:
                exclude.append('updated_at')
            if 'updated_by' not in exclude:
                exclude.append('updated_by')

        fields = getattr(meta, 'fields', None)

        if isinstance(fields, list) or isinstance(fields, tuple):
            fields = list(fields) # noqa
            if 'created_at' not in fields:
                fields.append('created_at')
            if 'created_by' not in fields:
                fields.append('created_by')
            if 'updated_at' not in fields:
                fields.append('updated_at')
            if 'updated_by' not in fields:
                fields.append('updated_by')
        elif fields == '__all__':
            del meta.fields
            setattr(meta, 'exclude', ('created_by', 'created_by', 'updated_at', 'updated_by'))
        return super().__new__(cls, *args, **kwargs)
