import spacy
import streamlit as st

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Define intents and responses
intents = {
    "greet": ["hello", "hi", "hey", "good morning", "good evening", "greetings"],
    "goodbye": ["goodbye", "bye", "see you", "take care", "farewell", "later"],
    "thankyou": ["thanks", "thank you", "appreciate", "grateful", "thankful"],
    "product_info": ["tell me about your products", "what do you sell", "product details", "product information", "what services do you offer", "product features"],
    "pricing": ["how much", "price", "cost", "pricing", "fees", "what is the price of", "how much does it cost", "what's the cost"],
    "availability": ["is it available", "in stock", "do you have", "stock availability", "is it still available", "product availability"],
    "order_status": ["track my order", "where is my order", "order status", "status of my order", "when will my order arrive", "track order"],
    "shipping_info": ["shipping options", "how long does shipping take", "delivery time", "when will I receive my order", "international shipping", "shipping methods"],
    "payment_methods": ["payment options", "how can I pay", "accepted payment methods", "do you accept credit cards", "do you take paypal", "payment methods"],
    "refund_policy": ["how can I get a refund", "refund process", "refund policy", "return my money", "refund my purchase", "how long for refund"],
    "returns": ["how do I return", "return policy", "can I return", "return process", "how do returns work", "return my order"],
    "account_help": ["account issue", "help with my account", "can't log in", "how to reset password", "recover my account", "update my account info"],
    "feedback": ["give feedback", "leave a review", "submit feedback", "customer feedback", "how to leave feedback", "how to give review"],
    "store_hours": ["business hours", "when are you open", "store hours", "what time do you open", "closing time", "opening hours"],
    "contact_info": ["contact information", "how do I contact", "phone number", "email address", "how to reach customer service", "contact customer service"],
    "location": ["where is your store", "store location", "find a store", "where are you located", "physical store", "store address"],
    "help": ["need help", "can you help me", "support", "how can I get help", "how do I", "help with issue"]
}

responses = {
    "greet": "Hello! How can I assist you today?",
    "goodbye": "Goodbye! Have a great day. Feel free to reach out if you need more assistance!",
    "thankyou": "You're welcome! If you have any more questions, feel free to ask.",
    "product_info": "We offer a wide range of products including [Product List]. You can find more details on our website or ask about specific items.",
    "pricing": "The price for [Product Name] is [Price]. We also offer discounts and deals, so be sure to check those out!",
    "availability": "[Product Name] is currently in stock and available for purchase. Would you like me to assist you with the order?",
    "order_status": "You can track your order by entering your order number on our website, or I can assist you further if you provide the order number.",
    "shipping_info": "We offer multiple shipping options, including standard and express shipping. Delivery times vary based on location. International shipping is also available.",
    "payment_methods": "We accept various payment methods including credit cards, PayPal, and more. Please let me know if you need more details on a specific method.",
    "refund_policy": "Our refund policy allows returns within [X days] of purchase. Refunds are processed within [Y days] after we receive the returned item.",
    "returns": "You can return items by following the instructions on our returns page. Please ensure the product is in its original condition.",
    "account_help": "If you're having trouble with your account, you can reset your password by clicking 'Forgot Password' on the login page, or I can help guide you through it.",
    "feedback": "We appreciate your feedback! You can leave a review on our website or share your thoughts with us directly.",
    "store_hours": "Our store is open from [Opening Time] to [Closing Time], Monday through Friday. We're closed on weekends.",
    "contact_info": "You can reach us at [Phone Number] or [Email Address]. Our customer service team is available from [Hours].",
    "location": "We are located at [Store Address]. You can visit us during our business hours.",
    "help": "I'm here to help! Please tell me more about the issue you're facing, and I'll do my best to assist you.",
    "unknown": "I'm sorry, I didn't understand that. Can you please rephrase?"
}

# Helper function to find the intent
def find_intent(user_input):
    doc = nlp(user_input.lower())  # Process user input with spaCy

    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in user_input.lower():
                return intent
    return 'unknown'


# Function to get chatbot response
def chatbot_response(user_input):
    # Find intent based on user input
    intent = find_intent(user_input)

    # Respond based on intent
    response = responses.get(intent, responses["unknown"])

    return response

# Streamlit app
st.title("Customer Support Chatbot")
st.write("Welcome! How can I assist you today?")

# Create a chat interface
user_input = st.text_input("You: ", "")

if user_input:
    # Get chatbot response
    response = chatbot_response(user_input)
    
    # Display chatbot's response
    st.text_area("Chatbot:", value=response, height=150)

