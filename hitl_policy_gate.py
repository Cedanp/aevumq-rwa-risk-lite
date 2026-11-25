import hashlib, time
HIGH_RISK_ACTIONS = {"approve_credit", "reject_candidate", "transfer_funds", "drop_table", "export_pii"}
def evaluate_policy(agent_id, action, amount_usd=0.0):
    blocked = action in HIGH_RISK_ACTIONS or amount_usd >= 1000.0
    token = hashlib.sha256(f"{agent_id}:{action}:{time.time()}".encode()).hexdigest()[:16]
    return {"allowed": not blocked, "requires_hitl": blocked, "approval_token": token if blocked else None, "article": "EU AI Act Art. 14"}
