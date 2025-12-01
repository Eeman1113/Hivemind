"""
ADVANCED USAGE GUIDE
====================

This guide covers advanced features and customization options
"""


# ============================================================================
# 1. CUSTOM AGENT CREATION
# ============================================================================

"""
Create agents with custom specialties and behaviors
"""

from agent import ResearchAgent
from orchestrator import ResearchOrchestrator

def create_custom_agent_team():
    orchestrator = ResearchOrchestrator()
    
    # Create specialized agents with custom prompts
    quantum_agent = orchestrator.add_agent(
        name="Dr. Quantum",
        specialty="Quantum Machine Learning and Quantum Computing",
        model="llama3.1"
    )
    
    # Customize the agent's prompt immediately
    quantum_agent.system_prompt = """You are Dr. Quantum, world expert in quantum ML.
    
Your expertise:
- Quantum algorithms for machine learning
- QAOA, VQE, and quantum neural networks
- Quantum advantage in AI applications
- Hybrid quantum-classical systems

When contributing to research:
- Focus on quantum speedups and advantages
- Explain quantum concepts clearly
- Bridge quantum and classical ML
- Be rigorous about quantum complexity theory
"""
    
    return orchestrator


# ============================================================================
# 2. CUSTOM SEARCH INTEGRATION
# ============================================================================

"""
Integrate your own search APIs for better research grounding
"""

from search_tool import ResearchSearch
import requests


class CustomResearchSearch(ResearchSearch):
    """
    Extended search with multiple API integrations
    """
    
    def __init__(self, api_keys: dict = None):
        super().__init__()
        self.api_keys = api_keys or {}
    
    def search_semantic_scholar(self, query: str, limit: int = 10):
        """
        Search Semantic Scholar for academic papers
        """
        url = "https://api.semanticscholar.org/graph/v1/paper/search"
        params = {
            "query": query,
            "limit": limit,
            "fields": "title,abstract,authors,year,citationCount,url"
        }
        
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                return [
                    {
                        "title": paper.get("title", ""),
                        "abstract": paper.get("abstract", "")[:500],
                        "authors": [a.get("name") for a in paper.get("authors", [])],
                        "year": paper.get("year"),
                        "citations": paper.get("citationCount", 0),
                        "url": paper.get("url", ""),
                        "source": "Semantic Scholar"
                    }
                    for paper in data.get("data", [])
                ]
        except Exception as e:
            return [{"error": str(e)}]
        
        return []
    
    def search_google_scholar(self, query: str):
        """
        Search Google Scholar (requires serpapi or similar)
        """
        # Implement with SerpAPI or similar service
        pass
    
    def search_pubmed(self, query: str, max_results: int = 10):
        """
        Search PubMed for biomedical research
        """
        base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        params = {
            "db": "pubmed",
            "term": query,
            "retmax": max_results,
            "retmode": "json"
        }
        
        try:
            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                ids = data.get("esearchresult", {}).get("idlist", [])
                
                # Fetch details for each ID
                # (simplified - full implementation would fetch abstracts)
                return [{"pubmed_id": id, "source": "PubMed"} for id in ids]
        except Exception as e:
            return [{"error": str(e)}]
        
        return []


# ============================================================================
# 3. ADVANCED ORCHESTRATION PATTERNS
# ============================================================================

"""
Complex multi-agent workflows
"""

def hierarchical_research_workflow(topic: str):
    """
    Hierarchical workflow: Lead agent coordinates specialists
    """
    orchestrator = ResearchOrchestrator()
    
    # Create lead researcher
    lead = orchestrator.add_agent("Dr. Lead", "Research Coordination", "llama3.1")
    lead.system_prompt = """You are the lead researcher coordinating a team.
    Your role:
    - Define research sub-questions
    - Assign tasks to specialists
    - Synthesize findings
    - Ensure coherence in final output
    """
    
    # Create specialists
    orchestrator.add_agent("Dr. Theory", "Theoretical Foundations", "llama3.1")
    orchestrator.add_agent("Dr. Empirical", "Experimental Methods", "llama3.1")
    orchestrator.add_agent("Dr. Applications", "Real-world Applications", "llama3.1")
    
    # Phase 1: Lead breaks down the problem
    breakdown_prompt = f"""Research topic: {topic}
    
    As lead researcher, break this into 3 focused sub-questions that our specialists can tackle.
    Assign each question to the most appropriate specialist."""
    
    breakdown = lead.generate_response(breakdown_prompt)
    
    # Phase 2: Specialists work on their parts
    # ... (implement delegation logic)
    
    # Phase 3: Lead synthesizes
    # ... (implement synthesis)
    
    return orchestrator


def debate_style_research(topic: str):
    """
    Agents debate different positions to explore the topic
    """
    orchestrator = ResearchOrchestrator()
    
    # Create opposing viewpoints
    optimist = orchestrator.add_agent("Dr. Optimist", "AI Optimism", "llama3.1")
    optimist.system_prompt = """You argue for the positive potential of AI.
    Focus on benefits, opportunities, and solutions."""
    
    skeptic = orchestrator.add_agent("Dr. Skeptic", "AI Risks", "llama3.1")
    skeptic.system_prompt = """You raise critical concerns about AI.
    Focus on risks, limitations, and challenges."""
    
    pragmatist = orchestrator.add_agent("Dr. Pragmatist", "Balanced Analysis", "llama3.1")
    pragmatist.system_prompt = """You provide balanced, practical analysis.
    Synthesize both optimistic and skeptical views."""
    
    # Run structured debate
    for round in range(3):
        # Optimist argues
        opt_arg = optimist.generate_response(f"Round {round+1}: Argue for {topic}")
        
        # Skeptic counters
        skep_arg = skeptic.generate_response(f"Counter the optimistic view: {opt_arg}")
        
        # Pragmatist synthesizes
        syn = pragmatist.generate_response(f"Synthesize these views: {opt_arg} vs {skep_arg}")
    
    return orchestrator


# ============================================================================
# 4. ADVANCED LATEX CUSTOMIZATION
# ============================================================================

"""
Create custom LaTeX templates and diagrams
"""

from latex_generator import LatexPaperGenerator


class AdvancedLatexGenerator(LatexPaperGenerator):
    """
    Extended LaTeX generator with more options
    """
    
    def generate_algorithm(self, algorithm_name: str, steps: list) -> str:
        """
        Generate LaTeX algorithm block
        """
        latex = f"""
\\begin{{algorithm}}
\\caption{{{algorithm_name}}}
\\begin{{algorithmic}}[1]
"""
        for step in steps:
            latex += f"\\STATE {step}\n"
        
        latex += """\\end{algorithmic}
\\end{algorithm}
"""
        return latex
    
    def generate_comparison_table(self, data: dict) -> str:
        """
        Generate comparison table
        """
        headers = list(data.keys())
        num_cols = len(headers)
        
        latex = f"""
\\begin{{table}}[h]
\\centering
\\begin{{tabular}}{{|{'c|' * num_cols}}}
\\hline
"""
        # Headers
        latex += " & ".join(headers) + " \\\\\n\\hline\n"
        
        # Data rows (simplified)
        # ... (add data rows)
        
        latex += """\\hline
\\end{tabular}
\\caption{Comparison Table}
\\end{table}
"""
        return latex
    
    def generate_neural_network_diagram(self, layers: list) -> str:
        """
        Generate detailed neural network diagram
        """
        latex = """
\\begin{tikzpicture}[
    node distance=2.5cm,
    neuron/.style={circle, draw, minimum size=0.8cm},
    layer/.style={rectangle, draw, minimum width=2cm, minimum height=1cm}
]
"""
        for i, layer in enumerate(layers):
            latex += f"    \\node[layer] (layer{i}) at ({i*3},0) {{{layer}}};\n"
        
        for i in range(len(layers) - 1):
            latex += f"    \\draw[->] (layer{i}) -- (layer{i+1});\n"
        
        latex += "\\end{tikzpicture}\n"
        return latex


# ============================================================================
# 5. PERFORMANCE OPTIMIZATION
# ============================================================================

"""
Optimize for speed and quality
"""

def optimize_agent_performance():
    """
    Tips for optimizing agent performance
    """
    
    tips = {
        "Model Selection": {
            "Fast responses": "Use llama3.1:8b or mistral:7b",
            "High quality": "Use llama3.1:70b or mixtral:8x7b",
            "Balanced": "Use llama3.1:13b"
        },
        
        "Context Management": {
            "Limit history": "Keep only last 10 messages in context",
            "Summarize": "Periodically summarize long discussions",
            "Prune": "Remove redundant information"
        },
        
        "Parallel Processing": {
            "Concurrent agents": "Use threading for independent agent tasks",
            "Async I/O": "Use asyncio for search operations",
            "Batch requests": "Group similar queries"
        },
        
        "Prompt Engineering": {
            "Be specific": "Clear, focused prompts get better results",
            "Examples": "Include examples in system prompts",
            "Constraints": "Specify output format and length"
        }
    }
    
    return tips


# ============================================================================
# 6. QUALITY ASSURANCE
# ============================================================================

"""
Implement quality checks and validation
"""

class QualityChecker:
    """
    Validate research quality
    """
    
    @staticmethod
    def check_citation_quality(paper_content: str) -> dict:
        """
        Verify citations are properly formatted
        """
        issues = []
        
        # Check for common citation issues
        if "[citation needed]" in paper_content:
            issues.append("Missing citations found")
        
        if "et al." not in paper_content and "al." in paper_content:
            issues.append("Possible citation formatting issues")
        
        return {
            "valid": len(issues) == 0,
            "issues": issues
        }
    
    @staticmethod
    def check_logical_flow(sections: list) -> dict:
        """
        Verify logical flow between sections
        """
        # Use an agent to check coherence
        # ... (implement with LLM)
        pass
    
    @staticmethod
    def check_technical_accuracy(content: str, domain: str) -> dict:
        """
        Verify technical accuracy
        """
        # Use specialized agent to fact-check
        # ... (implement with domain expert agent)
        pass


# ============================================================================
# 7. EXPORT AND INTEGRATION
# ============================================================================

"""
Export to different formats and integrate with other tools
"""

def export_to_markdown(orchestrator: ResearchOrchestrator) -> str:
    """
    Export research to Markdown format
    """
    md = f"# {orchestrator.research_topic}\n\n"
    
    md += "## Research Team\n\n"
    for agent in orchestrator.agents:
        md += f"- **{agent.name}**: {agent.specialty}\n"
    
    md += "\n## Discussion Log\n\n"
    for entry in orchestrator.discussion_log:
        md += f"### {entry['agent']}\n\n"
        md += f"{entry.get('content', '')}\n\n"
    
    return md


def export_to_notion(orchestrator: ResearchOrchestrator):
    """
    Export to Notion (requires Notion API)
    """
    # Implement Notion API integration
    pass


def export_to_overleaf(paper_file: str):
    """
    Upload to Overleaf (requires Overleaf API)
    """
    # Implement Overleaf integration
    pass


# ============================================================================
# 8. MONITORING AND LOGGING
# ============================================================================

"""
Advanced monitoring and debugging
"""

import logging
from datetime import datetime


def setup_advanced_logging():
    """
    Configure detailed logging
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f'research_session_{datetime.now():%Y%m%d_%H%M%S}.log'),
            logging.StreamHandler()
        ]
    )
    
    # Create loggers for different components
    agent_logger = logging.getLogger('agent')
    search_logger = logging.getLogger('search')
    orchestrator_logger = logging.getLogger('orchestrator')
    
    return agent_logger, search_logger, orchestrator_logger


# ============================================================================
# EXAMPLE: COMPLETE ADVANCED WORKFLOW
# ============================================================================

def run_advanced_research_workflow():
    """
    Complete example using advanced features
    """
    
    # Setup
    orchestrator = create_custom_agent_team()
    search_tool = CustomResearchSearch()
    
    # Set topic
    topic = "Quantum Advantage in Machine Learning"
    orchestrator.set_research_topic(topic)
    
    # Phase 1: Initial research
    queries = [
        "quantum machine learning algorithms",
        "quantum advantage demonstrations",
        "hybrid quantum-classical ML"
    ]
    
    for query in queries:
        results = search_tool.search_semantic_scholar(query, limit=5)
        # Process results...
    
    # Phase 2: Structured research
    brainstorm = orchestrator.conduct_brainstorm_session(rounds=3)
    
    # Phase 3: Self-improvement
    orchestrator.trigger_self_improvement()
    
    # Phase 4: Quality checking
    # ... (implement quality checks)
    
    # Phase 5: Generate paper
    paper_file = orchestrator.compile_final_paper()
    
    # Phase 6: Export
    markdown = export_to_markdown(orchestrator)
    
    return paper_file, markdown


if __name__ == "__main__":
    print("Advanced Usage Guide")
    print("=" * 50)
    print("\nThis file contains examples of advanced usage.")
    print("Import and use these functions in your own scripts.")
    print("\nKey features:")
    print("- Custom agent creation")
    print("- Advanced search integration")
    print("- Complex orchestration patterns")
    print("- LaTeX customization")
    print("- Performance optimization")
    print("- Quality assurance")
    print("- Export options")
    print("- Monitoring and logging")
