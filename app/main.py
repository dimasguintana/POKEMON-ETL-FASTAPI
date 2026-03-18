from fastapi import FastAPI, HTTPException, Depends

from sqlalchemy.orm import Session

from app.schema import *
from app.handle import Handle
from app.database import *

app = FastAPI()
Base.metadata.create_all(bind=engine)

prefix_url: str = "https://pokeapi.co/api/v2/ability"

@app.get("/")
def read_root():
    return {"status": "Aplikasi Berjalan!"}

@app.post("/process-ability", response_model = ResponseOutput)
async def process_ability(data: AbilityInput, db: Session = Depends(get_db)):
    handler: Handle = Handle(
        data = data,
        prefix_url = prefix_url,
        db = db
    )
    result = await handler.handle()
    
    if not result:
        raise HTTPException(status_code=404, detail="Ability not found")
    
    await handler.insert_to_db(result)
        
    return result