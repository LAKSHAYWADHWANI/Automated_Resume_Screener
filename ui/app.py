def run_app():
    import streamlit as st
    import pandas as pd

    from services.pre_processing import clean_text
    from services.text_extraction import (
        extract_text_from_pdf,
        extract_text_from_docx,
        extract_text_from_txt,
        name_from_text,
        extract_contact_info,
        extract_url,
        extarct_url_linkedin,
        extract_education,
    )
    from services.skills import extract_skills_from_text
    from services.scoring import score_resume_skills_semantic
    from core.config import SKILLS_FILE, supported_file_extensions as extensions
    from ui.utility import csv_to_excel, score_bar_plotly

    # ---------------- PAGE CONFIG ----------------
    st.set_page_config(page_title="Resume Screener", layout="wide")

    # ---------------- SIDEBAR ----------------
    with st.sidebar:
        st.title("Upload & Match")
        jd_input = st.text_area("Paste the Job Description here:", height=200)
        uploaded_files = st.file_uploader(
            "Upload resumes",
            accept_multiple_files=True,
            type=[ext.replace(".", "") for ext in extensions],
        )
        start_button = st.button("START SCREENING")

    # ---------------- MAIN TITLE ----------------
    st.title("Automated Resume Screener")
    st.write("Easily find the best candidates for your job description.")

    # ---------------- MAIN LOGIC ----------------
    if not start_button:
        return

    if not jd_input:
        st.warning("Please enter a job description.")
        return

    if not uploaded_files:
        st.warning("No resume uploaded.")
        return

    with st.spinner("Screening in progress..."):
        cleaned_jd = clean_text(jd_input)
        jd_skills = extract_skills_from_text(cleaned_jd, SKILLS_FILE)

        results = []

        for uploaded_file in uploaded_files:
            file_name = uploaded_file.name.lower()

            if file_name.endswith(".pdf"):
                resume_text = extract_text_from_pdf(uploaded_file)
            elif file_name.endswith(".docx"):
                resume_text = extract_text_from_docx(uploaded_file)
            elif file_name.endswith(".txt"):
                resume_text = extract_text_from_txt(uploaded_file)
            else:
                continue

            cleaned_resume = clean_text(resume_text)
            resume_skills = extract_skills_from_text(cleaned_resume, SKILLS_FILE)

            score, matched = score_resume_skills_semantic(resume_skills, jd_skills)

            name = name_from_text(resume_text)
            education = extract_education(resume_text)
            contact_info = extract_contact_info(cleaned_resume)

            all_urls = []
            if file_name.endswith(".pdf"):
                all_urls.extend(extract_url(uploaded_file))

            linkedin = extarct_url_linkedin(all_urls, "linkedin")
            github = extarct_url_linkedin(all_urls, "github")

            results.append(
                {
                    "Name": name,
                    "Filename": file_name,
                    "Score (%)": score,
                    "Education": education,
                    "Linkedin": ", ".join(linkedin),
                    "Github": ", ".join(github),
                    "Email": contact_info.get("email"),
                    "Phone": contact_info.get("phonenumber"),
                    "Matched Skills": ", ".join(matched) or "None",
                }
            )

    # ---------------- RESULTS DISPLAY ----------------
    df_results = pd.DataFrame(results).sort_values(by="Score (%)", ascending=False)

    st.success("Screening completed.")
    st.subheader("Visual Screening Results")
    st.plotly_chart(score_bar_plotly(df_results), use_container_width=True)

    st.subheader("All Screening Results")
    st.dataframe(df_results, use_container_width=True)

    excel_data = csv_to_excel(df_results)
    st.download_button(
        label="Download Results as Excel",
        data=excel_data,
        file_name="resume_screening_results.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
