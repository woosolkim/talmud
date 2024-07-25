from crewai import Agent, Task, Crew
from .tools.emotion_analysis_tool import EmotionAnalysisTool
from .tools.web_search_tool import WebSearchTool
from langdetect import detect
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
custom_llm = ChatOpenAI(model_name="gpt-4o-mini")

class TextAnalysisCrew:
    def __init__(self):
        emotion_tool = EmotionAnalysisTool()
        web_search_tool = WebSearchTool()
        
        self.emotion_analyst = Agent(
            role='Emotion Analyst',
            goal='Accurately analyze the emotional content and context of given text',
            backstory="""You are an expert in linguistic analysis with a focus on emotion and sentiment. 
            Your skills in natural language processing allow you to discern subtle emotional nuances in text.""",
            tools=[emotion_tool],
            llm=custom_llm,
            verbose=True
        )
        
        self.rebuttal_writer = Agent(
            role='Rebuttal Writer',
            goal='Create a logical and persuasive rebuttal to the given text with supporting evidence',
            backstory="""You are a skilled debater and critical thinker. Your ability to identify logical flaws 
            and present counterarguments is unparalleled. You always strive for objectivity and base your 
            rebuttals on facts and sound reasoning. You use web searches to find supporting evidence for your arguments.""",
            tools=[web_search_tool],
            llm=custom_llm,
            verbose=True
        )

        self.text_improver = Agent(
            role='Text Improver',
            goal='Enhance the quality, clarity, and effectiveness of the given text',
            backstory="""You are a master wordsmith with a keen eye for detail. Your expertise lies in refining text 
            to improve its impact, readability, and overall quality. You can adapt your writing style to suit various 
            contexts and audiences while maintaining the core message of the original text. 
            You search the web to find evidence to support your writing. """,
            tools=[web_search_tool],
            llm=custom_llm,
            verbose=True
        )

        self.conversation_sustainer = Agent(
            role='Conversation Sustainer',
            goal='Maintain a natural and engaging conversation flow based on the given text',
            backstory="""You are an empathetic and insightful conversationalist. Your ability to understand 
            and respond to emotional nuances allows you to keep conversations flowing naturally. You can 
            ask thoughtful questions, offer empathetic responses, and gently guide discussions to explore 
            deeper aspects of a topic.""",
            tools=[emotion_tool, web_search_tool],
            llm=custom_llm,
            verbose=True
        )


    def analyze(self, text, mode):
        detected_lang = detect(text)
        
        emotion_analysis_task = Task(
            description=f"""Analyze the emotional content of the following text: 
            
            {text}
            
            Provide a detailed breakdown of the emotional tones, intensity, and any notable patterns or shifts in emotion throughout the text. 
            Use the Emotion Analysis Tool to get detailed sentiment scores.
            Interpret these scores and explain what they mean in the context of the text.
            
            IMPORTANT: Respond in the same language as the input text, which is {detected_lang}.""",
            expected_output=f"""A comprehensive analysis of the text's emotional content, including overall sentiment, emotional intensity, specific emotions detected, and interpretation of sentiment scores. The response should be in {detected_lang}.""",
            agent=self.emotion_analyst
        )

        crew_tasks = [emotion_analysis_task]

        if mode == 'rebuttal':
            rebuttal_task = Task(
                description=f"""Based on the emotional analysis, create a logical and persuasive rebuttal to the following text:
                
                {text}
                
                Your rebuttal should:
                1. Address the main points of the original text.
                2. Identify any logical flaws or emotional manipulation.
                3. Present counter-arguments supported by reasoning.
                4. Use the Web Search tool to find relevant supporting evidence or factual information.
                5. Include at least 2-3 relevant URLs as references to support your arguments.
                6. If the analysis is emotionally biased, add a call to reason. 
                
                Be respectful but firm in your rebuttal. Ensure that your arguments are well-supported by the evidence you find.
                
                IMPORTANT: Write your rebuttal in the same language as the input text, which is {detected_lang}.""",
                expected_output=f"""A well-structured rebuttal that addresses the main points of the original text, 
                identifies flaws in reasoning or emotional appeals, presents logical counter-arguments, and includes 
                relevant URLs as references to support the arguments. The rebuttal should be in {detected_lang}.""",
                agent=self.rebuttal_writer
            )
            crew_tasks.append(rebuttal_task)
        elif mode == 'improve':
            improvement_task = Task(
                description=f"""Based on the emotional analysis, improve the following text:
                
                {text}
                
                Your improved version should:
                1. Enhance clarity and readability.
                2. Strengthen the emotional impact where appropriate.
                3. Improve the structure and flow of ideas.
                4. Correct any grammatical or stylistic issues.
                5. Add relevant details, 2-3 relevant URLs as references if needed(you can use a web search tool for this).
                
                Maintain the original intent and core message of the text while making it more effective and engaging.
                
                IMPORTANT: Write your improved version in the same language as the input text, which is {detected_lang}.""",
                expected_output=f"""An improved version of the original text that enhances its clarity, emotional impact, 
                structure, and overall effectiveness. The improved text should be in {detected_lang}.""",
                agent=self.text_improver
            )
            crew_tasks.append(improvement_task)
        elif mode == 'sustain':
            sustain_task = Task(
                description=f"""Based on the emotional analysis, generate a response that sustains the conversation about the following text:
                
                {text}
                
                Your response should:
                1. Show empathy and understanding of the emotions expressed in the text.
                2. Encourage further discussion by commenting on key points or themes.
                3. Ask open-ended questions that invite elaboration, if appropriate.
                4. Offer insights or perspectives that could deepen the conversation.
                5. Maintain a natural, conversational tone.
                
                Your goal is to keep the conversation flowing naturally, not necessarily to end with a question. 
                Use the Emotion Analysis Tool to understand the text's emotional context and the Web Search tool 
                if you need to reference any external information.
                
                IMPORTANT: Write your response in the same language as the input text, which is {detected_lang}.""",
                expected_output=f"""A thoughtful and engaging response that sustains the conversation, shows empathy, 
                and encourages further discussion. The response should feel natural and be in {detected_lang}.""",
                agent=self.conversation_sustainer
            )
            crew_tasks.append(sustain_task)

        crew = Crew(
            agents=[self.emotion_analyst, self.rebuttal_writer, self.text_improver, self.conversation_sustainer],
            tasks=crew_tasks,
            verbose=2
        )

        return crew.kickoff()