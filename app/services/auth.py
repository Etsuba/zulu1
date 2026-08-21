
from app.schemas.auth import UserCreate, UserUpdate


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
    
    def get_auth(self, user_id: int) -> dict | None:
        return self.self_users_db.get(user_id)

    def update_auth(self, user_id: int, update_data: UserUpdate) -> dict | None:
        user = self.get_auth(user_id)
        
        if not user:
            return None

        if update_data.username is not None:
            user["username"] = update_data.username
        if update_data.email is not None:
            user["email"] = update_data.email   
        if update_data.password is not None:
            user["password"] = update_data.password 

        return user

    def delete_auth(self, user_id: int) -> bool:
        if user_id in self.self_users_db:
            del self.self_users_db[user_id]
            return True
        return False

    
  

user_service = AuthService()
