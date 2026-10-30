param(
    [string]$BaseRef = "49e5d9b"   # compares current working tree against this commit/ref
)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$diff = git diff $BaseRef

if (-not $diff) {
    Write-Host "No diff found against $BaseRef"
    exit
}

$prompt = @"
Summarize this git diff as a concise pull-request description for a reviewer. Structure it as:

**What changed:** 2-3 sentences, plain language
**Files touched:** bullet list, one line each on what changed in that file
**Anything to double-check:** call out if the diff touches more than what a narrow change would suggest (e.g. production code changed alongside tests, when only tests were expected)

Diff:
$diff
"@

$body = @{
    messages = @(
        @{ role = "system"; content = "You write accurate, concise PR summaries for engineers reviewing a diff. You flag scope creep when you see it. Use only plain ASCII punctuation - regular hyphens, not em dashes or curly quotes." },
        @{ role = "user"; content = $prompt }
    )
    max_completion_tokens = 500
} | ConvertTo-Json -Depth 5

$aoaiUrl = "$($env:AOAI_ENDPOINT)/openai/deployments/gpt-5.4-mini/chat/completions?api-version=2024-10-21"
$result = Invoke-RestMethod -Uri $aoaiUrl -Headers @{ "api-key" = $env:AOAI_KEY } -Method Post -ContentType "application/json" -Body $body

$summary = $result.choices[0].message.content
Write-Host "`n--- PR SUMMARY ---`n$summary"
$summary | Out-File "pr-summary.md"