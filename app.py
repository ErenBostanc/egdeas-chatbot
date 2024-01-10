from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = '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'
model_name = "gpt-3.5-turbo"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    
    response = openai.Completion.create(
        model=model_name,
        prompt=user_input,
        max_tokens=150
    )
    
    gpt_response = response['choices'][0]['text']
    return render_template('index.html', user_input=user_input, gpt_response=gpt_response)

if __name__ == '__main__':
    app.run(debug=True, port=2000)
