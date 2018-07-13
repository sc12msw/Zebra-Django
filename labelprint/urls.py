from django.urls import path
from labelprint.views.printLabel import PrinterHandle

urlpatterns = [
    path('', PrinterHandle.as_view(), name='printer'),
]
