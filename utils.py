import os
import google.generativeai as genai
import praw
from dotenv import load_dotenv

# Suppress gRPC logging
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GRPC_LOG_SEVERITY_LEVEL"] = "ERROR"

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Configure Reddit API
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def extract_username(url):
    return url.strip("/").split("/")[-1]

def fetch_user_data(username):
    redditor = reddit.redditor(username)
    data = []

    for comment in redditor.comments.new(limit=50):
        data.append(f"Comment: {comment.body}")

    for post in redditor.submissions.new(limit=50):
        data.append(f"Post: {post.title}\n{post.selftext}")

    return data

def generate_persona(username, texts):
    combined_text = "\n".join(texts)
    limited_text = combined_text[:10000]

    prompt = f"""
You are an AI that builds detailed user personas from Reddit content.

Build a persona for the user `{username}` based on the following content. For each trait, cite 1–2 specific post/comment snippets to justify your observation.

Reddit Content:
{limited_text}

Output format:

Username: {username}

Interests:
- [Trait] (Cited from: "...")

Personality Traits:
- ...

Writing Style:
- ...

Likely Occupation or Demographics:
- ...

Political/Worldview:
- ...
"""

    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Gemini API error: {str(e)}"
