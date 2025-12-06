import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()

def gen_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.String, primary_key=True, default=gen_uuid)
    email = sa.Column(sa.String, unique=True, nullable=False, index=True)
    username = sa.Column(sa.String, nullable=False)
    password_hash = sa.Column(sa.String, nullable=False)
    role = sa.Column(sa.String, nullable=False, default="user")
    is_active = sa.Column(sa.Boolean, default=True)
    created_at = sa.Column(sa.DateTime, default=datetime.utcnow)
