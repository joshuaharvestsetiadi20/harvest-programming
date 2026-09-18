import streamlit as st

# Page setup
st.set_page_config(
    page_title="My Profile",
    page_icon="👤",
    layout="centered"
)

# Title
st.title("👤 My Profile")
st.write("Fill in your information below!")

# Input fields
name = st.text_input("What is your name?")
age = st.number_input("How old are you?", min_value=1, max_value=100, step=1)
school = st.text_input("What school do you go to?")
subject = st.text_input("What is your favorite subject?")
hobby = st.text_input("What is your favorite hobby?")

# Button
if st.button("✨ Create My Profile"):
    if name and school and subject and hobby:
        st.success("Profile created!")

        st.subheader(f"Hello! My name is {name}.")
        st.write(f"🎂 I am {age} years old.")
        st.write(f"🏫 I go to {school}.")
        st.write(f"📚 My favorite subject is {subject}.")
        st.write(f"🎮 I enjoy {hobby}.")

    else:
        st.warning("Please fill in all the fields!")
        import streamlit as st

import streamlit as st

import streamlit as st

st.set_page_config(
    page_title="Calculator",
    page_icon="🧮",
    layout="centered"
)

# -------------------------
# MEMORY
# -------------------------

if "display" not in st.session_state:
    st.session_state.display = "0"

if "first_number" not in st.session_state:
    st.session_state.first_number = None

if "operator" not in st.session_state:
    st.session_state.operator = None


# -------------------------
# FUNCTIONS
# -------------------------

def number_click(number):
    if st.session_state.display == "0":
        st.session_state.display = str(number)
    else:
        st.session_state.display += str(number)

    st.rerun()


def operator_click(op):
    st.session_state.first_number = float(st.session_state.display)
    st.session_state.operator = op
    st.session_state.display = "0"

    st.rerun()


def equals_click():
    if st.session_state.first_number is None:
        return

    first = st.session_state.first_number
    second = float(st.session_state.display)
    op = st.session_state.operator

    if op == "+":
        answer = first + second

    elif op == "-":
        answer = first - second

    elif op == "×":
        answer = first * second

    elif op == "÷":
        if second == 0:
            st.session_state.display = "Error"
            st.rerun()
            return

        answer = first / second

    if answer == int(answer):
        answer = int(answer)

    st.session_state.display = str(answer)
    st.session_state.first_number = None
    st.session_state.operator = None

    st.rerun()


def clear_click():
    st.session_state.display = "0"
    st.session_state.first_number = None
    st.session_state.operator = None

    st.rerun()


# -------------------------
# DISPLAY
# -------------------------

st.markdown(
    f"""
    <div style="
        background-color: #222222;
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: right;
        font-size: 40px;
        margin-bottom: 15px;
    ">
        {st.session_state.display}
    </div>
    """,
    unsafe_allow_html=True
)


# -------------------------
# ROW 1
# -------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("AC", use_container_width=True):
        clear_click()

with col2:
    if st.button("÷", use_container_width=True):
        operator_click("÷")

with col3:
    if st.button("×", use_container_width=True):
        operator_click("×")

with col4:
    if st.button("-", use_container_width=True):
        operator_click("-")


# -------------------------
# ROW 2
# -------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("7", use_container_width=True):
        number_click(7)

with col2:
    if st.button("8", use_container_width=True):
        number_click(8)

with col3:
    if st.button("9", use_container_width=True):
        number_click(9)

with col4:
    if st.button("+", use_container_width=True):
        operator_click("+")


# -------------------------
# ROW 3
# -------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("4", use_container_width=True):
        number_click(4)

with col2:
    if st.button("5", use_container_width=True):
        number_click(5)

with col3:
    if st.button("6", use_container_width=True):
        number_click(6)

with col4:
    if st.button("=", use_container_width=True):
        equals_click()


# -------------------------
# ROW 4
# -------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("1", use_container_width=True):
        number_click(1)

with col2:
    if st.button("2", use_container_width=True):
        number_click(2)

with col3:
    if st.button("3", use_container_width=True):
        number_click(3)

with col4:
    if st.button("0", use_container_width=True):
        number_click(0)

        import streamlit as st
import pandas as pd

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="GradeMaster",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

    .main {
        background-color: #f5f7fb;
    }

    .title {
        font-size: 45px;
        font-weight: 800;
        margin-bottom: 0px;
    }

    .subtitle {
        color: #6b7280;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .card {
        background-color: white;
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.06);
        margin-bottom: 20px;
    }

    .gpa {
        font-size: 55px;
        font-weight: 800;
    }

    .grade {
        font-size: 28px;
        font-weight: 700;
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------
# GPA CALCULATION
# -----------------------------
def get_grade(mark):

    if mark >= 90:
        return "A", 4.0
    elif mark >= 80:
        return "B", 3.0
    elif mark >= 70:
        return "C", 2.0
    elif mark >= 60:
        return "D", 1.0
    else:
        return "F", 0.0


# -----------------------------
# SESSION STATE
# -----------------------------
if "subjects" not in st.session_state:
    st.session_state.subjects = []


# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    '<div class="title">🎓 GradeMaster</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your personal GPA & Grade Calculator</div>',
    unsafe_allow_html=True
)


# -----------------------------
# ADD SUBJECT
# -----------------------------
st.markdown("### 📚 Add Your Subjects")

with st.container():

    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        subject_name = st.text_input(
            "Subject Name",
            placeholder="e.g. Mathematics"
        )

    with col2:
        mark = st.number_input(
            "Mark",
            min_value=0.0,
            max_value=100.0,
            value=80.0,
            step=1.0
        )

    with col3:
        credit = st.number_input(
            "Credits",
            min_value=1.0,
            max_value=10.0,
            value=1.0,
            step=1.0
        )

    if st.button("➕ Add Subject", use_container_width=True):

        if subject_name.strip() == "":
            st.warning("Please enter a subject name.")

        else:
            letter, gpa = get_grade(mark)

            st.session_state.subjects.append({
                "Subject": subject_name,
                "Mark": mark,
                "Letter": letter,
                "GPA": gpa,
                "Credits": credit
            })

            st.success(f"{subject_name} added successfully!")


# -----------------------------
# SUBJECT LIST
# -----------------------------
if len(st.session_state.subjects) > 0:

    st.markdown("### 📋 Your Subjects")

    df = pd.DataFrame(st.session_state.subjects)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # -----------------------------
    # CALCULATE GPA
    # -----------------------------

    total_points = 0
    total_credits = 0

    for subject in st.session_state.subjects:

        total_points += subject["GPA"] * subject["Credits"]
        total_credits += subject["Credits"]

    overall_gpa = total_points / total_credits

    # Determine overall letter
    if overall_gpa >= 3.5:
        overall_letter = "A"
    elif overall_gpa >= 2.5:
        overall_letter = "B"
    elif overall_gpa >= 1.5:
        overall_letter = "C"
    elif overall_gpa >= 0.5:
        overall_letter = "D"
    else:
        overall_letter = "F"


    # -----------------------------
    # RESULTS
    # -----------------------------
    st.markdown("### 🏆 Your Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class="card">
                <div>Overall GPA</div>
                <div class="gpa">{overall_gpa:.2f}</div>
                <div>out of 4.00</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="card">
                <div>Overall Grade</div>
                <div class="grade">{overall_letter}</div>
                <div>Your overall letter grade</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="card">
                <div>Total Subjects</div>
                <div class="gpa">{len(st.session_state.subjects)}</div>
                <div>Subjects calculated</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # -----------------------------
    # PERFORMANCE MESSAGE
    # -----------------------------

    if overall_gpa >= 3.5:
        st.success("🌟 Excellent! You're performing extremely well!")

    elif overall_gpa >= 3.0:
        st.info("👏 Great job! Keep up the good work!")

    elif overall_gpa >= 2.0:
        st.warning("💪 You're doing okay. There's room to improve!")

    else:
        st.error("📖 Keep working! You can definitely improve your GPA.")


    # -----------------------------
    # DELETE SUBJECTS
    # -----------------------------

    st.markdown("### 🗑️ Manage Subjects")

    subject_to_delete = st.selectbox(
        "Choose a subject to remove",
        [s["Subject"] for s in st.session_state.subjects]
    )

    if st.button("🗑️ Remove Selected Subject"):

        st.session_state.subjects = [
            s for s in st.session_state.subjects
            if s["Subject"] != subject_to_delete
        ]

        st.rerun()


# -----------------------------
# RESET
# -----------------------------
else:

    st.info("📚 Add your subjects above to start calculating your GPA!")


st.divider()

if st.button("🔄 Reset Everything", use_container_width=True):

    st.session_state.subjects = []

    st.rerun()


# -----------------------------
# FOOTER
# -----------------------------
st.markdown(
    "<center>🎓 GradeMaster • Built with Python & Streamlit</center>",
    unsafe_allow_html=True)

import streamlit as st

# -----------------------------
# PAGE SETTINGS
# -----------------------------
st.set_page_config(
    page_title="Quiz Master",
    page_icon="🧠",
    layout="centered"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #777;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .question-box {
        padding: 20px;
        border-radius: 15px;
        background-color: #f5f5f5;
        margin-bottom: 15px;
    }

    .score-box {
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        background-color: #f5f5f5;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------
# SESSION STATE
# -----------------------------
if "questions" not in st.session_state:
    st.session_state.questions = []

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False

if "score" not in st.session_state:
    st.session_state.score = 0


# -----------------------------
# TITLE
# -----------------------------
st.markdown('<div class="main-title">🧠 Quiz Master</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Create your own quiz and test your knowledge!</div>',
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR - QUIZ CREATOR
# =========================================================

st.sidebar.title("⚙️ Quiz Creator")

st.sidebar.write("Add your questions below.")

# Question input
question_text = st.sidebar.text_area(
    "Question",
    placeholder="Example: What is the capital of Indonesia?"
)

# Answer inputs
answer_a = st.sidebar.text_input(
    "Answer A",
    placeholder="Example: Jakarta"
)

answer_b = st.sidebar.text_input(
    "Answer B",
    placeholder="Example: Bandung"
)

answer_c = st.sidebar.text_input(
    "Answer C",
    placeholder="Example: Surabaya"
)

answer_d = st.sidebar.text_input(
    "Answer D",
    placeholder="Example: Manado"
)

correct_answer = st.sidebar.selectbox(
    "Correct Answer",
    ["A", "B", "C", "D"]
)


# -----------------------------
# ADD QUESTION
# -----------------------------
if st.sidebar.button("➕ Add Question", use_container_width=True):

    if not question_text:
        st.sidebar.error("Please enter a question.")

    elif not answer_a or not answer_b or not answer_c or not answer_d:
        st.sidebar.error("Please fill in all 4 answers.")

    else:

        new_question = {
            "question": question_text,
            "answers": {
                "A": answer_a,
                "B": answer_b,
                "C": answer_c,
                "D": answer_d
            },
            "correct": correct_answer
        }

        st.session_state.questions.append(new_question)

        st.sidebar.success("Question added!")

        st.rerun()


# =========================================================
# SIDEBAR - QUESTION LIST
# =========================================================

st.sidebar.divider()

st.sidebar.subheader("📚 Your Questions")

if len(st.session_state.questions) == 0:

    st.sidebar.info("No questions added yet.")

else:

    for i, q in enumerate(st.session_state.questions):

        st.sidebar.write(
            f"**{i + 1}.** {q['question']}"
        )

        if st.sidebar.button(
            f"🗑️ Delete Question {i + 1}",
            key=f"delete_{i}",
            use_container_width=True
        ):

            st.session_state.questions.pop(i)

            st.rerun()


# =========================================================
# MAIN PAGE
# =========================================================

if not st.session_state.quiz_started:

    st.header("📖 Quiz Setup")

    if len(st.session_state.questions) == 0:

        st.info(
            "👈 Start by adding questions using the Quiz Creator "
            "in the sidebar."
        )

    else:

        st.success(
            f"You currently have **{len(st.session_state.questions)} questions**."
        )

        st.write("### Questions in your quiz")

        for i, q in enumerate(st.session_state.questions):

            with st.container(border=True):

                st.write(
                    f"**Question {i + 1}:** {q['question']}"
                )

                st.write(
                    f"A. {q['answers']['A']}"
                )

                st.write(
                    f"B. {q['answers']['B']}"
                )

                st.write(
                    f"C. {q['answers']['C']}"
                )

                st.write(
                    f"D. {q['answers']['D']}"
                )

        st.divider()

        # Start quiz
        if st.button(
            "🚀 Start Quiz",
            use_container_width=True,
            type="primary"
        ):

            st.session_state.quiz_started = True
            st.session_state.quiz_finished = False
            st.session_state.score = 0

            st.rerun()


# =========================================================
# QUIZ
# =========================================================

else:

    st.header("📝 Take the Quiz")

    # If quiz hasn't been submitted
    if not st.session_state.quiz_finished:

        st.write(
            f"Answer all **{len(st.session_state.questions)} questions**."
        )

        st.divider()

        answers = []

        for i, q in enumerate(st.session_state.questions):

            st.subheader(
                f"Question {i + 1}"
            )

            st.write(
                f"**{q['question']}**"
            )

            selected = st.radio(
                "Choose your answer:",
                [
                    f"A. {q['answers']['A']}",
                    f"B. {q['answers']['B']}",
                    f"C. {q['answers']['C']}",
                    f"D. {q['answers']['D']}"
                ],
                key=f"question_{i}",
                index=None
            )

            answers.append(selected)

            st.divider()


        # Submit quiz
        if st.button(
            "✅ Submit Quiz",
            use_container_width=True,
            type="primary"
        ):

            score = 0

            unanswered = 0

            for i, selected in enumerate(answers):

                if selected is None:
                    unanswered += 1
                    continue

                selected_letter = selected[0]

                if selected_letter == st.session_state.questions[i]["correct"]:
                    score += 1

            if unanswered > 0:

                st.warning(
                    f"You still have {unanswered} unanswered question(s). "
                    "Please answer all questions."
                )

            else:

                st.session_state.score = score
                st.session_state.quiz_finished = True

                st.rerun()


    # =====================================================
    # RESULTS
    # =====================================================

    else:

        total = len(st.session_state.questions)

        score = st.session_state.score

        percentage = (score / total) * 100

        st.markdown(
            '<div class="score-box">',
            unsafe_allow_html=True
        )

        st.title("🎉 Quiz Complete!")

        st.metric(
            "Your Score",
            f"{score} / {total}"
        )

        st.metric(
            "Percentage",
            f"{percentage:.1f}%"
        )

        if percentage >= 90:
            st.success("🏆 Excellent! You really know your stuff!")

        elif percentage >= 75:
            st.success("👏 Great job! Keep it up!")

        elif percentage >= 50:
            st.warning("👍 Not bad! A little more practice will help.")

        else:
            st.error("📚 Keep practicing! You can improve!")

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

        st.divider()

        # -----------------------------------------
        # REVIEW ANSWERS
        # -----------------------------------------

        st.header("📋 Answer Review")

        for i, q in enumerate(st.session_state.questions):

            st.write(
                f"### Question {i + 1}"
            )

            st.write(q["question"])

            correct_letter = q["correct"]

            correct_text = q["answers"][correct_letter]

            st.success(
                f"✅ Correct Answer: {correct_letter}. {correct_text}"
            )

        st.divider()

        # -----------------------------------------
        # BUTTONS
        # -----------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "🔄 Retake Quiz",
                use_container_width=True
            ):

                st.session_state.quiz_started = True
                st.session_state.quiz_finished = False
                st.session_state.score = 0

                st.rerun()

        with col2:

            if st.button(
                "🏠 Back to Editor",
                use_container_width=True
            ):

                st.session_state.quiz_started = False
                st.session_state.quiz_finished = False

                st.rerun()


# =========================================================
# RESET EVERYTHING
# =========================================================

st.sidebar.divider()

if st.sidebar.button(
    "🧹 Reset Everything",
    use_container_width=True
):

    st.session_state.questions = []
    st.session_state.quiz_started = False
    st.session_state.quiz_finished = False
    st.session_state.score = 0

    st.rerun()