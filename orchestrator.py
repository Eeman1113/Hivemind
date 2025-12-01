"""
Multi-Agent Orchestrator
Manages multiple research agents and coordinates their collaboration
"""

from typing import List, Dict
import ollama
from agent import ResearchAgent
from search_tool import ResearchSearch
from latex_generator import LatexPaperGenerator
import json
from datetime import datetime


class ResearchOrchestrator:
    """
    Orchestrates multiple AI agents for collaborative research
    """
    
    def __init__(self):
        self.agents: List[ResearchAgent] = []
        self.search_tool = ResearchSearch()
        self.latex_generator = LatexPaperGenerator()
        self.discussion_log: List[Dict] = []
        self.research_topic = ""
        self.satisfaction_scores: Dict[str, int] = {}
        self.target_satisfaction = 8  # Out of 10
        
    def add_agent(self, name: str, specialty: str, model: str = "llama3.1"):
        """Add a new research agent to the team"""
        agent = ResearchAgent(name, specialty, model)
        self.agents.append(agent)
        self.satisfaction_scores[name] = 5  # Start at neutral
        return agent
    
    def initialize_default_team(self):
        """Initialize a default research team"""
        self.add_agent("Dr. Neural", "Neural Networks and Deep Learning", "llama3.1")
        self.add_agent("Dr. Ethics", "AI Ethics and Safety", "llama3.1")
        self.add_agent("Dr. NLP", "Natural Language Processing", "llama3.1")
        self.add_agent("Dr. Vision", "Computer Vision and Multimodal AI", "llama3.1")
        self.add_agent("Dr. RL", "Reinforcement Learning", "llama3.1")
    
    def set_research_topic(self, topic: str):
        """Set the research topic for the team"""
        self.research_topic = topic
    
    def conduct_brainstorm_session(self, rounds: int = 3) -> List[str]:
        """
        Conduct a brainstorming session among agents
        """
        brainstorm_results = []
        
        for round_num in range(rounds):
            round_ideas = []
            
            for agent in self.agents:
                prompt = f"""Research Topic: {self.research_topic}
                
Brainstorming Round {round_num + 1}/{rounds}

{'Previous ideas from team:' if brainstorm_results else 'Initial brainstorming - share your key ideas:'}
{chr(10).join(brainstorm_results[-5:]) if brainstorm_results else ''}

As an expert in {agent.specialty}, provide 2-3 key research directions or hypotheses.
Be specific and build upon previous ideas where relevant."""

                response = agent.generate_response(prompt)
                round_ideas.append(f"[{agent.name}]: {response}")
                
                self.discussion_log.append({
                    "round": round_num + 1,
                    "agent": agent.name,
                    "type": "brainstorm",
                    "content": response
                })
            
            brainstorm_results.extend(round_ideas)
        
        return brainstorm_results
    
    def conduct_research_phase(self, search_queries: List[str]) -> Dict[str, any]:
        """
        Agents conduct research using search tool
        """
        search_results = {}
        
        for query in search_queries:
            # Assign search to most relevant agent
            agent = self.agents[0]  # Simplified assignment
            
            # Perform search
            results = self.search_tool.search_arxiv(query, max_results=3)
            search_results[query] = results
            
            # Agent analyzes results
            analysis_prompt = f"""You searched for: "{query}"
            
Search Results:
{json.dumps(results, indent=2)}

Analyze these results and extract key findings relevant to our research on: {self.research_topic}
Provide a concise summary of the most important insights."""

            analysis = agent.generate_response(analysis_prompt)
            agent.add_research_note(f"Search: {query}\nFindings: {analysis}")
            
            self.discussion_log.append({
                "agent": agent.name,
                "type": "research",
                "query": query,
                "analysis": analysis
            })
        
        return search_results
    
    def structured_discussion(self, topic: str, rounds: int = 2) -> List[str]:
        """
        Conduct a structured discussion on a specific topic
        """
        discussion = []
        context = []
        
        for round_num in range(rounds):
            for agent in self.agents:
                prompt = f"""Discussion Topic: {topic}
                
Round {round_num + 1}/{rounds}
Research Context: {self.research_topic}

{'Recent discussion:' if context else 'Opening statement:'}
{chr(10).join(context[-3:]) if context else ''}

Provide your perspective from {agent.specialty}. Be analytical and critical.
{"Challenge or build upon previous points." if context else ""}"""

                response = agent.generate_response(prompt, context)
                
                message = f"[{agent.name}]: {response}"
                discussion.append(message)
                context.append({"role": "assistant", "content": message})
                
                self.discussion_log.append({
                    "round": round_num + 1,
                    "agent": agent.name,
                    "type": "discussion",
                    "topic": topic,
                    "content": response
                })
        
        return discussion
    
    def evaluate_satisfaction(self) -> Dict[str, int]:
        """
        Each agent evaluates their satisfaction with the research progress
        """
        for agent in self.agents:
            prompt = f"""Evaluate the research progress on: {self.research_topic}

Your contributions so far: {len(agent.research_notes)} research notes
Team discussions: {len(self.discussion_log)} messages

Rate your satisfaction with:
1. Quality of research conducted
2. Depth of analysis
3. Collaboration effectiveness
4. Readiness to publish findings

Respond with ONLY a number from 1-10, where:
1-3: Needs significant more work
4-6: Making progress but incomplete
7-8: Good progress, minor refinements needed
9-10: Excellent, ready to publish

Your rating:"""

            try:
                response = agent.generate_response(prompt)
                # Extract number from response
                score = int(''.join(filter(str.isdigit, response.split()[0])))
                score = max(1, min(10, score))  # Clamp between 1-10
                self.satisfaction_scores[agent.name] = score
            except:
                self.satisfaction_scores[agent.name] = 5  # Default neutral
        
        return self.satisfaction_scores
    
    def check_consensus(self) -> bool:
        """Check if agents have reached satisfactory consensus"""
        if not self.satisfaction_scores:
            return False
        
        avg_score = sum(self.satisfaction_scores.values()) / len(self.satisfaction_scores)
        return avg_score >= self.target_satisfaction
    
    def generate_paper_sections(self) -> Dict[str, str]:
        """
        Agents collaborate to generate paper sections
        """
        sections = {}
        
        # Title and abstract
        title_agent = self.agents[0]
        title_prompt = f"""Generate a compelling research paper title for our work on: {self.research_topic}

Respond with ONLY the title, nothing else."""
        
        title = title_agent.generate_response(title_prompt).strip()
        sections['title'] = title
        
        # Abstract
        abstract_prompt = f"""Write a concise abstract (150-200 words) for our research paper on: {self.research_topic}

Include:
- Main objective
- Methodology
- Key findings
- Significance

Respond with ONLY the abstract text."""

        abstract = title_agent.generate_response(abstract_prompt)
        sections['abstract'] = abstract
        
        # Introduction
        intro_agent = self.agents[1] if len(self.agents) > 1 else self.agents[0]
        intro_prompt = f"""Write the Introduction section for our paper on: {self.research_topic}

Include:
- Background and motivation
- Research gap
- Our contributions
- Paper structure

Provide the complete introduction section."""

        sections['introduction'] = intro_agent.generate_response(intro_prompt)
        
        # Methodology (each agent contributes from their expertise)
        methodology_parts = []
        for agent in self.agents:
            method_prompt = f"""Write a methodology subsection from your expertise in {agent.specialty}
            
For the research topic: {self.research_topic}

Describe the methods, techniques, or approaches relevant to your area.
Keep it concise (2-3 paragraphs)."""

            method_part = agent.generate_response(method_prompt)
            methodology_parts.append(f"\\subsection{{{agent.specialty}}}\n{method_part}")
        
        sections['methodology'] = "\n\n".join(methodology_parts)
        
        # Results and Discussion
        results_agent = self.agents[-1]
        results_prompt = f"""Write the Results and Discussion section.

Research topic: {self.research_topic}

Synthesize the key findings and discuss their implications.
Include analysis and interpretation."""

        sections['results'] = results_agent.generate_response(results_prompt)
        
        # Conclusion
        conclusion_prompt = f"""Write the Conclusion section.

Summarize:
- Main contributions
- Findings
- Limitations
- Future work

Be concise but comprehensive."""

        sections['conclusion'] = results_agent.generate_response(conclusion_prompt)
        
        return sections
    
    def compile_final_paper(self) -> str:
        """
        Compile all research into a final LaTeX paper
        """
        # Generate sections
        sections = self.generate_paper_sections()
        
        # Set metadata
        authors = [agent.name for agent in self.agents]
        self.latex_generator.set_metadata(
            sections['title'],
            authors,
            sections['abstract']
        )
        
        # Add sections
        self.latex_generator.add_section("Introduction", sections['introduction'])
        self.latex_generator.add_section("Methodology", sections['methodology'])
        self.latex_generator.add_section("Results and Discussion", sections['results'])
        
        # Save to file
        filename = self.latex_generator.save_to_file("research_paper.tex")
        return filename
    
    def export_session_log(self, filename: str = "research_session.json"):
        """Export complete session log"""
        session_data = {
            "topic": self.research_topic,
            "timestamp": datetime.now().isoformat(),
            "agents": [agent.get_summary() for agent in self.agents],
            "discussion_log": self.discussion_log,
            "satisfaction_scores": self.satisfaction_scores,
            "total_interactions": len(self.discussion_log)
        }
        
        with open(filename, 'w') as f:
            json.dump(session_data, f, indent=2)
        
        return filename
    
    def trigger_self_improvement(self):
        """Trigger all agents to improve their system prompts"""
        results = []
        for agent in self.agents:
            feedback = f"Research topic: {self.research_topic}. Recent discussions: {len(self.discussion_log)}."
            result = agent.improve_system_prompt(feedback)
            results.append((agent.name, result))
        return results
