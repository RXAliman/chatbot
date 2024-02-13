import streamlit as st

from datetime import datetime


st.title('CHATBOT')

prompt = st.chat_input('Enter something')

# Initialize chat history (You can replace 'messages with any name of your choice')
if 'messages' not in st.session_state:
	st.session_state.messages = []

for message in st.session_state.messages:
	user_input = st.chat_message(message['role'])
	user_input.write(message['content'])

st.chat_message('user').write(prompt)

if prompt and prompt.strip() != '':
	st.session_state.messages.append({
		'role': 'user',
		'content': prompt,
	})

if prompt == 'hi':
	st.chat_message('assistant').write('Hello!')
	st.session_state.messages.append({
		'role': 'assistant',
		'content': 'Hello!',
	})
elif prompt == 'hello':
	st.chat_message('assistant').write('Hi!')
	st.session_state.messages.append({
		'role': 'assistant',
		'content': 'Hi!',
	})
elif prompt == 'how are you':
	st.chat_message('assistant').write('I\'m fine! How about you?')
	st.session_state.messages.append({
		'role': 'assistant',
		'content': 'I\'m fine! How about you?',
	})
elif prompt == 'good':
	st.chat_message('assistant').write('Good to hear!')
	st.session_state.messages.append({
		'role': 'assistant',
		'content': 'Good to hear!',
	})
elif prompt == 'what time is it':
	now = datetime.now()
	current_time = now.strftime('%H:%M %p')
	st.chat_message('assistant').write(f'It\'s {current_time}')
	st.session_state.messages.append({
		'role': 'assistant',
		'content': f'It\'s {current_time}',
	})
elif prompt == 'anong pangalan mo':
	now = datetime.now()
	current_time = now.strftime('%H:%M %p')
	st.chat_message('assistant').write('Bakit? Hihingin mo number ko? Tapos mag-uusap tayo araw-araw? Tapos mafa-fall ako sayo? Tapos nun, magkakaaminan tayo ng feelings? Tapos magiging tayo? Tapos mamamasyal tayo nang magkasama? Tapos kalaunan magsasawa ka? Tapos makikipag-break ka saken? Tapos iiwan moko mag-isa? Tapos made-depress ako? Anyways, you can call me anything you want :3')
	st.session_state.messages.append({
		'role': 'assistant',
		'content': 'Bakit? Hihingin mo number ko? Tapos mag-uusap tayo araw-araw? Tapos mafa-fall ako sayo? Tapos nun, magkakaaminan tayo ng feelings? Tapos magiging tayo? Tapos mamamasyal tayo nang magkasama? Tapos kalaunan magsasawa ka? Tapos makikipag-break ka saken? Tapos iiwan moko mag-isa? Tapos made-depress ako? Anyways, you can call me anything you want :3',
	})