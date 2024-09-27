from rest_framework import generics
from rest_framework.permissions import AllowAny

from habits.models import Habits
from habits.paginators import HabitsPagination
from habits.serializers import HabitsSerializers
from users.permissions import IsOwner


class HabitsCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitsSerializers
    queryset = Habits.objects.all()

    def perform_create(self, serializer):
        habits = serializer.save()
        habits.user = self.request.user
        habits.save()


class HabitsListAPIView(generics.ListAPIView):
    serializer_class = HabitsSerializers
    queryset = Habits.objects.all()
    pagination_class = HabitsPagination


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitsSerializers
    queryset = Habits.objects.all()
    permission_classes = [IsOwner]


class HabitsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitsSerializers
    queryset = Habits.objects.all()
    permission_classes = [IsOwner]


class HabitsDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitsSerializers
    queryset = Habits.objects.all()
    permission_classes = [IsOwner]


class HabitsPublicListAPIView(generics.ListAPIView):
    serializer_class = HabitsSerializers
    queryset = Habits.objects.filter(is_public=True)
    permission_classes = [AllowAny]
    pagination_class = HabitsPagination
