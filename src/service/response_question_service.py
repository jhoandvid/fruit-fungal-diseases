from src.database.repository.response_question_repository import ResponseQuestionRepository
from fastapi import HTTPException, status
from src.entity.question_response import QuestionResponse

response_question_repository = ResponseQuestionRepository()


class ResponseQuestionService:

    def get_responses_questions(self, user_id: str, content_id: str):
        response_questions = response_question_repository.get_responses_questions(user_id, content_id)
        if response_questions is None:
            return []
        serialized_response_questions = []
        for response_question in response_questions:
            response_question['_id'] = str(response_question['_id'])
            serialized_response_questions.append(response_question)
        return serialized_response_questions

    def find_one_response_question_by_id(self, user_id:str, response_question_id: str):
        response_question = response_question_repository.find_one_response_question_by_id(user_id, response_question_id)
        if response_question is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Response question with id {response_question_id} not found"
            )
        response_question['_id'] = str(response_question['_id'])
        return response_question
    def create_response_question(self, data):
        question_response = QuestionResponse()
        question_response.user_id = data['user_id']
        question_response.prompt = data['prompt']
        question_response.response = data['response']
        question_response.fruit = data['fruit']
        response_question_repository.create_responses_questions(question_response)
