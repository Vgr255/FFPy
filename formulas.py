import types as _types
import constants as _constants

class _xattr:
    def __init__(self, func):
        self.func = func
    def __get__(self, instance, owner):
        def inner(*args, **kwargs):
            if instance is not None:
                args = (instance,) + args
            return self.func(*args, **kwargs)
        return inner

class _IterableNamespace(_types.SimpleNamespace):
    def __iter__(self):
        yield from self.__dict__

    __getitem__ = _xattr(getattr)
    __setitem__ = _xattr(setattr)
    __delitem__ = _xattr(delattr)

class _SummonMaker(type):
    def __prepare__(name, bases):
        return _IterableNamespace(__name__=name, __module__="summons")

    def __new__(meta, name, bases, namespace):
        if name == "Summon":
            return super().__new__(meta, name, bases, namespace.__dict__)
        if bases != (Summon,):
            raise TypeError("must subclass Summon")

        # I don't know how to do this right >_>
        #for item in namespace:
        #    pass

        return super().__new__(meta, name, bases, namespace.__dict__)

    def __call__(cls, *args, **kwargs):
        raise TypeError("%r object is not callable" % cls)

class AttackGenerator:
    def __init__(self, **kwargs):
        self.attributes = _types.SimpleNamespace()
        self.attributes.type = None
        self.attributes.element = None
        self.attributes.name = ""

        for attributes in kwargs.items():
            setattr(self.attributes, *attributes)

class Summon(metaclass=_SummonMaker):
    """Base class to create summons."""
