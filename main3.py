import streamlit as st

from google.cloud import dialogflow_v2beta1 as dialogflow

import os


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'assistant.json'

project_id = 'assistant-upty'
session_id = '2132024'
language_code = 'en'

session_client = dialogflow.SessionsClient()


def detect_intent_text(text):
	session = session_client.session_path(project_id, session_id)
	text_input = dialogflow.TextInput(text=text, language_code=language_code)
	query_input = dialogflow.QueryInput(text=text_input)

	response = session_client.detect_intent(request={
		'session': session,
		'query_input': query_input,
	})

	return response.query_result.fulfillment_text


# Program Entry
st.title('CHATBOT')

prompt = st.chat_input('Enter something')

# Initialize chat history (You can replace 'messages with any name of your choice')
if 'messages' not in st.session_state:
	st.session_state.messages = []

for message in st.session_state.messages:
	user_input = st.chat_message(message['role'])
	user_input.write(message['content'])


if prompt and prompt.strip() != '':
	st.chat_message('user').write(prompt)
	
	st.session_state.messages.append({
		'role': 'user',
		'content': prompt,
	})

	response = detect_intent_text(prompt)

	st.chat_message('assistant').write(response)
	st.session_state.messages.append({
		'role': 'assistant',
		'content': response,
	})