# Portfolio
DevOps Portfolio 🌐

A personal portfolio web application built using **FastAPI**, showcasing DevOps skills, projects, and experience.  
The site includes interactive sections, resume download, and links to GitHub and contact details.

## 🚀 Features:
- Built with **FastAPI** (Python)
- Responsive **HTML + CSS** with templates
- **Static files** for CSS, images, and resume
- Resume **download functionality**
- Containerization-ready for deployment
- Suitable for hosting on **AWS EC2**, **S3**, or **Docker**

## 🛠 Tech Stack:
- **Backend:** FastAPI (Python)
- **Frontend:** HTML, CSS (custom styling)
- **Version Control:** Git & GitHub

## project Structure:
├── portfolio/
│ ├── static/ # CSS, Resume files
│ ├── templates/ # HTML templates
│ ├── pycache/ # Cache files
│
├── main.py # FastAPI application entry point
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore file


## Create Virtual Environment & Install Dependencies
1-python -m venv venv
2-source venv/bin/activate    
#On Windows: venv\Scripts\activate
3-pip install -r requirements.txt


## Run the Application
python -m uvicorn main:app --reload
