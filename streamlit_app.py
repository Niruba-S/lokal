# streamlit_app.py

import streamlit as st
import requests

st.set_page_config(layout="wide")

st.title("Telugu News Article Summarizer and Title Generator")

telugu_text = st.text_area("Enter Telugu News Article (300-500 words):", height=200)

if st.button("Summarize and Generate Title"):
    if telugu_text:
        with st.spinner("Processing..."):
            try:
                response = requests.post("http://localhost:8000/analyze", json={"text": telugu_text})
                response.raise_for_status()
                data = response.json()
                
                st.success("Processing complete!")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Original Article (Telugu)")
                    st.markdown(f"<div style='background-color: #f0f2f6; padding: 10px; font-size: 16px;'>{telugu_text}</div>", unsafe_allow_html=True)
                    
                    st.subheader("Generated Content (Telugu)")
                    st.markdown(f"**హెడ్‌లైన్:** {data['telugu_title']}")
                    st.markdown(f"**సారాంశం:** {data['telugu_summary']}")
                
                with col2:
                    st.subheader("Full English Translation")
                    st.markdown(f"<div style='background-color: #f0f2f6; padding: 10px; font-size: 16px;'>{data['english_full_text']}</div>", unsafe_allow_html=True)
                    
                    st.subheader("English Translations")
                    st.markdown(f"**Headline:** {data['english_title']}")
                    st.markdown(f"**Summary:** {data['english_summary']}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a Telugu news article.")