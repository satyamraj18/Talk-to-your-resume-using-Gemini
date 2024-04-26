# Talk-to-your-resume-using-Gemini

**Project Description:**
As an applicant, I recognize the significance of understanding one's relevance to the job description they're applying for. To address this challenge, I leveraged Google's Gemini API to develop a web application using Streamlit. This platform enables candidates to assess their suitability for the role by providing insights such as their percentage match with the job description, areas where they may need improvement, and actionable suggestions to enhance their fit for the position.

To run it locally, clone the repository and insert your Google Gemini API key in the .env file. Then, execute the following command in your terminal to get started:

**Clone the repo :** 
```
git clone <repository Url>
```

**Run the following the command** 
```
streamlit run app.py
```

**IMPORTANT NOTE**
In this project, I utilized the pdf2image library, which has a dependency known as Poppler. To install Poppler on Windows, you can download it from the following link: https://github.com/oschwartz10612/poppler-windows/releases/. After downloading the latest release, navigate to the Program Files directory in the C drive. Create a folder named 'Poppler' and extract the contents of the downloaded folder into it. Within the 'Poppler' folder, navigate to the 'library' directory, then to 'bin'. Copy the path of the 'bin' directory and add it to the System variable of the environment variables. Once completed, you're all set to proceed with the project.

**Built with :**

Python, Gemini, LLM, Streamlit, PDF2Image

**Some screenshots of the tools :**
