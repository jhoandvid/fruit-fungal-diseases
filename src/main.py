from fastapi import FastAPI
from src.router import contents_router, response_question_router, fruit_fungal_diseases_router


app = FastAPI()


app.include_router(contents_router.contents_router, prefix="/contents", tags=["contents"])
app.include_router(response_question_router.response_question_router, prefix="/questions", tags=["questions"])
app.include_router(fruit_fungal_diseases_router.fruit_fungal_diseases_router, prefix="/fruit", tags=["fruitsDiseases"])
