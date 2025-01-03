"""This module contains all custom exceptions or errors."""

from ._info import VERSION, AUTHOR

__all__ = ["FeaturesDataTypeInconsistentError", "NotFittedError"]
__version__ = VERSION
__author__ = AUTHOR


class FeaturesDataTypeInconsistentError(Exception):
    """Raised when any column of the input argument `x` has more than one
    datatype when calling the function `_validate_feature_dtype_consistency`.
    """
    pass


class NotFittedError(Exception):
    """Raised when attempting to call the class method `transform` before the
     `MissForest` model has been trained."""
    pass
