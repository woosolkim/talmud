from dotenv import load_dotenv
from .crew import TextAnalysisCrew
import os
import sys
import argparse


load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
auth_key = os.getenv('DEEPL_API_KEY')

def run():
    parser = argparse.ArgumentParser(description="Talmud: AI-powered text analysis and response system")
    parser.add_argument('mode', choices=['improve', 'rebuttal', 'sustain'], help="Operation mode")
    parser.add_argument('--text', help="Input text for analysis. If not provided, will prompt for input.")
    args = parser.parse_args()

    if not args.text:
        print("Please enter the text for analysis (press Ctrl+D or Ctrl+Z (on Windows) when finished):")
        text = sys.stdin.read().strip()
    else:
        text = args.text

    if not text:
        print("Error: No input text provided.")
        sys.exit(1)
    crew = TextAnalysisCrew()
    result = crew.analyze(text, args.mode)

    print("\nResult:")
    print(result)

if __name__ == "__main__":
    run()
