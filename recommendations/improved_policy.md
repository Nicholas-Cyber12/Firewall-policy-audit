# Improved Firewall Policy Proposal

## Policy Principles
- Apply **least privilege** to all services
- Only allow traffic that is explicitly needed
- Block unused ports and protocols
- Deny by default unless explicitly allowed

---

### Proposed Ruleset:

- ALLOW 192.168.1.0/24 -> ANY on port 443
- ALLOW 192.168.1.10 -> 10.0.0.5 on port 22
- DENY ANY -> ANY on port 23
- DENY ALL

• Removed duplicate and overly broad rules
• Disabled Telnet
• Introduced explicit DENY ALL to enforce default deny
