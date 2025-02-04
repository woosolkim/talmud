# Talmud Crew

"Talmud" is a revolutionary AI-powered conversation analysis and response system designed to help you win every discussion. Like the Jewish Talmud, the system seeks deep analysis and logical thinking, leveraging modern technology to give users an edge in any conversational situation.

### Key features:
* Emotion Analysis (Emotion Analyst)
Deeply analyzes the emotional content of typed text.
Multilingual support provides accurate sentiment analysis regardless of language.

* Rebuttal generation (Rebuttal Writer)
Generates a logical and convincing rebuttal to a given text.
Increase the credibility of your rebuttal by searching the web for relevant evidence.


* Text Improver
Analyzes the original text and improves it into a clearer, more effective version.
Takes context into account to enhance emotional impact and logical structure.


* Conversation Sustainer
Continues the conversation naturally based on the given text.
Empathizes with the other person's feelings and invites deeper discussion.



* Technical features:
Multi-agent system utilizing the CrewAI framework
Advanced text analytics with natural language processing and machine learning technology
Global availability with multilingual support
Real-time web search for up-to-date information


* Use case
Support academic discussions and paper writing
Strategize business negotiations
Analyzing and responding to political discourse
Prepare legal arguments
Improve marketing messages and optimize customer response

More than just a conversational tool, "Talmud" is a partner that amplifies your intellectual power. It helps you gain an edge in every conversation and debate through in-depth analysis, logical thinking, and effective communication. In today's complex communication environment, "Talmud" will be your powerful intellectual companion. 😅

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:

```bash
poetry lock
```

```bash
poetry install
```

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/talmud/config/agents.yaml` to define your agents
- Modify `src/talmud/config/tasks.yaml` to define your tasks
- Modify `src/talmud/crew.py` to add your own logic, tools and specific args
- Modify `src/talmud/main.py` to add custom inputs for your agents and tasks

## Running the Project

To use the Talmud AI-powered text analysis and response system, run the following command from the root folder of your project:

#### 1. As a command-line argument
```bash
poetry run talmud [analysis|improve|rebuttal|sustain] [--text "Your text here"]
```

#### 2. Through interactive input

```bash
poetry run talmud [analysis|improve|rebuttal|sustain]
```
When prompted, enter your text. For multi-line input, press Enter for a new line.
When finished, press Ctrl+D (Unix) or Ctrl+Z (Windows) followed by Enter.


**Available Modes**
* analysis: Performs a detailed emotional and content analysis of the given text.
* improve: Enhances the quality and effectiveness of the given text.
* rebuttal: Generates a logical and persuasive rebuttal to the given text.
* sustain: Creates a response that sustains the conversation about the given text.


## Examples

#### 1. Analyzing text
```bash
poetry run talmud analysis --text "AI has the potential to revolutionize many industries, but it also poses significant ethical challenges that need to be addressed."
```
#### 2. Improving text
```bash
poetry run talmud improve --text "AI good but problems too."
```
#### 3. Generating a rebuttal
```bash
poetry run talmud rebuttal --text "Social media has only negative effects on society."
```
#### 4. Sustaining a conversation
```bash
poetry run talmud sustain --text "I believe climate change is the most pressing issue of our time."
```



