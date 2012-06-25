from dist import *
try:
    from local import *
except ImportError:
    from warnings import warn
    warn('Local settings not found. Using local_sample settings.')
    from local_sample import *
