from pydantic import BaseModel

class RssContentBase(BaseModel):
    title: str
    content: str

class RssContentCreate(RssContentBase):
    pass

class RssContent(RssContentBase):
    id: int
    owner_id: int
    
    class Config:
        orm_mode = True

class RssBase(BaseModel):
    title: str
    email: str
    rss_address: str
    description: str

class RssLinkAdd(RssBase):
    pass
    
class RssLink(RssBase):
    is_active: bool
    contents: list[RssContent] = []
    
    class Config:
        orm_mode = True