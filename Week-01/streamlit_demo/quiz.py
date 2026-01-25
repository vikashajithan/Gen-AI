import streamlit as st

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="Online Quiz App", layout="centered")

st.title("📝 Online Quiz Application")

# ----------------------------
# Quiz Questions (You can edit / add more)
# ----------------------------
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["Python", "HTML", "C", "Java"],
        "answer": "HTML"
    },
    {
        "question": "Who is the founder of Microsoft?",
        "options": ["Steve Jobs", "Elon Musk", "Bill Gates", "Mark Zuckerberg"],
        "answer": "Bill Gates"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Power Unit"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which one is a Python framework?",
        "options": ["React", "Angular", "Django", "Vue"],
        "answer": "Django"
    }
]

# ----------------------------
# Session State Initialization
# ----------------------------
if "current_q" not in st.session_state:
    st.session_state.current_q = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

# ----------------------------
# Quiz Logic
# ----------------------------
total_questions = len(questions)

# If quiz not finished
if st.session_state.current_q < total_questions:

    q = questions[st.session_state.current_q]

    st.subheader(f"Question {st.session_state.current_q + 1} of {total_questions}")
    st.write(q["question"])

    selected_option = st.radio(
        "Choose your answer:",
        q["options"],
        key=f"q_{st.session_state.current_q}"
    )

    col1, col2 = st.columns(2)

    # Next Button
    if col2.button("Next ➡️"):
        # Save answer
        st.session_state.answers[st.session_state.current_q] = selected_option

        # Check answer
        if selected_option == q["answer"]:
            st.session_state.score += 1

        st.session_state.current_q += 1
        st.rerun()

# ----------------------------
# Result Page
# ----------------------------
else:
    st.success("🎉 Quiz Completed!")

    st.write(f"**Your Score:** {st.session_state.score} / {total_questions}")

    percentage = (st.session_state.score / total_questions) * 100
    st.write(f"**Percentage:** {percentage:.2f}%")

    # Performance message
    if percentage >= 80:
        st.balloons()
        st.success("Excellent Performance! 🌟")
    elif percentage >= 50:
        st.info("Good Job! 👍")
    else:
        st.warning("Needs Improvement. Keep Practicing! 💪")

    # Show correct answers
    with st.expander("📖 View Answers"):
        for i, q in enumerate(questions):
            st.write(f"**Q{i+1}: {q['question']}**")
            st.write(f"Correct Answer: {q['answer']}")
            user_ans = st.session_state.answers.get(i, "Not Answered")
            st.write(f"Your Answer: {user_ans}")
            st.markdown("---")

    # Restart Button
    if st.button("🔄 Restart Quiz"):
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.answers = {}
        st.rerun()
