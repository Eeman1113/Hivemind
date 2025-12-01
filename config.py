"""
Configuration file for Multi-Agent Research System
Customize settings here
"""

# Ollama Settings
OLLAMA_MODEL = "llama3.1"  # Default model for all agents
OLLAMA_HOST = "http://localhost:11434"  # Ollama API host

# Agent Settings
DEFAULT_AGENTS = [
    {
        "name": "Dr. Neural",
        "specialty": "Neural Networks and Deep Learning",
        "model": "llama3.1"
    },
    {
        "name": "Dr. Ethics",
        "specialty": "AI Ethics and Safety",
        "model": "llama3.1"
    },
    {
        "name": "Dr. NLP",
        "specialty": "Natural Language Processing",
        "model": "llama3.1"
    },
    {
        "name": "Dr. Vision",
        "specialty": "Computer Vision and Multimodal AI",
        "model": "llama3.1"
    },
    {
        "name": "Dr. RL",
        "specialty": "Reinforcement Learning",
        "model": "llama3.1"
    }
]

# Research Settings
TARGET_SATISFACTION = 8  # Target satisfaction score (1-10)
DEFAULT_BRAINSTORM_ROUNDS = 3
DEFAULT_DISCUSSION_ROUNDS = 2
DEFAULT_SEARCH_RESULTS = 5

# UI Settings
UI_THEME = {
    "primary": "cyan",
    "secondary": "yellow",
    "success": "green",
    "error": "red",
    "warning": "yellow",
    "info": "blue"
}

# LaTeX Settings
LATEX_TEMPLATE = "article"  # Can be: article, report, book
INCLUDE_TIKZ_DIAGRAMS = True
INCLUDE_BIBLIOGRAPHY = True

# Search Settings
ENABLE_ARXIV_SEARCH = True
ENABLE_WEB_SEARCH = True
ENABLE_PAPERS_WITH_CODE = False  # Set to True if you have API access

# Output Settings
DEFAULT_PAPER_FILENAME = "research_paper.tex"
DEFAULT_SESSION_FILENAME = "research_session.json"
AUTO_SAVE_DISCUSSIONS = True

# Performance Settings
MAX_CONTEXT_MESSAGES = 10  # Number of previous messages to include in context
AGENT_RESPONSE_TIMEOUT = 120  # Seconds
ENABLE_STREAMING = False  # Stream agent responses (if supported)

# Experimental Features
ENABLE_AGENT_MEMORY = True  # Agents remember past interactions
ENABLE_CROSS_AGENT_LEARNING = True  # Agents learn from each other
AUTO_IMPROVEMENT_THRESHOLD = 10  # Trigger self-improvement after N interactions
