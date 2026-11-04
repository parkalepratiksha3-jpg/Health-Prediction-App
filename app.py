
import streamlit as st
import pandas as pd

from database import create_table, get_connection, get_all_patients
from validation import validate_patient
from ai_service import generate_remarks

st.set_page_config(page_title="Health Prediction App", page_icon="🏥")

create_table()

st.title("🏥 Health Prediction App")
st.write("Manage patient health records and view informational remarks.")

# Add Patient
st.header("Add Patient")

with st.form("patient_form"):
    full_name = st.text_input("Full Name")
    dob = st.text_input("Date of Birth (DD.MM.YYYY)")
    email = st.text_input("Email")
    glucose = st.text_input("Glucose")
    haemoglobin = st.text_input("Haemoglobin")
    cholesterol = st.text_input("Cholesterol")

    submitted = st.form_submit_button("Add Patient")

    if submitted:
        valid, message = validate_patient(
            full_name, dob, email,
            glucose, haemoglobin, cholesterol
        )

        if valid:
            remarks = generate_remarks(
                float(glucose),
                float(haemoglobin),
                float(cholesterol)
            )

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO patients
                (full_name, dob, email, glucose, haemoglobin,
                 cholesterol, remarks)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                full_name, dob, email,
                float(glucose), float(haemoglobin),
                float(cholesterol), remarks
            ))

            conn.commit()
            conn.close()

            st.success("Patient added successfully!")
            st.rerun()
        else:
            st.error(message)


# View Patients
st.header("All Patient Records")

records = get_all_patients()

if records:
    columns = [
        "ID", "Full Name", "DOB", "Email",
        "Glucose", "Haemoglobin", "Cholesterol", "Remarks"
    ]

    df = pd.DataFrame(records, columns=columns)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No patient records available.")


# Update Patient
st.header("Update Patient Email")

if records:
    patient_ids = [record[0] for record in records]

    selected_id = st.selectbox("Select Patient ID", patient_ids)
    new_email = st.text_input("Enter New Email")

    if st.button("Update Email"):
        import re

        if not re.match(r"^[\w.+-]+@[\w-]+\.[\w.-]+$", new_email):
            st.error("Please enter a valid email.")
        else:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "UPDATE patients SET email = ? WHERE id = ?",
                (new_email, selected_id)
            )

            conn.commit()
            conn.close()

            st.success("Email updated successfully!")
            st.rerun()


# Delete Patient
st.header("Delete Patient")

if records:
    delete_id = st.selectbox(
        "Select Patient ID to Delete",
        patient_ids,
        key="delete_id"
    )

    if st.button("Delete Patient"):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM patients WHERE id = ?",
            (delete_id,)
        )

        conn.commit()
        conn.close()

        st.success("Patient deleted successfully!")
        st.rerun()
