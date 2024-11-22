"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from openapi.utils import FieldMetadata
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ModelTypedDict(TypedDict):
    first_property: bool
    second_property: Nullable[bool]
    third_property: NotRequired[bool]
    fourth_property: NotRequired[Nullable[bool]]
    sixth_property: NotRequired[bool]


class Model(BaseModel):
    first_property: Annotated[
        bool,
        pydantic.Field(alias="firstProperty"),
        FieldMetadata(query=True, header=True, form=True),
    ]

    second_property: Annotated[
        Nullable[bool],
        pydantic.Field(alias="secondProperty"),
        FieldMetadata(query=True, header=True, form=True),
    ]

    third_property: Annotated[
        Optional[bool],
        pydantic.Field(alias="thirdProperty"),
        FieldMetadata(query=True, header=True, form=True),
    ] = None

    fourth_property: Annotated[
        OptionalNullable[bool],
        pydantic.Field(alias="fourthProperty"),
        FieldMetadata(query=True, header=True, form=True),
    ] = UNSET

    sixth_property: Annotated[
        Optional[bool],
        pydantic.Field(alias="sixthProperty"),
        FieldMetadata(query=True, header=True, form=True),
    ] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["thirdProperty", "fourthProperty", "sixthProperty"]
        nullable_fields = ["secondProperty", "fourthProperty"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
