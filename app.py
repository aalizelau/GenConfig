import streamlit as st
import requests

# Title for the Streamlit app
st.title("Network Configuration Generator")

# Input for the user to send a message
user_input = st.text_input("Enter your message:", "Write a comprehensive firewall configuration for a web server.")

# Button to submit the input
if st.button("Send Request"):
    # Backend API details
    url = "http://213.173.109.145:11158/v1/chat/completions"
    headers = {
        "Content-Type": "application/json"
    }

    system_prompt = "You are an IT infrastructure and network expert specializing in creating detailed and professional configuration files. Your role is to respond with complete, well-structured plain text configuration files tailored to the given scenario or requirement,including routers, firewalls, servers, cloud services. Provide no explanations or additional comments unless explicitly requested. All outputs must follow industry standards and best practices, formatted cleanly and consistently."
    data = {
        "model": "qwen2.5-coder:14b",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7
    }
    
    # Send request to the backend
    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            # Extract the content
            response_data = response.json()
            content = response_data['choices'][0]['message']['content']
            st.success("Response from API:")
            st.write(content)
        else:
            st.error(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")