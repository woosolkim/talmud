from dotenv import load_dotenv
from .crew import TextAnalysisCrew
import os
import sys

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
auth_key = os.getenv('DEEPL_API_KEY')

def run():
    if len(sys.argv) < 2:
        print("Usage: python -m src.my_agent.main [analysis|improve|rebuttal|sustain]")
        sys.exit(1)

    mode = sys.argv[1]
    if mode not in ['analysis','improve', 'rebuttal', 'sustain']:
        print("Invalid mode. Use 'analysis', 'improve', 'rebuttal', or 'sustain'.")
        sys.exit(1)


    text = """
            오징어다리는 2개의 촉완과 8개의 다리가 있고 끝이 가늘어져 안쪽에 짧은 자루가 있는 흡반이 있습니다
            제3, 제4다리 사이에 촉완이 있는데 다른 다리보다 길며 끝쪽이 약간 넓어져 있고 거기에 흡반이 있습니다보통 때는 주머니 속에 들어 있다가 먹이를 잡을 때에 뻗칩니다

오징어 다리는 길고  흡반에 톱니가 있답니다 
            """
    crew = TextAnalysisCrew()
    result = crew.analyze(text, mode)
    print(result)

if __name__ == "__main__":
    run()
