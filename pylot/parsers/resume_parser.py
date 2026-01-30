import PyPDF2
import re
from ..resources.skills_list import SK


class ResumeParser:
    """
    A class to parse resumes from PDF files, extracting text,
    skills, and contact information.
    """

    def __init__(self, pdf_path):
        """
        Initializes the parser with the path to the resume PDF.

        Args:
            pdf_path (str): The file path to the PDF resume.
        """
        self.pdf_path = pdf_path
        self.text = self._extract_text_from_pdf()

    def _extract_text_from_pdf(self):
        """
        Private method to extract text from the PDF file.
        Returns the extracted text as a string.
        """
        try:
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() or ""
                return text.lower()  # Standardize to lowercase
        except FileNotFoundError:
            print(f"Error: The file '{self.pdf_path}' was not found.")
            return ""
        except Exception as e:
            print(f"An error occurred while reading the PDF: {e}")
            return ""

    def get_skills(self):
        """
        Extracts skills from the resume text using the predefined skills list.

        Returns:
            list: A list of unique skills found in the text.
        """
        if not self.text:
            return []

        found_skills = set()
        for skill in SKILLS_LIST:
            # Use regex for whole word matching to avoid partial matches (e.g., 'java' in 'javascript')
            if re.search(r'\b' + re.escape(skill) + r'\b', self.text):
                found_skills.add(skill)
        return list(found_skills)

    def get_contact_info(self):
        """
        Extracts email and phone number from the resume text using regex.

        Returns:
            dict: A dictionary containing the found email and phone number.
        """
        if not self.text:
            return {'email': None, 'phone': None}

        contact_info = {'email': None, 'phone': None}

        # Regex for finding email
        email_regex = r'\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b'
        email_match = re.search(email_regex, self.text)
        if email_match:
            contact_info['email'] = email_match.group(0)

        # Regex for finding phone number
        phone_regex = r'(\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}'
        phone_match = re.search(phone_regex, self.text)
        if phone_match:
            contact_info['phone'] = phone_match.group(0)

        return contact_info