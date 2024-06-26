from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from . import schemas, crud
from database import database
from auth import auth, schemas as schemas_auth

router = APIRouter()

@router.post("/posts/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(database.get_db), current_user: schemas_auth.User = Depends(auth.get_current_user)):
    return crud.create_post(db=db, post=post, user_id=current_user.id)

@router.get("/posts/", response_model=List[schemas.Post])
def read_posts(db: Session = Depends(database.get_db), current_user: schemas_auth.User = Depends(auth.get_current_user)):
    posts = crud.get_posts_by_user(db, user_id=current_user.id)
    return posts

@router.delete("/posts/{post_id}", response_model=schemas.Post)
def delete_post(post_id: int, db: Session = Depends(database.get_db), current_user: schemas_auth.User = Depends(auth.get_current_user)):
    post = crud.get_posts_by_user(db, user_id=current_user.id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return crud.delete_post(db=db, post_id=post_id, user_id=current_user.id)
