import uvicorn
from fastapi import FastAPI
from src.router import contents_router, response_question_router, fruit_fungal_diseases_router, auth_router, rating_aplication_router
from fastapi.middleware.cors import CORSMiddleware

from fastapi import Depends
from src.utils.validRole import ValidRole

from src.utils.environment.env import setting

app = FastAPI()

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router.auth_router, prefix="/auth", tags=["Auth"])
app.include_router(contents_router.contents_router, prefix="/contents", tags=["contents"],
                   dependencies=[Depends(ValidRole(['user', 'admin']))])
app.include_router(response_question_router.response_question_router, prefix="/questions", tags=["questions"],
                   dependencies=[Depends(ValidRole(['user', 'admin']))])
app.include_router(rating_aplication_router.rating_aplication_router, prefix="/fruit", tags=["ratingAplication"],
                   dependencies=[Depends(ValidRole(['user', 'admin']))])
app.include_router(fruit_fungal_diseases_router.fruit_fungal_diseases_router, prefix="/fruit", tags=["fruitsDiseases"],
                   dependencies=[Depends(ValidRole(['user', 'admin']))])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=setting.PORT)



