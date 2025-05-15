# 🧠 Document RAG System

A **Retrieval-Augmented Generation (RAG)** system that allows users to upload documents and ask questions about their contents. It uses:

- 🧠 **Weaviate** for vector storage
- 📚 **Granite-Embedding-107M-Multilingual** for multilingual document embeddings
- 💬 **Granite 3-2B (Watsonx.ai)** for generating context-rich answers

---

## 🚀 Features

- ✅ Upload and process documents (PDF, DOCX, XLSX)
- ✅ Chunking and vectorizing via Granite embedding model
- ✅ Contextual search using Weaviate vector database
- ✅ Ask natural language queries
- ✅ Get formatted AI-generated answers using IBM Watsonx (Granite 3-2B)
- ✅ Built with Flask backend + React frontend

---

## 📁 Project Structure

```
📦 your-project/
├── frontend/
│   ├── components/
│   ├── assets/
│   ├── Home.jsx
│   └── ...
├── backend/
│   ├── app.py
│   ├── utils/
│   │   ├── loader.py        # Loads & chunks documents
│   │   ├── retriever.py     # RAG pipeline logic
│   └── routes/
│       └── upload.py
└── .env
```

---

## 🛠️ Setup Instructions

### 🧩 Backend

1. Clone the repo
2. Install Python requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your `.env`:
   ```
   WEAVIATE_URL=your_weaviate_url
   WATSONX_API_KEY=your_ibm_api_key
   WATSONX_PROJECT_ID=your_project_id
   WATSONX_URL=https://us-south.ml.cloud.ibm.com
   ```
4. Run Flask backend:
   ```bash
   flask run
   ```

### 💻 Frontend

1. Navigate to the `frontend` folder
2. Install dependencies:
   ```bash
   npm install
   ```
3. Add your `VITE_API_URL` to `.env`:
   ```
   VITE_API_URL=http://localhost:5000
   ```
4. Run frontend:
   ```bash
   npm run dev
   ```

---

## 📌 Tech Stack

| Layer        | Technology                       |
|--------------|----------------------------------|
| Frontend     | React, Tailwind CSS              |
| Backend      | Flask                            |
| Vector DB    | Weaviate                         |
| LLM          | Watsonx Granite 3-2B             |
| Embedding    | granite-embedding-107m-multilingual |

---

## ✅ Current Capabilities

- [x] Upload files (PDF, DOCX, XLSX)
- [x] Run queries on uploaded content
- [x] Display streamed, formatted answers
- [x] Auto-delete temp files after processing
- [x] Multilingual support
- [x] Answer formatting with line breaks and bullet points
- [x] Disable form during loading
- [x] Persistent context per file session

---

## 🧩 To Be Added

- [ ] User authentication
- [ ] Query history per user
- [ ] File management dashboard
- [ ] Role-based access control (Admin/User)
- [ ] Support for multiple file uploads
- [ ] Summarization of uploaded documents
- [ ] Audio-based querying (voice-to-text)
- [ ] Continuous learning feedback loop (RAG retraining)
- [ ] Exportable answer reports (PDF/Markdown)
- [ ] UI dark/light toggle

---

## 🤝 Contributing

Open to collaboration! PRs, feedback, or issues welcome.

---

## 📜 License

MIT