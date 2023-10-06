from src.database.config.collection import get_collection
from fastapi import HTTPException, status
from src.entity.contents import UpdateContents

from src.entity.contents import ConsultContentInformation

from bson import ObjectId

from src.entity.contents import ContentsEntity

contents_collection = get_collection('contents')


class ContentsRepository:

    def create_contents(self, contents):
        try:
            contents_collection.insert_one(contents)
            return {"ok": True, "msg": "Los datos fueron guardados"}
        except HTTPException as e:
            print(f"Error {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Hubo un error, contacte al administrador"
            )

    def search_info_contents(self, user_id, search: ConsultContentInformation):
        try:

            collection_result = contents_collection.find_one({"fruit": search.fruit})
            return collection_result
        except Exception as e:
            print(f"error in search: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="There was an error contact the administrator, please try again"
            )

    def find_contents_by_Id(self, content_id: str, user_id: str):
        try:
            contents_db = contents_collection.find_one({"_id": ObjectId(content_id), "user_id": user_id})
            if contents_db is not None:
                contents_db["_id"] = str(contents_db["_id"])
            return contents_db
        except Exception as e:
            print(f"Error {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Hubo un error contacta al administrador"
            )

    def update_contents(self, content_id: str, user_id, data_content: UpdateContents):
        try:
            update_data = data_content.dict(exclude_none=True)
            if data_content.information is None:
                del data_content.information

            content_db = contents_collection.update_one({"user_id": user_id, "_id": ObjectId(content_id)},
                                                        {"$set": update_data})
            print(content_db.modified_count)
            if content_db.modified_count == 1:
                updated_item = self.find_contents_by_Id(content_id, user_id)
                del updated_item["information"]
                return updated_item
        except Exception as e:
            print(f"Error {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="There was an error contact the administrator- update"
            )
