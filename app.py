import streamlit as st
from googletrans import Translator

def translate_text(text, target_lang):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    return translation.text

def main():
    st.title("Tamil Nadu Skill Development Corporation")

    # Translation dropdown
    target_lang = st.sidebar.selectbox("Select Language", ["English", "Tamil"], index=1)
    target_lang_code = "en" if target_lang == "English" else "ta"

    # Content
    heading = "தமிழ்நாடு திறனாளி மேம்பாட்டு நிறுவனம்" if target_lang_code == "ta" else "Tamil Nadu Skill Development Corporation"
    body_1 = "To see a list of training courses available in various states along with sector names: " \
             "[TNSDCTPSearch](https://trainingprovider.tnskill.tn.gov.in/TNSDCTPSearch)"

    body_3 = "To view the complete website: " \
             "[TNSkill](https://www.tnskill.tn.gov.in/)"

    if target_lang_code == "ta":
        heading = translate_text(heading, target_lang_code)
        body_1 = translate_text(body_1, target_lang_code)

        body_3 = translate_text(body_3, target_lang_code)

    st.markdown(
        f"""
        <style>
            .reportview-container .main .block-container{{
                max-width: 1000px;
                padding-top: 2rem;
                padding-right: 1rem;
                padding-left: 1rem;
                padding-bottom: 5rem;
            }}
            .reportview-container .main {{
                color: #333;
                background-color: #F5F5F5;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(f"## {heading}")
    st.markdown(body_1, unsafe_allow_html=True)

    st.markdown(body_3, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
