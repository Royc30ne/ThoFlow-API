from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, VARCHAR
from sqlalchemy.orm import relationship

from .database import Base


class RssLink(Base):
    __tablename__ = "tf_rss_link"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(128), unique=True, index=True, nullable=False)
    email = Column(VARCHAR(128), unique=True, index=True, nullable=False)
    rss_address = Column(VARCHAR(2083), unique=True, index=True, nullable=False)
    description = Column(VARCHAR(2083), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)

    items = relationship("RssContent", back_populates="owner")
    
class RssContent(Base):
    __tablename__ = "tf_rss_content"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(2083), index=True, nullable=False)
    content = Column(VARCHAR(2083), nullable=False)

    owner_id = Column(Integer, ForeignKey("tf_rss_link.id"))

    owner = relationship("RssLink", back_populates="items")