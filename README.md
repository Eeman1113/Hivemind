# 🤖 Multi-Agent AI Research System

A sophisticated multi-agent system powered by Ollama where AI agents collaborate as research experts, discuss topics, search for information, and autonomously generate research papers in LaTeX format with diagrams.

## ✨ Key Features

- **Multiple Specialized Agents**: Each agent specializes in different AI domains
- **Self-Improving Agents**: Agents can edit and improve their own system prompts
- **Collaborative Research**: Agents brainstorm, discuss, and debate together
- **Web Search Integration**: Ground research in real information
- **LaTeX Paper Generation**: Automatically generate formatted research papers
- **TikZ Diagrams**: Papers include automatically generated diagrams
- **Satisfaction Metrics**: Agents evaluate when research is complete
- **Beautiful Terminal UI**: Rich terminal interface with colors and formatting

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Terminal UI (Rich)                   │
├─────────────────────────────────────────────────────────┤
│                Research Orchestrator                    │
├──────────────┬──────────────┬──────────────────────────┤
│   Agent 1    │   Agent 2    │   Agent 3 ... Agent N   │
│ (Dr. Neural) │ (Dr. Ethics) │   (Specialists)         │
└──────────────┴──────────────┴──────────────────────────┘
        │              │                 │
        └──────────────┴─────────────────┘
                       │
        ┌──────────────┴──────────────┐
        │                              │
   ┌────▼────┐                  ┌─────▼────┐
   │ Search  │                  │  LaTeX   │
   │  Tool   │                  │Generator │
   └─────────┘                  └──────────┘
```

## 📋 Prerequisites

1. **Ollama**: Install from [ollama.ai](https://ollama.ai)
2. **Python 3.8+**: Make sure Python is installed
3. **LaTeX**: For compiling the generated papers (optional)

## 🚀 Installation

### Step 1: Install Ollama

```bash
# MacOS/Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Or visit https://ollama.ai for other platforms
```

### Step 2: Pull Required Model

```bash
ollama pull llama3.1
```

You can also use other models like:
- `llama3.2`
- `mistral`
- `codellama`
- `mixtral`

### Step 3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install ollama rich requests
```

### Step 4: (Optional) Install LaTeX

For compiling PDFs:

**Ubuntu/Debian:**
```bash
sudo apt-get install texlive-full
```

**MacOS:**
```bash
brew install basictex
```

**Windows:**
Download from [MiKTeX](https://miktex.org/) or [TeX Live](https://www.tug.org/texlive/)

## 🎮 Usage

### Start the System

```bash
python main.py
```

### Workflow

1. **Initialize Research Team** (Option 1)
   - Creates 5 specialized AI agents:
     - Dr. Neural: Neural Networks & Deep Learning
     - Dr. Ethics: AI Ethics & Safety
     - Dr. NLP: Natural Language Processing
     - Dr. Vision: Computer Vision
     - Dr. RL: Reinforcement Learning

2. **Set Research Topic** (Option 2)
   - Define what you want to research
   - Example: "Advances in Transformer Architectures"

3. **Brainstorming Session** (Option 3)
   - Agents generate and discuss ideas
   - Multiple rounds of collaborative ideation

4. **Conduct Research** (Option 4)
   - Agents search for relevant papers and information
   - Analyze and synthesize findings

5. **Structured Discussion** (Option 5)
   - Agents debate specific topics
   - Challenge and build upon each other's ideas

6. **Self-Improvement** (Option 7)
   - Agents analyze their performance
   - Automatically improve their system prompts
   - Become more effective over time

7. **Check Satisfaction** (Option 8)
   - Agents rate research quality (1-10)
   - System checks if consensus is reached
   - Target: 8/10 average satisfaction

8. **Generate Research Paper** (Option 9)
   - Compiles all research into LaTeX format
   - Includes sections: Abstract, Introduction, Methodology, Results, Conclusion
   - Generates TikZ diagrams automatically
   - Outputs `research_paper.tex`

9. **Compile PDF** (External)
   ```bash
   pdflatex research_paper.tex
   ```

## 📁 Project Structure

```
.
├── main.py              # Terminal UI and main application
├── orchestrator.py      # Multi-agent coordination
├── agent.py             # Individual agent implementation
├── search_tool.py       # Web search functionality
├── latex_generator.py   # LaTeX paper generation
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🔧 Configuration

### Change Model

Edit in `main.py` or when initializing agents:

```python
orchestrator.add_agent("Dr. Custom", "Your Specialty", model="llama3.2")
```

### Adjust Satisfaction Threshold

In `orchestrator.py`:

```python
self.target_satisfaction = 8  # Change from 8 to your preference (1-10)
```

### Add Custom Agents

```python
orchestrator.add_agent(
    name="Dr. Quantum",
    specialty="Quantum Machine Learning",
    model="llama3.1"
)
```

## 🎯 Example Session

```
╔═══════════════════════════════════════════════════════════════╗
║        🤖 MULTI-AGENT AI RESEARCH SYSTEM 🤖                  ║
╚═══════════════════════════════════════════════════════════════╝

1. Initialize Team
2. Set Topic: "Attention Mechanisms in Vision Transformers"
3. Brainstorm (3 rounds)
4. Research Phase
5. Discussion: "Scalability vs Accuracy Trade-offs"
6. Check Satisfaction: 8.2/10 ✓
7. Self-Improvement: All agents improved prompts
8. Generate Paper → research_paper.tex
9. Compile: pdflatex research_paper.tex
```

## 🤖 Agent Self-Improvement

Agents can modify their own system prompts! Each agent:

1. **Analyzes** its conversation history
2. **Identifies** areas for improvement
3. **Generates** an enhanced system prompt
4. **Updates** itself automatically

Example improvement cycle:
```
Initial Prompt (500 chars) →
Improved v1 (650 chars, +30% detail) →
Improved v2 (700 chars, +focus on critical thinking) →
Improved v3 (750 chars, +collaboration emphasis)
```

## 📊 Features in Detail

### Brainstorming
- Multiple rounds of idea generation
- Each agent contributes from their expertise
- Ideas build upon previous suggestions

### Research Phase
- Integration with arXiv API
- Web search capabilities
- Agents analyze and synthesize findings

### Structured Discussion
- Topic-focused debates
- Agents challenge each other's assumptions
- Critical thinking and peer review

### LaTeX Generation
- Professional paper formatting
- Automatic section generation
- TikZ diagrams for visualizations
- Bibliography support

## 🔍 Monitoring

View agent status anytime:
```
┌─────────────┬──────────────┬──────┬───────┬──────────────┐
│ Agent       │ Specialty    │ Conv │ Notes │ Improvements │
├─────────────┼──────────────┼──────┼───────┼──────────────┤
│ Dr. Neural  │ Deep Learning│  25  │   8   │      3       │
│ Dr. Ethics  │ AI Ethics    │  22  │   6   │      2       │
│ Dr. NLP     │ NLP          │  28  │  10   │      4       │
└─────────────┴──────────────┴──────┴───────┴──────────────┘
```

## 🐛 Troubleshooting

### Ollama Connection Error
```bash
# Make sure Ollama is running
ollama serve

# In another terminal
python main.py
```

### Model Not Found
```bash
# Pull the model first
ollama pull llama3.1
```

### LaTeX Compilation Issues
```bash
# Install missing packages
sudo apt-get install texlive-latex-extra texlive-pictures

# Or compile with different engine
xelatex research_paper.tex
```

### Slow Agent Responses
- Use smaller models: `llama3.1:8b` instead of `llama3.1:70b`
- Reduce context window in agent conversations
- Use GPU acceleration if available

## 🎨 Customization

### Change UI Colors

In `main.py`, modify styles:
```python
console.print("text", style="bold cyan")  # Change colors here
```

### Add New Research Specialties

```python
orchestrator.add_agent("Dr. BioAI", "Computational Biology + AI")
orchestrator.add_agent("Dr. Robotics", "Robot Learning")
```

### Customize LaTeX Template

Edit `latex_generator.py` → `generate_latex()` method

## 📝 Output Files

The system generates:
- `research_paper.tex` - LaTeX source
- `research_session.json` - Complete session log
- `research_paper.pdf` - Compiled paper (after pdflatex)

## 🚦 Best Practices

1. **Start with 2-3 brainstorm rounds** to generate ideas
2. **Conduct research** before detailed discussions
3. **Run discussions** on 2-3 focused topics
4. **Trigger self-improvement** after significant interactions
5. **Check satisfaction** before generating final paper
6. **Aim for 8+/10 satisfaction** for quality results

## 🔮 Advanced Features

### Custom Search Integration

Replace the search tool in `search_tool.py` with your preferred API:
- Google Search API
- Semantic Scholar
- PubMed
- Custom enterprise search

### Multi-Model Setup

Use different models for different agents:
```python
orchestrator.add_agent("Dr. Fast", "Quick Analysis", model="llama3.1:8b")
orchestrator.add_agent("Dr. Deep", "Detailed Research", model="llama3.1:70b")
```

### Distributed Agents

Modify `agent.py` to connect to remote Ollama instances for distributed computing.

## 🤝 Contributing

Ideas for enhancements:
- Integration with real search APIs
- Support for more LLM providers
- Enhanced diagram generation
- Multi-language support
- Collaborative editing interface
- Version control for agent prompts

## 📄 License

MIT License - Feel free to modify and distribute!

## 🙏 Acknowledgments

- **Ollama** for local LLM infrastructure
- **Rich** for beautiful terminal UI
- **LaTeX** for professional typesetting

## 📧 Support

For issues or questions:
1. Check Ollama is running: `ollama list`
2. Verify Python packages: `pip list`
3. Test with simple topic first
4. Review discussion logs for debugging

---

**Built with ❤️ using Ollama, Python, and AI**

*Let the agents research, discuss, improve, and create!*
