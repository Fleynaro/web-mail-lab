from flask import Blueprint, render_template, request, redirect, url_for
from mail.entities.message_entity import Message

from services.message_service import MessageService, ValidationError

message_blueprint = Blueprint('message', __name__, static_folder='../static', template_folder='../templates', static_url_path='/static/message')
message_template = {
    'id': '1000000001',
    'sender': '{sender}',
    'text': '{text}',
    'claps': '{claps}'
}

@message_blueprint.get('/')
def index():
    messages = MessageService.get_all_messages()
    return render_template('index_page.html',
        messages=messages,
        tpl_message=message_template)


@message_blueprint.post('/')
def add_message():
    sender = request.form['sender']
    text = request.form['message']
    try:
        new_message = MessageService.create_message(sender, text)
        return render_template('index_page.html',
            messages=MessageService.get_all_messages(),
            new_message=new_message)
    except ValidationError as e:
        return render_template('index_page.html',
            messages=MessageService.get_all_messages(),
            error=e)


@message_blueprint.get('/messages/<int:message_id>')
def message_page(message_id: int):
    message = MessageService.get_message_by_id(message_id)
    if message is None:
        return redirect('/')

    return render_template('message_page.html',
        message=message,
        is_individual=True)


@message_blueprint.post('/messages/<int:message_id>/claps')
def clap_message(message_id: int):
    message = MessageService.get_message_by_id(message_id)
    if message is None:
        return redirect('/')

    message_service = MessageService(message)
    message_service.clap_message()
    
    if request.form['is_individual'] == 'True':
        return redirect(url_for('message.message_page', message_id=message_id))
    return redirect('/')