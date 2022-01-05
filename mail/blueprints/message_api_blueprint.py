from flask import Blueprint, jsonify, request
from mail.entities.message_entity import Message

from services.message_service import MessageService, ValidationError

message_api_blueprint = Blueprint('message_api', __name__, url_prefix='/api')


class MessageDto:
    def __init__(self, message: Message):
        self.id = message.id
        self.author = message.sender
        self.message = message.text
        self.claps = message.claps


@message_api_blueprint.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    return response


@message_api_blueprint.get('/messages')
def api_get_messages():
    messages = MessageService.get_all_messages()
    return jsonify([vars(MessageDto(m)) for m in messages])


@message_api_blueprint.get('/messages/<int:message_id>')
def api_get_message(message_id: int):
    message = MessageService.get_message_by_id(message_id)
    if message is None:
        return jsonify({'message': 'Сообщение с таким ID не найдено'}), 404
    return jsonify(vars(MessageDto(message)))


@message_api_blueprint.post('/messages')
def api_post_message():
    try:
        message = MessageService.create_message(request.json['author'], request.json['message'])
    except ValidationError as e:
        return jsonify({'message': str(e)}), 422
    return jsonify(vars(MessageDto(message))), 201


@message_api_blueprint.post('/messages/<int:message_id>/claps')
def api_post_claps(message_id: int):
    message = MessageService.get_message_by_id(message_id)
    if message is None:
        return jsonify({'message': 'Сообщение с таким ID не найдено'}), 404
    
    message_service = MessageService(message)
    message_service.clap_message()

    return jsonify({'count': message.claps}), 201