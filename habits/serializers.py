from rest_framework import serializers
from habits.models import Habits
from habits.validators import HabitsValidator


class HabitsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = "__all__"
        validators = [HabitsValidator]

    def validate(self, attrs):
        if attrs.get("related") and attrs.get("reward"):
            raise serializers.ValidationError(
                "Вы не можете выбрать связанную привычку и "
                "указать вознаграждение одновременно."
            )

        if attrs.get("duration") > 2:  # Поскольку duration в минутах
            raise serializers.ValidationError(
                "Время выполнения привычки не может превышать 120 секунд."
            )

        if attrs.get("related") and not attrs["related"].is_good:
            raise serializers.ValidationError(
                "Связанной привычкой может быть только приятная привычка."
            )

        if attrs.get("is_good") and (attrs.get("related") or attrs.get("reward")):
            raise serializers.ValidationError(
                "Приятной привычке нельзя присваивать "
                "связанную привычку или вознаграждение."
            )

        if attrs.get("periodicity") < 7:
            raise serializers.ValidationError(
                "Периодичность привычки не может быть реже 1 раза в 7 дней."
            )

        return attrs
