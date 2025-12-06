from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.dependencies import get_current_user
from app.db.session import get_db
from app.schemas.users import UserOut, UserUpdate
from app.services.users import update_user, list_users, get_user

router = APIRouter(tags=["users"], prefix="/users")

@router.get("/me", response_model=UserOut)
async def read_me(current_user = Depends(get_current_user)):
    return current_user

@router.patch("/me", response_model=UserOut)
async def update_me(data: UserUpdate, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    user = await update_user(db, current_user, username=data.username)
    return user

@router.get("/", response_model=list[UserOut])
async def admin_list(db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")
    return await list_users(db)
