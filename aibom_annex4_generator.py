import json, time
def generate_aibom(system_name, models, mcp_tools, risk_category="Annex III High-Risk"):
    doc = {
        "schema": "AevumQ-AI-BOM-v1.0",
        "generated_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "system_name": system_name,
        "regulatory_scope": ["EU AI Act (Reg. 2026/1744)", "Art. 50 Transparency (Dec 2026)", "Annex III High-Risk (Dec 2027)"],
        "risk_classification": risk_category,
        "foundation_models": models,
        "mcp_tools_inventory": mcp_tools,
        "human_oversight_art14": "Enabled via AevumQ HITL Policy Gate",
        "record_keeping_art12": "Enabled via SHA-256 Cryptographic Sidecar"
    }
    return json.dumps(doc, indent=2)
