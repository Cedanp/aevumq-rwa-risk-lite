FROM python:3.12-slim
WORKDIR /app
COPY . .
CMD ["python3", "-c", "import cryptographic_sidecar, hitl_policy_gate, aibom_annex4_generator; print('AevumQ EU AI Act MCP Sidecar Ready')"]
