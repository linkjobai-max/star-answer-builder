import streamlit as st

st.set_page_config(page_title="STAR Answer Builder", page_icon="⭐")
st.title("⭐ STAR Answer Builder")
st.write(
    "Turn a messy story into a structured behavioral interview answer using the "
    "STAR method (Situation, Task, Action, Result). Aim for about 60-90 seconds "
    "when spoken; this tool estimates speaking time at ~140 words per minute."
)

question = st.text_input("Interview question", "Tell me about a time you resolved a conflict on your team.")
s = st.text_area("Situation - where and when? keep it to 1-2 sentences", height=80)
t = st.text_area("Task - what were YOU responsible for?", height=80)
a = st.text_area("Action - what did you do, step by step? (use 'I', not 'we')", height=120)
r = st.text_area("Result - what changed? add a number if you can", height=80)

parts = {"Situation": s, "Task": t, "Action": a, "Result": r}
words = {k: len(v.split()) for k, v in parts.items()}
total = sum(words.values())

if total:
    st.subheader("Your answer")
    st.markdown(f"**Q: {question}**")
    st.write(" ".join(v.strip() for v in parts.values() if v.strip()))
    secs = round(total / 140 * 60)
    st.caption(f"{total} words, roughly {secs} seconds spoken.")

    tips = []
    if total and words["Action"] < 0.4 * total:
        tips.append("Action is under 40% of the answer - interviewers care most about what you did.")
    if words["Situation"] > 0.25 * total:
        tips.append("Situation is long - trim background and get to the problem faster.")
    if r and not any(ch.isdigit() for ch in r):
        tips.append("Result has no number - add a metric, time saved, or concrete outcome.")
    if " we " in f" {a.lower()} " and " i " not in f" {a.lower()} ":
        tips.append("Action uses 'we' only - make your personal contribution explicit.")
    if secs > 120:
        tips.append("Over two minutes - cut it down; you can add detail in follow-ups.")
    for tip in tips:
        st.warning(tip)
    if not tips:
        st.success("Balanced answer. Practice saying it out loud twice.")

st.divider()
st.caption(
    "Made by the team behind [Linkjob AI](https://www.linkjob.ai/), an AI interview "
    "assistant for practice and live interviews. Nothing you type here is stored."
)
