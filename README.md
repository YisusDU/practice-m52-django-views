# 🛒 EBAC Practice M52: "Hellodjango" E-commerce
## 🧪 Tech Stack

![Django](https://img.shields.io/badge/Django-5.0-092E20?style=flat&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-06B6D4?style=flat&logo=tailwindcss&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=flat&logo=celery&logoColor=white)

## 📁 Overview

This document provides a **comprehensive technical overview** of the **Hellodjango Application**, a robust e-commerce boilerplate designed to demonstrate the full **CRUD (Create, Read, Update, Delete)** lifecycle within a containerized environment.

The system enables:

- **Full Product Management:** Create, edit, and delete products via standard Django Forms.
- **Modern Asset Pipeline:** Utilization of `esbuild` and `TailwindCSS` for high-performance frontend delivery.
- **Async Task Processing:** Integration of **Celery** and **Redis** for background operations.
- **Production-Ready Infrastructure:** Fully Dockerized setup with separated services (Web, Worker, DB).

This overview includes:

- **MTV Architecture:** The classic Model-Template-View pattern implementation.
- **URL Routing:** RESTful-style paths for resource management.
- **Database Migrations:** Schema evolution for the `ProductModel`.

> For more detailed subsystem documentation, see:
- `Docker Infrastructure` – Compose profiles & Services
- `Asset Management` – esbuild & WhiteNoise
- `Security` – CSRF & Environment Variables

---

## 🧭 System Overview

**Hellodjango** acts as a bridge between basic Django concepts and professional deployment standards.

### 🏭 The "Factory" Pattern (MTV)
The application logic is centralized in the `ecommerce` app.
* **Model:** `ProductModel` defines the data (Price, Seller, Availability).
* **Template:** Uses Django Template Language (DTL) combined with Tailwind classes for rendering.
* **View:** Orchestrates the data flow, handling Form validation and database queries.

### 🐳 Containerized Ecosystem
Unlike simple script execution, this project runs inside an orchestrated cluster defined in `compose.yaml`. The Django app (`web`) talks to `postgres` for data and `redis` for caching, mimicking a real-world microservices topology.

### ⚡ Next-Gen Tooling
It replaces legacy tools with modern equivalents: `pip` is replaced by **uv** (10x faster), and Webpack is replaced by **esbuild**.

> **Sources:**
- `hellodjango/README.md` (Architecture section)
- `src/ecommerce/models.py` (Data definition)

---

## 🏗️ Architecture & Data Flow

The user interaction follows a strict **Request-Response Cycle**:

1.  **Route:** User accesses `/ecommerce/create`.
2.  **View:** The view instantiates an empty `ProductForm`.
3.  **Template:** Renders the HTML form with CSRF tokens.
4.  **Submission:** User POSTs data; the View validates and saves to PostgreSQL.
5.  **Redirect:** User is sent to the Detail View of the new product.


> **Sources:**
- `hellodjango/src/ecommerce/views.py` (Implied Logic)
- `hellodjango/src/ecommerce/models.py` (Lines 4-9)

---

## 🧰 Technology Stack and Project Structure

The project leverages a high-performance stack:

| Technology | Version | Purpose |
|------------|---------|---------|
| **Django** | v5.x | Core Web Framework |
| **PostgreSQL**| v17.x | Relational Database |
| **TailwindCSS**| v4.x | Utility-First Styling |
| **uv** | Latest | Python Package Manager |

### 🗂️ Project Structure
```text
practice-m52-django-views/
├── hellodjango/
│   ├── src/
│   │   ├── ecommerce/
│   │   │   ├── models.py      # ProductModel Definition
│   │   │   ├── forms.py       # Input Validation
│   │   │   ├── views.py       # CRUD Logic
│   │   │   └── templates/     # HTML Files (list-view.html)
│   ├── compose.yaml           # Docker Services
│   ├── Dockerfile             # Image Build Instructions
│   └── pyproject.toml         # Dependencies (uv)
└── .env.example               # Config Template
```
> **Sources:**
- `hellodjango/CHANGELOG.md` (Stack updates)

---

## 🪟 Feature Spotlight: Full CRUD Implementation

This project is a textbook example of implementing the four fundamental operations of persistent storage applications.

### 1. Unified Form Handling
Instead of manually processing `request.POST`, the project uses **Django Forms**.
* **Benefit:** Automatic validation (e.g., ensuring "Price" is a number) and security sanitization.

### 2. Context-Aware Templates
The templates are not just static HTML; they adapt based on context.
* **Example:** The `list-view.html` iterates over `{% for product in object_list %}`, dynamically generating a card for every item in the database, whether there are 10 or 10,000.



> **Sources:**
- `src/ecommerce/templates/ecommerce/` (Template files)
- `src/ecommerce/models.py` (Product fields)

---

## 📚 Relevant Source Files & Logic Map

To understand how the e-commerce engine works, follow this logic path:

| File Path | Role | Description |
|-----------|------|-------------|
| **`src/ecommerce/models.py`** | 💾 **Schema** | Defines the `ProductModel` table with fields like `price` (Float) and `seller` (Text). |
| **`src/ecommerce/views.py`** | 🧠 **Logic** | Connects the URL to the Template. Handles the `POST` requests to save data. |
| **`src/ecommerce/urls.py`** | 🚦 **Routing** | Maps paths like `/ecommerce/<id>/edit` to the specific update view. |
| **`compose.yaml`** | ⚙️ **Infra** | Orchestrates the database and web server startup sequence. |

---

>[!Note]
>You can check the full documentation <a href="https://deepwiki.com/YisusDU/practice-m52-django-views">-here-</a>
