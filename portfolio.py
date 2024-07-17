import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Set page configuration
st.set_page_config(layout="wide")

def add_background_animation():
    st.markdown(
        """
        <style>
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
            background: black;
        }

        .stars {
            width: 1px;
            height: 1px;
            background: transparent;
            box-shadow: 
                1000px 300px white,
                1100px 500px white,
                900px 800px white,
                1200px 600px white,
                950px 550px white,
                1050px 750px white,
                850px 650px white;
            animation: animStar 50s linear infinite;
        }

        @keyframes animStar {
            from { transform: translateY(0px); }
            to { transform: translateY(-2000px); }
        }

        .stars:after {
            content: ' ';
            position: absolute;
            top: 0px;
            width: 1px;
            height: 1px;
            background: transparent;
            box-shadow: 
                1000px 300px white,
                1100px 500px white,
                900px 800px white,
                1200px 600px white,
                950px 550px white,
                1050px 750px white,
                850px 650px white;
            animation: animStar 100s linear infinite;
        }

        </style>
        <div class="stars"></div>
        """,
        unsafe_allow_html=True
    )


def main():
    add_background_animation()
    st.title("Ritam Halder - Portfolio")
    
    # Sidebar styling
    st.markdown(
        """
        <style>
            .sidebar .sidebar-content {
                background-color: #f0f2f6;
                padding: 20px;
                border-radius: 5px;
            }
            .sidebar .sidebar-content img {
                border-radius: 50%;
                margin-bottom: 20px;
            }
            .sidebar .sidebar-content a {
                color: #0366d6;
                text-decoration: none;
            }
            .sidebar .sidebar-content a:hover {
                text-decoration: underline;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.sidebar.image("2.jpg", width=250, use_column_width=False)
    st.sidebar.title("Contact Me:")
    st.sidebar.markdown(
        "You can reach out to me via email at ritamhalder655@gmail.com or connect with me on LinkedIn [here](https://www.linkedin.com/in/ritam-halder-a8b46a220/)."
    )
    # Sidebar navigation and chat icon
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["About Me", "Skills", "Projects", "Certificate", "Accomplishments"])

    if page == "About Me":
        show_about_me()
    elif page == "Skills":
        show_skills()
    elif page == "Projects":
        show_projects()
    elif page == "Certificate":
        show_certificate()
    elif page == "Accomplishments":
        show_accomplishments()


def show_about_me():
    st.header("About Me")
    st.write("I'm a B.Tech student majoring in Artificial Intelligence and Machine Learning, deeply passionate about data science's transformative potential.")
    st.write("With a strong foundation in Python, R, and machine learning frameworks, I aspire to contribute to innovative projects that drive meaningful change.")
    st.write("Dedicated to achieving demanding development objectives according to tight schedules while producing impeccable code.")
    st.write("Here's a bit more about me:")
    st.subheader("Education:")
    st.write("- 2021-08 - 2025-05: B.Tech - Artificial Intelligence and Machine Learning, Netaji Subhash Engineering College")
    st.write("- 2021-04: Higher Secondary Education - Science, Burikhali K.M Institution")
    st.write("- Percentage: 89%, Board: WBCHSE")
    st.write("In my leisure time, I indulge in the art of cooking and immerse myself in the captivating worlds of manhwa and manga.")
    st.write("My intellectual pursuits are fueled by a profound interest in political affairs, the evolving paradigms of AI and machine learning, intricate geopolitical dynamics, and the complexities of human relationships.")
    st.write("Guided by these passions, my career goal is to carve a path as an AIML developer, harnessing data science to innovate and shape impactful solutions.")
    st.write("My journey is fueled by a relentless pursuit of knowledge and a drive to excel as a senior data scientist in a leading organization.")
    
    # Download CV button
    st.markdown("<h3 style='color: #5e8ec8;'>Download CV</h3>", unsafe_allow_html=True)
    st.markdown("<a href='link_to_your_cv.pdf' download='Ritam_Halder_CV.pdf'><button>Download CV</button></a>", unsafe_allow_html=True)


def show_skills():
    st.header("Skills")
    
    proficiency_levels = {
        "Data Analysis": {"description": "Proficient in analyzing datasets to extract insights and make data-driven decisions.", "proficiency": 80},
        "Data Science": {"description": "Experienced in applying machine learning algorithms to solve real-world problems and extract valuable insights from data.", "proficiency": 75},
        "Data Structures and Algorithms (DSA)": {"description": "Solid understanding of fundamental data structures and algorithms for efficient problem-solving.", "proficiency": 70},
        "Python programming": {"description": "Strong proficiency in Python programming language for data analysis, machine learning, and web development.", "proficiency": 90},
        "Java programming": {"description": "Proficient in Java programming language with experience in developing robust and scalable applications.", "proficiency": 80},
        "R programming": {"description": "Experienced in statistical computing and data visualization using R programming language.", "proficiency": 70},
        "Natural Language Processing (NLP)": {"description": "Developed NLP models to analyze public sentiment and extract insights from textual data using TensorFlow's KerasNLP API.", "proficiency": 75},
        "Good Communication and Teamwork skill": {"description": "Effective communication and collaboration skills with the ability to work efficiently in a team environment.", "proficiency": 90},
        "TensorFlow": {"description": "Proficient in building deep learning models using TensorFlow for various applications including computer vision and natural language processing.", "proficiency": 80},
        "Database Management Systems (DBMS)": {"description": "Familiar with designing and managing relational databases to store and retrieve data efficiently.", "proficiency": 75},
        "Data Mining": {"description": "Experienced in extracting valuable insights and patterns from large datasets using data mining techniques.", "proficiency": 70}
    }
    
    for skill, details in proficiency_levels.items():
        st.write(f"- {skill}:")
        st.write(f"   - {details['description']}")
        st.progress(details['proficiency'] / 100)

def show_projects():
    st.header("Projects")
    
    st.subheader("Project 1: COVID-19 Sentiment Analysis (LSTM)")
    st.write("Description: Utilized cutting-edge LSTM models in TensorFlow's KerasNLP API to dissect public sentiment surrounding COVID-19 data, unraveling intricate insights into societal perceptions, and identifying prevalent concerns.")
    st.write("GitHub Repository: [Link](https://github.com/RitamHalder/Data_Science_ritam_1st/blob/main/Sentiment_analysis%20on%20Covid19.ipynb)")
    
    st.subheader("Project 2: Healthcare System")
    st.write("Our Healthcare System is a groundbreaking platform designed to revolutionize patient care and diagnosis through advanced machine learning techniques. With a comprehensive approach encompassing multiple health conditions, this system integrates cutting-edge technologies to provide accurate and timely assessments.")
    st.write("At the heart of our system lies a sophisticated hybrid model, meticulously crafted to address various medical concerns. This model amalgamates three powerful machine learning algorithms, each tailored to tackle distinct health challenges.")
    st.write("1. Skin Cancer Detection: The first feature of our healthcare system is a robust skin cancer detection model. Leveraging the power of image processing techniques and Convolutional Neural Networks (CNN), this module can analyze dermoscopic images with exceptional precision. By scrutinizing the intricate details of skin lesions, it accurately identifies potential malignancies, enabling early intervention and treatment.")
    st.write("2. General Heart Attack Prediction: Our system also boasts a comprehensive heart attack prediction model, capable of evaluating the risk factors associated with cardiovascular diseases. Utilizing Support Vector Machine (SVM) classification, this module analyzes a range of input parameters to predict the likelihood of a heart attack. By assessing vital indicators such as blood pressure, cholesterol levels, and lifestyle factors, it empowers users with insights into their cardiovascular health, facilitating proactive measures for prevention and management.")
    st.write("3. Breast Cancer Prediction: Furthermore, our healthcare system incorporates a sophisticated breast cancer prediction model based on Random Forest classification. By examining a multitude of patient-specific factors and diagnostic features, this module delivers accurate assessments of breast cancer risk. Whether it's identifying suspicious abnormalities or reassuring patients with negative results, this tool plays a pivotal role in early detection and personalized healthcare planning.")
    st.write("Website link: [Link](https://aquarion.streamlit.app/)")

def show_certificate():
    st.header("Certificates")
    
    certificates = [
        {"name": "Natural Language Processing with Classification and Vector Spaces - Coursera", "description": "This specialization covers various aspects of machine learning, including supervised learning, unsupervised learning, and deep learning.", "issue_date": "January 2023", "company": "Coursera", "image": "certificates/NLP.png"},
        {"name": "Neural Networks and Deep Learning - Coursera", "description": "This specialization covers various aspects of machine learning, including supervised learning, unsupervised learning, and deep learning.", "issue_date": "April 2023", "company": "Coursera", "image": "certificates/NL&DL.png"},
        {"name": "Supervised Machine Learning: Regression and Classification - Coursera", "description": "This specialization covers various aspects of machine learning, including supervised learning, unsupervised learning, and deep learning.", "issue_date": "April 2023", "company": "Coursera", "image": "certificates/SL.png"},
        {"name": "Java Programming: Solving Problems with Software - Coursera", "description": "This specialization covers various aspects of machine learning, including supervised learning, unsupervised learning, and deep learning.", "issue_date": "April 2023", "company": "Coursera", "image": "certificates/java.png"},
        {"name": "Python Project for Data Science - Coursera", "description": "This specialization covers various aspects of machine learning, including supervised learning, unsupervised learning, and deep learning.", "issue_date": "April 2023", "company": "Coursera", "image": "certificates/Project.png"},
        {"name": "Introduction to Front-End Development - Coursera", "description": "This specialization covers various aspects of machine learning, including supervised learning, unsupervised learning, and deep learning.", "issue_date": "April 2023", "company": "Coursera", "image": "certificates/frontend.png"}
    ]
    
    for cert in certificates:
        st.subheader(cert["name"])
        st.write(f"Description: {cert['description']}")
        st.write(f"Issue Date: {cert['issue_date']}")
        st.write(f"Issuing Company: {cert['company']}")
        st.image(cert["image"], caption=cert["name"], use_column_width=False, width=800)

def show_accomplishments():
    st.header("Accomplishments")
    accomplishments = [
        "Completed a focused IoT training with a hands-on project, developing a Vehicle Tracking System. Demonstrated expertise in sensor integration, wireless communication, and real-time analytics.",
        "Completed a successful industrial training program on Cybersecurity and Blockchain conducted by AiLABS.",
        "Attended the seminar on 'QUANTUM INTELLIGENCE' and Machine learning at edge.",
        "Solved 180+ coding questions in Leetcode and Coding Ninjas.",
        "Completed an entrepreneurship program conducted by Wadhwani Foundation."
    ]
    
    for accomplishment in accomplishments:
        st.markdown(f"- {accomplishment}")

if __name__ == "__main__":
    main()

