from src.database.repository.rating_aplication import RatingAplicationRepository
from src.entity.raiting_aplication import RatingAplication

rating_aplication_repository = RatingAplicationRepository();


class RatingAplicationService:
    def create_rating_aplication(self, rating_aplication: RatingAplication):
        print(rating_aplication.user_id)

        rating_db = self.find_rating_aplication(rating_aplication.user_id)
        if rating_db is not None:
            return rating_aplication_repository.update_rating_aplication(rating_aplication)
        return rating_aplication_repository.create_rating_aplicacion(rating_aplication)

    def find_rating_aplication(self, user_id: str):
        rating_db = rating_aplication_repository.find_rating_aplication(user_id)
        if rating_db is not None:
            rating_db["_id"] = str(rating_db["_id"])
            return rating_db
        return None
