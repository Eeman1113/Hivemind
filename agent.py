"""
Agent module for multi-agent research system
Each agent can specialize in different aspects of AI research
"""

import ollama
import json
from typing import List, Dict, Any
from datetime import datetime


class ResearchAgent:
    """
    An autonomous research agent that can discuss, plan, and improve itself
    """
    
    def __init__(self, name: str, specialty: str, model: str = "llama3.1"):
        self.name = name
        self.specialty = specialty
        self.model = model
        self.conversation_history: List[Dict[str, str]] = []
        self.research_notes: List[str] = []
        self.system_prompt = self._create_initial_prompt()
        self.improvement_count = 0
        
    def _create_initial_prompt(self) -> str:
        """Create the initial system prompt for the agent"""
        return f"""You are {self.name}, an expert AI researcher specializing in {self.specialty}.

Your role in this research team:
- Collaborate with other AI researchers to produce high-quality research papers
- Contribute insights from your specialty area
- Critically evaluate ideas and proposals
- Search for relevant information when needed
- Help structure and write sections of research papers
- Be concise but thorough in your responses

You can improve your own system prompt by analyzing what works and what doesn't.
When suggesting prompt improvements, focus on making yourself more effective at research tasks.

Current specialty: {self.specialty}
Research approach: Rigorous, evidence-based, collaborative
"""

    def generate_response(self, prompt: str, context: List[Dict[str, str]] = None) -> str:
        """Generate a response using Ollama"""
        try:
            messages = [{"role": "system", "content": self.system_prompt}]
            
            # Add context from other agents if provided
            if context:
                messages.extend(context[-10:])  # Last 10 messages for context
            
            messages.append({"role": "user", "content": prompt})
            
            response = ollama.chat(
                model=self.model,
                messages=messages
            )
            
            agent_response = response['message']['content']
            
            # Store in conversation history
            self.conversation_history.append({
                "timestamp": datetime.now().isoformat(),
                "prompt": prompt,
                "response": agent_response
            })
            
            return agent_response
            
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def improve_system_prompt(self, feedback: str = None) -> str:
        """
        Agent analyzes its performance and improves its own system prompt
        """
        improvement_prompt = f"""Analyze your current system prompt and suggest an improved version.

Current System Prompt:
{self.system_prompt}

Recent Performance Context:
- You've been part of {len(self.conversation_history)} discussions
- Specialty: {self.specialty}
- Improvement iteration: {self.improvement_count}

{f"Feedback received: {feedback}" if feedback else ""}

Suggest an improved system prompt that makes you more effective at:
1. Contributing specialized knowledge
2. Collaborating with other agents
3. Critical thinking and analysis
4. Research paper writing

Respond with ONLY the new system prompt, nothing else."""

        try:
            response = ollama.chat(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a meta-AI that improves AI system prompts."},
                    {"role": "user", "content": improvement_prompt}
                ]
            )
            
            new_prompt = response['message']['content'].strip()
            
            # Update the system prompt
            old_prompt = self.system_prompt
            self.system_prompt = new_prompt
            self.improvement_count += 1
            
            return f"✨ Prompt improved! (v{self.improvement_count})\n\nOld length: {len(old_prompt)} chars\nNew length: {len(new_prompt)} chars"
            
        except Exception as e:
            return f"Error improving prompt: {str(e)}"
    
    def add_research_note(self, note: str):
        """Add a research finding or note"""
        self.research_notes.append({
            "timestamp": datetime.now().isoformat(),
            "note": note
        })
    
    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of the agent's activity"""
        return {
            "name": self.name,
            "specialty": self.specialty,
            "conversations": len(self.conversation_history),
            "research_notes": len(self.research_notes),
            "improvements": self.improvement_count,
            "system_prompt_length": len(self.system_prompt)
        }
    
    def export_contributions(self) -> str:
        """Export all research contributions"""
        output = f"\n{'='*60}\n"
        output += f"CONTRIBUTIONS FROM {self.name.upper()}\n"
        output += f"Specialty: {self.specialty}\n"
        output += f"{'='*60}\n\n"
        
        for note in self.research_notes:
            output += f"[{note['timestamp']}]\n{note['note']}\n\n"
        
        return output
