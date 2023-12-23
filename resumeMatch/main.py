import os

# Example file paths (replace these with your file paths)
resume_file_path = 'resume/Laurente.txt'
job_description_file_path = 'resume/sample_job_desc.txt'

def read_files_to_list(resume_path, job_description_path):
    content_list = []

    # Read content of resume file
    with open(resume_path, 'r') as resume_file:
        content_list.append(resume_file.read().lower().strip())

    # Read content of job description file
    with open(job_description_path, 'r') as job_description_file:
        content_list.append(job_description_file.read().lower().strip())

    return content_list

# Get script directory
script_dir = os.path.dirname(__file__)
resume_path = os.path.join(script_dir, resume_file_path)
job_description_path = os.path.join(script_dir, job_description_file_path)

# Call the function with the file paths
resume_list = read_files_to_list(resume_path, job_description_path)

resume = resume_list[0]
job_description = resume_list[1]

print(resume)
print(job_description)


