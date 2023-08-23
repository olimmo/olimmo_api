from rest_framework import status, viewsets
from rest_framework.response import Response

from myapi.tasks.lobstr.external_property_create_task import (
    create_external_property_task,
)


class LobstrExternalPropertyViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        run_id = request.data.get("id")
        source = request.data.get("cluster")

        if not run_id or not source:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        create_external_property_task.delay(run_id, source)

        return Response({"status": "Job started"}, status=status.HTTP_202_ACCEPTED)
