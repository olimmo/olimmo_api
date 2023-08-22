from rest_framework import status, viewsets
from rest_framework.response import Response


from myapi.tasks.lobstr.leboncoin.external_property_create_task import (
    create_external_property_task,
)


class LobstrLeboncoinExternalPropertyViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        run_id = request.data.get("id")
        if not run_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        create_external_property_task.delay(run_id)

        return Response({"status": "Job started"}, status=status.HTTP_202_ACCEPTED)
