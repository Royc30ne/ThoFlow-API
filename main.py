from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/rsslink/", response_model=schemas.RssLink)
def add_rsslink(rss_link: schemas.RssLinkAdd, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_rss_address(db, rss_address=rss_link.rss_address)
    if db_user:
        raise HTTPException(status_code=400, detail="RSS link already registered")
    
    return crud.add_rss(db=db, rss_link=rss_link)


@app.get("/rsslinks/", response_model=list[schemas.RssLink])
def read_rsslinks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_rss_links(db, skip=skip, limit=limit)
    return users


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items