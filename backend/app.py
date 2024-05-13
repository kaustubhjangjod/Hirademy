from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from database.mongoDB import Assistant  # Import the MongoDB model
import os
import mongoengine
app = Flask(__name__)

load_dotenv()
url=os.getenv('url')
mongoengine.connect(host=url)
#db = client.hirademy
#collection = db.assistant

# Route to create a new assistant
@app.route('/assistant', methods=['POST'])
def create_assistant():
    data = request.json
    assistant = Assistant(**data)  # Create a new instance of Assistant model
    assistant.save()  # Save the assistant document to MongoDB
    return jsonify({'id': str(assistant.id)}), 201

# Route to retrieve details of a specific assistant
@app.route('/assistant/<assistant_id>', methods=['GET'])
def get_assistant(assistant_id):
    assistant = Assistant.objects(id=assistant_id).first()  # Query assistant by ID
    if assistant:
        return jsonify(assistant.to_json()), 200  # Serialize assistant document to JSON
    else:
        return jsonify({'error': 'Assistant not found'}), 404

# Route to update details of a specific assistant
@app.route('/assistant/<assistant_id>', methods=['PUT'])
def update_assistant(assistant_id):
    data = request.json
    assistant = Assistant.objects(id=assistant_id).first()  # Query assistant by ID
    if assistant:
        assistant.modify(**data)  # Update assistant fields
        return jsonify({'message': 'Assistant updated successfully'}), 200
    else:
        return jsonify({'error': 'Assistant not found'}), 404

# Route to delete a specific assistant
@app.route('/assistant/<assistant_id>', methods=['DELETE'])
def delete_assistant(assistant_id):
    assistant = Assistant.objects(id=assistant_id).first()  # Query assistant by ID
    if assistant:
        assistant.delete()  # Delete assistant document from MongoDB
        return jsonify({'message': 'Assistant deleted successfully'}), 200
    else:
        return jsonify({'error': 'Assistant not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
