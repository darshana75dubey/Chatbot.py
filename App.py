import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)

st.title("Chat Bot")

prompt = st.chat_input("Ask me anything")

if prompt:
    with st.chat_message("Me"):
        st.write(prompt)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    with st.chat_message("🤖"):
        st.write(response.choices[0].message.content)
