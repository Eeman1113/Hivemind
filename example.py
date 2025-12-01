"""
Example script demonstrating programmatic usage of the multi-agent system
Run this for a quick demo without the interactive UI
"""

from orchestrator import ResearchOrchestrator
from rich.console import Console

console = Console()


def run_automated_research_demo():
    """
    Automated demo of the research system
    """
    
    console.print("\n[bold cyan]═══ AUTOMATED RESEARCH DEMO ═══[/bold cyan]\n")
    
    # Initialize orchestrator
    console.print("[yellow]1. Initializing Research Team...[/yellow]")
    orchestrator = ResearchOrchestrator()
    
    # Add specialized agents
    orchestrator.add_agent("Dr. Neural", "Neural Networks and Deep Learning")
    orchestrator.add_agent("Dr. Ethics", "AI Ethics and Safety")
    orchestrator.add_agent("Dr. NLP", "Natural Language Processing")
    
    console.print(f"[green]✓ Created {len(orchestrator.agents)} agents[/green]\n")
    
    # Set research topic
    console.print("[yellow]2. Setting Research Topic...[/yellow]")
    topic = "Ethical Considerations in Large Language Models"
    orchestrator.set_research_topic(topic)
    console.print(f"[green]✓ Topic: {topic}[/green]\n")
    
    # Brainstorming
    console.print("[yellow]3. Brainstorming Session (2 rounds)...[/yellow]")
    brainstorm_results = orchestrator.conduct_brainstorm_session(rounds=2)
    console.print(f"[green]✓ Generated {len(brainstorm_results)} ideas[/green]\n")
    
    # Show a sample idea
    if brainstorm_results:
        console.print("[cyan]Sample Idea:[/cyan]")
        console.print(f"  {brainstorm_results[0][:200]}...\n")
    
    # Research phase
    console.print("[yellow]4. Conducting Research...[/yellow]")
    search_queries = ["ethical AI frameworks", "LLM bias mitigation"]
    results = orchestrator.conduct_research_phase(search_queries)
    console.print(f"[green]✓ Completed {len(search_queries)} searches[/green]\n")
    
    # Discussion
    console.print("[yellow]5. Structured Discussion...[/yellow]")
    discussion = orchestrator.structured_discussion("Bias mitigation strategies", rounds=1)
    console.print(f"[green]✓ {len(discussion)} discussion messages[/green]\n")
    
    # Self-improvement
    console.print("[yellow]6. Agent Self-Improvement...[/yellow]")
    improvements = orchestrator.trigger_self_improvement()
    for agent_name, result in improvements:
        console.print(f"[magenta]  • {agent_name}: Improved![/magenta]")
    console.print()
    
    # Check satisfaction
    console.print("[yellow]7. Evaluating Satisfaction...[/yellow]")
    scores = orchestrator.evaluate_satisfaction()
    avg_score = sum(scores.values()) / len(scores) if scores else 0
    console.print(f"[green]✓ Average satisfaction: {avg_score:.1f}/10[/green]\n")
    
    for agent, score in scores.items():
        emoji = "🟢" if score >= 8 else "🟡" if score >= 6 else "🔴"
        console.print(f"  {emoji} {agent}: {score}/10")
    console.print()
    
    # Generate paper
    console.print("[yellow]8. Generating Research Paper...[/yellow]")
    paper_file = orchestrator.compile_final_paper()
    console.print(f"[bold green]✓ Paper generated: {paper_file}[/bold green]\n")
    
    # Export session
    console.print("[yellow]9. Exporting Session Data...[/yellow]")
    session_file = orchestrator.export_session_log()
    console.print(f"[green]✓ Session data: {session_file}[/green]\n")
    
    # Summary
    console.print("[bold cyan]═══ DEMO COMPLETE ═══[/bold cyan]\n")
    console.print(f"[white]Research Topic:[/white] {topic}")
    console.print(f"[white]Total Interactions:[/white] {len(orchestrator.discussion_log)}")
    console.print(f"[white]Average Satisfaction:[/white] {avg_score:.1f}/10")
    console.print(f"[white]Output Files:[/white]")
    console.print(f"  • {paper_file}")
    console.print(f"  • {session_file}\n")
    
    console.print("[dim]To compile PDF: pdflatex research_paper.tex[/dim]\n")


def run_minimal_example():
    """
    Minimal example showing core functionality
    """
    
    console.print("\n[bold cyan]═══ MINIMAL EXAMPLE ═══[/bold cyan]\n")
    
    # Quick setup
    orchestrator = ResearchOrchestrator()
    orchestrator.add_agent("Dr. AI", "Artificial Intelligence")
    orchestrator.set_research_topic("The Future of AI")
    
    # One round of ideas
    console.print("[yellow]Brainstorming...[/yellow]")
    ideas = orchestrator.conduct_brainstorm_session(rounds=1)
    
    # Show result
    console.print(f"\n[green]Generated {len(ideas)} ideas:[/green]\n")
    for i, idea in enumerate(ideas, 1):
        console.print(f"{i}. {idea[:150]}...\n")
    
    console.print("[cyan]✓ Minimal example complete![/cyan]\n")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "minimal":
        run_minimal_example()
    else:
        run_automated_research_demo()
