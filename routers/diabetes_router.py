from fastapi import APIRouter
 # pyright: ignore[reportMissingImports]
from schemas.diabetes_schemas import PatientDiabetesData, patienDiabetesOutput
from services.diabetes_service import diabetes_prediction

router = APIRouter()

@router.post("/predict")
async def predict(data: PatientDiabetesData):
     #prediction ="sano"#
     prediction =diabetes_prediction(data)

     result = patienDiabetesOutput(
          first_name= data.first_name,
          last_name=data.last_name,
          prediction=prediction
            )

     return result 
    