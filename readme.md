<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="readmeai/assets/logos/purple.svg" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# QA_SYSTEM_WITH_LOCAL_MODELS

<em>Local AI, Powerful Answers, Instantly.</em>

<!-- BADGES -->

<!-- default option, no dependency badges. -->


<!-- default option, no dependency badges. -->

</div>
<br>

---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
    - [Project Index](#project-index)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - 
- [Roadmap](#roadmap)

---

## Overview

QA_system_with_local_models.git is a Retrieval Augmented Generation (RAG) based question-answering system designed for local deployment, offering speed, efficiency, and control.

**Why QA_system_with_local_models.git?**

This project provides a complete, locally-hosted question-answering solution, eliminating reliance on external APIs and offering enhanced performance and control. The core features include:

- **🟢 Local Models & Pre-downloaded Models:**  Instantly deployable; no API keys or external dependencies needed for immediate use.
- **🟡 RAG Architecture:**  Ensures accurate and context-aware answers by combining local LLMs with a vector database.
- **🔵 Customizable Prompting:**  Fine-tune the system's behavior and mitigate risks of unsafe or biased outputs.
- **🔴 Robust Error Handling & Logging:**  Facilitates easy debugging and maintenance with detailed error reports and logs.
- **🟣 User-Friendly Web Interface:**  Access the powerful question-answering capabilities through a simple and intuitive web application.
- **🟠 Comprehensive Dependency Management:**  `requirements.txt` ensures easy setup and reproducibility across different environments.

---

## Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Flask web framework for the API.</li><li>Sentence Transformers for embedding generation.</li><li>FAISS for efficient similarity search.</li><li>Langchain for LLM interaction and chain building (potentially).</li><li>Local model loading and querying.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Requires further assessment.  No obvious style guide adherence or linting is evident from a cursory review.</li><li>Potential for improvement in code comments and documentation.</li></ul> |
| 📄 | **Documentation** | <ul><li>Minimal documentation.  README provides basic instructions but lacks detailed explanations.</li><li>No API documentation or code comments.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates Sentence Transformers, FAISS, Flask, and Langchain.</li><li>Supports PDF file uploads (using PyPDF2).</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Moderate modularity.  Code appears somewhat compartmentalized but could benefit from further refactoring.</li><li>Potential for improved separation of concerns.</li></ul> |
| 🧪 | **Testing**       | <ul><li>No dedicated tests found.</li><li>Lack of testing is a significant concern.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Performance depends heavily on the size of the local knowledge base and the chosen LLM.</li><li>FAISS usage suggests an attempt at optimization for similarity search.</li><li>Further benchmarking is needed.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Security considerations are minimal or absent.  Input sanitization and validation are likely missing.</li><li>Vulnerable to various attacks without proper security measures.</li></ul> |
| 📦 | **Dependencies**  | <ul><li> `sentence-transformers`</li><li> `faiss-cpu`</li><li> `transformers`</li><li> `flask`</li><li> `PyPDF2`</li><li> `tqdm`</li><li> `langchain`</li><li> `langchain-community`</li><li> `torch`</li><li> `pypdf`</li><li> `python-dotenv`</li></ul> |
| 🚀 | **Scalability**   | <ul><li>Scalability is limited by the local model's capacity and the single-server Flask architecture.</li><li>Requires significant changes for horizontal scaling.</li></ul> |

**Note:** This analysis is based on limited information and a high-level overview of the provided context. A thorough code review is necessary for a more comprehensive assessment.

---

## Project Structure

```sh
└── QA_system_with_local_models.git/
    ├── data
    │   └── RAG_QA.pdf
    ├── download_models.py
    ├── install.bat
    ├── install.sh
    ├── requirements.txt
    ├── run.bat
    ├── run.sh
    ├── src
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── app.py
    │   ├── data_ingestion.py
    │   ├── embedding.py
    │   ├── exception.py
    │   ├── logger.py
    │   ├── model_loader.py
    │   └── qa_chain.py
    ├── static
    │   └── style.css
    └── templates
        └── chat.html
```

### Project Index

<details open>
	<summary><b><code>QA_SYSTEM_WITH_LOCAL_MODELS.GIT/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/shahabas9/QA_system_with_local_models.git/blob/master/requirements.txt'>requirements.txt</a></b></td>
					<td style='padding: 8px;'>- Requirements.txt specifies the projects dependencies<br>- It ensures the applications successful execution by defining necessary libraries, including Langchain for LLM interaction, Flask for web framework, Transformers and Sentence-Transformers for NLP tasks, PyPDF2 for PDF handling, and others for optimization and efficient processing<br>- The listed packages support the core functionality of the application.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/shahabas9/QA_system_with_local_models.git/blob/master/download_models.py'>download_models.py</a></b></td>
					<td style='padding: 8px;'>- The script pre-downloads machine learning models, namely a large language model for question answering and a sentence embedding model<br>- This improves the applications initial performance by eliminating the need for model downloads during first-time execution<br>- The downloaded models are utilized by other parts of the application for tasks such as question answering and semantic similarity calculations.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/shahabas9/QA_system_with_local_models.git/blob/master/install.bat'>install.bat</a></b></td>
					<td style='padding: 8px;'>- The <code>install.bat</code> script sets up the RAG QA systems environment<br>- It verifies Pythons presence, installing version 3.10 if needed<br>- A virtual environment is then created, followed by dependency installation using <code>requirements.txt</code><br>- Successful execution prepares the system for execution via <code>run.bat</code>, indicating a complete setup process.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/shahabas9/QA_system_with_local_models.git/blob/master/run.bat'>run.bat</a></b></td>
					<td style='padding: 8px;'>- The <code>run.bat</code> script initiates the RAG QA system<br>- It activates the projects virtual environment, then launches the main application, accessible via a local server<br>- The script provides user feedback indicating system startup and shutdown instructions, simplifying the execution process for the entire application<br>- The scripts purpose is to streamline the launch of the question-answering system.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/shahabas9/QA_system_with_local_models.git/blob/master/run.sh'>run.sh</a></b></td>
					<td style='padding: 8px;'>- The <code>run.sh</code> script initiates the RAG QA system<br>- It activates a virtual environment, then launches the main application, making the system accessible via a local server<br>- The script provides clear startup messages indicating system status and instructions for termination<br>- Its purpose is to streamline the execution of the Python-based question-answering application.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/shahabas9/QA_system_with_local_models.git/blob/master/install.sh'>install.sh</a></b></td>
					<td style='padding: 8px;'>- The <code>install.sh</code> script sets up the RAG QA system environment<br>- It verifies Python 3.10+ installation, creates a virtual environment named <code>rag_env</code>, upgrades pip, and installs project dependencies listed in <code>requirements.txt</code><br>- Successful execution prepares the system for execution via <code>run.sh</code> or manual activation and execution of <code>src/app.py</code>.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- templates Submodule -->
	<details>
		<summary><b>templates</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ templates</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/shahabas9/QA_system_with_local_models.git/blob/master/templates/chat.html'>chat.html</a></b></td>
					<td style='padding: 8px;'>- The <code>chat.html</code> template renders the user interface for a chatbot application<br>- It provides a visually appealing chat window, incorporating styling from Bootstrap and Font Awesome<br>- The template facilitates user input and displays both user messages and chatbot responses, dynamically updating the conversation flow using AJAX calls to a backend endpoint for processing user queries<br>- The design emphasizes a clean and interactive user experience.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- src Submodule -->
	<details>
		<summary><b>src</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ src</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/shahabas9/QA_system_with_local_models.git/blob/master/src/exception.py'>exception.py</a></b></td>
					<td style='padding: 8px;'>- The <code>src/exception.py</code> file defines a custom exception class<br>- It enhances standard exception handling by providing more context, including the error message, line number, and filename where the exception originated<br>- This improves debugging within the larger application by offering richer error reporting.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/shahabas9/QA_system_with_local_models.git/blob/master/src/data_ingestion.py'>data_ingestion.py</a></b></td>
					<td style='padding: 8px;'>- Data ingestion is handled by <code>src/data_ingestion.py</code><br>- It loads PDF documents from a specified directory, using a directory loader and PDF loader<br>- The function logs progress and handles exceptions, providing a crucial initial step in the projects data pipeline, preparing data for subsequent processing stages within the larger application.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/shahabas9/QA_system_with_local_models.git/blob/master/src/logger.py'>logger.py</a></b></td>
					<td style='padding: 8px;'>- The <code>logger.py</code> module establishes a logging mechanism for the application<br>- It creates a dedicated log directory, generates uniquely timestamped log files, and configures the logging format, ensuring all events are recorded with timestamps, line numbers, and severity levels<br>- This centralized logging facilitates debugging and monitoring across the entire application.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/shahabas9/QA_system_with_local_models.git/blob/master/src/embedding.py'>embedding.py</a></b></td>
					<td style='padding: 8px;'>- Src/embedding.py` generates and stores document embeddings<br>- It loads data, splits it into chunks, creates embeddings using a HuggingFace model, and persists them in a FAISS vector database<br>- This module facilitates efficient semantic search within the larger application by providing a searchable index of the processed documents<br>- Error handling and logging mechanisms ensure robustness.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/shahabas9/QA_system_with_local_models.git/blob/master/src/model_loader.py'>model_loader.py</a></b></td>
					<td style='padding: 8px;'>- Src/model_loader.py<code> provides a function to load a local FLAN-T5 language model<br>- This model, crucial for question-answering within the application, is initialized using the </code>transformers<code> and </code>langchain` libraries<br>- The function returns a HuggingFacePipeline instance, integrating the loaded model into the larger applications architecture for subsequent use in question answering tasks<br>- Error handling ensures robust model loading.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/shahabas9/QA_system_with_local_models.git/blob/master/src/app.py'>app.py</a></b></td>
					<td style='padding: 8px;'>- The <code>src/app.py</code> file implements a Flask web application serving as a user interface for a question-answering system<br>- It initializes a retrieval augmented generation (RAG) chain, handles user queries via a web form, forwards them to the RAG chain for processing, and displays the responses<br>- Error handling and logging mechanisms ensure system robustness and facilitate debugging<br>- The application renders a chat interface using HTML templates.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/shahabas9/QA_system_with_local_models.git/blob/master/src/qa_chain.py'>qa_chain.py</a></b></td>
					<td style='padding: 8px;'>- Src/qa_chain.py` configures a local question-answering chain<br>- It integrates a local large language model with a vector database, enabling question answering based solely on provided context<br>- The chain uses a custom prompt to ensure safe and accurate responses, prioritizing information retrieval from the embedded data and falling back to a default response if the answer is unavailable<br>- Error handling ensures robust operation.</td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip

### Installation

Build QA_system_with_local_models.git from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/shahabas9/QA_system_with_local_models.git
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd QA_system_with_local_models
    ```

3. **Install the dependencies:**

---

  **For Windows Users:** 

	1. Double-click install.bat

 	2. Wait for installation to complete

	3. Double-click run.bat

	4. Open your browser to: http://localhost:5000

Ask questions about the RAG document!

**For Linux/Mac Users:**

	1. Open Terminal in this folder

	2. Run: bash install.sh

	3. Wait for installation to complete

	4. Run: bash run.sh

	5. Open your browser to: http://localhost:5000

Ask questions about the RAG document!

⚙️ System Requirements
Windows 10/11 or Linux or MacOS

Python 3.8 or higher

4GB RAM minimum

2GB disk space for AI models

⏳ First Run Notes
🔽 First time will download AI models (~1.5GB)

⏱️ This may take 10-30 minutes depending on internet speed

✅ Subsequent runs will be fast and work offline


Make sure you have internet connection for the first run



🛑 To Stop the System
Press Ctrl+C in the command window

Close the browser tab

### Usage

Run the project with following url if you want to check immediately and to avoid installation:

****
```sh
https://systemqquesans-shahabas.streamlit.app/
```


---
