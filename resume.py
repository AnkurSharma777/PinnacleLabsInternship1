class Resume:
    def __init__(self, name, email, phone, address, skills, experience, education, certifications):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.skills = skills
        self.experience = experience
        self.education = education
        self.certifications = certifications

    def get_personal_info(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address
        }

    def get_skills(self):
        return self.skills

    def get_experience(self):
        return self.experience

    def get_education(self):
        return self.education

    def get_certifications(self):
        return self.certifications

    def display_resume(self):
        resume_info = f"Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\nAddress: {self.address}\n"
        resume_info += "Skills: " + ", ".join(self.skills) + "\n"
        resume_info += "Experience:\n"
        for exp in self.experience:
            resume_info += f"  - {exp['position']} at {exp['company']} ({exp['duration']}): {exp['description']}\n"
        resume_info += "Education:\n"
        for edu in self.education:
            resume_info += f"  - {edu['degree']} from {edu['university']} ({edu['year']})\n"
        resume_info += "Certifications: " + ", ".join(self.certifications) + "\n"
        return resume_info.strip()