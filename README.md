# Project Overview - Agent Shuttle 🛡️

AI-Powered Cybersecurity Incident Triage Agent System — a multi-agent system that automates alert triage using parallel AI agents, OSINT tools, log analysis, memory, and observability. This project was built as a capstone-style submission for the Google AI Agents Intensive (Freestyle Track).

Table of contents
- Problem Statement
- Solution Statement
- Architecture
- Essential Tools and Utilities
- Conclusion
- Value Statement
- Installation
- Running the Agent in ADK Web mode
- Project Structure

## Problem Statement
Security analysts spend large amounts of time manually:
- Interpreting alerts
- Checking OSINT sources for indicator reputation
- Verifying indicators and correlating logs

Consequences:
- Slower incident response
- Increased chance of missing real threats
- Wasted analyst time on false positives

## Solution Statement
A multi-agent AI triage system that automates end-to-end triage by:
- Extracting indicators (IP, URL, hashes, usernames)
- Looking up OSINT using search tools
- Matching patterns across log files via code execution
- Classifying severity with reasoning models
- Generating a complete triage report with remediation steps

The system orchestrates sequential and parallel agents, uses session memory for multi-turn context, and provides observability via tracing, logging, and metrics — reducing triage time from minutes to seconds.

## Architecture

### Agents Used
1. Alert Intake Agent
   - Cleans and normalizes alert text
   - Extracts indicators (IPs, URLs, hashes, usernames)
   - Stores extracted data in session memory

2. Threat Intelligence Agent (Parallel Agent 1)
   - Uses search / OSINT tools
   - Investigates reputation of indicators
   - Fetches and summarizes relevant OSINT results

3. Pattern Matching Agent (Parallel Agent 2)
   - Uses a code execution tool (Python)
   - Runs log-parsing scripts to match indicators in logs
   - Extracts suspicious patterns and contextual matches

4. Severity Classifier Agent
   - Consumes intel + log patterns
   - Scores severity: Low / Medium / High / Critical
   - Provides reasoning for the score

5. Recommendation Agent
   - Produces remediation actions and containment steps
   - Creates the final triage report and stores it in memory

### Tools Used
- Google Search Tool — OSINT, reputation lookups
- Code Execution Tool — custom log parsing & pattern matching
- MCP-Compatible utilities (optional) — file system access, connectors

### Memory System
- InMemorySessionService (or pluggable alternative)
- Stores:
  - Original alert text
  - Extracted indicators
  - Threat intel results
  - Log pattern matches
  - Final triage report
- Enables multi-turn workflows and analyst follow-ups

### Observability
- @trace() decorator wrapping each agent execution
- Console logs for each step
- Execution time metrics per agent
- A complete trace span that covers the entire triage workflow

## Essential Tools and Utilities
- Python 3.8+ (or compatible runtime for code execution tool)
- Access to a search/OSINT tool or API (Google Search Tool integration shown)
- Log files or log ingestion endpoint for pattern matching
- Optional: MCP-compatible extensions for file and environment integrations

## Conclusion
This multi-agent triage system demonstrates how combining agent orchestration, parallel processing, and automated OSINT/log analysis accelerates incident response and reduces false positives. The modular design allows adapting agents, tools, and scoring models to different environments.

## Value Statement
- Faster triage: seconds vs. minutes
- Consistent, explainable severity scoring
- Actionable remediation guidance for analysts
- Reusable agent components and observability for production readiness

## Installation
1. Clone the repo:
   git clone https://github.com/Pawanchandraupreti/Cyber_hero_agent.git
2. Change directory:
   cd Cyber_hero_agent
3. Create a virtual environment and install dependencies:
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
4. Configure credentials for any external tools (search APIs, etc.) via environment variables or config files.

## Running the Agent in ADK Web mode
- Ensure ADK / agent runtime is installed and configured.
- Start the web runtime (example command; adapt to your ADK setup):
  export ADK_CONFIG=path/to/config
  adk web --project ./ --port 8080
- Use the web UI to submit an alert or call the agent API endpoint to initiate a triage session.
- Check logs and traces in the console or configured observability backend.

## Project Structure
- agents/ — agent implementations (intake, intel, pattern, classifier, recommendations)
- tools/ — integrations (search tool wrappers, code execution helpers)
- memory/ — session memory implementations (InMemorySessionService, adapters)
- observability/ — tracing, logging, metrics utilities
- examples/ — example alerts, test logs, and sample configurations
- README.md — this file

If you want, I can:
- Add a generated Table of Contents with anchors
- Convert the "Project Structure" list into an actual directory tree that matches the repo
- Create an installation script or example config file for ADK integration
