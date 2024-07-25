from crewai_tools import SerperDevTool

class WebSearchTool(SerperDevTool):
    def __init__(self):
        super().__init__()
        self.name = "Web Search"
        self.description = "Searches the web for relevant information and returns a list of search results with URLs."
