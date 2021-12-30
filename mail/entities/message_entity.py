from sqlalchemy import Column, Integer, String
from database import Base


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    sender = Column(String(50))
    text = Column(String(300))
    claps = Column(Integer)

    def __init__(self, sender: str, text: str, claps: int = 0):
        self.sender = sender
        self.text = text
        self.claps = claps

    def __repr__(self) -> str:
        return f'<Message {self.id!r}>'