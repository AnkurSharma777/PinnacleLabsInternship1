from flask import Flask, render_template, request, jsonify
import os
from parser.extractor import extract

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'resume' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400

        file = request.files['resume']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        if file and file.filename.lower().endswith(('.pdf', '.docx')):
            try:
                # Save uploaded file temporarily
                upload_dir = 'uploads'
                if not os.path.exists(upload_dir):
                    os.makedirs(upload_dir)

                file_path = os.path.join(upload_dir, file.filename)
                file.save(file_path)

                # Extract resume data
                resume_data = extract(file_path)

                # Clean up uploaded file
                os.remove(file_path)

                return jsonify({
                    'success': True,
                    'data': resume_data
                })

            except Exception as e:
                return jsonify({'error': str(e)}), 500
        else:
            return jsonify({'error': 'Invalid file type. Only PDF and DOCX files are allowed.'}), 400

    return render_template('index.html')

if __name__ == '__main__':
    print("Starting Resume Parser Flask server...")
    print("Server will be available at: http://localhost:5001")
    print("Press Ctrl+C to stop the server")
    app.run(debug=True, port=5001, host='0.0.0.0')
