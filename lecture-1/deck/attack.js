/* Schematic MITRE ATT&CK Enterprise matrix for Lecture 1: the 15 tactics in matrix order, a curated
   subset of techniques per tactic (real IDs and names), and the current per-tactic technique counts so the
   "+N more" line is honest. Content from MITRE ATT&CK, Copyright The MITRE Corporation, used under the
   ATT&CK terms of use (https://attack.mitre.org/resources/legal-and-branding/terms-of-use/).
   Counts, names and tactic membership checked against attack.mitre.org and the v20.0 STIX bundle on 2026-10-13. */
window.ATTACK = {
  version: "Enterprise v20.0 (13 October 2026): 15 tactics, 227 techniques, 479 sub-techniques",
  tactics: [
    { id: "TA0043", name: "Reconnaissance", short: "Recon", count: 12, techniques: [
      { id: "T1595", name: "Active Scanning" },
      { id: "T1589", name: "Gather Victim Identity Information" },
      { id: "T1598", name: "Phishing for Information" },
      { id: "T1596", name: "Search Open Technical Databases" } ] },
    { id: "TA0042", name: "Resource Development", short: "Resource Dev.", count: 9, techniques: [
      { id: "T1583", name: "Acquire Infrastructure" },
      { id: "T1586", name: "Compromise Accounts" },
      { id: "T1587", name: "Develop Capabilities" },
      { id: "T1588", name: "Obtain Capabilities" },
      { id: "T1608", name: "Stage Capabilities" } ] },
    { id: "TA0001", name: "Initial Access", short: "Initial Access", count: 11, techniques: [
      { id: "T1566", name: "Phishing" },
      { id: "T1190", name: "Exploit Public-Facing Application" },
      { id: "T1078", name: "Valid Accounts", d: "Adversaries may obtain and abuse credentials of existing accounts as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion." },
      { id: "T1133", name: "External Remote Services" },
      { id: "T1195", name: "Supply Chain Compromise" },
      { id: "T1189", name: "Drive-by Compromise" } ] },
    { id: "TA0002", name: "Execution", short: "Execution", count: 22, techniques: [
      { id: "T1059", name: "Command and Scripting Interpreter", subs: [
        { id: "T1059.001", name: "PowerShell", d: "Adversaries may abuse PowerShell commands and scripts for execution." },
        { id: "T1059.003", name: "Windows Command Shell" },
        { id: "T1059.005", name: "Visual Basic" },
        { id: "T1059.007", name: "JavaScript" } ] },
      { id: "T1204", name: "User Execution" },
      { id: "T1047", name: "Windows Management Instrumentation" },
      { id: "T1053", name: "Scheduled Task/Job" },
      { id: "T1203", name: "Exploitation for Client Execution" } ] },
    { id: "TA0003", name: "Persistence", short: "Persistence", count: 22, techniques: [
      { id: "T1547", name: "Boot or Logon Autostart Execution" },
      { id: "T1053", name: "Scheduled Task/Job" },
      { id: "T1136", name: "Create Account" },
      { id: "T1505", name: "Server Software Component" },
      { id: "T1098", name: "Account Manipulation" } ] },
    { id: "TA0004", name: "Privilege Escalation", short: "Priv. Escalation", count: 13, techniques: [
      { id: "T1068", name: "Exploitation for Privilege Escalation", d: "Adversaries may exploit software vulnerabilities in an attempt to elevate privileges." },
      { id: "T1548", name: "Abuse Elevation Control Mechanism" },
      { id: "T1055", name: "Process Injection" },
      { id: "T1078", name: "Valid Accounts" },
      { id: "T1134", name: "Access Token Manipulation" } ] },
    { id: "TA0005", name: "Stealth (Defense Evasion until April 2026)", short: "Stealth", count: 31, techniques: [
      { id: "T1620", name: "Reflective Code Loading", d: "Adversaries may reflectively load code into a process in order to conceal the execution of malicious payloads." },
      { id: "T1027", name: "Obfuscated Files or Information", subs: [
        { id: "T1027.010", name: "Command Obfuscation", d: "Adversaries may obfuscate content during command execution to impede detection." } ] },
      { id: "T1218", name: "System Binary Proxy Execution" },
      { id: "T1055", name: "Process Injection" },
      { id: "T1574", name: "Hijack Execution Flow", subs: [
        { id: "T1574.001", name: "DLL", d: "Search-order hijacking and side-loading, merged into one sub-technique in April 2025." } ] },
      { id: "T1497", name: "Virtualization/Sandbox Evasion" } ] },
    { id: "TA0112", name: "Defense Impairment (new in April 2026)", short: "Defense Impairment", count: 18, techniques: [
      { id: "T1685", name: "Disable or Modify Tools", d: "Replaced Impair Defenses (T1562) in April 2026; its sub-techniques include disabling event logs and, since v20 in October 2026, impairing autonomous defenses.", subs: [
        { id: "T1685.001", name: "Disable or Modify Windows Event Log" },
        { id: "T1685.007", name: "Impair Autonomous Defenses" } ] },
      { id: "T1686", name: "Disable or Modify System Firewall" },
      { id: "T1688", name: "Safe Mode Boot" },
      { id: "T1689", name: "Downgrade Attack" },
      { id: "T1690", name: "Prevent Command History Logging" } ] },
    { id: "TA0006", name: "Credential Access", short: "Credential Access", count: 18, techniques: [
      { id: "T1003", name: "OS Credential Dumping" },
      { id: "T1110", name: "Brute Force" },
      { id: "T1555", name: "Credentials from Password Stores" },
      { id: "T1539", name: "Steal Web Session Cookie" },
      { id: "T1621", name: "Multi-Factor Authentication Request Generation" },
      { id: "T1528", name: "Steal Application Access Token" } ] },
    { id: "TA0007", name: "Discovery", short: "Discovery", count: 34, techniques: [
      { id: "T1082", name: "System Information Discovery" },
      { id: "T1083", name: "File and Directory Discovery", d: "Adversaries enumerate files and directories to find information of interest." },
      { id: "T1087", name: "Account Discovery" },
      { id: "T1018", name: "Remote System Discovery" },
      { id: "T1046", name: "Network Service Discovery" } ] },
    { id: "TA0008", name: "Lateral Movement", short: "Lateral Movement", count: 9, techniques: [
      { id: "T1021", name: "Remote Services", d: "Adversaries use valid accounts to log into a service that accepts remote connections, such as RDP, SMB, SSH or WinRM, and act as the logged-on user.", subs: [
        { id: "T1021.001", name: "Remote Desktop Protocol" },
        { id: "T1021.002", name: "SMB/Windows Admin Shares" },
        { id: "T1021.006", name: "Windows Remote Management" } ] },
      { id: "T1570", name: "Lateral Tool Transfer" },
      { id: "T1550", name: "Use Alternate Authentication Material" },
      { id: "T1080", name: "Taint Shared Content" } ] },
    { id: "TA0009", name: "Collection", short: "Collection", count: 17, techniques: [
      { id: "T1005", name: "Data from Local System", d: "Adversaries may search local sources (file systems, configuration files, databases, VM files, process memory) for sensitive data prior to exfiltration." },
      { id: "T1560", name: "Archive Collected Data", d: "An adversary may compress and/or encrypt data that is collected prior to exfiltration." },
      { id: "T1114", name: "Email Collection" },
      { id: "T1074", name: "Data Staged" },
      { id: "T1113", name: "Screen Capture" },
      { id: "T1039", name: "Data from Network Shared Drive" } ] },
    { id: "TA0011", name: "Command and Control", short: "C2", count: 18, techniques: [
      { id: "T1071", name: "Application Layer Protocol", subs: [
        { id: "T1071.001", name: "Web Protocols", d: "Adversaries communicate using application layer protocols associated with web traffic, such as HTTP and HTTPS, to blend in with existing traffic." } ] },
      { id: "T1573", name: "Encrypted Channel" },
      { id: "T1105", name: "Ingress Tool Transfer" },
      { id: "T1219", name: "Remote Access Tools", d: "An adversary may use legitimate remote access tools to establish an interactive command and control channel within a network. Sub-techniques since April 2025: IDE Tunneling, Remote Desktop Software, Remote Access Hardware." },
      { id: "T1572", name: "Protocol Tunneling" },
      { id: "T1090", name: "Proxy" } ] },
    { id: "TA0010", name: "Exfiltration", short: "Exfiltration", count: 10, techniques: [
      { id: "T1041", name: "Exfiltration Over C2 Channel", d: "Adversaries may steal data by exfiltrating it over an existing command and control channel." },
      { id: "T1567", name: "Exfiltration Over Web Service", subs: [
        { id: "T1567.002", name: "Exfiltration to Cloud Storage", d: "Adversaries exfiltrate data to a cloud storage service rather than over their primary command and control channel." } ] },
      { id: "T1048", name: "Exfiltration Over Alternative Protocol" },
      { id: "T1030", name: "Data Transfer Size Limits" },
      { id: "T1029", name: "Scheduled Transfer" } ] },
    { id: "TA0040", name: "Impact", short: "Impact", count: 15, techniques: [
      { id: "T1486", name: "Data Encrypted for Impact" },
      { id: "T1490", name: "Inhibit System Recovery" },
      { id: "T1489", name: "Service Stop" },
      { id: "T1485", name: "Data Destruction" },
      { id: "T1657", name: "Financial Theft" },
      { id: "T1498", name: "Network Denial of Service" } ] }
  ]
};
