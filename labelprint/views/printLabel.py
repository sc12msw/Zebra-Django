from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from labelprint.models import Printer
from django.core.exceptions import ObjectDoesNotExist
import socket


class PrinterHandle(APIView):
    """
    A view that can accept POST requests with JSON content.
    """
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer,)

    # Respond with number of printers available on GET
    def get(self, request, format=None):
        printer_count = Printer.objects.count()
        content = {'printer_count': printer_count}
        return Response(content)

    # Post JSON to server check if printer exists and print
    def post(self, request, format=None):
        data = request.data
        # Search for printer by name if exists in DB get printer ip
        try:
            printer = Printer.objects.get(name=data['printer'])
            TCP_IP = printer.ip
            TCP_PORT = printer.port
        except ObjectDoesNotExist:
            return Response({'Error': 'This printer does not exist'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            barcode = data['barcode']
            product = data['product']
            zplraw = printer.label_zpl
            if (data['printer'] == 'Small'):
                zpl = zplraw.format(barcode=barcode)
            else:
                zpl = zplraw.format(product=product, barcode=barcode)

        except KeyError:
            return Response({'Error': 'String formatting incorrect' },
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TCP_IP, TCP_PORT))
            s.send(bytes(zpl, "utf-8"))
            s.close()
        except socket.error:
            print('Print Error Occured')
            return Response({'Error':'Printer Not Found'},
                            status=status.HTTP_404_NOT_FOUND)

        return Response({'Message': 'Data sent to printer'},
                        status=status.HTTP_200_OK)
