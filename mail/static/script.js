/*
    ==========================
    GLOBAL VALUES
    ==========================
*/
const API_URL = '/api'





/*
    ==========================
    EXCEPTIONS
    ==========================
*/
class ValidationError extends Error {
    constructor(message) {
        super(message);
        this.name = 'ValidationError';
    }
}





/*
    ==========================
    API
    ==========================
*/
async function postMessage(message) {
    const response = await fetch(`${API_URL}/messages`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(message),
    });

    if (!response.ok) {
        if(response.status === 422) {
            const error = await response.json();
            throw new ValidationError(error.message);
        }
        throw new Error('Something went wrong');
    }

    const newMessage = await response.json();
    return newMessage;
}

async function clapMessage(messageId) {
    const response = await fetch(`${API_URL}/messages/${messageId}/claps`, {
        method: 'POST',
    });

    if (!response.ok) {
        if(response.status === 404) {
            const error = await response.json();
            throw new ValidationError(error.message);
        }
        throw new Error('Something went wrong');
    }

    const info = await response.json();
    return info.count;
}

async function getMessages() {
    const response = await fetch(`${API_URL}/messages`);

    if (!response.ok) {
        throw new Error('Something went wrong');
    }

    const messages = await response.json();
    return messages;
}





/*
    ==========================
    DOM MANIPULATION
    ==========================
*/
function createMessageArticleNode(message) {
    const template = document.querySelector('#message-template');
    const articleNodeHtml = template.content.firstElementChild.outerHTML
        .replaceAll('1000000001', message.id)
        .replaceAll('{sender}', message.author)
        .replaceAll('{text}', message.message)
        .replaceAll('{claps}', message.claps);
    const domParser = new DOMParser();
    const articleNode = domParser.parseFromString(articleNodeHtml, 'text/html')
        .body.firstElementChild;
    return articleNode;
}






/*
    ==========================
    HANDLERS
    ==========================
*/
async function handleCreateSubmit(event) {
    event.preventDefault();

    const form = event.target;
    const messageDto = {
        author: form.sender.value,
        message: form.message.value
    };

    // alert message
    const alertLoadingNode = form.querySelector('.send-form__loading');
    const alertSuccessNode = form.querySelector('.send-form__success');
    const alertErrorNode = form.querySelector('.send-form__error');
    alertLoadingNode.classList.remove('d-none');
    alertSuccessNode.classList.add('d-none');
    alertErrorNode.classList.add('d-none');

    form.querySelector('fieldset').disabled = true;

    try {
        const newMessage = await postMessage(messageDto);
        form.reset();
        form.sender.focus();

        // update list of messages
        const articleNode = createMessageArticleNode(newMessage);
        const listNode = document.querySelector('ul.list-messages');
        listNode.appendChild(articleNode);
        
        alertSuccessNode.classList.remove('d-none');
    } catch (error) {
        if (error.name != 'ValidationError')
            throw error;
        alertErrorNode.classList.remove('d-none');
        alertErrorNode.querySelector('.alert').textContent = error.message;
    } finally {
        alertLoadingNode.classList.add('d-none');
        form.querySelector('fieldset').disabled = false;
    }
}

async function handleClapSubmit(event) {
    event.preventDefault();

    const form = event.target;
    const messageId = form.dataset.message_id;
    if(form.disabled)
        return;
        
    form.querySelector('.btn').disabled = true;

    try {
        const newCount = await clapMessage(messageId);
        
        if(document.querySelector('ul.list-messages')) {
            // update list of messages
            const messages = await getMessages();

            const listNode = document.querySelector('ul.list-messages');
            listNode.textContent = '';

            messages.forEach(message => {
                const articleNode = createMessageArticleNode(message);
                listNode.appendChild(articleNode);
            });
        } else {
            // update message
            const clapCountNode = form.querySelector('span[data-test="clap-count"]');
            clapCountNode.textContent = newCount;
        }
    } catch (error) {
        console.error(error);
    } finally {
        form.querySelector('.btn').disabled = false;
    }
}




/*
    ==========================
    INIT
    ==========================
*/
function init() {
    const createForm = document.querySelector('form.send-form');
    if (createForm) {
        createForm.addEventListener('submit', handleCreateSubmit);
    }

    const clapForm = document.querySelector('.message-container');
    if(clapForm) {
        clapForm.addEventListener('submit', handleClapSubmit);
    }
}