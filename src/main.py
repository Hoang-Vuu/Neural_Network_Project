from dotenv import load_dotenv
import os

from groq import Groq

from db import initialize_db
from agent import run_agent


load_dotenv()

MODEL_ID = "qwen/qwen3-32b"


def main():

    initialize_db()

    client = Groq(
        api_key=os.environ["GROQ_API_KEY"]
    )

    print("\nWeather-Aware Trip Planner")
    print("Type 'exit' to quit\n")

    while True:

        question = input("> ")

        if question.lower() == "exit":
            break

        trace = run_agent(question)

        print(trace["answer"])

        print("\n======= TRACE =======")

        for item in trace["trace"]:
            print(item)

if __name__ == "__main__":
    main()