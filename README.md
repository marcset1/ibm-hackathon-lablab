# BobFlow — AI Developer Workflow CLI

> From idea to living codebase — powered by IBM Bob

BobFlow brings IBM Bob into your existing developer workflow.
No new interface. No context switching. Just simple commands.

## The Problem
Developers lose hours on repetitive tasks: understanding legacy code,
writing tests, updating docs, reviewing quality. BobFlow automates
all of this using IBM Bob as the AI engine.

## Commands

| Command | What IBM Bob does |
|---|---|
| `bobflow explain <path>` | Reads your codebase, explains it, suggests next steps |
| `bobflow scaffold <feature>` | Builds a new feature from a description |
| `bobflow test <file>` | Generates unit tests for any file |
| `bobflow docs <path>` | Creates or updates documentation |
| `bobflow review <path>` | Reviews code quality and security |

## Installation

```bash
# 1. Install IBM Bob Shell (required)
curl -fsSL https://bob.ibm.com/download/bobshell.sh | bash

# 2. Install BobFlow
pip install pipx && pipx ensurepath
pipx install git+https://github.com/sachasmartdot/bobflow.git

# 3. Verify
bobflow --help
```

## Live Demo — AI-FitShop

We use BobFlow to upgrade an incomplete e-commerce project
(AI-FitShop) from a hardcoded chatbot to an LLM-powered
shopping assistant in 3 commands:

```bash
# Step 1 — Understand what exists
bobflow explain . --depth detailed

# Step 2 — Build missing AI feature
bobflow scaffold ai-agent --stack "Python FastAPI" \
  --idea "LLM shopping assistant with sizing recommendations"

# Step 3 — Review generated code
bobflow review .
```

## Architecture

Developer
↓
BobFlow CLI (Python + Click)
↓
Bob Shell (IBM Bob)
↓
Generated code / analysis / tests / docs

## IBM Bob Hackathon 2026
Built at lablab.ai IBM Bob Hackathon | Theme: "Turn idea into impact faster"
