_**Overview of the Agent**_

The AI Social Media Agent is a Streamlit-based application that generates platform-ready social media content using the Google Gemini API. Users provide brand details, audience information, tone, and desired number of posts, and the agent produces structured flashcards containing titles, captions, and image suggestions. All processing—UI, logic, and API interaction—is handled within a single Python application, making the tool simple to run and deploy.


_**Features & Limitations
Features:**_
 Intelligent task handling, 
Multi-step reasoning, 
Integration with APIs

_**Limitations:**_
 Dependent on API rate limits, 
Requires stable environment variables, 
Feature availability may differ by deployment

_**Tech Stack & APIs Used:**_
 Backend: Python (Streamlit-based execution layer), 
Frontend: Streamlit UI,  
External APIs: Google Gemini API (via google-generativeai), 
Utilities: pandas, python-dotenv (environment management)

_**Setup & Run Instructions:**_
 Clone the repository, 
Install dependencies: npm install or pip install -r requirements.txt, 
Add environment variables in .env, 
Run development server: npm start or python app.py, 
Access the agent via localhost URL

_**Potential Improvements:**_
 Add analytics dashboard, 
Improve scheduling accuracy, 
Add more export formats (PDF, XLSX), 
Role-based authentication, 
Offline mode
