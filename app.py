import streamlit as st
from model_script import predict_emotion

st.set_page_config(page_title="Text Emotion Predictor", page_icon="💬", layout="centered")

st.title("💬 Text Emotion Predictor")
st.subheader("Predict emotions from any text input using NLP models")

# User input section
st.markdown("### Enter your text below:")
text_input = st.text_input("Text Input", placeholder="Type something like 'I'm so happy today!'")

# Predict button
if st.button("🔍 Predict Emotion"):
    if text_input:
        prediction = predict_emotion(text_input)
        emoji_dict = {
            "joy": "😂", "fear": "😱", "anger": "😠",
            "sadness": "😢", "disgust": "😒", "shame": "😳", "guilt": "😳"
        }
        st.markdown(f"### Predicted Emotion: {emoji_dict.get(prediction, '🤖')} **{prediction.upper()}**")
    else:
        st.warning("Please enter some text to predict.")


# Emoji result placeholder
st.markdown("### Predicted Emotion")
st.markdown("<div style='font-size:60px;'>🤖</div>", unsafe_allow_html=True)

# Example Emojis
st.markdown("### Emotion Legend")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("😂 Joy")
    st.markdown("😱 Fear")
    st.markdown("😠 Anger")
with col2:
    st.markdown("😢 Sadness")
    st.markdown("😒 Disgust")
    st.markdown("😳 Shame")
with col3:
    st.markdown("😳 Guilt")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")

