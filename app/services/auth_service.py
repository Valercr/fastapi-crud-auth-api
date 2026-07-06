from sqlalchemy.orm import Session
from app.repositories.user_repository import (get_user_by_username, create_user)
from app.core.security import hash_password, verify_password, create_access_token


def register_user(db: Session, user):
    existing = get_user_by_username(db, user.username)

    if existing:
        raise ValueError("Username already exists")

    new_user = create_user(
        db,
        username=user.username,
        password_hash=hash_password(user.password)
    )

    return {
        "id": new_user.id,
        "username": new_user.username
    }



def login_user(db: Session, user):
    db_user = get_user_by_username(db, user.username)

    if not db_user:
        raise ValueError("Invalid credentials")

    if not verify_password(user.password, db_user.password_hash):
        raise ValueError("Invalid credentials")

    token = create_access_token(
        data={"sub": str(db_user.id)}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }