from rest_framework import serializers


class TemperatureSerializer(serializers.Serializer):
    """ temperature serializer Class"""
    city = serializers.CharField(
        max_length=50,
        required=True,
        allow_null=False)
    days = serializers.IntegerField(
        required=True,
    )
    maximum = serializers.FloatField(read_only=True)
    minimum = serializers.FloatField(read_only=True)
    average = serializers.FloatField(read_only=True)
    median = serializers.FloatField(read_only=True)
