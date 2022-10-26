from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    maximum = serializers.FloatField()
    minimum = serializers.FloatField()
    average = serializers.FloatField()
    median = serializers.FloatField()

class WeatherInputSerializer(serializers.Serializer):
    city = serializers.CharField()
    days = serializers.IntegerField()