from labelprint.models import Printer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.renderers import TemplateHTMLRenderer


# Home page view
class Home(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        allPrintersAvailable = Printer.objects.all()
        return Response({'printers': allPrintersAvailable},
                        template_name='labelprint/index.html')
