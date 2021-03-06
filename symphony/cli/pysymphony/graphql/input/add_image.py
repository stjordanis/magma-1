#!/usr/bin/env python3
# @generated AUTOGENERATED file. Do not Change!

from dataclasses import dataclass
from datetime import datetime
from functools import partial
from gql.gql.datetime_utils import DATETIME_FIELD
from numbers import Number
from typing import Any, Callable, List, Mapping, Optional

from dataclasses_json import DataClassJsonMixin

from gql.gql.enum_utils import enum_field
from ..enum.image_entity import ImageEntity

@dataclass
class AddImageInput(DataClassJsonMixin):
    entityId: str
    imgKey: str
    fileName: str
    fileSize: int
    contentType: str
    entityType: ImageEntity = enum_field(ImageEntity)
    modified: datetime = DATETIME_FIELD
    category: Optional[str] = None
    annotation: Optional[str] = None

