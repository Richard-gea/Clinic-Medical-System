from rest_framework import generics, permissions

from .models import Appointment
from .serializers import AppointmentSerializer


class AppointmentListCreateView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Appointment.objects.all()

        status_filter = self.request.query_params.get("status")
        if status_filter:
            queryset = queryset.filter(status=status_filter)

        return queryset


class AppointmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.AllowAny]

    lookup_field = "id"
    lookup_url_kwarg = "id"

    def get_queryset(self):
        return Appointment.objects.all()

    def perform_destroy(self, instance):
        instance.delete()