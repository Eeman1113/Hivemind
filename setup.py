#!/usr/bin/env python3
"""
Setup and verification script for Multi-Agent Research System
Run this first to ensure everything is configured correctly
"""

import subprocess
import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        return True, f"Python {version.major}.{version.minor}.{version.micro}"
    return False, f"Python {version.major}.{version.minor}.{version.micro} (Need 3.8+)"


def check_ollama_installation():
    """Check if Ollama is installed"""
    try:
        result = subprocess.run(['ollama', '--version'], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        if result.returncode == 0:
            return True, result.stdout.strip()
        return False, "Not found"
    except FileNotFoundError:
        return False, "Not installed"
    except Exception as e:
        return False, str(e)


def check_ollama_running():
    """Check if Ollama service is running"""
    try:
        import ollama
        models = ollama.list()
        return True, "Running"
    except Exception as e:
        return False, str(e)


def check_required_model():
    """Check if required model is available"""
    try:
        import ollama
        models = ollama.list()
        model_names = [m['name'] for m in models.get('models', [])]
        
        required = "llama3.1"
        for name in model_names:
            if required in name:
                return True, f"Found: {name}"
        
        return False, "llama3.1 not found"
    except Exception as e:
        return False, str(e)


def check_python_packages():
    """Check if required Python packages are installed"""
    required_packages = {
        'ollama': 'ollama',
        'rich': 'rich',
        'requests': 'requests'
    }
    
    results = {}
    for package, import_name in required_packages.items():
        try:
            __import__(import_name)
            results[package] = (True, "Installed")
        except ImportError:
            results[package] = (False, "Not installed")
    
    return results


def install_packages():
    """Install required Python packages"""
    console.print("\n[yellow]Installing Python packages...[/yellow]\n")
    
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'],
                      check=True)
        console.print("[green]✓ Packages installed successfully![/green]\n")
        return True
    except subprocess.CalledProcessError:
        console.print("[red]✗ Failed to install packages[/red]\n")
        return False


def install_ollama_model():
    """Install required Ollama model"""
    console.print("\n[yellow]Pulling llama3.1 model (this may take a while)...[/yellow]\n")
    
    try:
        subprocess.run(['ollama', 'pull', 'llama3.1'], check=True)
        console.print("[green]✓ Model installed successfully![/green]\n")
        return True
    except subprocess.CalledProcessError:
        console.print("[red]✗ Failed to install model[/red]\n")
        return False


def run_verification():
    """Run complete system verification"""
    
    console.print("\n[bold cyan]╔═══════════════════════════════════════════╗[/bold cyan]")
    console.print("[bold cyan]║  Multi-Agent Research System - Setup     ║[/bold cyan]")
    console.print("[bold cyan]╚═══════════════════════════════════════════╝[/bold cyan]\n")
    
    # Create verification table
    table = Table(title="System Verification", show_header=True)
    table.add_column("Component", style="cyan", width=25)
    table.add_column("Status", style="white", width=15)
    table.add_column("Details", style="dim", width=30)
    
    issues = []
    
    # Check Python
    status, details = check_python_version()
    table.add_row(
        "Python Version",
        "[green]✓[/green]" if status else "[red]✗[/red]",
        details
    )
    if not status:
        issues.append(("Python", "Upgrade to Python 3.8 or higher"))
    
    # Check Ollama installation
    status, details = check_ollama_installation()
    table.add_row(
        "Ollama Installation",
        "[green]✓[/green]" if status else "[red]✗[/red]",
        details
    )
    if not status:
        issues.append(("Ollama", "Install from https://ollama.ai"))
    
    # Check Ollama running
    status, details = check_ollama_running()
    table.add_row(
        "Ollama Service",
        "[green]✓[/green]" if status else "[red]✗[/red]",
        details
    )
    if not status:
        issues.append(("Ollama Service", "Run 'ollama serve' in terminal"))
    
    # Check model
    status, details = check_required_model()
    table.add_row(
        "Required Model",
        "[green]✓[/green]" if status else "[yellow]⚠[/yellow]",
        details
    )
    model_missing = not status
    
    # Check packages
    packages = check_python_packages()
    all_packages_ok = all(status for status, _ in packages.values())
    
    package_status = "[green]✓[/green]" if all_packages_ok else "[red]✗[/red]"
    package_details = "All installed" if all_packages_ok else "Missing packages"
    
    table.add_row("Python Packages", package_status, package_details)
    
    if not all_packages_ok:
        for pkg, (status, _) in packages.items():
            if not status:
                issues.append((f"Package: {pkg}", "Run 'pip install -r requirements.txt'"))
    
    console.print(table)
    console.print()
    
    # Show issues
    if issues:
        console.print("[bold yellow]⚠ Issues Found:[/bold yellow]\n")
        for component, solution in issues:
            console.print(f"  [red]✗[/red] {component}")
            console.print(f"    [dim]→ {solution}[/dim]\n")
        
        # Offer to fix
        if not all_packages_ok:
            try:
                from rich.prompt import Confirm
                if Confirm.ask("\n[yellow]Install missing Python packages?[/yellow]"):
                    install_packages()
            except:
                pass
        
        if model_missing:
            try:
                from rich.prompt import Confirm
                if Confirm.ask("\n[yellow]Download llama3.1 model?[/yellow]"):
                    install_ollama_model()
            except:
                pass
    else:
        console.print(Panel(
            "[bold green]✓ All systems ready![/bold green]\n\n"
            "You can now run: [cyan]python main.py[/cyan]",
            title="Success",
            border_style="green"
        ))
    
    return len(issues) == 0


def show_quick_start():
    """Show quick start guide"""
    console.print("\n[bold cyan]Quick Start Guide:[/bold cyan]\n")
    
    commands = [
        ("Start the system", "python main.py"),
        ("Run automated demo", "python example.py"),
        ("Run minimal example", "python example.py minimal"),
        ("List Ollama models", "ollama list"),
        ("Pull a model", "ollama pull llama3.1"),
        ("Check Ollama status", "ollama ps"),
    ]
    
    for description, command in commands:
        console.print(f"  • {description}")
        console.print(f"    [cyan]$ {command}[/cyan]\n")


if __name__ == "__main__":
    try:
        all_ok = run_verification()
        
        if all_ok:
            show_quick_start()
        else:
            console.print("\n[yellow]Please resolve the issues above and run setup.py again.[/yellow]\n")
            
    except KeyboardInterrupt:
        console.print("\n\n[yellow]Setup interrupted by user[/yellow]\n")
    except Exception as e:
        console.print(f"\n[red]Setup error: {str(e)}[/red]\n")
