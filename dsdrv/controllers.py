from enum import Enum


class controllers(Enum):
    """The console generation of each controller type
"""
    DualShock4 = 8
    DualSense = 9

products = {
    "09cc": controllers.DualShock4,
    "0ce6": controllers.DualSense
}

def determineGenerationHidraw(input_device):
    productCode = "{:04x}".format(input_device.info.product)
    return products.get(productCode)
