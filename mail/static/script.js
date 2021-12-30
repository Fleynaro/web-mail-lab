const API_URL = '/api'

class ValidationError extends Error {
    constructor(message) {
        super(message);
    }
}

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

async function handleCreateSubmit(event) {
    event.preventDefault();

    const form = event.target;
    const message = {
        author: form.sender.value,
        message: form.message.value
    };

    try {
        const newMessage = await postMessage(message);
        form.reset();
        form.author.focus();
        //...
    } catch (error) {
        console.error(error);
    }
}

async function handleClapSubmit(event) {
    event.preventDefault();

    const form = event.target;
    const messageId = form.dataset.message_id;

    try {
        const newCount = await clapMessage(messageId);
        //...
    } catch (error) {
        console.error(error);
    }
}

function init() {
    const createForm = document.querySelector('form.send-form');
    createForm.addEventListener('submit', handleCreateSubmit);

    const clapForm = document.querySelector('div.message-form-clap');
    clapForm.addEventListener('submit', handleClapSubmit);
}

init();