from django.db import models

# Create your models here.


class Printer (models.Model):
    name = models.CharField(max_length=50, default="Unassigned")
    ip = models.GenericIPAddressField(default="1.1.1.1")
    label_zpl = models.TextField(default="""^XA
                                            ^LH30,30
                                            ^FO20,10
                                            ^ADN,90,50
                                            ^AD^FDYour Company^FS
                                            ^XZ""")
    port = models.IntegerField(default=9100)

    def __str__(self):
        return self.name
