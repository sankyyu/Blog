from django.contrib.auth.models import User
from rest_framework import serializers, viewsets,permissions
from rest_framework.response import Response
from blogpost.models import Blogpost


class BlogpsotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blogpost
        fields = ('title', 'author', 'body', 'slug')

class BlogpostSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = BlogpsotSerializer
    search_fields = 'title'

    def list(self, request):
        queryset = Blogpost.objects.all()

        search_param = self.request.query_params.get('title', None)
        if search_param is not None:
            queryset = Blogpost.objects.filter(title__contains=search_param)

        serializer = BlogpsotSerializer(queryset, many=True)
        return Response(serializer.data)