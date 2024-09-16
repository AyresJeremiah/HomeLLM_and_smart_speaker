from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

# Load model and tokenizer
model_name = "gpt2"  # Replace with your model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

@app.route('/api/inference', methods=['POST'])
def infer():
    data = request.json
    query = data.get('query')
    
    # Generate response
    inputs = tokenizer.encode(query, return_tensors='pt')
    
    # Adjust generation parameters here
    with torch.no_grad():
        outputs = model.generate(inputs, max_length=50, num_return_sequences=1, 
                                 temperature=0.7, top_k=50, top_p=0.95, 
                                 no_repeat_ngram_size=2)
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
