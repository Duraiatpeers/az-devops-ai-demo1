# ai-dev-demo

Seed project for the Module 7 (AI-Assisted Development, Code Review & Test
Generation) case study. `order_totals.py` has a deliberate gap: it never
validates `quantity` or `unit_price`, so a negative quantity silently
*shrinks* the total instead of being rejected. That's the edge case Copilot's
generated tests are meant to surface.

## Setup

```powershell
cd ai-dev-demo
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
```

If `Activate.ps1` is blocked by execution policy, run
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` first, just for
that session.

## Push to Azure Repos

```powershell
git init
git add .
git commit -m "Initial commit: calculate_total with seed test"
git remote add origin https://dev.azure.com/<org>/<project>/_git/<project>
git push -u origin main
```
