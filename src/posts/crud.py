from sqlalchemy.orm import Session
from . import  schemas
from database import models
from cachetools import TTLCache, cached

cache = TTLCache(maxsize=100, ttl=300)

@cached(cache)
def create_post(db: Session, post: schemas.PostCreate, user_id: int):
    db_post = models.Post(**post.dict(), owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts_by_user(db: Session, user_id: int):
    return db.query(models.Post).filter(models.Post.owner_id == user_id).all()

def delete_post(db: Session, post_id: int, user_id: int):
    db_post = db.query(models.Post).filter(models.Post.id == post_id, models.Post.owner_id == user_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post
