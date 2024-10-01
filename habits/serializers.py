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

        if attrs.get("duration") > 120:  # Поскольку duration в минутах
            raise serializers.ValidationError(
                "Время выполнения привычки не может превышать 120 минут."
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

        # Новая проверка на периодичность (целое число)
        if 7 > attrs.get("periodicity") > 0:
            raise serializers.ValidationError(
                "Периодичность привычки должна быть больше 7 дней."
            )

        return attrs
