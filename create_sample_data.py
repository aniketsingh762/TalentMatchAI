import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TalentMatch_AI.settings')
django.setup()

from resume_checker.models import JobDescription

# Create sample job descriptions
job_descriptions = [
    {
        'job_title': 'Software Engineer',
        'job_description': 'We are looking for a skilled Software Engineer with experience in Python, Django, and REST APIs. The candidate should have knowledge of database design, testing, and deployment processes. Experience with cloud platforms like AWS or Azure is a plus.'
    },
    {
        'job_title': 'Data Scientist',
        'job_description': 'Seeking a Data Scientist with expertise in machine learning, statistical analysis, and data visualization. Proficiency in Python, R, and SQL is required. Experience with TensorFlow, PyTorch, or scikit-learn is highly valued.'
    },
    {
        'job_title': 'Frontend Developer',
        'job_description': 'Looking for a Frontend Developer with strong skills in React, JavaScript, HTML, and CSS. Experience with modern frontend frameworks and tools like Webpack, Redux, and responsive design is essential. Knowledge of TypeScript is a plus.'
    },
    {
        'job_title': 'DevOps Engineer',
        'job_description': 'We need a DevOps Engineer with experience in CI/CD pipelines, Docker, Kubernetes, and cloud infrastructure. Knowledge of monitoring tools, automation, and security best practices is required. Experience with Terraform and Ansible is preferred.'
    },
    {
        'job_title': 'Product Manager',
        'job_description': 'Seeking a Product Manager with experience in agile methodologies, product lifecycle management, and stakeholder communication. Strong analytical skills and experience with product analytics tools are essential. MBA or related advanced degree is preferred.'
    }
]

# Create job descriptions in the database
for job_data in job_descriptions:
    job, created = JobDescription.objects.get_or_create(
        job_title=job_data['job_title'],
        defaults={'job_description': job_data['job_description']}
    )
    if created:
        print(f"Created job: {job.job_title}")
    else:
        print(f"Job already exists: {job.job_title}")

print("Sample data creation completed!")