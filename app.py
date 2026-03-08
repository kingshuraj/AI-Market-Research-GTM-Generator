import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="YOUR_API_KEY")

st.title("AI Market Research & GTM Strategy Generator")

st.write("Generate quick consulting-style market insights.")

market = st.text_input("Enter Industry / Market / Company")

if st.button("Generate Insights"):

    prompt = f"""
    You are a strategy consultant.

    Generate a structured market research report for: {market}

    Format the response using the following sections:

    Market Overview
    Market Size & Growth
    Key Competitors
    Customer Segments
    Go-To-Market Strategy
    Risks
    Opportunities

    Keep the analysis concise and professional.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        st.subheader("Market Research Report")
        st.write(response.choices[0].message.content)

    except Exception as e:
        st.error(
            "⚠️ API quota not available. This demo requires OpenAI API credits to generate live insights."
        )
        st.info(
            "The tool architecture is functional. Once API credits are added, it will generate full market intelligence reports automatically."
        )