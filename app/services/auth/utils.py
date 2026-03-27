from datetime import timedelta, timezone, datetime
import jwt
from core.config import jwt_settings
import bcrypt

def encode(payload : dict,
    key = jwt_settings.private_key_path.read_text(),
    algorithm = jwt_settings.algorithm ,
    expire_minutes = jwt_settings.access_token_expire_minutes,
    expire_delta : timedelta | None = None):
    to_encode = payload.copy()
    now = datetime.now(timezone.utc)
    if expire_delta:
        expire = now + expire_delta
    else:
        expire = now + timedelta(minutes=expire_minutes)
    to_encode.update(exp=expire,iat=now)
    encoded = jwt.encode(
        to_encode,
        key,
        algorithm=algorithm
    )
    return encoded

def decode(token: str | bytes,
           key = jwt_settings.public_key_path.read_text(),
           algorithm = jwt_settings.algorithm):
    decoded = jwt.decode(token,key,algorithms=[algorithm])
    return decoded

def hash_password(password : str)->bytes:
    salt = bcrypt.gensalt()
    pwd_bytes = password.encode()
    return bcrypt.hashpw(pwd_bytes,salt=salt)

def validate_password(password: str,hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password.encode(),hashed_password)
