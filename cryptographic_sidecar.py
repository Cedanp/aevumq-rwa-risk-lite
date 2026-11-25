import hashlib, json, time
class CryptographicSidecar:
    def __init__(self, chain_file="/mnt/c/AevumQ/audit_chain.jsonl"):
        self.chain_file = chain_file
    def _last_hash(self):
        try:
            with open(self.chain_file, "r") as f:
                lines = f.readlines()
                return json.loads(lines[-1])["hash"] if lines else "0"*64
        except FileNotFoundError:
            return "0"*64
    def record_event(self, agent_id, tool_name, payload_summary, risk_score=0.0):
        prev = self._last_hash()
        ts = time.time()
        raw = f"{prev}|{ts}|{agent_id}|{tool_name}|{payload_summary}|{risk_score}".encode()
        curr_hash = hashlib.sha256(raw).hexdigest()
        entry = {"ts": ts, "agent_id": agent_id, "tool": tool_name, "risk": risk_score, "prev_hash": prev, "hash": curr_hash}
        with open(self.chain_file, "a") as f:
            f.write(json.dumps(entry) + "\n")
        return entry
