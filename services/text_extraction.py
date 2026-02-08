import pdfplumber
import streamlit as st
import docx2txt
import re
#extracting text from the resumes given (.pdf, .docx, .txt):
def extract_text_from_pdf(uploaded_file):
    text = ""
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text +=page_text + "/n"
    except Exception as e:
        st.error(f"error extarctimg text from pdf:{e}")
        text =""
    return text

def extract_text_from_docx(uploaded_file):
    return docx2txt.process(uploaded_file)

def extract_text_from_txt(uploaded_file):
        return uploaded_file.read().decode("utf-8")
    
## extracting name from resume
def name_from_text(text):
    name_pattern = re.compile(r'^[A-Z][a-z]+(?:\s+[A-Z][a-z]+){1}')
    match = re.search(name_pattern,text)
    if match:
        return match.group(0)
    allCaps_pattern = re.compile(r'^[A-Z][A-Z]+(?:\s+[A-Z][A-Z]+){1}')
    match = re.search(allCaps_pattern,text)
    if match:
        return match.group(0).strip()
    return "Name not found"
## extracting contact info from resume
def extract_contact_info(text):
    email= None
    phone_number= None
    linkedin = None
    
    clean_numbers_string = re.sub(r'[^0-9]', '', text)
    
    email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+')
    
    linkedin_pattern = re.compile(r'linkedin\.com/in/[\w-]+')
    
    email_match = re.search(email_pattern, text)
    if email_match:
        email = email_match.group(0)
        
    phone_match = re.search(r'91(\d{10})', clean_numbers_string)
    if phone_match:
        phone_number = phone_match.group(1)
        
    linkedin_match = re.search(linkedin_pattern,text)
    if linkedin_match:
        linkedin = linkedin_match.group(0) 
        
    return{
        "email": email,
        "phonenumber": phone_number,
        "Linkedin": linkedin
    }
## extarcting urls for finding linekdin links of candidates
def extract_url(uploaded_file):
    found_urls = []
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                for link in page.hyperlinks:
                    if link and link.get("uri"):
                        found_urls.append(link["uri"])
    except Exception as e:
        print(f"error extarcting embedded urls with pdf plumber: {e}")
    return list(set(found_urls))
def extarct_url_linkedin(found_urls,keyword):
    return[url for url in found_urls if keyword.lower() in url.lower()]
    

##education extraction
def extract_education(text):
    education_keyword = ["Education", "Academics", "Educational Background", "Academics Background", "Qualification", "EDUCATION", "QUALIFICATION", "ACADEMICS", "ACADEMICS BACKGROUND", "EDUCATIONAL BACKGROUND"]
    next_section= ["Skills", "SKILLS", "EXPERIENCE", "PROJECTS", "CERTIFICATIONS", "WORK HISTORY", "INTERNSHIPS", 
                   "INTERNSHIPS", "PROFESSIONAL", "PROFILE", "SUMMARY","experience", "projects", "certifications",
                    "work history", "professional", "internship", "INTERNSHIP EXPERIENCES" "profile", "summary", "contact","Awards", "Publications", "Interests", "Technical Skills"]
    education_keyword = [kw.lower() for  kw in education_keyword]
    next_section = [kw.lower() for kw in next_section]
    lines = text.split('\n')
    education_lines = []
    capture = False
    
    for line in lines:
        line_clean = line.strip().lower()
        if not capture and any(keyword in line_clean for keyword in education_keyword):
            capture = True
            continue
        if capture and any(keyword in line_clean for keyword in next_section):
            break
        if capture and line.strip():
            education_lines.append(line.strip())
    if education_lines:
        return '\n'.join(education_lines)
    else:
        return "Educational details not found."    
    

folder_path = "resumes"