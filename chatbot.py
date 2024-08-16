import streamlit as st
import google.generativeai as genai

# Configure the API key
Google_Api_key = "AIzaSyDa3yBtGOkodNxoa-qksMY8sbRNVu7ztbM"
genai.configure(api_key=Google_Api_key)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

# Set up the Streamlit app
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")

# Sidebar options
st.sidebar.title("AI Chatbot Options")
st.sidebar.subheader("Instructions")
st.sidebar.markdown("""
- This chatbot is powered by Google Gemini.
- Type your message in the input field and press enter to get a response from the chatbot.
- The chat history will be displayed on the right.
""")

# Add a slider for response length
# response_length = st.sidebar.slider("Response Length", min_value=50, max_value=500, value=150)

# Main app
st.title("AI Chatbot")
st.write("Welcome to the AI Chatbot! Ask me anything.")

# Chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

    # Display chat history
for chat in st.session_state.chat_history:
    st.markdown(f"""
    <div style="
        background-color: #d1d3e0;
        border-radius: 15px;
        padding: 10px 15px;
        margin: 5px 0;
        max-width: 70%;
        text-align: left;
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>You:</b> {chat['You']} 😊</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="
        background-color: #e1ffc7;
        border-radius: 15px;
        padding: 10px 15px;
        margin: 5px 0;
        max-width: 70%;
        text-align: left;
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>Bot:</b> {chat['bot']} 🤖</p>
    </div>
    """, unsafe_allow_html=True)

# User input form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Enter your query here:", max_chars=300)
    submit_button = st.form_submit_button("Send")
    if user_input:
           response = getResponseFromModel(user_input)
           st.session_state.chat_history.append({"You": user_input, "bot": response})
    


# Footer
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        <p>Developed by [Rashid Khan]</p>
    </div>
    """, unsafe_allow_html=True)
