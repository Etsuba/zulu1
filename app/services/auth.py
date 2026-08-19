

from app.schemas.auth import UserCreate


class AuthService:

    self_users_db: dict[int, dict] = {}
    self_next_id: int = 1

    def create_user(self, user: UserCreate) -> dict:
        user_id=self.self_next_id
        self.self_next_id += 1

        new_user = {
            "id": user_id,
            "username": user.username,
            "email": user.email,
            "password": user.password,
        }

        self.self_users_db[user_id] = new_user
        return new_user

user_service = AuthService()
