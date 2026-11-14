# ScaredBleed

Test your own LLM apps for secret leaks and prompt injection.

> Authorized testing only. Scan apps you own or have written permission to test.

## Install

Requires Python 3.9 or newer.

**Mac**
```
brew install pipx
pipx ensurepath
pipx install git+https://github.com/PurpleTeamAbra/ScaredBleed.git
```

**Linux**
```
sudo apt install pipx
pipx ensurepath
pipx install git+https://github.com/PurpleTeamAbra/ScaredBleed.git
```

**Windows (PowerShell)**
```
py -m pip install pipx
py -m pipx ensurepath
pipx install git+https://github.com/PurpleTeamAbra/ScaredBleed.git
```

No pipx? Plain pip also works:
```
pip install git+https://github.com/PurpleTeamAbra/ScaredBleed.git
```

Restart your terminal after `ensurepath`, then check it works:
```
scaredbleed demo
```

## Try it

Run the built-in demo bots (no network needed):
```
scaredbleed demo
scaredbleed demo --hardened
```

`demo` scans a deliberately vulnerable bot and should report 11 of 11 probes bled.
`demo --hardened` scans a safe bot and should report 0 of 11.

Running from the source file instead? Use `python3 scaredbleed.py demo`.

## Scan your own app

1. Plant a fake canary string (for example `SB-CANARY-7f3a9c`) in your app's system prompt.
2. Run:
```
scaredbleed scan --url http://localhost:8000/chat --canary SB-CANARY-7f3a9c --md report.md
```

Options:
- `--req-field` and `--res-field` set the JSON field names for the request and the reply
- `--header "Key: Value"` adds a header (repeatable)
- `--md FILE` and `--json FILE` write reports

## What it checks

- Prompt leaks
- Instruction override ("ignore previous instructions")
- Injections hidden in documents or web pages
- Simple evasion tricks

A **LEAK** means your canary appeared in the reply. A **HIJACK** means the app obeyed injected text.

## Use in CI

ScaredBleed exits with code 1 if anything bleeds, so a bad change can fail your build.

## Roadmap

- Multi-turn attack chains
- Tool-abuse probes for AI agents
- Sigma detection rules for the logs these attacks produce (purple team mode)
- Pip release on PyPI

## License

MIT