# HACKOWEEK WEEK 1 TASK: Library Management REST API

### 👤 Student Information
* **Developer Name:** Rohan Laharwani
* **Roll Number / PRN:** 24070521055
* **Submission Context:** Hackoweek - Week 1 Assignment

---

## 📖 Project Overview
This project is a fully functional **RESTful Web API** for a **Library Management System** built from scratch using **Python** and **FastAPI**. 

The application serves as a backend communication engine that enables users to manage a digital book inventory seamlessly. It processes data payloads, applies data integrity checks, and executes core management actions using standard HTTP web communication rules.

---

## 🛠️ What We Did (Technical Architecture)

* **Isolated Dependency Management:** Initialized a secure Python **Virtual Environment (`venv`)** in VS Code using PowerShell to isolate the execution environment and prevent framework version conflicts.
* **Strict Schema Validation:** Built a structural **Pydantic Model (`BookInput`)** acting as an automated validation barrier. It enforces data types and ensures required fields (`title` and `author`) are present before system processing.
* **Efficient In-Memory Storage:** Established a fast **in-memory data store list** with pre-seeded mock books (*The Hobbit* and *1984*) to manage records instantaneously without complex external engine configurations.
* **Programmed Core CRUD Endpoints:** Designed and mapped backend code functions to standardized REST endpoints:
  * `GET /api/books` - Reads and returns the complete active book repository.
  * `POST /api/books` - Validates, assigns an auto-incremented unique ID, and appends a new book.
  * `PUT /api/books/{book_id}` - Searches for a record by its path parameters and updates its availability details.
  * `DELETE /api/books/{book_id}` - Locates a book by ID and pops it out of the storage list.
* **Live Server Execution:** Deployed the API utilizing **Uvicorn**, a lightning-fast ASGI web server engine, listening live on `http://127.0.0.1:8000`.
* **Automated Interface Documentation:** Leveraged FastAPI's native **Swagger OpenAPI documentation engine** to test all live route functionality inside the web browser without requiring external software like Postman.

---

## 🚀 How to Run and Test This Project Locally

Follow these sequential terminal steps to turn on and evaluate the application on your computer:

### 1. Environment Activation
Open your terminal inside Visual Studio Code and enter the script activation command:
```powershell
# Unblock Windows execution policies for PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Activate your isolated environment
.\venv\Scripts\Activate.ps1
```

### 2. Boot Up the API Server
Start your local server instance by launching Uvicorn with automated reloading enabled:
```powershell
uvicorn main:app --reload
```
*Look for the message: `INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)`*

### 3. Interactive Testing
1. Open your web browser of choice.
2. Navigate directly to the live auto-generated testing dashboard:
   👉 **[http://localhost:8000/docs](http://localhost:8000/docs)**
3. Expand any route drawer (such as **GET** or **POST**), select **"Try it out"**, adjust the payload fields, and press **"Execute"** to watch live data process.
