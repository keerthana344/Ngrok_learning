from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from repositories import user_repo
from schemas.user_schema import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])


# --- Create User ---
@router.post(
    "/",
    response_model=UserResponse,
    summary="Create User",
    description="Create a new user with username, email, password, and optional phone number.",
)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    db_user = user_repo.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Check if username already exists
    db_user = user_repo.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    return user_repo.create_user(db=db, user=user)


# --- Get All Users ---
@router.get(
    "/",
    response_model=List[UserResponse],
    summary="Get All Users",
    description="Retrieve a list of all users with optional pagination.",
)
def get_all_users(
    skip: int = Query(0, ge=0, description="Number of users to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of users to return"),
    db: Session = Depends(get_db),
):
    return user_repo.get_all_users(db, skip=skip, limit=limit)


# --- Get User by ID ---
@router.get(
    "/{user_id}",
    response_model=UserResponse,
    summary="Get User By Id",
    description="Retrieve a single user by their unique ID.",
)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = user_repo.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

