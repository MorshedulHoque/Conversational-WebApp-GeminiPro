# Gemini LLM Q&A Application

## Project Overview
This project utilizes the powerful Gemini language model from Google's generative AI suite to create a Q&A application. Integrated with Streamlit, the app offers a user-friendly interface where users can pose questions and receive responses generated by the Gemini model.

## Features

| Feature               | Description                                                         |
|-----------------------|---------------------------------------------------------------------|
| Environment Variables | Securely load necessary credentials using `dotenv`.                 |
| Streamlit Interface   | A sleek, web-based interface for users to interact with the model.  |
| Gemini Pro Model      | Leverage the advanced capabilities of the Gemini Pro model.         |
| Real-time Interaction | Users can input questions and get immediate responses.              |

## How It Works
1. **Setup Environment**: Utilizes Python's `dotenv` package to manage environment variables securely.
2. **Streamlit Application**: The app is built with Streamlit, providing an interactive interface for users.
3. **Gemini Model Integration**: Integrates Google's Gemini Pro model to generate accurate and contextually relevant answers.

## Getting Started
To run this application, you will need to set up your environment with the necessary API keys and install the required packages.

### Prerequisites
- Python 3.8+
- Streamlit
- dotenv Python package

### Installation
1. Clone the repository:
```bash
git clone https://github.com/MorshedulHoque/Conversational-WebApp-GeminiPro.git
```
2. Install dependencies:
```bash
pip install -r requirement.txt
```
3. Obtain a Google API key for the Gemini Pro model and add it to the .env file:
```bash
echo GOOGLE_API_KEY=your_api_key_here > .env
```
4. Run the Streamlit application:
```bash
streamlit run app.py
```

## Usage
- Launch the application.
  ![benchmark](https://github.com/MorshedulHoque/Conversational-WebApp-GeminiPro/blob/main/images/1.png)
- Enter your question in the input field.
  ![benchmark](https://github.com/MorshedulHoque/Conversational-WebApp-GeminiPro/blob/main/images/2.png)
- Press 'Ask the question' to receive a response.
  ![benchmark](https://github.com/MorshedulHoque/Conversational-WebApp-GeminiPro/blob/main/images/3.png)


## Live Demo
You can see the demo of the project in the following link:
[https://conversational-webapp-geminipro-1.onrender.com/](https://conversational-webapp-geminipro-1.onrender.com/)

**Note**: The application might be slow as it is hosted on a very low configured free server.

## Acknowledgments
- Google AI for the Gemini language model.
- Streamlit for the interactive web framework.

## Contributions
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please ensure to update tests as appropriate.

## Contact
For further inquiries, contact asmmorshedulhoque

## Version
This is version 1.0 of the Gemini LLM Q&A Application.
