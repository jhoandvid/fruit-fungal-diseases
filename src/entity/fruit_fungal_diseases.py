from pydantic import BaseModel, Field
from datetime import datetime


class FruitFungalDiseaseBase(BaseModel):
    scientific_name: str
    common_name: str
    description: str
    image_url: str
    host_plants: list[str]
    symptoms: str
    prevention_methods: list[str]
    management: str
    references: list[dict]


class FruitFungalDisease(FruitFungalDiseaseBase):
    class Config:
        schema_extra = {
            "example": {
                "scientific_name": "Gray Mold",
                "common_name": "Gray mold is a common fungal disease affecting various fruits.",
                "description": "El moho gris es una enfermedad fúngica común que afecta a varias frutas.",
                "image_url": "https://www.vinoble.org/sites/default/files/media/vinoble_botrytis2.png",
                "host_plants": ["Uvas", "Fresas", "Tomates"],
                "symptoms": "Crecimiento grisáceo-marrón difuso en la fruta afectada, pudrición y marchitamiento.",
                "prevention_methods": [
                    "Poda de partes infectadas de la planta",
                    "Aplicación de fungicidas",
                    "Mejora de la circulación de aire",
                ],
                "management": "Inspección regular y eliminación de frutas infectadas.",
                "references": [
                    {"title": "Guía de Enfermedades en Frutas", "url": "URL de la guía"},
                    {"title": "Artículo de Investigación", "url": "URL del artículo de investigación"},
                ]
            }
        }
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())
