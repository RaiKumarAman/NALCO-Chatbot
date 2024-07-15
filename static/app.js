class Chatbot {
    constructor(){
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        }
        this.state = false;
        this.messages  = [];
    }

    display(){
        const {openButton, chatBox, sendButton} = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox));
        sendButton.addEventListener('click', () => this.onSendButton(chatBox));

        const node = chatBox.querySelector('input');
        node.addEventListener('keyup', ({key}) => {
            if(key === "Enter"){
                this.onSendButton(chatBox);
            }
        })
    }

    toggleState(x){
        this.state = !this.state;

        if(this.state){
            x.classList.add('chatbox--active');
        }
        else{
            x.classList.remove('chatbox--active');
        }
    }

    onSendButton(x){
        var textFeild = x.querySelector('input');
        let text1 = textFeild.value;

        if(text1 === ""){
            return;
        }

        let msg1 = {name: "User", message: text1};
        this.messages.push(msg1);

        fetch('http://127.0.0.1:5000/bot', {
            method: 'POST',
            body: JSON.stringify({message: text1}),
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
        })
        .then(r => r.json())
        .then(r => {
            let msg2 = {name: "Sam", message: r.answer};
            this.messages.push(msg2);
            this.updateChatText(x);
            textFeild.value = '';
        })
        .catch((err) => {
            console.error('Error: ', err);
            this.updateChatText(x);
            textFeild.value = '';
        });
    }

    updateChatText(x){
        var html = '';
        this.messages.slice().reverse().forEach(function(item){
            if(item.name ==="Sam"){
                html += '<div class="messages__item messages__item--vistor">' + item.message + '</div>';
            }
            else{
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>';
            }
        });

        const chatmessage = x.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }
}

const chatbot = new Chatbot();
chatbot.display();