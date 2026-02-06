import streamlit as st

# Title of the app
st.title("JournalMe")

# Topic selection
topics = ["Gratitude", "Reflection", "Goals", "Daily Events", "Feelings"]
selected_topic = st.selectbox("Select a topic for your journal entry:", topics)

# Journal entry form
with st.form(key='journal_form'):
    journal_entry = st.text_area("Write your journal entry here:")
    submit_button = st.form_submit_button(label='Submit')

# Display the submitted entry
if submit_button:
    st.write(f"**Topic:** {selected_topic}")
    st.write("**Journal Entry:**")
    st.write(journal_entry)