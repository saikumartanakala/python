class DevOpsPortfolio:
    def __init__(self, name, skills, projects, experience, contact):
        self.name = name
        self.skills = skills
        self.projects = projects
        self.experience = experience
        self.contact = contact

    def display_portfolio(self):
        print(f"Portfolio of {self.name}\n")
        print("Skills:")
        for skill in self.skills:
            print(f"- {skill}")
        
        print("\nProjects:")
        for project in self.projects:
            print(f"- {project['name']}: {project['description']} (Technologies: {', '.join(project['technologies'])})")
        
        print("\nExperience:")
        for exp in self.experience:
            print(f"- {exp['role']} at {exp['company']} ({exp['duration']})")
        
        print("\nContact Information:")
        print(f"Email: {self.contact['email']}")
        print(f"LinkedIn: {self.contact['linkedin']}")

# Sample usage
if __name__ == "__main__":
    # Define the portfolio details
    name = "John Doe"
    skills = ["Docker", "Kubernetes", "CI/CD", "AWS", "Terraform"]
    projects = [
        {"name": "Web App Deployment", "description": "Deployed a web application using Docker and Kubernetes.", "technologies": ["Docker", "Kubernetes", "AWS"]},
        {"name": "Infrastructure as Code", "description": "Automated infrastructure provisioning using Terraform.", "technologies": ["Terraform", "AWS"]},
    ]
    experience = [
        {"role": "DevOps Engineer", "company": "Tech Solutions Inc.", "duration": "Jan 2021 - Present"},
        {"role": "Systems Administrator", "company": "IT Services Co.", "duration": "Jun 2019 - Dec 2020"},
    ]
    contact = {
        "email": "john.doe@example.com",
        "linkedin": "https://www.linkedin.com/in/johndoe"
    }

    # Create and display the portfolio
    portfolio = DevOpsPortfolio(name, skills, projects, experience, contact)
    portfolio.display_portfolio()
