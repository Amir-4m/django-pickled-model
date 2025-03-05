from rest_framework import views
from rest_framework.response import Response

from ..models import Pickle


class PicklesAPIView(views.APIView):
    """Shows init configs params"""

    def get(self, request, *args, **kwargs):
        configs = Pickle.objects.all()
        data = {}
        if configs:
            for config in configs:
                data.update({config.name: config.value})
        return Response(data)
