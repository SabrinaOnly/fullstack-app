from rest_framework import viewsets

from .models import Record
from .serializers import RecordSerializer


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all().order_by('-id')
    serializer_class = RecordSerializer