from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from .models import Doctor
from .serializers import DoctorSerializer


class DoctorListCreateView(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.AllowAny]
    ordering_fields = ["full_name", "specialty", "created_at"]

    def get_queryset(self):
        queryset = Doctor.objects.all()
        search = self.request.query_params.get("search", "").strip()
        disease_id = self.request.query_params.get("disease", "").strip()
        ordering = self.request.query_params.get("ordering", "full_name").strip()

        if search:
            queryset = queryset.filter(Q(full_name__icontains=search) | Q(email__icontains=search))
      
        if disease_id:
            queryset = queryset.filter(diseases__id=disease_id)
        if ordering in ["full_name", "-full_name",  "created_at", "-created_at"]:
            queryset = queryset.order_by(ordering)
        return queryset.distinct()


class DoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Doctor.objects.all()

    def get_object(self):
        key = self.kwargs.get("pk")
        queryset = self.get_queryset()
        obj = queryset.filter(pk=key).first() or queryset.filter(email__iexact=key).first()
        if obj is None:
            obj = get_object_or_404(queryset, pk=key)
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_destroy(self, instance):
        instance.delete()
