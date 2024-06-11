from flask import Flask, render_template,jsonify, request
from jinja2 import FileSystemLoader
from latex import build_pdf
from latex.jinja2 import make_env
import json
import json2latex
import os
import os
from flask import send_file

import google.generativeai as genai
app = Flask(__name__)
env = make_env(loader=FileSystemLoader('templates'))
genai.configure(api_key="AIzaSyAshMXJwZLroZQ8avg8JSr3hcrTJCwOQiE")
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)
chat_session = model.start_chat(
  history=[
  ]
)
resume = """RANGEL ANSELM KOLI
Syracuse, NY, 13210 | +1 315 374 9529 | rangelkoli@gmail.com | linkedin.com/in/rangelkoli | github.com/rangelkoli | Portfolio|
CAREER OBJECTIVE
I aspire to secure a versatile role in a reputable organization, utilizing my technical acumen in Artificial Intelligence and Machine
Learning to drive innovation, promote organizational growth, and contribute to the development of cutting-edge technologies in the
field of computer science.
EDUCATION
Syracuse University - College of Engineering & Computer Science, Syracuse, NY August 2023 - Present
Master of Science
• Major in Computer Science
Mumbai University - St. Francis Institute of Technology, Mumbai, Maharashtra August 2019 - May 2023
Bachelors in Information Technology
• Completed 120 credit hours toward a Bachelors’ in Information Technology
• Relevant Coursework: Advanced Data Structure and Algorithms, Database Management System, Operating Systems,
Software Engineering, Artificial Intelligence, and Data Science, Cloud Computing
SKILLS
• Programming Languages: C, C++, Java, Python, Javascript
• Web Technologies: React, HTML, CSS, NodeJS, TypeScript, ReactJS, Machine Learning, Pytorch, Angular, Agile, Laravel,
MVC, PHP, Ruby, Slack, Vue, Web Application
• Database Technologies: SQL, PostgreSQL, GraphQL, Oracle, MySQL
• Soft Skills: Leadership, Communication Skills, Teamwork, Critical Reasoning, Analytical and Problem Solver, Business
Processes
EXPERIENCE
Intern, GRIP(The Sparks Foundation) – Mumbai, Maharashtra March 2022 - May 2023
• Designed and developed a frontend user-friendly charity website with a secure Payment Gateway integration using React,
resulting in a 9% increase in online donations
• Collaborated with the team to enhance website design and functionality, resulting in a 23% increase in user engagement
and clearly communicating the charity's mission online
Technologies Used: React, MongoDB, NodeJS, JavaScript, API
PROJECTS
WalkSafe: Enhancing Safety and Connectivity through Innovative Mobile Solutions Spring 2024
• Implemented real-time tracking feature using React-Native, enhancing user connectivity and peace of mind by enabling
effortless monitoring of friends and family on an interactive map.
• Developed route optimization algorithm utilizing Flask, contributing to user safety by suggesting secure paths through
crime data analysis, ensuring a safer navigation experience.
• Engineered Check-In Service using Supabase, automating notifications upon reaching designated destinations, providing
reassurance to loved ones and promoting a sense of security.
Technologies Used: React-Native, Flask, Supabase, Google Cloud
FindX (Missing Persons Website) Fall 2022- Spring 2023
• Leveraged image processing and software integration skills to bolster law enforcement support, enabling real-time
DeepFace library utilization for instant image uploads
• Optimized the workflow for law enforcement agencies, enabling efficient tracking and verification of the whereabouts of
missing persons, thereby bolstering public safety measures
Technologies Used: Django, Python, PostgreSQL, Machine Learning
Anonimo (Social Network) Spring 2022
• Utilized Machine Learning to create a user-friendly social platform, fostering interaction, and providing support for users in
distress
• Executed the deployment of a robust Machine Learning paradigm, adept at the classification of users into the spheres of
neutrality or desolation
Technologies Used: Django, Python, PostgreSQL, API,
ACHIEVEMENTS, INVOLVEMENTS AND CERTIFICATIONS
• Won 1st Place in the Code Crush 1.0 Hackathon organized by St. Francis Institute of Technology
• Volunteered for the Madh Christian Koli Samaj (NGO) in helping with medical camps for the elderly and organizing
educational seminars for the youth
• Won 1st Place at the CuseHacks Beta 2024 Hackathon organized by Syracuse University
• Created Content on “YouTube” for 15K active subscribers"""

def JSONData():
    return {
        "careerObjective": "I aspire to secure a versatile role in a reputable organization, utilizing my technical acumen in Artificial Intelligence and Machine Learning to drive innovation, promote organizational growth, and contribute to the development of cutting-edge technologies in the field of computer science.",
        "TechSkills": {
            "TechSkillsLanuages": "Python, JavaScript, Java, C++",
            "TechSkillsFrameworks": "React, Django, Flask",
            "TechSkillsDevTools": "VS Code, Jupyter Notebook, Postman",
            "TechSkillsLibraries": "TensorFlow, Keras, OpenCV",
        },
        "projects" : [
            {
                "ProjOneName": "WalkSafe",
                "ProjOneDescOne": "Implemented real-time tracking feature using React-Native, enhancing user connectivity and peace of mind by enabling effortless monitoring of friends and family on an interactive map.",
                "ProjOneDescTwo": "Developed route optimization algorithm utilizing Flask, contributing to user safety by suggesting secure paths through crime data analysis, ensuring a safer navigation experience.",
                "ProjOneDescThree": "Engineered Check-In Service using Supabase, automating notifications upon reaching designated destinations, providing reassurance to loved ones and promoting a sense of security.",
                "ProjOneTech": "React-Native, Flask, Supabase, Google Cloud",
                "ProjOneDuration": "Spring 2024"
            },
            {
                "ProjTwoName": "FindX",
                "ProjTwoDescOne": "Leveraged image processing and software integration skills to bolster law enforcement support, enabling real-time DeepFace library utilization for instant image uploads.",
                "ProjTwoDescTwo": "Optimized the workflow for law enforcement agencies, enabling efficient tracking and verification of the whereabouts of missing persons, thereby bolstering public safety measures.",
                "ProjTwoDescThree": "",
                "ProjTwoTech": "Django, Python, PostgreSQL, Machine Learning",
                "ProjTwoDuration": "Fall 2022 -- Spring 2023"
            },
            {
                "ProjThreeName": "Anonimo",
                "ProjThreeDescOne": "Utilized Machine Learning to create a user-friendly social platform, fostering interaction, and providing support for users in distress.",
                "ProjThreeDescTwo": "Executed the deployment of a robust Machine Learning paradigm, adept at the classification of users into the spheres of neutrality or desolation.",
                "ProjThreeDescThree": "",
                "ProjThreeTech": "Django, Python, PostgreSQL, API",
                "ProjThreeDuration": "Spring 2022"
            }
        ],
        "experience":   [
            {
                "ExpOneCompName": "GRIP (The Sparks Foundation)",
                "ExpOneRole": "Intern",
                "ExpOneDescOne": "Designed and developed a frontend user-friendly charity website with a secure Payment Gateway integration using React, resulting in a 9%\ increase in online donations.",
                "ExpOneDescTwo": "Collaborated with the team to enhance website design and functionality, resulting in a 23\%\ increase in user engagement and clearly communicating the charity's mission online.",
                "ExpOneDescThree": "",
                "ExpOneTechnologies": ["React", "MongoDB", "NodeJS", "JavaScript", "API"],
                "ExpOneDuration": "March 2022 - May 2023"
            }
        ]
        
    }

format = """

   "careerObjective": "I aspire to secure a versatile role in a reputable organization, utilizing my technical acumen in Artificial Intelligence and Machine Learning to drive innovation, promote organizational growth, and contribute to the development of cutting-edge technologies in the field of computer science.",
        "TechSkills": {
            "TechSkillsLanuages": "Python, JavaScript, Java, C++",
            "TechSkillsFrameworks": "React, Django, Flask",
            "TechSkillsDevTools": "VS Code, Jupyter Notebook, Postman",
            "TechSkillsLibraries": "TensorFlow, Keras, OpenCV",
        },
        "projects" : [
            {
                "ProjOneName": "WalkSafe",
                "ProjOneDescOne": "Implemented real-time tracking feature using React-Native, enhancing user connectivity and peace of mind by enabling effortless monitoring of friends and family on an interactive map.",
                "ProjOneDescTwo": "Developed route optimization algorithm utilizing Flask, contributing to user safety by suggesting secure paths through crime data analysis, ensuring a safer navigation experience.",
                "ProjOneDescThree": "Engineered Check-In Service using Supabase, automating notifications upon reaching designated destinations, providing reassurance to loved ones and promoting a sense of security.",
                "ProjOneTech": "React-Native, Flask, Supabase, Google Cloud",
                "ProjOneDuration": "Spring 2024"
            },
            {
                "ProjTwoName": "FindX",
                "ProjTwoDescOne": "Leveraged image processing and software integration skills to bolster law enforcement support, enabling real-time DeepFace library utilization for instant image uploads.",
                "ProjTwoDescTwo": "Optimized the workflow for law enforcement agencies, enabling efficient tracking and verification of the whereabouts of missing persons, thereby bolstering public safety measures.",
                "ProjTwoDescThree": "",
                "ProjTwoTech": "Django, Python, PostgreSQL, Machine Learning",
                "ProjTwoDuration": "Fall 2022 -- Spring 2023"
            },
            {
                "ProjThreeName": "Anonimo",
                "ProjThreeDescOne": "Utilized Machine Learning to create a user-friendly social platform, fostering interaction, and providing support for users in distress.",
                "ProjThreeDescTwo": "Executed the deployment of a robust Machine Learning paradigm, adept at the classification of users into the spheres of neutrality or desolation.",
                "ProjThreeDescThree": "",
                "ProjThreeTech": "Django, Python, PostgreSQL, API",
                "ProjThreeDuration": "Spring 2022"
            }
        ],
        "experience":   [
            {
                "ExpOneCompName": "GRIP (The Sparks Foundation)",
                "ExpOneRole": "Intern",
                "ExpOneDescOne": "Designed and developed a frontend user-friendly charity website with a secure Payment Gateway integration using React, resulting in a 9\%\ increase in online donations.",
                "ExpOneDescTwo": "Collaborated with the team to enhance website design and functionality, resulting in a 23\%\ increase in user engagement and clearly communicating the charity's mission online.",
                "ExpOneDescThree": "",
                "ExpOneTechnologies": ["React", "MongoDB", "NodeJS", "JavaScript", "API"],
                "ExpOneDuration": "March 2022 - May 2023"
            }
        ]
        
        """


def geminiAPIGen():
    JobDescription = """UNPAID INTERNSHIP

🌳 About the Role

Paprika is an innovative food discovery app designed for personalized dining experiences. With Paprika, you can browse a diverse range of restaurants, cafes, and eateries that cater to your unique dietary needs by menu item. Our mission is to revolutionize the way people explore and enjoy food.

Our founding team has worked at elite startups like those under Y-Combinator and at top-tier financial firms such as Jefferies, bringing together a diverse wealth of experience spanning across Finance, Early-Stage Startups and Engineering.

🏆 What You’ll Achieve

Responsibilities

As a Software Engineering Intern at Paprika, you will have the opportunity to contribute to the development of our mobile and web app. You will work closely with our CTO. Your responsibilities will include:

Assisting in mobile app and web app development, including coding, testing, and debugging for iOS and web
Collaborating with the development team to enhance and optimize app features and functionality
Assisting in API integrations and working with external services to enhance app capabilities
Participating in code reviews and providing constructive feedback for improvements
Our Tech Stack: Javascript / Typescript, Node.js, Express, React Native, Supabase, AWS

📈 Requirements

Proficient understanding of Javascript
Familiarity with using Open AI API is a plus
Familiarity with mobile app development frameworks and tools a plus
Familiarity with responsive development and Figma a plus
Ability to work independently and collaborate effectively in a remote team environment

Internship Duration And Schedule

This is a remote, unpaid internship opportunity. We are open to accommodating different schedules and availability."""
    response = chat_session.send_message("You are a resume reviewer with 20 years of experience in the tech industry. Your job is to tailor the resume to the given Job Description. And Make sure to provide it in JSON format.DO NOT give me any prefix or suffix text and make sure each point in the JSON data is filled" + JobDescription + "This is the resume" + resume + "You have to provide the output in the following format: " + format)
    return response.text

@app.route('/generate')
def generate():
    response = geminiAPIGen()
    print(response)
    variables = eval(response)
    latex_template = env.get_template('resume.tex')
    pdf = build_pdf(latex_template.render(
        careerObjective=variables['careerObjective'],

    ))  # Fixed: Added 'latex_template.'

    return bytes(pdf), 200, {
        'Content-Type': 'application/pdf',
        'Content-Disposition': 'inline; filename="example.pdf"'}

data = {
      "careerObjective": "I aspire to secure a versatile role in a reputable organization, utilizing my technical acumen in Artificial Intelligence and Machine Learning to drive innovation, promote organizational growth, and contribute to the development of cutting-edge technologies in the field of computer science.",
        "TechSkills": {
            "TechSkillsLanuages": "Python, JavaScript, Java, C++",
            "TechSkillsFrameworks": "React, Django, Flask",
            "TechSkillsDevTools": "VS Code, Jupyter Notebook, Postman",
            "TechSkillsLibraries": "TensorFlow, Keras, OpenCV",
        },
        "projects" : [
            {
                "ProjOneName": "WalkSafe",
                "ProjOneDescOne": "Implemented real-time tracking feature using React-Native, enhancing user connectivity and peace of mind by enabling effortless monitoring of friends and family on an interactive map.",
                "ProjOneDescTwo": "Developed route optimization algorithm utilizing Flask, contributing to user safety by suggesting secure paths through crime data analysis, ensuring a safer navigation experience.",
                "ProjOneDescThree": "Engineered Check-In Service using Supabase, automating notifications upon reaching designated destinations, providing reassurance to loved ones and promoting a sense of security.",
                "ProjOneTech": "React-Native, Flask, Supabase, Google Cloud",
                "ProjOneDuration": "Spring 2024"
            },
            {
                "ProjTwoName": "FindX",
                "ProjTwoDescOne": "Leveraged image processing and software integration skills to bolster law enforcement support, enabling real-time DeepFace library utilization for instant image uploads.",
                "ProjTwoDescTwo": "Optimized the workflow for law enforcement agencies, enabling efficient tracking and verification of the whereabouts of missing persons, thereby bolstering public safety measures.",
                "ProjTwoDescThree": "",
                "ProjTwoTech": "Django, Python, PostgreSQL, Machine Learning",
                "ProjTwoDuration": "Fall 2022 -- Spring 2023"
            },
            {
                "ProjThreeName": "Anonimo",
                "ProjThreeDescOne": "Utilized Machine Learning to create a user-friendly social platform, fostering interaction, and providing support for users in distress.",
                "ProjThreeDescTwo": "Executed the deployment of a robust Machine Learning paradigm, adept at the classification of users into the spheres of neutrality or desolation.",
                "ProjThreeDescThree": "",
                "ProjThreeTech": "Django, Python, PostgreSQL, API",
                "ProjThreeDuration": "Spring 2022"
            }
        ],
        "experience":   [
            {
                "ExpOneCompName": "GRIP (The Sparks Foundation)",
                "ExpOneRole": "Intern",
                "ExpOneDescOne": "Designed and developed a frontend user-friendly charity website with a secure Payment Gateway integration using React, resulting in a 9% increase in online donations.",
                "ExpOneDescTwo": "Collaborated with the team to enhance website design and functionality, resulting in a 23% increase in user engagement and clearly communicating the charity's mission online.",
                "ExpOneDescThree": "",
                "ExpOneTechnologies": ["React", "MongoDB", "NodeJS", "JavaScript", "API"],
                "ExpOneDuration": "March 2022 - May 2023"
            }
        ]
        
}

def gemAPI(resume, jobDesc):
    response = chat_session.send_message("""You are a resume reviewer with 20 years of experience in the tech industry. 
                                         Your job is to tailor the resume to the given Job Description. 
                                         And Make sure to provide it in JSON format.
                                         DO NOT give me any prefix or suffix text and make sure each point in the JSON data is filled.
                                         For each of the project Description, make sure to write it in a better way and make sure to include the technologies used in the project. 
                                         And also make sure my resume is tailored to the job descriptionso that I can secure the interview.
                                         """ + jobDesc + "This is the resume" + resume + "You have to provide the output in the following format: " + format)
    return response.text

@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        jobDesc = request.form['jobDesc']
        res = gemAPI(resume, jobDesc)
        print(res)
        resJ = json.loads(res)
        with open('ex3.sty', 'w') as f:
            json2latex.dump('data', resJ, f)

        current_dir = os.path.abspath(os.path.dirname(__file__))
        pdf = build_pdf(open('templates/resume.tex'), texinputs=[current_dir, ''])
        pdf.save_to('ex3.pdf')

        return bytes(pdf), 200, {
            'Content-Type': 'application/pdf',
            'Content-Disposition': 'inline; filename="RangelResume.pdf"'}

    return render_template('form.html')

@app.route('/')
def home():

    res = geminiAPIGen()
    print(res)
    resJ = json.loads(res)
    with open('ex3.sty', 'w') as f:
        json2latex.dump('data', resJ, f)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    pdf = build_pdf(open('templates/resume.tex'), texinputs=[current_dir, ''])
    pdf.save_to('ex3.pdf')

    return bytes(pdf), 200, {
        'Content-Type': 'application/pdf',
        'Content-Disposition': 'inline; filename="RangelResume.pdf"'}


if __name__ == '__main__':
    app.run(debug=True)


asd = "I am particularly drawn to Paprika’s mission to personalize dining experiences, as it aligns with my passion for creating innovative solutions that improve everyday life. My experience with diverse technologies, including React Native, Supabase, and various web technologies, positions me well to contribute to your team. Additionally, my leadership, communication, and problem-solving skills have been honed through successful hackathons and volunteer work, further preparing me to excel in a fast-paced startup environment. I am excited about the opportunity to contribute to Paprika’s mission and look forward to discussing how my skills and experiences align with your team’s needs."