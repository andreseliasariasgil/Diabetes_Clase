from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

class PatientData(BaseModel):   
  

    first_name: str
    last_name: str


class PatientDiabetesData(BaseModel):
       first_name: str
       last_name: str
       pregnancies:int
       glucose: int
       bloodpressure: int
       skinthickness:int
       insulin:int
       bmi:float
       diabetespedigreefunction: float
       age:int



class patienDiabetesOutput(BaseModel):
      first_name: str
      last_name: str
      prediction:str
      
