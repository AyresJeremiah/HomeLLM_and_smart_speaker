from flask import Flask, request, jsonify
from transformers import GPTJForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

# Load model and tokenizer
model_name = "EleutherAI/gpt-j-6B"  # Change this if using a different model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = GPTJForCausalLM.from_pretrained(model_name)

@app.route('/api/inference', methods=['POST'])
def infer():
    data = request.json
    query = data.get('query')
    
    # Generate response
    inputs = tokenizer(query, return_tensors='pt')
    with torch.no_grad():
        outputs = model.generate(inputs['input_ids'], max_length=100)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
