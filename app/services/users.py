from app.db.models import User
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import hash_password
from typing import Optional

async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
    q = await db.execute(select(User).where(User.email == email))
    return q.scalars().first()

async def get_user(db: AsyncSession, user_id: str) -> Optional[User]:
    q = await db.execute(select(User).where(User.id == user_id))
    return q.scalars().first()

async def create_user(db: AsyncSession, email: str, username: str, password: str) -> User:
    user = User(email=email, username=username, password_hash=hash_password(password))
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def list_users(db: AsyncSession, limit: int = 100):
    q = await db.execute(select(User).limit(limit))
    return q.scalars().all()

async def update_user(db: AsyncSession, user: User, username: Optional[str] = None):
    if username:
        user.username = username
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
