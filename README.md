# Hirademy
## Backend Application Development
- **Objective**:

  Develop a backend application with CRUD APIs for managing assistants using PYTHON programming language and MongoDB database. The application includes defining database models, implementing API endpoints, and testing with Postman.
- **Tools And Technology Used**:
  1. Python flask framework
  2. MongoDB database
  3. Postman Collections
- **Application Requirements:**

  Implement CRUD APIs (POST, GET, PUT, DELETE) for managing Assistants.
Define database model(s) for the Assistant, including applicable fields such as ID, name, mobile, email, salary, city, country, department, role, etc.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kaustubhjangjod/Hirademy.git
2. Navigate to the project directory

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
4. Set up environment variables:

   Create a .env file in the root directory and add your environment variables:
   Replace placeholders (your_username, your_password, your_cluster_url, your_database_name) with your MongoDB connection details
   ```bash
   MONGODB_URI=mongodb+srv://your_username:your_password@your_cluster_url/your_database_name
   
5. Run the Application:
      
   ```bash
   python app.py
  The application will start running locally at http://localhost:5000/.

## Usage

1. Create a new assistant:

   Send a POST request to `http://localhost:5000/assistant` with JSON data containing assistant details.

2. Retrieve assistant details:

   Send a GET request to `http://localhost:5000/assistant/<assistant_id>` to retrieve details of a specific assistant.

3. Update assistant details:

   Send a PUT request to `http://localhost:5000/assistant/<assistant_id>` with JSON data to update assistant information.

4. Delete an assistant:

   Send a DELETE request to `http://localhost:5000/assistant/<assistant_id>` to delete a specific assistant.

## API Endpoints

- `POST /assistant`: Create a new assistant.
- `GET /assistant/<assistant_id>`: Retrieve details of a specific assistant.
- `PUT /assistant/<assistant_id>`: Update details of a specific assistant.
- `DELETE /assistant/<assistant_id>`: Delete a specific assistant.

## Configuration

- `MONGODB_URI`: MongoDB connection URI for database access.

