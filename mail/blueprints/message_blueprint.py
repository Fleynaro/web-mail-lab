from flask import Blueprint, render_template, request, redirect
from flask import session as flask_session

from services.message_service import MessageService, ValidationError

from blueprints.message_api_blueprint import message_api_blueprint

message_blueprint = Blueprint('message', __name__, static_folder='../static', template_folder='../templates', static_url_path='/static/message', url_prefix='')
message_template = {
    'id': '1000000001',
    'sender': '{sender}',
    'text': '{text}',
    'claps': '{claps}'
}


# for global var in templates
@message_blueprint.context_processor
def inject_stage_and_region():
    return dict(
        tpl_message=message_template,
        api_url_prefix=message_api_blueprint.url_prefix)


@message_blueprint.get('/')
def index():
    messages = MessageService.get_all_messages()
    return render_template('index_page.html',
        messages=messages)


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
        return redirect(request.referrer)

    return render_template('message_page.html',
        message=message,
        is_individual=True)


@message_blueprint.post('/messages/<int:message_id>/claps')
def clap_message(message_id: int):
    message = MessageService.get_message_by_id(message_id)
    if message is not None:
        message_service = MessageService(message)
        message_service.clap_message()
    return redirect(request.referrer)


@message_blueprint.post('/ajax')
def ajax():
    if 'ajax' in flask_session and flask_session['ajax']:
        flask_session['ajax'] = False
    else:
        flask_session['ajax'] = True
    return redirect(request.referrer)