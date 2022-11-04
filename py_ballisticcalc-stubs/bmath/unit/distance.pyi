# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# Variables with simple values

DistanceCentimeter = 16
DistanceFoot = 11
DistanceInch = 10
DistanceKilometer = 18
DistanceLine = 19
DistanceMeter = 17
DistanceMile = 13
DistanceMillimeter = 15
DistanceNauticalMile = 14
DistanceYard = 12

# functions

def __pyx_unpickle_Distance(*args, **kwargs): # real signature unknown
    pass

# classes

class Distance(object):
    # no doc
    def convert(self, units: int) -> Distance: # real signature unknown
        """
        Returns the value into the specified units
        :param units: Units consts
        :return: Units object in the specified units
        """
        pass

    def get_in(self, units: int) -> float: # real signature unknown
        """
        Converts the value in the specified units.
        Returns 0 if unit conversion is not possible.
        :param units: Units consts
        :return: float
        """
        pass

    def units(self) -> int: # real signature unknown
        """
        :return: default units
        """
        pass

    def value(self, units: int) -> float: # real signature unknown
        """
        :param units: Units consts
        :return: Value of the unit in the specified units
        """
        pass

    def __init__(self, value: float, units: int): # real signature unknown
        """
        Creates a units value, strongly recommended validate it with validate() method
        usage example: Convertor(value, units).validate()
        :param value: units value
        :param units: UnitsConvertor constsS
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self) -> str: # real signature unknown
        """
        :return: formatted value in default units
        """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000012BDDFF57A0>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000012BDC830A50>'

__spec__ = None # (!) real value is "ModuleSpec(name='py_ballisticcalc.bmath.unit.distance', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000012BDC830A50>, origin='C:\\\\Users\\\\Sergey\\\\PycharmProjects\\\\archer_ballistics_constructor\\\\venv11\\\\Lib\\\\site-packages\\\\py_ballisticcalc\\\\bmath\\\\unit\\\\distance.cp311-win_amd64.pyd')"

__test__ = {}

