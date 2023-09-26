from fastapi import FastAPI
from src.router import contents_router, response_question_router, fruit_fungal_diseases_router, auth_router
from fastapi.middleware.cors import CORSMiddleware

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
app.include_router(contents_router.contents_router, prefix="/contents", tags=["contents"])
app.include_router(response_question_router.response_question_router, prefix="/questions", tags=["questions"])
app.include_router(fruit_fungal_diseases_router.fruit_fungal_diseases_router, prefix="/fruit", tags=["fruitsDiseases"])


