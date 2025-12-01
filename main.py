"""
Terminal GUI for Multi-Agent Research System
Using Rich library for beautiful terminal interface
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.live import Live
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich import box
from rich.text import Text
import time
from orchestrator import ResearchOrchestrator


console = Console()


class ResearchTerminalUI:
    """
    Beautiful terminal interface for the research system
    """
    
    def __init__(self):
        self.orchestrator = ResearchOrchestrator()
        self.running = True
        
    def display_banner(self):
        """Display welcome banner"""
        banner = """
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║        🤖 MULTI-AGENT AI RESEARCH SYSTEM 🤖                  ║
║                                                               ║
║     Collaborative AI Agents for Research Paper Generation    ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
"""
        console.print(banner, style="bold cyan")
        console.print("\n[dim]Powered by Ollama + Python + Rich[/dim]\n")
    
    def display_menu(self):
        """Display main menu"""
        table = Table(title="Main Menu", box=box.ROUNDED, style="cyan")
        table.add_column("Option", style="bold yellow", width=10)
        table.add_column("Action", style="white")
        
        table.add_row("1", "Initialize Research Team")
        table.add_row("2", "Set Research Topic")
        table.add_row("3", "Start Brainstorming Session")
        table.add_row("4", "Conduct Research & Search")
        table.add_row("5", "Structured Discussion")
        table.add_row("6", "View Agent Status")
        table.add_row("7", "Trigger Self-Improvement")
        table.add_row("8", "Check Satisfaction Levels")
        table.add_row("9", "Generate Research Paper")
        table.add_row("10", "Export Session Data")
        table.add_row("11", "View Discussion Log")
        table.add_row("0", "Exit")
        
        console.print(table)
    
    def initialize_team(self):
        """Initialize the research team"""
        console.print("\n[bold cyan]Initializing Research Team...[/bold cyan]\n")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            task = progress.add_task("Creating agents...", total=5)
            
            self.orchestrator.initialize_default_team()
            progress.update(task, advance=5)
        
        # Display team
        table = Table(title="Research Team", box=box.DOUBLE, style="green")
        table.add_column("Agent", style="bold cyan")
        table.add_column("Specialty", style="yellow")
        table.add_column("Status", style="green")
        
        for agent in self.orchestrator.agents:
            table.add_row(
                agent.name,
                agent.specialty,
                "✓ Ready"
            )
        
        console.print(table)
        console.print(f"\n[green]✓[/green] Successfully initialized {len(self.orchestrator.agents)} agents!\n")
    
    def set_research_topic(self):
        """Set the research topic"""
        console.print("\n[bold cyan]Research Topic Setup[/bold cyan]\n")
        
        topic = Prompt.ask(
            "[yellow]Enter the research topic[/yellow]",
            default="Advances in Transformer Architectures"
        )
        
        self.orchestrator.set_research_topic(topic)
        
        console.print(Panel(
            f"[white]{topic}[/white]",
            title="Research Topic Set",
            border_style="green",
            box=box.ROUNDED
        ))
    
    def brainstorm_session(self):
        """Conduct brainstorming session"""
        if not self.orchestrator.agents:
            console.print("[red]Error: Initialize team first![/red]")
            return
        
        if not self.orchestrator.research_topic:
            console.print("[red]Error: Set research topic first![/red]")
            return
        
        console.print("\n[bold cyan]Starting Brainstorming Session...[/bold cyan]\n")
        
        rounds = int(Prompt.ask("Number of brainstorming rounds", default="2"))
        
        with console.status("[bold green]Agents are brainstorming...") as status:
            results = self.orchestrator.conduct_brainstorm_session(rounds)
        
        console.print("\n[bold green]Brainstorming Complete![/bold green]\n")
        
        for i, idea in enumerate(results[-6:], 1):  # Show last 6 ideas
            agent_name = idea.split(']:')[0].replace('[', '')
            content = idea.split(']: ', 1)[1] if ']: ' in idea else idea
            
            console.print(Panel(
                content,
                title=f"{agent_name} - Idea {i}",
                border_style="cyan",
                box=box.ROUNDED
            ))
    
    def conduct_research(self):
        """Conduct research phase"""
        if not self.orchestrator.agents:
            console.print("[red]Error: Initialize team first![/red]")
            return
        
        console.print("\n[bold cyan]Research Phase[/bold cyan]\n")
        
        queries_input = Prompt.ask(
            "Enter search queries (comma-separated)",
            default="transformer architecture,attention mechanism"
        )
        
        queries = [q.strip() for q in queries_input.split(',')]
        
        with console.status("[bold green]Conducting research..."):
            results = self.orchestrator.conduct_research_phase(queries)
        
        console.print("\n[bold green]Research Complete![/bold green]\n")
        console.print(f"Performed {len(queries)} searches")
    
    def structured_discussion(self):
        """Conduct structured discussion"""
        if not self.orchestrator.agents:
            console.print("[red]Error: Initialize team first![/red]")
            return
        
        console.print("\n[bold cyan]Structured Discussion[/bold cyan]\n")
        
        topic = Prompt.ask(
            "Discussion topic",
            default="Research methodology and approach"
        )
        
        rounds = int(Prompt.ask("Number of discussion rounds", default="2"))
        
        with console.status("[bold green]Agents are discussing..."):
            discussion = self.orchestrator.structured_discussion(topic, rounds)
        
        console.print("\n[bold green]Discussion Complete![/bold green]\n")
        
        for message in discussion[-4:]:  # Show last 4 messages
            agent_name = message.split(']:')[0].replace('[', '')
            content = message.split(']: ', 1)[1] if ']: ' in message else message
            
            console.print(Panel(
                content[:500] + "..." if len(content) > 500 else content,
                title=agent_name,
                border_style="blue",
                box=box.ROUNDED
            ))
    
    def view_agent_status(self):
        """View status of all agents"""
        if not self.orchestrator.agents:
            console.print("[red]Error: No agents initialized![/red]")
            return
        
        table = Table(title="Agent Status Dashboard", box=box.DOUBLE_EDGE)
        table.add_column("Agent", style="cyan", width=15)
        table.add_column("Specialty", style="yellow", width=30)
        table.add_column("Conversations", style="green", justify="right")
        table.add_column("Notes", style="green", justify="right")
        table.add_column("Improvements", style="magenta", justify="right")
        table.add_column("Prompt Length", style="blue", justify="right")
        
        for agent in self.orchestrator.agents:
            summary = agent.get_summary()
            table.add_row(
                summary['name'],
                summary['specialty'],
                str(summary['conversations']),
                str(summary['research_notes']),
                str(summary['improvements']),
                str(summary['system_prompt_length'])
            )
        
        console.print("\n")
        console.print(table)
        console.print()
    
    def trigger_improvements(self):
        """Trigger self-improvement for all agents"""
        if not self.orchestrator.agents:
            console.print("[red]Error: No agents initialized![/red]")
            return
        
        console.print("\n[bold cyan]Triggering Self-Improvement...[/bold cyan]\n")
        
        with console.status("[bold yellow]Agents are improving themselves..."):
            results = self.orchestrator.trigger_self_improvement()
        
        console.print("\n[bold green]Self-Improvement Complete![/bold green]\n")
        
        for agent_name, result in results:
            console.print(Panel(
                result,
                title=f"{agent_name} Improvement",
                border_style="magenta",
                box=box.ROUNDED
            ))
    
    def check_satisfaction(self):
        """Check agent satisfaction levels"""
        if not self.orchestrator.agents:
            console.print("[red]Error: No agents initialized![/red]")
            return
        
        console.print("\n[bold cyan]Evaluating Satisfaction Levels...[/bold cyan]\n")
        
        with console.status("[bold green]Agents are evaluating..."):
            scores = self.orchestrator.evaluate_satisfaction()
        
        table = Table(title="Satisfaction Scores", box=box.HEAVY)
        table.add_column("Agent", style="cyan")
        table.add_column("Score", style="yellow", justify="center")
        table.add_column("Status", style="white")
        
        for agent_name, score in scores.items():
            status = "🟢 Satisfied" if score >= 8 else "🟡 Neutral" if score >= 6 else "🔴 Needs More"
            table.add_row(agent_name, str(score) + "/10", status)
        
        avg_score = sum(scores.values()) / len(scores)
        
        console.print(table)
        console.print(f"\n[bold]Average Satisfaction:[/bold] {avg_score:.1f}/10")
        
        if avg_score >= 8:
            console.print("[green]✓ Team is ready to generate paper![/green]\n")
        else:
            console.print("[yellow]⚠ Consider more research/discussion before generating paper[/yellow]\n")
    
    def generate_paper(self):
        """Generate the final research paper"""
        if not self.orchestrator.agents:
            console.print("[red]Error: No agents initialized![/red]")
            return
        
        if not self.orchestrator.research_topic:
            console.print("[red]Error: Set research topic first![/red]")
            return
        
        console.print("\n[bold cyan]Generating Research Paper...[/bold cyan]\n")
        
        confirm = Confirm.ask("This will generate a LaTeX paper. Continue?")
        if not confirm:
            return
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
        ) as progress:
            task = progress.add_task("Generating sections...", total=100)
            
            progress.update(task, advance=20, description="Generating title & abstract...")
            time.sleep(0.5)
            
            progress.update(task, advance=20, description="Writing introduction...")
            time.sleep(0.5)
            
            progress.update(task, advance=20, description="Compiling methodology...")
            time.sleep(0.5)
            
            progress.update(task, advance=20, description="Writing results...")
            time.sleep(0.5)
            
            filename = self.orchestrator.compile_final_paper()
            
            progress.update(task, advance=20, description="Finalizing LaTeX...")
        
        console.print("\n[bold green]✓ Research Paper Generated![/bold green]\n")
        console.print(Panel(
            f"[white]Paper saved to: {filename}[/white]\n\n"
            f"To compile:\n"
            f"[cyan]pdflatex {filename}[/cyan]",
            title="Success",
            border_style="green",
            box=box.DOUBLE
        ))
    
    def export_data(self):
        """Export session data"""
        if not self.orchestrator.agents:
            console.print("[red]Error: No agents initialized![/red]")
            return
        
        console.print("\n[bold cyan]Exporting Session Data...[/bold cyan]\n")
        
        filename = self.orchestrator.export_session_log()
        
        console.print(f"[green]✓ Session data exported to: {filename}[/green]\n")
    
    def view_discussion_log(self):
        """View discussion log"""
        if not self.orchestrator.discussion_log:
            console.print("[yellow]No discussions yet![/yellow]")
            return
        
        console.print("\n[bold cyan]Discussion Log[/bold cyan]\n")
        console.print(f"Total interactions: {len(self.orchestrator.discussion_log)}\n")
        
        # Show last 5 interactions
        for entry in self.orchestrator.discussion_log[-5:]:
            console.print(Panel(
                f"Type: {entry.get('type', 'N/A')}\n"
                f"Content: {str(entry.get('content', ''))[:300]}...",
                title=f"{entry['agent']} - Round {entry.get('round', 'N/A')}",
                border_style="dim",
                box=box.ROUNDED
            ))
    
    def run(self):
        """Main application loop"""
        self.display_banner()
        
        while self.running:
            self.display_menu()
            
            try:
                choice = Prompt.ask("\n[bold yellow]Select an option[/bold yellow]", default="0")
                
                if choice == "1":
                    self.initialize_team()
                elif choice == "2":
                    self.set_research_topic()
                elif choice == "3":
                    self.brainstorm_session()
                elif choice == "4":
                    self.conduct_research()
                elif choice == "5":
                    self.structured_discussion()
                elif choice == "6":
                    self.view_agent_status()
                elif choice == "7":
                    self.trigger_improvements()
                elif choice == "8":
                    self.check_satisfaction()
                elif choice == "9":
                    self.generate_paper()
                elif choice == "10":
                    self.export_data()
                elif choice == "11":
                    self.view_discussion_log()
                elif choice == "0":
                    console.print("\n[bold cyan]Thank you for using Multi-Agent Research System![/bold cyan]\n")
                    self.running = False
                else:
                    console.print("[red]Invalid option! Please try again.[/red]")
                
                if self.running and choice != "0":
                    Prompt.ask("\n[dim]Press Enter to continue[/dim]", default="")
                    console.clear()
                    self.display_banner()
                    
            except KeyboardInterrupt:
                console.print("\n\n[yellow]Interrupted by user[/yellow]")
                self.running = False
            except Exception as e:
                console.print(f"[red]Error: {str(e)}[/red]")


if __name__ == "__main__":
    ui = ResearchTerminalUI()
    ui.run()
