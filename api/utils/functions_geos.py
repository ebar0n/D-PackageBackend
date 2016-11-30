from decimal import Decimal

from django.contrib.gis.geos import GEOSGeometry


def calculate_price(shipment):
    price_base = shipment.shipmenttype.price
    price_package = shipment.packagetype.price

    if shipment.insured:
        price_insured_value = shipment.shipmenttype.price
    else:
        price_insured_value = Decimal(0)

    pnt1 = GEOSGeometry(shipment.origin)
    pnt2 = GEOSGeometry(shipment.destination)
    distance = pnt1.distance(pnt2) * 100
    price_km = Decimal(int(distance * 50))

    price_total = price_base + price_package + price_insured_value + price_km

    return price_total
