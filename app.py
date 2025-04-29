# ClassConnect - Streamlit App
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="ClassConnect", layout="wide")
st.title("📚 ClassConnect")
st.write("A simple student app for collaboration and productivity.")

# Initialize session state if not already
if "assignments" not in st.session_state:
    st.session_state.assignments = []
if "notes" not in st.session_state:
    st.session_state.notes = []
if "poll_votes" not in st.session_state:
    st.session_state.poll_votes = {"Yes": 0, "No": 0, "Maybe": 0}

# Sidebar navigation
page = st.sidebar.radio("Go to", ["📅 Schedule", "📝 Assignments", "📚 Notes", "📊 Polls", "📢 Notices"])

# Page: Schedule
if page == "📅 Schedule":
    st.header("Weekly Class Schedule")
    schedule = {
        "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "Dept": ["MBA", "BBA/MBA", "BBA", "BBA/MBA", "BBA/MBA"]
    }
    df_schedule = pd.DataFrame(schedule)
    st.table(df_schedule)

# Page: Assignments
elif page == "📝 Assignments":
    st.header("Assignment Tracker")
    with st.form("add_assignment"):
        title = st.text_input("Assignment Title")
        due_date = st.date_input("Due Date", min_value=date.today())
        submitted = st.checkbox("Mark as submitted")
        if st.form_submit_button("Add Assignment"):
            st.session_state.assignments.append({
                "title": title,
                "due": due_date,
                "submitted": submitted
            })
    
    if st.session_state.assignments:
        st.subheader("Your Assignments")
        df = pd.DataFrame(st.session_state.assignments)
        st.dataframe(df)

# Page: Notes
elif page == "📚 Notes":
    st.header("Shared Notes")
    with st.form("upload_note"):
        note_title = st.text_input("Note Title")
        note_content = st.text_area("Note Content")
        if st.form_submit_button("Add Note"):
            st.session_state.notes.append({"title": note_title, "content": note_content})

    if st.session_state.notes:
        for note in st.session_state.notes:
            st.markdown(f"### {note['title']}")
            st.markdown(note['content'])
            st.markdown("---")

# Page: Polls
elif page == "📊 Polls":
    st.header("Quick Class Poll")
    st.write("Do you like this app so far?")
    choice = st.radio("Vote", ["Yes", "No", "Maybe"])
    if st.button("Submit Vote"):
        st.session_state.poll_votes[choice] += 1
    
    st.subheader("Poll Results")
    st.bar_chart(pd.DataFrame.from_dict(st.session_state.poll_votes, orient='index', columns=['Votes']))

# Page: Notices
elif page == "📢 Notices":
    st.header("Class Notice Board")
    st.info("📌 Tomorrow's class will be online via Zoom at 10 AM.")
    st.info("📌 Assignment 2 deadline extended to Friday.")
