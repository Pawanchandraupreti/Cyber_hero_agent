#🛡️ AI-Powered Cybersecurity Incident Triage Agent System

This project is my submission for the Google AI Agents Intensive Capstone Project (Nov 2025) under the Freestyle Track.
It automates cybersecurity alert triage using multi-agent orchestration, parallel AI agents, OSINT tools, log analysis, memory, and observability.

#🎯 Problem Statement

Security analysts spend too much time manually interpreting alerts, checking OSINT sources, verifying indicators, and correlating logs.
This leads to:

Slower incident response

Higher chance of missing real threats

Wasted analyst time on false positives

#💡 Solution Statement

I built an AI-powered multi-agent triage system that automatically:

Extracts indicators (IP, URL, hashes, usernames)

Looks up OSINT using Google Search Tool

Matches patterns across log files using Python code execution

Classifies severity using a reasoning model

Generates a complete triage report with remediation steps

This system uses:

Sequential agents for triage flow

Parallel agents (Threat Intel Agent + Log Pattern Agent)

Google tools (Search + Code Execution)

Session memory for multi-turn context

Observability: tracing, logging, metrics

It reduces triage time from minutes to seconds.

#🧠 System Architecture

##🔹 Agents Used
###1. Alert Intake Agent

Cleans the alert text

Extracts indicators (IPs, URLs, hashes, usernames)

Stores extracted data in session memory

###2. Threat Intelligence Agent (Parallel Agent 1)

Uses Google Search Tool

Investigates reputation of indicators

Fetches OSINT results

Runs concurrently with Pattern Matching Agent

###3. Pattern Matching Agent (Parallel Agent 2)

Uses Code Execution Tool

Runs a custom Python script

Matches indicators in log files

Extracts suspicious patterns

###4. Severity Classifier Agent

Consumes intel + log patterns

Scores severity as: Low / Medium / High / Critical

Explains reasoning

###5. Recommendation Agent

Produces remediation actions

Creates final triage report

Saves report in session memory

##🔹 Tools Used
Tool	Purpose
Google Search Tool	OSINT, indicator reputation
Code Execution Tool	Custom log parsing & pattern matching
MCP-Compatible Tools	File system (optional)
##🔹 Memory System

Using InMemorySessionService to store:

Original alert

Extracted indicators

Threat intel results

Log pattern matches

Final report

Memory allows multi-turn triage if needed.

##🔹 Observability

Included:

@trace() decorator around each agent

Console logs for every step

Execution time per agent

Complete trace span for the whole workflow
