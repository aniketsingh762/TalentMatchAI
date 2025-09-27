# **TalentMatch AI** 🎯📄  

**AI-powered Resume Ranking System built with Django**  

## **📌 Overview**  

TalentMatch AI is a Django-based web application that uses **Natural Language Processing (NLP) and Machine Learning (ML)** to analyze and rank resumes based on job descriptions. It helps recruiters efficiently filter and prioritize resumes based on skills, experience, and qualifications.  

![TalentMatch AI Dashboard](screenshots/dashboard.png)
*Modern UI with dark mode support*

## **🚀 Features**  

✅ **AI-Powered Resume Screening** – Automatically ranks resumes based on relevance to the job description.  
✅ **Skill Matching** – Extracts and compares candidate skills with job requirements.  
✅ **Experience & Qualification Analysis** – Evaluates work experience and education.  
✅ **Customizable Ranking Criteria** – Adjust weights for different parameters.  
✅ **PDF & TXT Parsing** – Supports multiple resume formats.  
✅ **Admin Dashboard** – Manage resumes, job descriptions, and ranking criteria.  
✅ **REST API Support** – Integrate with external HR systems.  
✅ **Advanced Filtering** – Filter by experience level and skill focus.  
✅ **Dark Mode Support** – Toggle between light and dark themes.  
✅ **Enhanced Visualization** – Beautiful result displays with progress indicators.  

## **✨ Recent Improvements**  

### **UI/UX Enhancements**

- Modern, responsive design with Tailwind CSS
- Dark mode toggle with automatic preference saving
- Improved form handling and user feedback
- Enhanced result visualization with skill tags and progress bars
- Better file input handling with filename display

### **Filtering Capabilities**

- Experience level filtering (Entry, Mid, Senior)
- Skills focus filtering (Technical, Soft, Leadership)
- Improved job description selection

### **Visualization Improvements**

- Visual progress indicators for match scores
- Interactive skill tags with search functionality
- Enhanced result cards with hover effects
- Action buttons for downloading and sharing results

## **🛠️ Tech Stack**  

- **Backend:** Django, Django REST Framework  
- **Frontend:** HTML, CSS, JavaScript, HTMX, Tailwind CSS  
- **AI/NLP:** SpaCy, Groq API  
- **Database:** SQLite (development), PostgreSQL/MySQL (production)  
- **File Handling:** pdfplumber  

## **🔧 Installation & Setup**  

### **1️⃣ Clone the Repository**  

```bash
git clone https://github.com/yourusername/Resume_Ranking_AI_by_Django.git
cd Resume_Ranking_AI_by_Django
```

### **2️⃣ Create & Activate Virtual Environment**  

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### **3️⃣ Install Dependencies**  

```bash
pip install -r requirements.txt
```

### **4️⃣ Set up Environment Variables**  

Create a `.env` file in the project root with your configuration:

```env
API_KEY=your_groq_api_key_here
```

### **5️⃣ Run Database Migrations**  

```bash
python manage.py migrate
```

### **6️⃣ Create a Superuser (Optional)**  

```bash
python manage.py createsuperuser
```

### **7️⃣ Start the Development Server**  

```bash
python manage.py runserver
```

Access the app at **<http://127.0.0.1:8000/>**  

## **📂 Project Structure**  

```
TalentMatch_AI/
│── TalentMatch_AI/      # Main Django app
│── resume_checker/      # AI resume processing logic
│── templates/           # Frontend templates
│── static/              # CSS, JS, images
│── media/               # Uploaded resumes
│── requirements.txt     # Dependencies
│── manage.py            # Django entry point
│── .env                 # Environment variables
```

<!-- ## **📸 Screenshots**
![Main Dashboard](screenshots/dashboard.png)
*Main dashboard with job selection and resume upload*

![Results View](screenshots/results.png)
*Enhanced results visualization with skill tags and match score*

![Dark Mode](screenshots/dark-mode.png)
*Dark mode support for comfortable nighttime use* -->

## **📌 Future Enhancements**  

✅ AI-based **Resume Summarization**  
✅ **Job Matching Recommendations**  
✅ **Dashboard with Data Analytics**  
✅ **Multi-language Support**  
✅ **Advanced Filtering Options**  
✅ **Export to PDF/CSV**  

## **🤝 Contributing**  

Pull requests are welcome! Follow the standard **Git flow** and create a feature branch before submitting PRs.  

## **📜 License**  

This project is open-source under the **MIT License**.  
