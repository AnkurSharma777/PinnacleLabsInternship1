def clean_text(text):
    # Remove unnecessary whitespace and special characters
    return ' '.join(text.split())

def read_file(file_path):
    # Read the content of a file and return it
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_to_file(file_path, content):
    # Write content to a file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def format_extracted_data(data):
    # Format the extracted data into a structured format
    return {
        'name': data.get('name', ''),
        'email': data.get('email', ''),
        'phone': data.get('phone', ''),
        'skills': data.get('skills', []),
        'experience': data.get('experience', []),
        'education': data.get('education', []),
        'certifications': data.get('certifications', [])
    }