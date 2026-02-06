# JournalMe

## Overview

The JournalMe project is designed to provide users with an intuitive interface for journaling. The application allows users to create, read, update, and delete journal entries efficiently. 

## Architecture

The project is structured with a focus on modular design, enabling easy maintenance and scalability. Key components include:

- **Frontend:** Built with React, the frontend offers a user-friendly interface that interacts with the backend.
- **Backend:** The server is developed using Node.js and Express, providing RESTful APIs for data manipulation.
- **Database:** MongoDB is used for persistent storage of journal entries, allowing for efficient querying and retrieval.

## Setup Instructions

### Prerequisites
- Node.js (v14 or higher)
- MongoDB (local installation or cloud service)

### Installation Steps
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/McCluskism/JournalMe.git
   cd JournalMe
   ```

2. **Install Dependencies**  
   For the frontend:
   ```bash
   cd frontend
   npm install
   ```
   For the backend:
   ```bash
   cd backend
   npm install
   ```

3. **Configure Environment Variables**  
   Create a `.env` file in the backend directory with the following variables:
   ```
   MONGODB_URI=your_mongodb_connection_string
   PORT=5000
   ```

4. **Run the Application**  
   Start the backend server:
   ```bash
   cd backend
   npm start
   ```
   And the frontend:
   ```bash
   cd frontend
   npm start
   ```

5. **Access the Application**  
   Open your browser and go to `http://localhost:3000` to start journaling!

## Usage Guide

- **Create an Entry:** Click on the 'New Entry' button, fill out the form, and save.
- **View Entries:** Navigate through the list of journal entries on the main page.
- **Edit an Entry:** Click on an existing entry and choose the edit option.
- **Delete an Entry:** Select an entry and confirm deletion.

### Additional Features
- **Search Functionality:** Quickly find entries using the search bar.
- **Responsive Design:** The application is optimized for both desktop and mobile views.

## Contributing

Contributions are welcome! Please submit a pull request or report issues through the GitHub repository. 

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---  
For more information and updates, follow the project repository on GitHub.