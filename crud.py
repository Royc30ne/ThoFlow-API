from sqlalchemy.orm import Session

from . import models, schemas

def get_rss(db: Session, rss_id: int):
    return db.query(models.RssLink).filter(models.RssLink.id == rss_id).first()

def get_user_by_title(db: Session, title: str):
    return db.query(models.RssLink).filter(models.RssLink.title == title).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.RssLink).filter(models.RssLink.email == email).first()

def get_user_by_rss_address(db: Session, rss_address: str):
    return db.query(models.RssLink).filter(models.RssLink.rss_address == rss_address).first()
    
def get_rss_links(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.RssLink).offset(skip).limit(limit).all()

def add_rss(db: Session, rss_link: schemas.RssLinkAdd):
    db_rss_link = models.RssLink(title=rss_link.title, email=rss_link.email, rss_address=rss_link.rss_address, description=rss_link.description, is_active=True)
    db.add(db_rss_link)
    db.commit()
    db.refresh(db_rss_link)
    return db_rss_link


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item