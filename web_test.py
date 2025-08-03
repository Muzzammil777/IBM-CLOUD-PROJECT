#!/usr/bin/env python3
"""
Flask Web App for MedBot Testing
This creates a simple web interface to test your MedBot service
"""

from flask import Flask, request, jsonify, render_template_string
import json
from unittest.mock import Mock
from medbot import gen_ai_service

app = Flask(__name__)

class FlaskMockContext:
    """Mock context for Flask testing"""
    
    def __init__(self, messages, token="test-token"):
        self.messages = messages
        self.token = token
        self.headers = {"X-Ai-Interface": "assistant"}
    
    def generate_token(self):
        return self.token
    
    def get_token(self):
        return self.token
    
    def get_json(self):
        return {"messages": self.messages}
    
    def get_headers(self):
        return self.headers

# HTML template for the web interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>MedBot Test Interface</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .chat-container { border: 1px solid #ddd; height: 400px; overflow-y: auto; padding: 10px; margin: 10px 0; }
        .message { margin: 10px 0; padding: 10px; border-radius: 5px; }
        .user-message { background-color: #e3f2fd; text-align: right; }
        .bot-message { background-color: #f5f5f5; }
        .input-container { display: flex; gap: 10px; }
        input[type="text"] { flex: 1; padding: 10px; border: 1px solid #ddd; border-radius: 5px; }
        button { padding: 10px 20px; background-color: #2196F3; color: white; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background-color: #1976D2; }
        .warning { background-color: #fff3e0; border-left: 4px solid #ff9800; padding: 10px; margin: 10px 0; }
    </style>
</head>
<body>
    <h1>🤖 MedBot Test Interface</h1>
    
    <div class="warning">
        <strong>⚠️ This is a test interface with mock responses.</strong><br>
        This simulates how MedBot would work with real IBM Watson integration.
        Actual deployment would connect to IBM Watson services.
    </div>
    
    <div class="chat-container" id="chatContainer">
        <div class="message bot-message">
            <strong>MedBot:</strong> Hello! I'm MedBot, your AI-powered health assistant. 
            I can help you understand your symptoms and guide you on what steps to take—backed by trusted medical sources. 
            If you're comfortable, please share your location and describe your symptoms in your own words.
        </div>
    </div>
    
    <div class="input-container">
        <input type="text" id="messageInput" placeholder="Describe your symptoms..." onkeypress="handleKeyPress(event)">
        <button onclick="sendMessage()">Send</button>
    </div>
    
    <script>
        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }
        
        function sendMessage() {
            const input = document.getElementById('messageInput');
            const message = input.value.trim();
            
            if (!message) return;
            
            // Add user message to chat
            addMessage(message, 'user');
            input.value = '';
            
            // Send to backend
            fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({message: message})
            })
            .then(response => response.json())
            .then(data => {
                addMessage(data.response, 'bot');
            })
            .catch(error => {
                addMessage('Sorry, there was an error processing your request.', 'bot');
            });
        }
        
        function addMessage(message, sender) {
            const chatContainer = document.getElementById('chatContainer');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${sender}-message`;
            
            if (sender === 'user') {
                messageDiv.innerHTML = `<strong>You:</strong> ${message}`;
            } else {
                messageDiv.innerHTML = `<strong>MedBot:</strong> ${message.replace(/\\n/g, '<br>')}`;
            }
            
            chatContainer.appendChild(messageDiv);
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
    </script>
</body>
</html>
"""

def generate_mock_response(message):
    """Generate mock medical responses"""
    message_lower = message.lower()
    
    if any(word in message_lower for word in ['hello', 'hi', 'hey', 'start']):
        return """Hello! I'm MedBot, your AI-powered health assistant. I can help you understand your symptoms and guide you on what steps to take—backed by trusted medical sources. If you're comfortable, please share your location and describe your symptoms in your own words."""
    
    elif any(word in message_lower for word in ['fever', 'temperature']):
        return """**Fever Analysis**\\n\\n**Possible Causes:**\\n1. **Viral Infection** (Common cold, flu) - Urgency: Mild to Moderate\\n2. **Bacterial Infection** - Urgency: Moderate\\n\\n**Home Care:**\\n• Stay hydrated with plenty of fluids\\n• Rest and avoid strenuous activities\\n• Use fever reducers as directed\\n• Monitor temperature regularly\\n\\n**Seek Medical Care If:**\\n• Fever above 103°F (39.4°C)\\n• Fever lasting more than 3 days\\n• Difficulty breathing\\n• Severe headache or neck stiffness\\n\\nDo you have any other symptoms I should know about?"""
    
    elif any(word in message_lower for word in ['sore throat', 'throat']):
        return """**Sore Throat Analysis**\\n\\n**Possible Causes:**\\n1. **Viral Pharyngitis** (Most common) - Urgency: Mild\\n2. **Strep Throat** (Bacterial) - Urgency: Moderate\\n3. **Allergies/Irritants** - Urgency: Mild\\n\\n**Home Care:**\\n• Gargle with warm salt water\\n• Drink warm liquids (tea with honey)\\n• Use throat lozenges\\n• Stay hydrated and rest\\n\\n**Seek Medical Care If:**\\n• Severe difficulty swallowing\\n• High fever with sore throat\\n• White patches on throat\\n• Symptoms worsen after 3-4 days\\n\\nDo you have fever or swollen glands with the sore throat?"""
    
    elif any(word in message_lower for word in ['headache', 'head pain']):
        return """**Headache Analysis**\\n\\n**Possible Causes:**\\n1. **Tension Headache** - Urgency: Mild\\n2. **Migraine** - Urgency: Mild to Moderate\\n3. **Dehydration** - Urgency: Mild\\n4. **Sinus Issues** - Urgency: Mild\\n\\n**Home Care:**\\n• Rest in quiet, dark room\\n• Apply cold or warm compress\\n• Stay hydrated\\n• Gentle neck stretches\\n• OTC pain relievers as directed\\n\\n**Seek Immediate Care If:**\\n• Sudden, severe "thunderclap" headache\\n• Headache with fever and neck stiffness\\n• Headache after head injury\\n• Vision changes or weakness\\n\\nCan you describe the type and severity of your headache?"""
    
    elif any(word in message_lower for word in ['nausea', 'vomit', 'stomach', 'belly']):
        return """**Digestive Symptoms Analysis**\\n\\n**Possible Causes:**\\n1. **Viral Gastroenteritis** - Urgency: Mild to Moderate\\n2. **Food Poisoning** - Urgency: Moderate\\n3. **Indigestion** - Urgency: Mild\\n\\n**Home Care:**\\n• Rest and avoid solid foods initially\\n• Stay hydrated with small, frequent sips\\n• Try clear liquids (broth, electrolyte solutions)\\n• BRAT diet when ready (Bananas, Rice, Applesauce, Toast)\\n\\n**Seek Medical Care If:**\\n• Signs of severe dehydration\\n• Blood in vomit or stool\\n• Severe abdominal pain\\n• High fever\\n• Symptoms persist > 24-48 hours\\n\\nHow long have you been experiencing these symptoms?"""
    
    else:
        return """Thank you for describing your symptoms. To provide the most accurate guidance:\\n\\n**Next Steps:**\\n1. Monitor your symptoms closely\\n2. Note any changes or new symptoms\\n3. Stay hydrated and rest\\n\\n**General Red Flags - Seek immediate care for:**\\n• Difficulty breathing\\n• Chest pain\\n• Severe pain\\n• High fever (>103°F)\\n• Signs of dehydration\\n\\n**Questions to Consider:**\\n• How long have you had these symptoms?\\n• Rate your discomfort (1-10 scale)\\n• Any recent exposures or travel?\\n• Current medications?\\n\\nWould you like to share your location for regional health advisories?\\n\\n*Remember: I provide information and guidance, but cannot replace professional medical advice.*"""

@app.route('/')
def index():
    """Serve the main chat interface"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        # Generate mock response
        response = generate_mock_response(user_message)
        
        return jsonify({'response': response})
        
    except Exception as e:
        return jsonify({'response': f'Sorry, I encountered an error: {str(e)}'})

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'MedBot Test Interface'})

if __name__ == '__main__':
    print("🚀 Starting MedBot Test Web Interface")
    print("Open your browser and go to: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    app.run(debug=True, host='0.0.0.0', port=5000)
