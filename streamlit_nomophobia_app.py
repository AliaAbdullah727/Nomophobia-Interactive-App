# streamlit_nmpq_app.py
"""
Nomophobia Questionnaire (NMP-Q) — Interactive Streamlit App
Based on Yildirim & Correia (2015)
https://www.sciencedirect.com/science/article/pii/S0747563215001806
"""

import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="NMP-Q App", layout="centered")

# ===============================
# Header / Identification Card
# ===============================
st.title("Nomophobia Questionnaire (NMP-Q)")
st.markdown(
    """
**Based on a validated research instrument**  
Yildirim, C., & Correia, A.‑P. (2015). *Computers in Human Behavior*  

🔗 Original paper:  
https://www.sciencedirect.com/science/article/pii/S0747563215001806  

⚠️ This tool is for **screening and educational purposes only** — not a diagnostic test.

**Made by: Alia Al-Qadri**
"""
)

st.divider()

# ===============================
# Questionnaire
# ===============================
st.header("Questionnaire")
st.write("Rate each statement from **1 (Strongly disagree)** to **7 (Strongly agree)**.")
prefix="If I Didn't Have My Smartphone with me:"


questions = [
    "I would feel uncomfortable without constant access to information through my smartphone.",
    "I would be annoyed if I could not look information up on my smartphone when I wanted to do so.",
    "Being unable to get the news on my smartphone would make me nervous.",
    "I would be annoyed if I could not use my smartphone when I wanted to.",
    "Running out of battery in my smartphone would scare me.",
    "If I were to run out of credits or data, I would panic.",
    "Without data or Wi‑Fi, I would constantly look for a connection.",
    "If I could not use my smartphone, I would be afraid of getting stranded.",
    "If I could not check my smartphone for a while, I would feel a desire to check it.",
    "I would feel anxious because I could not instantly communicate with family or friends.",
    "I would be worried because my family or friends could not reach me.",
    "I would feel nervous because I could not receive calls or messages.",
    "I would be anxious because I could not stay in touch with others.",
    "I would be nervous because I would not know if someone tried to reach me.",
    "I would feel anxious because my constant connection would be broken.",
    "I would be nervous because I would be disconnected from my online identity.",
    "I would feel uncomfortable because I could not stay up‑to‑date with social media.",
    "I would feel awkward because I could not check notifications.",
    "I would feel anxious because I could not check my emails.",
    "I would feel weird because I would not know what to do."
]
total_qs=len(questions)
last_ten_qs=total_qs - 10
responses = []
for i, q in enumerate(questions, start=1):
    if i== last_ten_qs+1:
        st.write(prefix)
   # score = st.slider(q, 1, 7, 1, key=f"q{i}")
    score = st.slider(q,min_value=1,
                      max_value=7, 
                      value=4, 
                      step=1,)
    responses.append(score)

st.divider()

# ===============================
# Results Button
# ===============================
if st.button("Show Results"):
    total_score = sum(responses)

    # Interpretation
    if total_score == 20:
        level = "No Nomophobia"
        advice = "Healthy smartphone habits detected. Maintain balance."
    elif total_score <= 59:
        level = "Mild Nomophobia"
        advice = "Consider short phone‑free periods and reduce notifications."
    elif total_score <= 99:
        level = "Moderate Nomophobia"
        advice = "Digital detox routines and mindfulness are recommended."
    else:
        level = "Severe Nomophobia"
        advice = "Professional psychological support may be beneficial."

    st.subheader("Results")
    st.metric("Total Score", f"{total_score} / 140")
    st.success(level)
    st.info(advice)

    # ===============================
    # Visualizations
    # ===============================
    df = pd.DataFrame({
        "Question": [f"Q{i}" for i in range(1, 21)],
        "Score": responses
    })

    st.subheader("Item Scores")
    bar = alt.Chart(df).mark_bar().encode(
        x="Question",
        y="Score"
    ).properties(height=300)

    st.altair_chart(bar, use_container_width=True)

    st.subheader("Severity Gauge")
    gauge_df = pd.DataFrame({"Score": [total_score]})
    gauge = alt.Chart(gauge_df).mark_bar(size=50).encode(
        x=alt.X("Score", scale=alt.Scale(domain=[0, 140]))
    ).properties(height=80)

    st.altair_chart(gauge, use_container_width=True)

st.divider()
st.caption("Nomophobia Questionnaire (NMP‑Q) • Research‑based screening tool")
