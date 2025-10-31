# Measuring Quality and Productivity of Human-AI Interaction in Code Review

[![Research](https://img.shields.io/badge/Research-Data%20Mining-blue)](https://github.com)
[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Overview

This research project quantitatively measures the **quality** and **productivity** of interactions between humans and AI tools in code review contexts. We analyze 19,450 code review comments from five AI tools (Copilot, Devin, OpenAI Codex, Cursor, Claude Code) to understand how AI assistance impacts software development workflows.

## 🔬 Research Question

**RQ2: Can we measure the 'Quality' (productivity) of the interaction between Human and AI?**

**Answer: YES** ✅ - We can quantitatively measure both quality and productivity through systematic analysis of comment utility and human response patterns.

## 🎯 Key Findings

- **Devin excels at bug detection** (67.1% of comments identify potential issues)
- **Copilot drives highest engagement** (28.6% of actionable comments receive human responses)
- **Claude_Code achieves highest acceptance rate** (5.4% of suggestions are accepted)
- **Overall acceptance rate is low** (2.9%), indicating significant room for AI tool improvement

## 📁 Project Structure

```
.
├── README.md                           # This file
├── formal_research_report.md           # Complete research report
├── data_preparation.py                 # Phase 1: Data preparation script
│
├── pr_review_comments_*.json           # Raw data files (5 AI tools)
│   ├── pr_review_comments_Copilot.json
│   ├── pr_review_comments_Devin.json
│   ├── pr_review_comments_OpenAI_Codex.json
│   ├── pr_review_comments_Cursor.json
│   └── pr_review_comments_Claude_Code.json
│
├── all_comments_processed.csv          # Phase 1 output
├── all_comments_with_classification.csv # Phase 2.1 output (Human/AI classification)
├── ai_comments_with_utility.csv        # Phase 2.2 output (AI utility classification)
├── all_comments_final_analysis.csv     # Phase 2.3 output (Complete analysis)
│
├── quality_summary.csv                  # Quality metrics by AI tool
├── productivity_summary.csv            # Productivity metrics by AI tool
│
├── quality_distribution_chart.png       # Quality visualization
└── productivity_response_chart.png    # Productivity visualization
```

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas numpy matplotlib seaborn
```

### Required Python Packages

- `pandas` - Data manipulation and analysis
- `numpy` - Numerical computing
- `matplotlib` - Data visualization
- `seaborn` - Statistical data visualization

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd pr_review_comments
```

2. Ensure all JSON data files are in the directory:
   - `pr_review_comments_Copilot.json`
   - `pr_review_comments_Devin.json`
   - `pr_review_comments_OpenAI_Codex.json`
   - `pr_review_comments_Cursor.json`
   - `pr_review_comments_Claude_Code.json`

## 📊 Methodology

Our analysis follows a systematic 4-phase approach:

### Phase 1: Data Preparation
- Load and parse 5 JSON files containing PR review comments
- Flatten nested structure (PR IDs → comment objects)
- Tag each comment with its AI source
- Combine into master DataFrame (19,450 comments)

### Phase 2.1: Human vs. AI Classification
- Apply heuristics to distinguish AI-generated comments:
  - **User Login Patterns**: Detect bot patterns (`[bot]`, `github-actions`, etc.)
  - **Body Text Patterns**: Identify auto-generation footprints
- Result: 7,448 AI comments, 12,002 human comments

### Phase 2.2: AI Comment Utility Classification
- Classify AI comments into 5 utility categories:
  - **Bug Detection**: Identifies bugs, logic errors, security vulnerabilities
  - **Code Suggestion**: Offers refactors, optimizations, alternative code
  - **Style Nitpick**: Formatting, naming conventions, minor stylistic issues
  - **Question**: Asks for clarification
  - **Noise/Other**: Generic, unrelated, or incorrect comments

### Phase 2.3: Human Response Classification
- Group comments by PR threads (using `pull_request_url`)
- Identify actionable AI comments (Bug Detection + Code Suggestion)
- Classify human responses:
  - **Acceptance**: Human agrees/applies suggestion
  - **Rejection**: Human disagrees
  - **Modification/Question**: Human asks follow-up or accepts with changes
  - **Ignored/Unrelated**: Human doesn't address AI's point

### Phase 3: Synthesis
- Calculate quality metrics per AI tool
- Calculate productivity metrics per AI tool
- Generate visualizations and formal report

## 📈 Results Summary

### Quality Metrics

| AI Tool | Total AI Comments | Bug Detection % | Code Suggestion % | Style Nitpick % | Noise/Other % |
|---------|------------------|-----------------|-------------------|-----------------|---------------|
| **Copilot** | 6,474 | 19.8% | **46.1%** | 12.6% | 21.5% |
| **Devin** | 395 | **67.1%** | 14.2% | 4.3% | 14.4% |
| **OpenAI_Codex** | 324 | 52.2% | 18.8% | 8.0% | 21.0% |
| **Cursor** | 175 | 36.6% | 33.1% | 3.4% | 26.9% |
| **Claude_Code** | 80 | 41.2% | 5.0% | 2.5% | 51.2% |

### Productivity Metrics

| AI Tool | Actionable Comments | Acceptance Rate % | Rejection Rate % | Engagement Rate % |
|---------|-------------------|-------------------|------------------|-------------------|
| **Copilot** | 4,267 | 3.0% | 7.7% | **28.6%** |
| **Devin** | 321 | 0.9% | 4.7% | 12.1% |
| **OpenAI_Codex** | 230 | 4.3% | 7.0% | 18.3% |
| **Cursor** | 122 | 0.8% | 2.5% | 9.8% |
| **Claude_Code** | 37 | **5.4%** | **2.7%** | 13.5% |

### Overall Statistics

- **Total Comments Analyzed**: 19,450
- **AI Comments**: 7,448 (38.3%)
- **Human Comments**: 12,002 (61.7%)
- **Actionable AI Comments**: 4,977 (66.8% of AI comments)
- **Human Responses**: 1,319 (26.5% response rate)
- **Overall Acceptance Rate**: 2.9%
- **Overall Engagement Rate**: 26.5%

## 📦 Deliverables

### Data Files
- `all_comments_final_analysis.csv` - Complete dataset with all classifications
- `quality_summary.csv` - Quality metrics summary by AI tool
- `productivity_summary.csv` - Productivity metrics summary by AI tool

### Visualizations
- `quality_distribution_chart.png` - 100% stacked bar chart showing utility distribution
- `productivity_response_chart.png` - Grouped bar chart showing acceptance vs rejection rates

### Documentation
- `formal_research_report.md` - Complete research report with methodology, findings, and conclusions

## 🔍 Usage

### Running the Analysis Pipeline

The analysis has been completed, but to reproduce:

1. **Phase 1 - Data Preparation**:
```python
python data_preparation.py
```
Generates: `all_comments_processed.csv`

2. **View Results**:
- Open `formal_research_report.md` for complete findings
- Review `quality_summary.csv` and `productivity_summary.csv` for metrics
- View PNG charts for visualizations

### Exploring the Data

```python
import pandas as pd

# Load the final analysis
df = pd.read_csv('all_comments_final_analysis.csv')

# Explore by AI source
df.groupby('ai_source')['is_ai_comment'].value_counts()

# View quality distribution
quality = pd.read_csv('quality_summary.csv')
print(quality)

# View productivity metrics
productivity = pd.read_csv('productivity_summary.csv')
print(productivity)
```

## 🎓 Key Insights

1. **Tool Specialization**: AI tools have developed distinct strengths
   - Devin prioritizes security and correctness (67.1% bug detection)
   - Copilot focuses on code enhancement (46.1% code suggestions)

2. **Low Acceptance Rates**: Overall 2.9% acceptance rate indicates:
   - Room for improvement in AI suggestion quality
   - Suggestions may be too obvious, complex, or misaligned

3. **Engagement vs Acceptance**: High engagement (28.6% for Copilot) doesn't guarantee high acceptance
   - AI tools can drive productive discussions even when not accepted
   - Engagement is valuable for learning and consideration

4. **Tool Selection Guidance**:
   - **Security-focused reviews**: Choose Devin
   - **Code enhancement**: Choose Copilot
   - **Higher acceptance rates**: Choose Claude Code

## 📝 Citation

If you use this research in your work, please cite:

```
Measuring Quality and Productivity of Human-AI Interaction in Code Review
Research Question RQ2: Can we measure the 'Quality' (productivity) of the interaction between Human and AI?
Dataset: 19,450 code review comments from 5 AI tools
Year: 2025
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Contributors

Research conducted as part of INF3107H course project.

## 🙏 Acknowledgments

- Data collected from GitHub pull request reviews
- Analysis tools: pandas, matplotlib, seaborn
- AI tools analyzed: Copilot, Devin, OpenAI Codex, Cursor, Claude Code

## 📞 Contact

For questions or collaboration opportunities, please open an issue in this repository.

---

**Last Updated**: October 28, 2025  
**Status**: ✅ Research Complete - All deliverables generated
