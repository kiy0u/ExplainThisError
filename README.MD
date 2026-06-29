# ExplainThisError 🔍

An AI-powered web app that takes any error message — from your code or terminal — and explains what it means, why it happened, and how to fix it.

Built with Python, Flask, and the OpenAI API (GPT-4o mini).

---

## Features

- Paste any error message and get a plain-English explanation
- Covers coding errors, terminal errors, stack traces, and more
- Clean web UI — no setup needed beyond running the server
- Graceful error handling for missing input or API issues

---

## Tech Stack

- **Backend:** Python, Flask
- **AI:** OpenAI API (`gpt-4o-mini`)
- **Frontend:** HTML, CSS (served via Flask templates)
- **Config:** `python-dotenv` for environment variables
- **Deployment:** Gunicorn-ready

---

## Getting Started

### Prerequisites

- Python 3.8+
- An [OpenAI API key](https://platform.openai.com/api-keys)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/kiy0u/ExplainThisError.git
   cd ExplainThisError
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment**

   Create a `.env` file in the root directory:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the app**

   ```bash
   python app.py
   ```

   Then open your browser to `http://localhost:5000`.

---

## Usage

1. Copy an error message from your terminal or code editor
2. Paste it into the input field on the web app
3. Click **Analyze** — the AI will explain what went wrong and suggest a fix

---

## Project Structure

```
ExplainThisError/
├── app.py               # Flask app and routes
├── requirements.txt     # Python dependencies
├── prompts/
│   └── debug_prompt.txt # Prompt template sent to the AI
├── services/            # Additional service logic
├── static/              # CSS and static assets
└── templates/
    └── index.html       # Main UI template
```

---

## Deployment

The app is Gunicorn-compatible and ready for platforms like Render, Railway, or Heroku. It reads the `PORT` environment variable automatically, so no extra config is needed.

```bash
gunicorn app:app
```

---

## Contributing

Pull requests are welcome! If you find a bug or have an idea for a new feature, feel free to open an issue.

---

## License

This project does not currently specify a license. Contact the author for usage permissions.