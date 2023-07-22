from rest_framework import serializers


def validate_method_name(value):
    if value.isupper():
        return value
    raise serializers.ValidationError("Method name must be in Upper Case.")
