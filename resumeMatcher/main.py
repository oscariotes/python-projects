from flask import Flask, request, render_template
import os

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the POST request has the file part for resumeFile
        if 'resumeFile' not in request.files:
            return 'No Resume File part'
        
        resumeFile = request.files['resumeFile']
        
        # Check if the user doesn't select a file for resumeFile
        if resumeFile.filename == '':
            return 'No selected file for Resume'

        # Check if the POST request has the file part for jobDescriptionFile
        if 'jobDescriptionFile' not in request.files:
            return 'No Job Description File part'
        
        jobDescriptionFile = request.files['jobDescriptionFile']
        
        # Check if the user doesn't select a file for jobDescriptionFile
        if jobDescriptionFile.filename == '':
            return 'No selected file for Job Description'
        
        # Specify the subdirectories within the current directory
        resume_folder = 'resume'
        job_description = 'job'
        
        os.makedirs(resume_folder, exist_ok=True)  # Create the directory if it doesn't exist
        os.makedirs(job_description, exist_ok=True)  # Create the directory if it doesn't exist
        
        # Save the uploaded files to the respective subdirectories
        resume_folder_path = os.path.join(resume_folder, resumeFile.filename)
        job_description_path = os.path.join(job_description, jobDescriptionFile.filename)
        
        resumeFile.save(resume_folder_path)
        jobDescriptionFile.save(job_description_path)

        return 'Files uploaded successfully'

    return render_template('upload.html')  # Render an HTML template with the file upload form


    

if __name__ == '__main__':
    app.run(debug=True)

