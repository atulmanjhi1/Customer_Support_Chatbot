# Customer_Support_Chatbot
# NLP Project

A simple customer support chatbot built using Python, SpaCy for natural language processing, and Streamlit for the web interface. This bot is designed to handle common customer queries such as greeting, pricing, order status, and more. It responds based on predefined intents and keywords to provide relevant information.

Features
•	Intent Recognition: The bot can recognize various user intents such as greetings, product information, pricing, order status, etc.
•	Predefined Responses: Provides helpful responses based on identified intents.
•	Streamlit Interface: User-friendly web interface where users can interact with the chatbot in real-time.

Technologies Used
•	Python: Core programming language for developing the chatbot.
•	SpaCy: For natural language processing and recognizing user intents.
•	Streamlit: For building the interactive web interface.

Installation
1.	Create a virtual environment and activate it:
python -m venv env
 env\Scripts\activate
2.	Install the required dependencies:
pip install -r requirements.txt
3.	Download the SpaCy model:
python -m spacy download en_core_web_sm

Usage
To run the chatbot locally:
1.	Start the Streamlit application:
streamlit run app.py
2.	The chatbot will be available at http://localhost:8501.
   
Adding Custom Intents and Responses
•	You can modify the intents dictionary in the chatbot.py file to add new keywords and responses.
•	The corresponding responses are defined in the responses dictionary.


Example:
intents = {
    "new_intent": ["keyword1", "keyword2", ...]
}
responses = {
    "new_intent": "Your custom response here."
}
