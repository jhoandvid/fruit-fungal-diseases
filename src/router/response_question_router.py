from fastapi import APIRouter, Request
from src.service.response_question_service import ResponseQuestionService

response_question_service = ResponseQuestionService()

response_question_router = APIRouter()


@response_question_router.get("/{content_id}")
async def get_response_question(request: Request, content_id: str):
    user_id = ""
    return response_question_service.get_responses_questions(user_id, content_id)


@response_question_router.get("/collection/{response_question_id}")
async def find_one_question_response(request: Request, response_question_id: str):
    user_id = ""
    return response_question_service.find_one_response_question_by_id(user_id, response_question_id)
