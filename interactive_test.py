#!/usr/bin/env python3
"""
Interactive MedBot Test Script
This script simulates a conversation with MedBot using mock data
"""

import json
from unittest.mock import Mock, MagicMock, patch
from medbot import gen_ai_service

class InteractiveMockContext:
    """Interactive mock context for testing conversations"""
    
    def __init__(self, messages=None):
        self.messages = messages or []
        self.mock_token = "test-token-interactive"
        self.headers = {"X-Ai-Interface": "assistant"}
    
    def generate_token(self):
        return self.mock_token
    
    def get_token(self):
        return self.mock_token
    
    def get_json(self):
        return {"messages": self.messages}
    
    def get_headers(self):
        return self.headers

def create_mock_response(user_message):
    """Create a mock response based on user input"""
    user_message_lower = user_message.lower()
    
    # Simple keyword-based responses for testing
    if any(word in user_message_lower for word in ['hello', 'hi', 'hey']):
        return """Hello! I'm MedBot, your AI-powered health assistant. I can help you understand your symptoms and guide you on what steps to take—backed by trusted medical sources. If you're comfortable, please share your location and describe your symptoms in your own words."""
    
    elif any(word in user_message_lower for word in ['fever', 'temperature', 'hot']):
        return """Based on your mention of fever, here are some possible considerations:

**Possible Causes:**
1. **Viral Infection** (Common cold, flu) - Urgency: Mild to Moderate
2. **Bacterial Infection** - Urgency: Moderate
3. **Other conditions** depending on additional symptoms

**Home Care Suggestions:**
- Stay hydrated with plenty of fluids
- Rest and avoid strenuous activities
- Use fever reducers like acetaminophen or ibuprofen as directed
- Monitor your temperature regularly

**When to Seek Medical Help:**
- Fever above 103°F (39.4°C)
- Fever lasting more than 3 days
- Difficulty breathing or chest pain
- Severe headache or neck stiffness

Would you like to share your location for region-specific health advisories? Also, do you have any other symptoms?"""
    
    elif any(word in user_message_lower for word in ['sore throat', 'throat pain', 'swallowing']):
        return """For sore throat symptoms, here are some possibilities:

**Possible Causes:**
1. **Viral Pharyngitis** (Most common) - Urgency: Mild
2. **Strep Throat** (Bacterial) - Urgency: Moderate
3. **Allergies or Irritants** - Urgency: Mild

**Home Care Suggestions:**
- Gargle with warm salt water
- Drink warm liquids like tea with honey
- Use throat lozenges or sprays
- Stay hydrated and rest

**Red Flags - Seek Medical Care If:**
- Severe difficulty swallowing
- High fever with sore throat
- White patches on throat
- Symptoms worsen after 3-4 days

Do you have any fever, swollen glands, or other symptoms along with the sore throat?"""
    
    elif any(word in user_message_lower for word in ['headache', 'head pain', 'migraine']):
        return """For headache symptoms, here are some considerations:

**Possible Causes:**
1. **Tension Headache** - Urgency: Mild
2. **Migraine** - Urgency: Mild to Moderate
3. **Dehydration** - Urgency: Mild
4. **Sinus Issues** - Urgency: Mild

**Home Care Suggestions:**
- Rest in a quiet, dark room
- Apply cold or warm compress
- Stay hydrated
- Gentle neck and shoulder stretches
- Over-the-counter pain relievers as directed

**Seek Immediate Medical Care If:**
- Sudden, severe "thunderclap" headache
- Headache with fever and neck stiffness
- Headache after head injury
- Vision changes or weakness

Can you describe the type of headache pain and any triggers you've noticed?"""
    
    else:
        return """Thank you for sharing your symptoms. To provide you with the most accurate guidance, I'd like to gather a bit more information:

1. How long have you been experiencing these symptoms?
2. On a scale of 1-10, how would you rate your discomfort?
3. Have you noticed any patterns or triggers?
4. Are you taking any medications currently?

If you're comfortable sharing your general location, I can also check for any regional health advisories that might be relevant.

**General Advice:**
- Monitor your symptoms closely
- Stay hydrated and rest
- Seek medical attention if symptoms worsen or persist

**Seek immediate medical care if you experience:**
- Difficulty breathing
- Chest pain
- Severe pain
- High fever
- Signs of dehydration

Remember, I'm here to provide information and guidance, but I cannot replace professional medical advice. When in doubt, always consult with a healthcare provider."""

def simulate_conversation():
    """Simulate an interactive conversation with MedBot"""
    print("🤖 MedBot Interactive Test")
    print("=" * 50)
    print("This simulation shows how MedBot would respond to health-related queries.")
    print("Type 'quit' to exit the simulation.\n")
    
    conversation_history = []
    
    while True:
        # Get user input
        user_input = input("👤 You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("🤖 MedBot: Take care and feel better soon! Remember to consult healthcare professionals for serious concerns.")
            break
        
        if not user_input:
            continue
        
        # Add user message to history
        conversation_history.append({"role": "user", "content": user_input})
        
        # Generate mock response
        response = create_mock_response(user_input)
        
        # Add assistant response to history
        conversation_history.append({"role": "assistant", "content": response})
        
        # Display response
        print(f"\n🤖 MedBot: {response}\n")
        print("-" * 50)

def test_specific_scenarios():
    """Test specific medical scenarios"""
    print("🧪 Testing Specific Medical Scenarios")
    print("=" * 50)
    
    test_cases = [
        "Hello, I need help with my symptoms",
        "I have a high fever and sore throat",
        "I've been having severe headaches for 3 days",
        "My throat hurts when I swallow",
        "I feel nauseous and have stomach pain"
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📝 Test Case {i}: {test_case}")
        print("-" * 30)
        response = create_mock_response(test_case)
        print(f"🤖 Response: {response[:200]}...")
        print()

def main():
    """Main function with menu options"""
    print("MedBot Test Suite")
    print("Choose an option:")
    print("1. Interactive conversation simulation")
    print("2. Test specific scenarios")
    print("3. Both")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        simulate_conversation()
    elif choice == "2":
        test_specific_scenarios()
    elif choice == "3":
        test_specific_scenarios()
        print("\n" + "=" * 50)
        simulate_conversation()
    else:
        print("Invalid choice. Running interactive simulation...")
        simulate_conversation()

if __name__ == "__main__":
    main()
