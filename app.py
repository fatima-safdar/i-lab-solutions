from flask import Flask, request, jsonify, render_template_string, url_for
from config.settings import Config
from src.ai_agent import AIAgent
from src.whatsapp_client import WhatsAppClient

app = Flask(__name__)
ai_agent = AIAgent()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>i Lab Solutions</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f2f5; margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; height: 100vh; }
        .chat-container { width: 480px; background: #ffffff; border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.12); display: flex; flex-direction: column; height: 85vh; overflow: hidden; }
        .chat-header { background: #005e54; color: white; padding: 15px 20px; font-size: 20px; font-weight: 600; display: flex; align-items: center; gap: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .header-logo { width: 35px; height: 35px; border-radius: 50%; object-fit: contain; background: #ffffff; padding: 0px; }
        .chat-box { flex: 1; padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 14px; background-color: #efeae2; }
        .message { padding: 11px 16px; border-radius: 12px; max-width: 80%; word-wrap: break-word; white-space: pre-line; font-size: 15px; line-height: 1.5; box-shadow: 0 1px 2px rgba(0,0,0,0.08); }
        .user-msg { background: #d9fdd3; color: #111b21; align-self: flex-end; border-top-right-radius: 2px; }
        .bot-msg { background: #ffffff; color: #111b21; align-self: flex-start; border-top-left-radius: 2px; }
        
        /* Links Blue aur Underlined */
        .bot-msg a { 
            color: #007bff; 
            text-decoration: underline; 
            font-weight: 600;
        }
        .bot-msg a:hover { color: #0056b3; }
        
        .input-area { padding: 15px; display: flex; background: #f0f2f5; border-top: 1px solid #e9edef; align-items: center; }
        .input-area input { flex: 1; padding: 12px 18px; border: none; border-radius: 24px; outline: none; font-size: 15px; background: #ffffff; }
        .input-area button { background: #00a884; color: white; border: none; padding: 12px 20px; margin-left: 10px; border-radius: 24px; font-weight: 600; cursor: pointer; }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">
            <img src="{{ url_for('static', filename='logo.png') }}" class="header-logo" alt="Logo">
            i Lab Solutions AI Agent
        </div>
        <div class="chat-box" id="chatBox"></div>
        <div class="input-area">
            <input type="text" id="userInput" placeholder="Type your message here..." onkeypress="handleKeyPress(event)">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>
    <script>
        function handleKeyPress(e) { if(e.keyCode === 13) sendMessage(); }
        async function sendMessage() {
            let input = document.getElementById('userInput');
            let text = input.value.trim();
            if(!text) return;
            let chatBox = document.getElementById('chatBox');
            chatBox.innerHTML += `<div class="message user-msg">${text}</div>`;
            input.value = '';
            chatBox.scrollTop = chatBox.scrollHeight;
            let response = await fetch('/chat', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ message: text }) });
            let data = await response.json();
            chatBox.innerHTML += `<div class="message bot-msg">${data.reply}</div>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index(): return render_template_string(HTML_TEMPLATE)

@app.route('/chat', methods=['POST'])
def chat():
    user_data = request.get_json()
    return jsonify({"reply": ai_agent.generate_reply(user_data.get('message', ''))})

@app.route('/webhook', methods=['GET'])
def verify_webhook():
    if request.args.get('hub.verify_token') == Config.VERIFY_TOKEN: return request.args.get('hub.challenge'), 200
    return "Forbidden", 403

@app.route('/webhook', methods=['POST'])
def receive_message():
    data = request.get_json()
    try:
        msg = data['entry'][0]['changes'][0]['value']['messages'][0]
        WhatsAppClient.send_message(msg['from'], ai_agent.generate_reply(msg['text']['body']))
    except: pass
    return jsonify({"status": "success"}), 200

if __name__ == '__main__': app.run(port=Config.PORT, debug=True)