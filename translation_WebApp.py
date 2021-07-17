# ------ TRANSLATION WEB APP IN JUPYTER NOTEBOOK ------

# !pip3 install torch torchvision torchaudio -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html
# !pip install transformers ipywidgets gradio --upgrade
import gradio as gr                
#UI library
from transformers import pipeline  
# Transformers pipeline https://huggingface.co/models?search


translation_pipeline = pipeline('translation_en_to_fr')


# translation_pipeline('I love icecream')
# --> returns = [{'translation_text': "J'aime la crème glacée"}] 

results = translation_pipeline('I love icecream')
results[0]['translation_text']
# --> returns = "J'aime la crème glacée"

# ---- CREATE GRADIO FUNCTION AND INTERFACE --------
def translate_transformer(from_text):
    results = translation_pipeline(from_text)
    return results[0]['translation_text']

translate_transformer('My name is Cori')
# --> returns 'Mon nom est Cori'


interface = gr.Interface(fn=translate_transformer,
                       inputs=gr.inputs.Textbox(lines=2,placeholder='Text to translate'),
                       outputs='text')

interface.launch()
"""
 --> returns 
 
 Running locally at: http://127.0.0.1:7860/  -----> OPEN THIS IN A NEW WINDOW
To create a public link, set `share=True` in `launch()`.
Interface loading below...

FROM TEXT ___________________ OUTPUT __________________

Clear               Submit   Screenshot
Flag
"""
