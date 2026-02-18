#!/usr/bin/env python3
"""Module that provides a function to safely get a value from a mapping."""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Return the value from the mapping for the given key if it exists.
    Otherwise, return the default value.
    """
    if key in dct:
        return dct[key]
    return default
