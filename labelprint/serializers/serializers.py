from labelprint.models import Printer
from rest_framework import serializers


class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printer
        fields = ('name', 'ip', 'labe_zpl')
