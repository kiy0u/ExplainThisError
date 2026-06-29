from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os


load_dotenv()
app = Flask(__name__)

BASE_DIR = Path(__file__).parent
PROMPT_FILE = BASE_DIR / "prompts" / "debug_prompt.txt"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/analyze", methods=["POST"])
def analyze():
    error_text = request.form["error_text"]

    result = None
    error_message = None

    if not error_text: # validate user input
        error_message = "Please enter an error message before analyzing."
        return render_template(
            "index.html",
            result = None,
            error_message = error_message,
            user_input = error_text 
        )

    try: #load prompt safely
        if not PROMPT_FILE.exists():
            error_message = "Server configuration error: prompt file missing"
            return render_template(
                "index.html",
                result = None,
                error_message = error_message,
                user_input = error_text
            )

        with open(PROMPT_FILE, "r", encoding="utf-8") as file:
            prompt = file.read()

        prompt = prompt.replace("{error_text}", error_text)

    
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful debugging assistant."},
                {"role": "user", "content":prompt}
            ],
            timeout=20
        )
        
        raw = response.choices[0].message.content

        import json
        result = json.loads(raw)

        return render_template(
            "index.html",
            result = result,
            error_message = None,
            user_input = error_text
        )



    except Exception as e:
        print("Error: ", str(e))
        
        error_message = "Unable to analyze error right now. Try again later."

        return render_template(
            "index.html",
            result = None,
            error_message = error_message,
            user_input = error_text
        )



if __name__ == "__main__":
    app.run()
