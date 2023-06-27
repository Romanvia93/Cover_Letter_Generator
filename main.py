import os
import openai
import gradio as gr
import nltk
from dotenv import load_dotenv

# 1. Env
load_dotenv()

# 2. Save keys
openai.api_key = os.getenv("OPENAI_API_KEY")

def rephraseText(name, size, mention, concept_file):

    # 1. Param
    size_dict = {
        "small": 100, 
        "medium": 200,
        "big": 450
    }

    # 2. Generate queries
    if mention is None:
        prompt = f"""Write a cover letter for {name} with 
                    less than {size_dict[size]} words for the job description below. 
                    Start with Dear Hiring Manager, mention the company name.
                    Job description: {concept_file}
                    """
    else:
        prompt = f"""Write a cover letter for {name} with 
                    less than {size_dict[size]} words for the job description below. 
                    Start with Dear Hiring Manager, mention the company name
                    in the first paragraph, and mention {mention} in any part. 
                    Job description: {concept_file}
                    """
    # 3. Request 
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    # 4. Save result
    with open("cover letter.txt", "w") as f:
        f.write(response.choices[0].text)

    # 5. Calculate numer of words and characters
    sentences = nltk.sent_tokenize(response.choices[0].text)
    words = []
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence):
            words.append(word)
    print(f"Sentences : {len(sentences)} | Words: {len(words)} | Characters: {len(response.choices[0].text)}")

    return response.choices[0].text, len(words), len(response.choices[0].text)


with gr.Blocks() as demo:
    gr.Markdown(
        """<h1>Cover Letter generator</h1> 
            <h3>This app generates personolised cover letter for any job.</h3>
            <h6>1. Fill in your name, cover letter size, and important notions which should be in your Cover Letter.txt</h6> 
            <h6>2. Copy and paste job posting</h6>
            <h6>3. Click Submit </h6>""")
    with gr.Tab("Make a cover letter"):
        with gr.Row() as row:
            with gr.Column() as test:
                name = gr.Textbox(label="Your name")
                size = gr.Radio(["small", "medium", "big"], 
                                   label="Cover letter size",
                                   )
                mention = gr.Textbox(label="What to mention in cover letter, e.g. Tableau knowmledge")
            concept_file = gr.Textbox(label="Job posting")
        with gr.Row():
            rephrase_text = gr.TextArea(label="Generated cover letter")
        with gr.Row():
            number_of_rephrased_words = gr.Text(label="Number of words")
            number_of_rephrased_chars = gr.Text(label="Number of characters")
        rephrase_button = gr.Button("Submit")
    rephrase_button.click(rephraseText, 
                          inputs=[name, size, mention, concept_file], 
                          outputs=[rephrase_text, 
                                   number_of_rephrased_words,
                                     number_of_rephrased_chars])
demo.launch()
