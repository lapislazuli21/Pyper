from parsers.resume_parser import ResumeParser


def main():
    """Main function to run the application."""

    # Path to the resume, relative to the root `career-copilot/` directory
    resume_path = 'resources/resumes/my_resume.pdf'

    print(f"--- Parsing Resume: {resume_path} ---")

    # 1. Create an instance of the parser
    parser = ResumeParser(resume_path)

    # 2. Extract information using the class methods
    skills = parser.get_skills()
    contacts = parser.get_contact_info()

    # 3. Display the extracted information
    print("\n--- Extracted Information ---")
    print(f"Email: {contacts.get('email', 'Not found')}")
    print(f"Phone: {contacts.get('phone', 'Not found')}")

    if skills:
        print("\n--- Found Skills ---")
        for skill in sorted(skills):  # Sort skills alphabetically
            print(f"- {skill.capitalize()}")
    else:
        print("\nNo skills from our list were found.")


if __name__ == "__main__":
    main()