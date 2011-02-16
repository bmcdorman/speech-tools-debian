# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_EST_Relation', [dirname(__file__)])
        except ImportError:
            import _EST_Relation
            return _EST_Relation
        if fp is not None:
            try:
                _mod = imp.load_module('_EST_Relation', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _EST_Relation = swig_import_helper()
    del swig_import_helper
else:
    import _EST_Relation
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


read_ok = _EST_Relation.read_ok
read_format_error = _EST_Relation.read_format_error
read_not_found_error = _EST_Relation.read_not_found_error
read_error = _EST_Relation.read_error
write_ok = _EST_Relation.write_ok
write_fail = _EST_Relation.write_fail
write_error = _EST_Relation.write_error
write_partial = _EST_Relation.write_partial
connect_ok = _EST_Relation.connect_ok
connect_not_found_error = _EST_Relation.connect_not_found_error
connect_not_allowed_error = _EST_Relation.connect_not_allowed_error
connect_system_error = _EST_Relation.connect_system_error
connect_error = _EST_Relation.connect_error
import EST_Item
class EST_Relation(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, EST_Relation, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, EST_Relation, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _EST_Relation.new_EST_Relation(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _EST_Relation.delete_EST_Relation
    __del__ = lambda self : None;
    def load(self, *args): return _EST_Relation.EST_Relation_load(self, *args)
    def save(self, *args): return _EST_Relation.EST_Relation_save(self, *args)
    def evaluate_item_features(self): return _EST_Relation.EST_Relation_evaluate_item_features(self)
    def clear(self): return _EST_Relation.EST_Relation_clear(self)
    def utt(self): return _EST_Relation.EST_Relation_utt(self)
    def set_utt(self, *args): return _EST_Relation.EST_Relation_set_utt(self, *args)
    def name(self): return _EST_Relation.EST_Relation_name(self)
    def head(self): return _EST_Relation.EST_Relation_head(self)
    def root(self): return _EST_Relation.EST_Relation_root(self)
    def tail(self): return _EST_Relation.EST_Relation_tail(self)
    def first(self): return _EST_Relation.EST_Relation_first(self)
    def first_leaf(self): return _EST_Relation.EST_Relation_first_leaf(self)
    def last(self): return _EST_Relation.EST_Relation_last(self)
    def last_leaf(self): return _EST_Relation.EST_Relation_last_leaf(self)
    def append(self, *args): return _EST_Relation.EST_Relation_append(self, *args)
    def prepend(self, *args): return _EST_Relation.EST_Relation_prepend(self, *args)
    def length(self): return _EST_Relation.EST_Relation_length(self)
    def empty(self): return _EST_Relation.EST_Relation_empty(self)
    def remove_item(self, *args): return _EST_Relation.EST_Relation_remove_item(self, *args)
    def remove_item_feature(self, *args): return _EST_Relation.EST_Relation_remove_item_feature(self, *args)
    def items(self): return _EST_Relation.EST_Relation_items(self)
EST_Relation_swigregister = _EST_Relation.EST_Relation_swigregister
EST_Relation_swigregister(EST_Relation)


def copy_relation(*args):
  return _EST_Relation.copy_relation(*args)
copy_relation = _EST_Relation.copy_relation


