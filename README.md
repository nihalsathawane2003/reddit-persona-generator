# Reddit User Persona Generator

This project generates a user persona from a Reddit user's public comments and posts using Google Gemini API.

## Requirements

- Python 3.7 or above
- Reddit API credentials (client ID, client secret, user agent)
- Google Gemini API key

## Setup Instructions

1. Clone the repository:

   git clone https://github.com/nihalsathawane2003/reddit-persona-generator.git
   cd reddit-persona-generator
2. Install the required libraries:

   pip install -r requirements.txt
3. Create a .env file in the root directory and add your credentials:

   REDDIT_CLIENT_ID=your_client_id
   REDDIT_CLIENT_SECRET=your_client_secret
   REDDIT_USER_AGENT=your_user_agent
   GOOGLE_API_KEY=your_gemini_api_key

## How to Run

Use the following command to run the script:

   python reddit_persona.py --url https://www.reddit.com/user/kojied/

The output will be saved in a file named `kojied_persona.txt`.

## Output Format

The output includes the following details about the Reddit user:

- Interests
- Personality traits
- Writing style
- Likely occupation or demographics
- Political or worldview insights
- Citations for each trait

## Libraries Used

- praw
- python-dotenv
- google-generativeai
