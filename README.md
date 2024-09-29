# Cover Letter Generator
This project is a cover letter generator app that allows you to generate personalized cover letters for any job. The app utilizes the OpenAI GPT-3 model to generate the cover letter based on the provided inputs. Here's how the app works:


## Installation
To run this project, you need to have the following dependencies installed:

- openai
- gradio
- nltk
- dotenv

You can install the dependencies by running the following command:

```sh
pip install -r requirements.txt
```

## Setup
Before running the app, you need to set up your OpenAI API key. Follow these steps:

- 1. Create an account on the OpenAI website.
- 2. Generate an API key from the OpenAI dashboard.
- 3. Create a .env file in the project directory.
- 4. Add the following line to the .env file, replacing YOUR_API_KEY with your actual API key:

```sh
OPENAI_API_KEY=YOUR_API_KEY
```

## Usage
To use the cover letter generator, follow these steps:

- 1. Run the Python script or execute the code in a Python environment.
- 2. The app will launch, displaying a user interface.
- 3. Fill in your name, select the cover letter size (small, medium, or big), and enter any important notions you want to include in your cover letter.
- 4. Copy and paste the job posting into the provided text box.
- 5. Click the "Submit" button.
- 6. The generated cover letter will be displayed in the app, along with the number of words and characters in the generated text.

## Additional Information
The app uses the rephraseText function to generate the cover letter. It utilizes the OpenAI GPT-3 model (text-davinci-003) and sets various parameters such as temperature, max tokens, frequency penalty, and presence penalty to guide the text generation process.

The cover letter text is saved in a file named "cover letter.txt" in the project directory.

Please note that this app is a demonstration and the generated cover letters may require further refinement to match specific requirements and preferences.

Enjoy using the Cover Letter Generator app!