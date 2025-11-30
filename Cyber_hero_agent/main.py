import re
import json

# -----------------------------

# AGENT FUNCTIONS

# -----------------------------

def alert_intake_agent(alert_text):
# Extract IPs
    ips = re.findall(r'\b(?:[0-9]{1,3}.){3}[0-9]{1,3}\b', alert_text)
# Extract usernames
    usernames = re.findall(r'user[s]? (\w+)', alert_text, flags=re.IGNORECASE)
    indicators = {
    "ips": ips,
    "usernames": usernames
    }
    return json.dumps(indicators)

def pattern_matching_agent(logs, indicators_json):
    indicators = json.loads(indicators_json)
    matches = []
    for line in logs.splitlines():
        for ip in indicators.get("ips", []):
            if ip in line:
                matches.append(line)
    for user in indicators.get("usernames", []):
        if user in line:
            matches.append(line)
    return matches

def severity_classifier_agent(matches):
    if not matches:
        severity = "Low"
        reasoning = "No matches found in logs."
    elif len(matches) < 3:
        severity = "Medium"
        reasoning = "Few matches found, may indicate suspicious activity."
    elif len(matches) < 6:
        severity = "High"
        reasoning = "Multiple matches found, likely malicious activity."
    else:
        severity = "Critical"
        reasoning = "Many matches found, immediate attention required."
    return severity, reasoning

def recommendation_agent(severity, matches):
    remediation = ""
    if severity in ["High", "Critical"]:
        remediation = (
        "1. Block suspicious IPs.\n"
        "2. Force password resets for affected users.\n"
        "3. Investigate related logs.\n"
        "4. Monitor network traffic.\n"
    )
    else:
        remediation = "Monitor the situation and review logs regularly."

    report = (
    f"Severity: {severity}\n"
    f"Matching logs:\n" + "\n".join(matches) + "\n\n"
    f"Recommended actions:\n{remediation}"
)
    return report


# -----------------------------

# MASTER ORCHESTRATOR

# -----------------------------

def triage_system(alert_text, logs):
    indicators = alert_intake_agent(alert_text)
    matches = pattern_matching_agent(logs, indicators)
    severity, reasoning = severity_classifier_agent(matches)
    report = recommendation_agent(severity, matches)
    report = f"{report}\nReasoning: {reasoning}"
    return report

# -----------------------------

# RUN EXAMPLE

# -----------------------------

if __name__ == "__main__":
    with open("alert.txt", "r") as f:
        real_alert = f.read().strip()
    with open("logs.txt", "r") as f:
        real_logs = f.read()

print(triage_system(real_alert, real_logs))
