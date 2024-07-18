from flask import Flask, render_template
from flask import Flask, render_template, request
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM
from transformers import pipeline
from transformers import AutoTokenizer
app = Flask(__name__)
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-mr")

# Create the translator pipeline
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-mr", tokenizer=tokenizer)
@app.route('/')
def index():
    return render_template('Home.html', translated_text='')

@app.route('/translate', methods=['POST'])
def translate():
    model_checkpoint = "Helsinki-NLP/opus-mt-en-hi"
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
    model = TFAutoModelForSeq2SeqLM.from_pretrained(r"C:\Users\Dell_Owner\OneDrive\Desktop\SE\BE SME8\major project\MT\dhruv\Dhruv Projecr\tf_model")
  #  model = TFAutoModelForSeq2SeqLM.from_pretrained("C:\\Users\\Dell_Owner\\OneDrive\\Desktop\\SE\\BE SME8\\major project\\MT\\final\\Dhruv Projecr\\tf_model")

    input_text = request.form['input_text']
    language = request.form['language']
    translated_text = ""
    print(language)
    if language == 'hindi':
        tokenized = tokenizer([input_text], return_tensors='np')
        out = model.generate(**tokenized, max_length=128)
        with tokenizer.as_target_tokenizer():
            translated_text = tokenizer.decode(out[0], skip_special_tokens=True)
    if language=='marathi':
        translated_text = translator(input_text)
        translated_text = translated_text[0]['translation_text']
        
    
    return render_template('Home.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)

