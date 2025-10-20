import re
import importlib

try:
    pdfplumber = importlib.import_module('pdfplumber')
except ImportError:
    pdfplumber = None

try:
    docx = importlib.import_module('docx')
except ImportError:
    docx = None

def extract_text_from_pdf(file):
    if pdfplumber is None:
        raise ImportError("pdfplumber is required. Install with: pip install pdfplumber")
    with pdfplumber.open(file) as pdf:
        return "\n".join(page.extract_text() or "" for page in pdf.pages)

def extract_text_from_docx(file):
    if docx is None:
        raise ImportError("python-docx is required. Install with: pip install python-docx")
    doc = docx.Document(file)
    return "\n".join(para.text for para in doc.paragraphs)

def extract_personal_info(text):
    info = {}
    email = re.search(r'[\w\.-]+@[\w\.-]+', text)
    if email:
        info['email'] = email.group(0)
    phone = re.search(r'(\+\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}', text)
    if phone:
        info['phone'] = phone.group(0)
    for line in text.split('\n'):
        line = line.strip()
        if line and line not in (info.get('email', ''), info.get('phone', '')):
            info['name'] = line
            break
    return info

def extract_section(text, keywords, all_keywords):
    content = []
    start_pattern = r'(?i)^(' + '|'.join(keywords) + r')[:\s]*$'
    stop_keywords = [k for k in all_keywords if k not in keywords]
    stop_pattern = r'(?i)^(' + '|'.join(stop_keywords) + r')[:\s]*$'

    lines = text.split('\n')
    capturing = False
    current = ""

    for line in lines:
        if re.match(start_pattern, line.strip()):
            if capturing and current:
                content.append(current.strip())
            capturing = True
            current = ""
            continue
        if re.match(stop_pattern, line.strip()) and capturing:
            if current:
                content.append(current.strip())
            capturing = False
            current = ""
        if capturing:
            current += line + '\n'

    if capturing and current:
        content.append(current.strip())
    return content or ["Not found"]

ALL_KEYWORDS = [
    'Experience', 'Employment History', 'Work Experience', 'Education', 'Academic Background',
    'Certifications', 'Licenses', 'Honors', 'Professional Certifications', 'Certificates',
    'Certifications & Awards', 'Professional Development', 'Training & Certifications',
    'Credentials', 'Qualifications', 'Awards', 'Skills', 'Technical Skills', 'Programming Languages'
]

def extract_skills(text):
    section = ' '.join(extract_section(text, ['Skills', 'Technical Skills', 'Programming Languages'], ALL_KEYWORDS))
    search_text = section if section != "Not found" else text

    skills = []
    skill_list = [
        'Python', 'Java', 'C++', 'C#', 'JavaScript', 'TypeScript', 'Go', 'Rust', 'PHP', 'Ruby',
        'React', 'Angular', 'Vue.js', 'Node.js', 'Express.js', 'Django', 'Flask', 'Spring Boot',
        'SQL', 'NoSQL', 'PostgreSQL', 'MySQL', 'MongoDB', 'Redis', 'Cassandra',
        'AWS', 'Azure', 'Google Cloud', 'GCP', 'Docker', 'Kubernetes', 'Terraform', 'Ansible',
        'Machine Learning', 'Data Science', 'TensorFlow', 'PyTorch', 'scikit-learn', 'Pandas', 'NumPy',
        'Data Analysis', 'CI/CD', 'Git', 'Agile', 'Scrum', 'DevOps', 'Microservices', 'RESTful APIs',
        'GraphQL', 'HTML', 'CSS', 'SASS', 'LESS', 'Bootstrap', 'Tailwind CSS', 'Jenkins', 'CircleCI',
        'Travis CI', 'JIRA', 'Confluence', 'Figma', 'Adobe XD', 'Photoshop', 'Illustrator', 'SEO',
        'Content Management', 'WordPress', 'Drupal', 'Magento', 'Salesforce', 'C', 'Linux', 'Unix',
        'Shell Scripting', 'PowerShell', 'Hadoop', 'Spark', 'Tableau', 'Power BI', 'Software Development',
        'Web Development', 'Mobile Development', 'iOS', 'Android', 'Swift', 'Kotlin', 'Communication Skills',
        'Problem-Solving', 'Leadership', 'Teamwork', 'Project Management'
    ]

    for skill in skill_list:
        if re.search(r'\b' + re.escape(skill) + r'\b', search_text, re.IGNORECASE):
            skills.append(skill)
    return skills

def extract_experience(text):
    sections = extract_section(text, ['Experience', 'Employment History', 'Work Experience'], ALL_KEYWORDS)
    if not sections or sections == ["Not found"]:
        return ["Not found"]

    jobs = []
    for section in sections:
        lines = [line.strip() for line in section.split('\n') if line.strip()]
        i = 0
        while i < len(lines):
            title = ''
            if len(lines[i].split()) <= 3 and any(k in lines[i].upper() for k in ['ENGINEER', 'DEVELOPER', 'MANAGER', 'ANALYST', 'DESIGNER', 'CONSULTANT', 'SPECIALIST', 'DIRECTOR', 'LEAD', 'SENIOR', 'JUNIOR', 'WEB', 'SOFTWARE', 'DATA', 'SYSTEMS', 'NETWORK', 'SECURITY', 'QUALITY', 'PRODUCT', 'PROJECT', 'BUSINESS', 'SALES', 'MARKETING', 'HR', 'FINANCE', 'ACCOUNTING', 'LEGAL', 'OPERATIONS', 'LOGISTICS', 'SUPPLY', 'PURCHASING', 'ADMINISTRATIVE', 'EXECUTIVE', 'PRESIDENT', 'CEO', 'CTO', 'CFO', 'COO', 'VP', 'DIRECTOR', 'MANAGER', 'SUPERVISOR', 'COORDINATOR', 'ASSISTANT', 'SPECIALIST', 'ANALYST', 'CONSULTANT', 'ARCHITECT', 'ENGINEER', 'DEVELOPER', 'DESIGNER', 'TESTER', 'ADMIN', 'SUPPORT', 'TECHNICIAN', 'INTERN', 'TRAINEE']):
                title = lines[i]
                i += 1
            if i < len(lines) and '•' in lines[i]:
                company = lines[i]
                i += 1
                if i < len(lines) and re.search(r'\d{2}/\d{4}', lines[i]):
                    # Skip date line
                    i += 1
                    description = []
                    while i < len(lines) and not (len(lines[i].split()) <= 3 and any(k in lines[i].upper() for k in ['ENGINEER', 'DEVELOPER', 'MANAGER', 'ANALYST', 'DESIGNER', 'CONSULTANT', 'SPECIALIST', 'DIRECTOR', 'LEAD', 'SENIOR', 'JUNIOR', 'WEB', 'SOFTWARE', 'DATA', 'SYSTEMS', 'NETWORK', 'SECURITY', 'QUALITY', 'PRODUCT', 'PROJECT', 'BUSINESS', 'SALES', 'MARKETING', 'HR', 'FINANCE', 'ACCOUNTING', 'LEGAL', 'OPERATIONS', 'LOGISTICS', 'SUPPLY', 'PURCHASING', 'ADMINISTRATIVE', 'EXECUTIVE', 'PRESIDENT', 'CEO', 'CTO', 'CFO', 'COO', 'VP', 'DIRECTOR', 'MANAGER', 'SUPERVISOR', 'COORDINATOR', 'ASSISTANT', 'SPECIALIST', 'ANALYST', 'CONSULTANT', 'ARCHITECT', 'ENGINEER', 'DEVELOPER', 'DESIGNER', 'TESTER', 'ADMIN', 'SUPPORT', 'TECHNICIAN', 'INTERN', 'TRAINEE'])) and not ('•' in lines[i]):
                        description.append(lines[i])
                        i += 1
                    jobs.append({
                        'title': title or 'Title not specified',
                        'company': company,
                        'description': description
                    })
                else:
                    i += 1
            else:
                i += 1

    return jobs if jobs else sections

def extract_education(text):
    return extract_section(text, ['Education', 'Academic Background'], ALL_KEYWORDS)

def extract_certifications(text):
    return extract_section(text, ['Certifications', 'Licenses', 'Honors', 'Professional Certifications',
                                'Certificates', 'Certifications & Awards', 'Professional Development',
                                'Training & Certifications', 'Credentials', 'Qualifications', 'Awards'], ALL_KEYWORDS)

def extract(file_path):
    try:
        filename = file_path.lower()
        if filename.endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
        elif filename.endswith('.docx'):
            text = extract_text_from_docx(file_path)
        else:
            return {"Error": "Unsupported file format. Only PDF and DOCX files are supported."}

        if not text.strip():
            return {"Error": "Could not extract text from the file."}

        return {
            "Personal Info": extract_personal_info(text),
            "Skills": extract_skills(text),
            "Experience": extract_experience(text),
            "Education": extract_education(text),
            "Certifications": extract_certifications(text)
        }
    except Exception as e:
        return {"Error": str(e)}
