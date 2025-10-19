# Resume Parser

This project is a Resume Parser application developed using Python and Flask. It aims to extract and organize information from resumes to enhance HR processes and candidate selection.

## Project Structure

The project is organized as follows:

```
resume-parser
├── src
│   ├── app.py                # Main entry point of the application
│   ├── parser
│   │   ├── __init__.py       # Marks the parser directory as a package
│   │   ├── extractor.py       # Core logic for extracting information from resumes
│   │   └── utils.py          # Utility functions for the parsing process
│   ├── models
│   │   ├── __init__.py       # Marks the models directory as a package
│   │   └── resume.py         # Defines the Resume class for parsed resumes
│   ├── static
│   │   └── style.css         # CSS styles for the web application
│   └── templates
│       └── index.html        # Main HTML template for the web application
├── flask_env/                # Virtual environment directory
├── requirements.txt           # Lists Python dependencies required for the project
├── README.md                  # Documentation for the project
└── .gitignore                 # Specifies files and directories to be ignored by Git
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd resume-parser
   ```

2. **Activate the Virtual Environment**
   ```bash
   source flask_env/bin/activate  # On Windows use `flask_env\Scripts\activate`
   ```

3. **Run the Application**
   ```bash
   python src/app.py
   ```

4. **Access the Application**
   Open your web browser and navigate to `http://127.0.0.1:5001` to access the Resume Parser application.

## Usage Guidelines

- Upload a resume in PDF or DOCX format using the provided interface.
- The application will parse the resume and display the extracted information, including personal details, skills, experience, education, and certifications.

## Overview of Functionality

The Resume Parser utilizes text extraction techniques to extract relevant information from resumes. Key features include:

- **Personal Information Extraction**: Captures name, email, phone number.
- **Skills Extraction**: Identifies technical and soft skills listed in the resume.
- **Experience Extraction**: Parses work experience details.
- **Education Extraction**: Extracts educational qualifications.
- **Certifications Extraction**: Extracts certifications and awards.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
