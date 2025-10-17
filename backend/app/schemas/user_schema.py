from os import name
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Optional
from bson.objectid import ObjectId

class PyObjectId (ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Id de MongoDb inválido')
        return ObjectId(v)

class User_schema(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias='_id')
    name: str
    email:str
    password: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        