from django.utils import timezone

from rest_framework.viewsets import ModelViewSet
from library.models import Event
from library.serializers import EventSerializer

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        event_type = self.request.query_params.get('type')
        library = self.request.query_params.get('library')
        if event_type == 'future':
            queryset = queryset.filter(date__gt=timezone.now())
        if event_type == 'past':
            queryset = queryset.filter(date__lt=timezone.now())
        if library:
            queryset = queryset.filter(library__name__iexact=library)

        return queryset


