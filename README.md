# Reddit User Persona Generator

This project scrapes Reddit user data (comments and posts) from a given user profile URL and generates a detailed **user persona** using an LLM (GPT-3.5 or GPT-4 via OpenAI API).

It was created as part of an assignment for a Generative AI Internship.

---

##  Features

- Takes a Reddit user profile URL as input
- Uses Reddit API (`praw`) to scrape latest posts and comments
- Combines the data into a raw `.txt` file
- Sends data to OpenAI GPT to build a psychological/personality-based persona
- Cites specific posts/comments that support each trait
- Outputs a clean `.txt` persona file

---

## Technologies Used

- Python 3
- Reddit API via [PRAW](https://praw.readthedocs.io/)
- OpenAI API (ChatGPT)
- Text output (no frontend/UI required)

---



