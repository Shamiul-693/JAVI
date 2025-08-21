# Financial Policy Chatbot

This project is a simple **AI-powered chatbot** that can answer questions about a financial policy document using semantic search.

## 🚀 Features
- Parses and extracts text from a financial policy PDF.
- Splits the document into smaller chunks for better retrieval.
- Uses **SentenceTransformers** to generate embeddings.
- Stores embeddings in **FAISS** for fast similarity search.
- Answers user questions based on the most relevant PDF section.
- Provides **page references** with answers.
- Runs as a simple **terminal chatbot**.

## 📂 Project Structure
```
financial_policy_chatbot/
│── chatbot.py              # Main chatbot script (terminal)
│── requirements.txt        # Dependencies
│── financial_policy.pdf    # Your financial policy document
│
├── data/                   # (optional) store processed chunks
│   └── chunks.json         
│
└── README.md               # Instructions
```

## 🔧 Installation & Setup

1. Clone or download this repository.
2. Place your `financial_policy.pdf` in the project root folder.
3. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```
   Activate it:
   - Windows:
     ```bash
     venv\Scripts\activate.bat
     ```
   - Mac/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Run the Chatbot

```bash
python chatbot.py
```

Expected output:
```
💬 Financial Policy Chatbot (type 'exit' to quit)
You: Which sections of the Financial Management Act 1996 provide for the presentation and preparation of the Territory’s Budget??
Bot: - 1.2 FINANCIAL  POLICY  OBJECTIVES AND STRA TEGIES
 ST ATEMENT
The presentation and preparation of the Territory’s Budget is provided for in sections 11 and
11A of the Financial Management Act 1996  (the Act) (Page 1)
```
<img width="938" height="144" alt="1" src="https://github.com/user-attachments/assets/6b02e359-96de-405d-8718-872d419d2d8b" />

Expected output:
```
💬 Financial Policy Chatbot (type 'exit' to quit)
You:  What is the Government’s target for the coverage of accrued superannuation liabilities by 2039-40?
Bot: - - The Governm ent ha s a com mitment to fund 90% of accrued 
superannuation liabilities by 30 June 2040 (Page 5)
```
<img width="747" height="104" alt="2" src="https://github.com/user-attachments/assets/d0e4b0e7-c3ff-4a3b-8963-1a15e619534b" />

Expected output:
```
💬 Financial Policy Chatbot (type 'exit' to quit)
You:   What is the Government’s target for the measure relating to the maintenance of physical assets?
Bot: - The Government’s target for this measure is to demonstrate and provide for the maintenance
of the existing level of physical assets (as at 30 June 2005) (Page 3)
```
<img width="723" height="104" alt="3" src="https://github.com/user-attachments/assets/5cf5306c-eec7-41d1-bced-f598bf92b6f2" />

<img width="747" height="106" alt="4" src="https://github.com/user-attachments/assets/b72323e1-d200-4ae4-864a-4d3d5c9505b6" />





## 🛠 Dependencies
- `pypdf2`
- `sentence-transformers`
- `faiss-cpu`
- `fastapi` (optional for API version)
- `uvicorn` (optional for API version)

## 📌 Notes
- Ensure `financial_policy.pdf` is in the same directory as `chatbot.py`.


---
Made with ❤️ for the AI Developer Assessment.
