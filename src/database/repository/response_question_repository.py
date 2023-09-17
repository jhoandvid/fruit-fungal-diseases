from fastapi import HTTPException, status
from src.database.config.collection import get_collection
from src.entity.question_response import QuestionResponse
from bson import ObjectId
response_question_document = get_collection("responses_questions")


class ResponseQuestionRepository:
    def create_responses_questions(self, data: QuestionResponse):
        try:
            json_data = data.dict()
            response_question_document.insert_one(json_data)
            json_data["_id"] = str(json_data["_id"])
            return json_data
        except HTTPException as e:
            print(f"Error {e}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ocurrido un error, cont´sctese con el administrador"
            )

    def find_one_response_question_by_id(self, user_id: str, response_question_id: str):
        try:
            response_question = response_question_document.find_one(
                {'user_id': user_id, '_id': ObjectId(response_question_id)})
            if response_question is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No fue encontrada la pregunta"
                )
            return response_question
        except HTTPException as e:
            print(f'Error {e}')
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Ocurrido un error, contáctese con el administrador'
            )

    def get_responses_questions(self, user_id: str, content_id: str):
        try:
            print(content_id)
            response_question = response_question_document.find(
                {'user_id': user_id, 'content_id': content_id})
            return response_question
        except HTTPException as e:
            print(f'Error {e}')
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Ocurrido un error, contáctese con el administrador'
            )
