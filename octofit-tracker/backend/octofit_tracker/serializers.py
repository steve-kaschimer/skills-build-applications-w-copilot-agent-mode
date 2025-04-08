from rest_framework import serializers
from .models import Team, Activity, Leaderboard, Workout
from bson import ObjectId
from octofit_tracker.models import User as OctofitUser

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)

class UserSerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField()  # Update to IntegerField to match the model's AutoField

    class Meta:
        model = OctofitUser
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField()  # Update to IntegerField to match the model's AutoField
    members = UserSerializer(many=True)

    class Meta:
        model = Team
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField()  # Update to IntegerField to match the model's AutoField
    user = ObjectIdField()

    class Meta:
        model = Activity
        fields = '__all__'

class LeaderboardSerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField()  # Update to IntegerField to match the model's AutoField
    user = UserSerializer()

    class Meta:
        model = Leaderboard
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField()  # Update to IntegerField to match the model's AutoField

    class Meta:
        model = Workout
        fields = '__all__'