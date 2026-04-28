# Praxis

**Your personal AI operations team — 4 specialized agents that coordinate to build software with you.**

## What It Is

Praxis is a **local, file-based multi-agent system** that runs inside Claude Code. No APIs, no cloud, no costs. Just you and your team of AI specialists.

## The Team

| Agent | Role | You Say |
|-------|------|---------|
| **Manager** | Strategic coordinator, your direct report | `@manager` |
| **Business Analyst** | Requirements, user stories | `@ba` |
| **Software Engineer** | Architecture, code, tests | `@engineer` |
| **Ops Specialist** | Infrastructure, deployment | `@ops` |

## How It Works

```
You: @manager Build user notifications

Manager (Claude as Manager):
  1. Creates session in praxis/sessions/
  2. Briefs BA, Engineer, Ops
  3. Reports: "BA on requirements, Engineer spiking architecture..."

You: @ba What are the requirements?

BA (Claude as BA):
  "3 user stories identified..."

You: @engineer Why SQS over Redis?

Engineer (Claude as Engineer):
  "SQS has DLQ, managed, better for scale..."
```

Each agent has a **template** (markdown file) that defines their role, responsibilities, and how they collaborate. Claude switches personas based on who you address.

## Key Features

**🎯 Project-Based**  
Each project gets its own sessions folder. Work stays organized by codebase.

**🧠 Remembers**  
`praxis/memory/patterns.yml` stores what worked and what failed across sessions.

**📝 Tracks Everything**  
Every session has state files:
- `assignments.yml` — Who's doing what
- `briefing.md` — Manager's report to you
- `decisions.yml` — What was decided and why
- `conflicts.yml` — Active disputes

**🔧 Customizable**  
Edit templates or create new agents with `python praxis/custom/generate-agent.py`

## Why Use It

| Without Praxis | With Praxis |
|----------------|-------------|
| One generic AI assistant | 4 specialists with domain expertise |
| Context gets lost | Sessions persist across conversations |
| You do the coordination | Manager coordinates for you |
| Same mistakes repeated | System remembers patterns |
| "Build this" → vague result | Structured process → better outcomes |

## Quick Start

```bash
# 1. Start session
@manager Build [your feature]

# 2. Talk to any agent
@ba Requirements?
@engineer Architecture?
@ops Deployment?

# 3. Make decisions when escalated
"Go with SQS"

# 4. Review progress
cat praxis/sessions/[session]/briefing.md
```

## Use Cases

- **New feature** → Manager coordinates full build
- **Refactoring** → Engineer plans, Manager sequences
- **Production issue** → Ops investigates, Engineer fixes
- **Technical decision** → All agents debate, you choose
- **Learning** → BA documents, Engineer prototypes

## The Philosophy

**Action over theory.** Praxis means "doing" — not just planning, not just coding, but the integrated practice of building software well.

Your team practices:
- **Reflection** — Agents review their own work
- **Learning** — Remembers across sessions
- **Coordination** — Specialized roles, shared context
- **Accountability** — Decisions logged, state tracked

## Files You Care About

```
praxis/
├── templates/              # Agent definitions (edit these)
│   ├── manager.md
│   ├── business-analyst.md
│   ├── software-engineer.md
│   └── ops-specialist.md
├── sessions/               # Your active work (gitignored)
│   └── 2025-01-feature/
│       ├── briefing.md    # ← Read this for status
│       ├── assignments.yml
│       └── decisions.yml
├── memory/
│   └── patterns.yml       # ← Learnings across sessions
└── custom/
    └── generate-agent.py  # ← Make new agents
```

## In One Sentence

**Praxis is your personal AI operations team that coordinates specialized agents to build software with structure, memory, and accountability.**

---

**Try it:** `@manager I want to build [your idea]`
