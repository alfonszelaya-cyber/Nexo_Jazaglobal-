# ============================================================
# ZYRA / NEXO
# USERS ROUTER — CLEAN STABLE
# ============================================================

from fastapi import APIRouter, HTTPException

from app.Schemas.users.users_schema import (
    UserStatusResponse,
    CreateUserRequest,
    CreateUserResponse,
    GetUserRequest,
    UserResponse,
    UpdateUserRequest,
    DeleteUserRequest,
    UserActionResponse
)

from app.Services.users.users_services import UsersService


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

users_service = UsersService()


# ============================================================
# STATUS
# ============================================================

@router.get("/status", response_model=UserStatusResponse)
def users_status():
    return users_service.get_status()


# ============================================================
# CREATE USER
# ============================================================

@router.post("/create", response_model=CreateUserResponse)
def create_user(payload: CreateUserRequest):
    return users_service.create_user(payload)


# ============================================================
# GET USER
# ============================================================

@router.post("/get", response_model=UserResponse)
def get_user(payload: GetUserRequest):
    user = users_service.get_user(payload)

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return user


# ============================================================
# UPDATE USER
# ============================================================

@router.post("/update", response_model=UserActionResponse)
def update_user(payload: UpdateUserRequest):
    return users_service.update_user(payload)


# ============================================================
# DELETE USER
# ============================================================

@router.post("/delete", response_model=UserActionResponse)
def delete_user(payload: DeleteUserRequest):
    return users_service.delete_user(payload)
