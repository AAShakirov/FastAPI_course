from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from auth.base_config import auth_backend
from auth.models import User
from auth.schemas import UserRead, UserCreate
from auth.manager import get_user_manager

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


app = FastAPI(
    title='Trading App'
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()

# @app.get("/protected-route")
# def protected_route(user: User = Depends(current_user)):
#     return f"Hello, {user.username}"

# @app.get("/unprotected-route")
# def unprotected_route():
#     return "Hello, anonym"
