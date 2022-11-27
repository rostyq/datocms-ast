from typing import Literal, TypedDict, NewType

from ..types.relationships import FieldId, FieldSetId, ItemId, WorkflowId


__all__ = [
    "ModelId",
    "Model",
    "Attributes",
    "Id",
    "FieldId",
    "FieldSetId",
    "WorkflowId",
    "ItemId",
    "Fields",
    "FieldSets",
    "Relationships",
]

ModelId = NewType("ModelId", str)

class Attributes(TypedDict):
    name: str
    api_key: str
    singleton: bool
    sortable: bool
    modular_block: bool
    tree: bool
    ordering_direction: Literal["asc", "desc"] | None
    ordering_meta: Literal[
        "created_at", "updated_at", "first_published_at", "published_at"
    ] | None
    draft_mode_active: bool
    all_locales_required: bool
    collection_appearance: Literal["compact", "table"]
    has_singleton_item: bool
    hint: str | None


class Fields(TypedDict):
    data: list[FieldId]


class FieldSets(TypedDict):
    data: list[FieldSetId]


class Relationships(TypedDict):
    singleton_item: TypedDict("SingletonItem", {"data": ItemId}) | None
    fields: Fields
    field_sets: FieldSets
    title_field: TypedDict("TitleField", {"data": FieldId}) | None
    image_preview_field: TypedDict("ImagePreviewField", {"data": FieldId}) | None
    excerpt_field: TypedDict("ExcerptField", {"data": FieldId}) | None
    ordering_field: TypedDict("OrderingField", {"data": FieldId}) | None
    workflow: TypedDict("Workflow", {"data": WorkflowId}) | None


ModelTypeName = Literal["item_type"]


class Model(TypedDict):
    id: ModelId
    type: ModelTypeName
    attributes: Attributes
    relationships: Relationships
