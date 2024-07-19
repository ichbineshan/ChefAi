import requests
from flask import Flask, request, jsonify, render_template
from togetherai_config import url, headers, model, temperature, max_tokens
from prompt_examples import examples

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_recipe', methods=['POST'])
def generate_recipe():
    user_prompt = request.json.get('prompt')
    
    full_prompt = f"""
    {examples}
    [INST] Generate a concise recipe with minimal text for the following prompt, including ingredients 
    and brief instructions -
    {user_prompt} 
    [/INST]"""
    
    data = {
        "model": model,
        "prompt": full_prompt,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    
    response = requests.post(url, headers=headers, json=data)
    output = response.json().get('output', {}).get('choices', [{}])[0].get('text', '')
    
    return jsonify({"recipe": output})

if __name__ == '__main__':
    app.run(debug=True)
