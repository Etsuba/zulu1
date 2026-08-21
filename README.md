# 🚀 Task Management System API

A lightweight, high-performance RESTful API for task management and user authentication, built with **FastAPI**, **Pydantic**, and Python's `asyncio` ecosystem.

---

## 📌 Project Overview

This project provides a robust backend system for organizing workflows, user roles, and tasks. It handles client requests with fast validation pipelines, structured data modeling, and clean architecture separating data persistence from route handlers.

### Key Features

* **User Authentication & Authorization:** Secure user registration, authentication, and role-based access control (`user`, `admin`).
* **Task Management (CRUD):** Full lifecycle tracking for task creation, retrieval, updates, and deletion.
* **Schema Validation:** Strict runtime data typing and validation powered by Pydantic v2.
* **Modular Architecture:** Layered design separating routes, schemas, services, and repositories for clean maintainability.

---

## 🛠️ Tech Stack

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Runtime/Server:** [Uvicorn](https://www.uvicorn.org/)
* **Package Manager:** [uv](https://github.com/astral-sh/uv)
* **Data Validation:** [Pydantic](https://docs.pydantic.dev/)
* **Language:** Python 3.13+

---

## 📂 Project Structure

```text
zulu-project/
├── app/
│   ├── main.py              
│   ├── repositories/        
│   │   ├── __init__.py
│   │   └── task_repository.py
│   ├── routes/              
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── tasks.py
│   │   └── workspace.py
│   ├── schemas/             
│   │   ├── auth.py
│   │   ├── tasks.py
│   │   └── workspace.py
│   └── services/           
│       ├── auth.py
│       └── task.py
├── pyproject.toml          
└── README.md
```
