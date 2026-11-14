# ScaredBleed

Test your own LLM apps for secret leaks and prompt injection.

> Authorized testing only. Scan apps you own or have written permission to test.

## Try it
```
python3 scaredbleed.py demo
python3 scaredbleed.py demo --hardened
```

## Scan your own app
Plant a fake canary string in your app's system prompt, then:
```
python3 scaredbleed.py scan --url http://localhost:8000/chat --canary SB-CANARY-7f3a9c --md report.md
```

## What it checks
- Prompt leaks
- Instruction override ("ignore previous instructions")
- Injections hidden in documents or web pages
- Simple evasion tricks

Exits with code 1 if anything bleeds, so it works in CI.