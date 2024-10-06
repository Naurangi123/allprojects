import pdfplumber
import re
import pyresumeparser 
import docx
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm

class ResumeParser:
    def __init__(self, file):
        self.file = file
        self.data = {
            "name": "",
            "phone": "",
            "email": "",
            "link": "",
            "education": [],
            "professional_experience": [],
            "technologies": [],
            "projects": [] 
        }

    def parse(self):
        file_extension = self.file.name.split('.')[-1].lower()
        if file_extension in ['pdf', 'docx', 'txt']:
            parse_func = getattr(self, f'parse_{file_extension}', None)
            if parse_func:
                return parse_func()
        raise ValueError(f"Unsupported file format: {file_extension}")

    def parse_pdf(self):
        # Extract text from PDF
        with pdfplumber.open(self.file) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:  # Check if text was extracted
                    text += page_text + "\n"
        
        if not text.strip():  # If no text is extracted
            raise ValueError("No text could be extracted from the PDF.")

        # Use pyresumeparser for structured extraction
        return self.extract_info_with_pyresumeparser(text)

    def parse_docx(self):
        text = ""
        doc = docx.Document(self.file)
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        
        self.extract_info(text)
        return self.data

    def parse_txt(self):
        text = self.file.read().decode('utf-8')
        self.extract_info(text)
        return self.data

    def extract_info_with_pyresumeparser(self, text):
        # You can save the text to a temporary file for pyresumeparser
        with open('temp_resume.txt', 'w') as temp_file:
            temp_file.write(text)
        
        # Parse the resume using pyresumeparser
        data = pyresumeparser().get_extracted_data('temp_resume.txt')
        
        # Fill in the data based on extracted information
        self.data['name'] = data.get('name', "")
        self.data['phone'] = data.get('phone', "")
        self.data['email'] = data.get('email', "")
        self.data['link'] = data.get('linkedin', "")  # Assuming linkedin is the link you want
        self.data['education'] = data.get('education', [])
        self.data['professional_experience'] = data.get('experience', [])
        self.data['technologies'] = data.get('skills', [])
        self.data['projects'] = data.get('projects', [])

        return self.data

    def extract_info(self, text):
        # Retain your existing extract_info methods for DOCX and TXT
        self.data["name"] = self.extract_name(text)
        self.data["phone"] = self.extract_phone(text)
        self.data["email"] = self.extract_email(text)
        self.data["link"] = self.extract_link(text)
        self.data["education"] = self.extract_education(text)
        self.data["professional_experience"] = self.extract_work_experience(text)
        self.data["technologies"] = self.extract_technologies(text)
        self.data["projects"] = self.extract_projects_from_resume(text)

    def extract_name(self, text):
        name_regex = r"(?i)(?:Name|Candidate)\s*:\s*([A-Za-z\s]+)"
        name_match = re.search(name_regex, text)
        return name_match.group(1).strip() if name_match else text.split('\n')[0].strip()

    def extract_phone(self, text):
        phone_regex = r'\+?\d[\d -]{8,12}\d'
        phone_matches = re.findall(phone_regex, text)
        return phone_matches[0] if phone_matches else ""

    def extract_email(self, text):
        email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        email_matches = re.findall(email_regex, text)
        return email_matches[0] if email_matches else ""
    def extract_link(self, text):
        link_regex = r"\b(?:https?://|www\.)[^\s/$.?#].[^\s]*\b"
        link_matches = re.findall(link_regex, text)
        return link_matches[0] if link_matches else ""

    def extract_education(self, text):
        education_pattern = r"(?i)(?:Bachelor|CSE|B\.S\.|B\.A\.|Master|M\.S\.|M\.A\.|Ph\.D\.)\s(?:[A-Za-z]+\s)*[A-Za-z]+"
        return re.findall(education_pattern, text)

    def extract_work_experience(self, text):
        # Regex for company name
        company_pattern = r'(?i)(?:Company|Employer|Organization|Client)\s*:\s*([A-Za-z\s&]+)'
        
        # Regex for job profile
        profile_pattern = r'(?i)(?:Profile|Role|Position)\s*:\s*([A-Za-z\s]+)'
        
        # Regex for duration
        duration_pattern = r'(?i)(\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{4})\s*-\s*'
        
        # Regex for tech stack
        tech_stack_pattern = r'(?i)(?:Tech Stack|Technologies|Tools)\s*:\s*([A-Za-z0-9\s,\/]+)'

        company_matches = re.findall(company_pattern, text, re.IGNORECASE)
        profile_matches = re.findall(profile_pattern, text, re.IGNORECASE)
        duration_matches = re.findall(duration_pattern, text)
        tech_stack_matches = re.findall(tech_stack_pattern, text, re.IGNORECASE)

        return {
            'Company': company_matches,
            'Profiles': profile_matches,
            'Durations': duration_matches,
            'Tech Stacks': tech_stack_matches
        }

    def extract_projects_from_resume(self, text):
        work_pattern = r"(?i)(?P<title>[^\-\(\[]+?)(?:\s*:\s*(?P<duration>[\w\s]+))?\s*(?:\{(?P<month_year>[\w\s,]+)\})?\s*(?:\s*-\s*(?P<tech_stack>[\w\s,]+))?"
        
        projects = []
        
        for match in re.finditer(work_pattern, text):
            project_info = {
                'title': match.group('title').strip() if match.group('title') else "",
                'duration': match.group('duration').strip() if match.group('duration') else "",
                'month_year': match.group('month_year').strip() if match.group('month_year') else "",
                'tech_stack': match.group('tech_stack').strip() if match.group('tech_stack') else "",
            }
            projects.append(project_info)

        return projects

    def extract_technologies(self, text):
        tech_pattern = r"(?i)(?:Python|GitHub|C\+\+|JavaScript|HTML5|CSS|SQL|Django|Flask|React.js|Node.js|AWS|Express.js|MongoDB|MySQL|Git)"
        return list(set(re.findall(tech_pattern, text)))

def upload_resume(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            parser = ResumeParser(uploaded_file)
            try:
                extracted_data = parser.parse()
            except ValueError as e:
                return render(request, 'parser/upload.html', {'form': form, 'error': str(e)})
            
            return render(request, 'parser/data.html', {'data': extracted_data})

    else:
        form = UploadFileForm()
    return render(request, 'parser/upload.html', {'form': form})
