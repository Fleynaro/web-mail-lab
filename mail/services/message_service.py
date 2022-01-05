from typing import List, Optional

from database import db_session
from entities.message_entity import Message

from shared.exception import ValidationError


class MessageService:
    def __init__(self, message: Message):
        self.message = message

    def get_message_by_id(message_id: int) -> Optional[Message]:
        return Message.query.filter_by(id=message_id).first()


    def get_all_messages() -> List[Message]:
        return Message.query.order_by(Message.claps.desc()).all()


    def create_message(sender: str, text: str) -> Message:
        if len(sender) < 1 or len(sender) > 30:
            raise ValidationError('Имя отправителя должно быть от 1 до 30 символов')
        if len(text) < 1 or len(text) > 1000:
            raise ValidationError('Текст сообщения должен быть от 1 до 1000 символов')
        message = Message(sender, text)
        db_session.add(message)
        db_session.commit()
        return message
        

    def clap_message(self):
        self.message.claps += 1
        db_session.commit()