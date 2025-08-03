# Agentic AI Health Symptom Checker (Med Bot)

This directory contains your MedBot service and comprehensive test scripts to validate its functionality.

## Files Overview

- **`medbot.py`** - Your main MedBot service with IBM Watson integration
- **`test_medbot.py`** - Comprehensive test suite for validation
- **`interactive_test.py`** - Interactive console-based testing
- **`web_test.py`** - Web-based test interface

## Testing Your MedBot

### 1. Basic Validation Test

Run this first to check if all dependencies are installed correctly:

```cmd
C:/Users/Abumuzzammil/AppData/Local/Programs/Python/Python313/python.exe test_medbot.py
```

### 2. Interactive Console Testing

Test MedBot responses in a conversation format:

```cmd
C:/Users/Abumuzzammil/AppData/Local/Programs/Python/Python313/python.exe interactive_test.py
```

### 3. Web Interface Testing

Launch a web browser interface to test MedBot:

```cmd
C:/Users/Abumuzzammil/AppData/Local/Programs/Python/Python313/python.exe web_test.py
```

Then open your browser to: http://localhost:5000

## Dependencies

Make sure you have installed all required packages:

```cmd
C:/Users/Abumuzzammil/AppData/Local/Programs/Python/Python313/python.exe -m pip install langchain-ibm ibm-watsonx-ai langchain-core langgraph requests flask
```

## What Each Test Does

### `test_medbot.py`

- ✅ Validates all imports work correctly
- ✅ Checks function definitions and signatures
- ✅ Tests basic service structure
- ✅ Provides detailed error reporting

### `interactive_test.py`

- 🤖 Simulates conversation with MedBot
- 📝 Tests specific medical scenarios
- 💬 Interactive chat experience
- 🧪 Validates response generation

### `web_test.py`

- 🌐 Web-based chat interface
- 📱 Mobile-friendly design
- 🔄 Real-time conversation
- 🎨 Professional UI/UX

## MedBot Features Tested

Your MedBot service includes:

- **Symptom Analysis** - Analyzes user-described symptoms
- **Medical Guidance** - Provides possible conditions and urgency levels
- **Home Care Suggestions** - Safe remedies and lifestyle tips
- **Professional Referrals** - Guidance on when to seek medical help
- **Regional Health Info** - Location-based health advisories
- **Multi-language Support** - Adapts to user's language
- **Safety Focus** - Emphasizes professional medical advice

## Mock vs Real Responses

⚠️ **Important**: The test scripts use mock responses to simulate MedBot behavior.

- **Mock responses** are used in testing (realistic but pre-programmed)
- **Real responses** would come from IBM Watson services with your credentials
- **Same structure** - both follow the same response format and medical guidelines

## Next Steps for Production

1. **Set up IBM Watson credentials**
2. **Deploy to IBM Cloud Functions or your preferred platform**
3. **Test with real API calls**
4. **Configure authentication and security**
5. **Set up monitoring and logging**

## Troubleshooting

If tests fail:

1. **Check dependencies**: Run the pip install command again
2. **Verify Python version**: Should be Python 3.8+
3. **Check file permissions**: Ensure files are readable
4. **Review error messages**: The test scripts provide detailed error information

## Medical Disclaimer

⚠️ **Important Medical Disclaimer**:
MedBot is designed to provide health information and guidance, but it is not a substitute for professional medical advice, diagnosis, or treatment. Always consult qualified healthcare providers for medical concerns.

## Support

For technical issues:

1. Run `test_medbot.py` first to identify the problem
2. Check that all dependencies are installed
3. Verify that `medbot.py` has no syntax errors
4. Review the console output for specific error messages

Enjoy testing your MedBot! 🤖⚕️


