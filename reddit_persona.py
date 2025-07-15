import os
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GRPC_LOG_SEVERITY_LEVEL"] = "ERROR"

import argparse
from utils import extract_username, fetch_user_data, generate_persona

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, help="Reddit profile URL")
    args = parser.parse_args()

    if not args.url:
        print("Please provide a Reddit profile URL using --url")
        exit()

    username = extract_username(args.url)
    user_data = fetch_user_data(username)
    print(f"✅ Fetched {len(user_data)} entries for u/{username}...")

    persona = generate_persona(username, user_data)

    output_file = f"{username}_persona.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(persona)

    print(f"✅ Persona for {username} saved to {output_file}")

