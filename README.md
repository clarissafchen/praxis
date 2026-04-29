# Multi-Agent System

A personal, project-based multi-agent system for AI-assisted software development.

Built to work with Claude Code (no API costs, local execution).

## Prerequisites

Before using Praxis, you need:

1. **Claude Code** installed — [Download here](https://claude.ai/code)
2. **Git** to clone the repository

## Setup

```bash
# 1. Clone the repository
git clone git@github.com:clarissafchen/praxis.git

# 2. Navigate into the praxis folder
cd praxis

# 3. Launch Claude Code
claude
```

Once Claude Code is running, you're ready to use Praxis.

## Quick Start

### NEW: Autonomous Coordination Mode (Recommended)
One command coordinates your entire team:

```bash
@manager Build user notifications for order updates
```
### Manager automatically:
- Convenes full team meeting
- Coordinates all 4-5 agents
- Delivers unified plan in 15 seconds
- Saves complete meeting log for transparency

### Traditional: Direct Agent Control
Talk to individual agents directly:

```bash
# Talk to specific agents
@ba What are the requirements?
@engineer What's the architecture?
@ops What's the deployment plan?
@specialist Build a POC for [uncertain approach]

# Check overall status
@manager Status update?
```

### View Team Meeting Log
```bash
cat praxis/sessions/*/team_meeting.md
```

## Architecture

Praxis runs entirely inside Claude Code using persona switching:

```
You (Human)
    ↓
Claude Code (me) with Agent Personas
    ↓
Local Files (praxis/sessions/)
    ↓
Git Repository (your code)
```

**How it works:**

1. You launch Claude Code from the `praxis/` directory: `claude`
2. You type `@agent` (e.g., `@manager`)
3. I read the agent template and switch persona
4. I read session state from local files
5. I respond as that agent
6. I update state files

No external APIs, no cloud services, no costs.

## Agent Team

### Core Agents (in `templates/`)

| Agent | Role | Trigger |
|-------|------|---------|
| **Manager** | Strategic coordinator, your direct report | `@manager` |
| **Business Analyst** | Requirements, user stories | `@ba`, `@business-analyst` |
| **Software Engineer** | Architecture, code, tests | `@engineer`, `@dev` |
| **Ops Specialist** | Infrastructure, deployment | `@ops`, `@sre` |
| **Specialist** | POCs & Documentation | `@specialist` |

### Autonomous Coordination Mode

**NEW**: One command coordinates your entire team automatically.

```
You: @manager Build user notifications for order updates

Manager: "I've coordinated the team. Here's our plan:
🎯 SCOPE: Order notifications (confirmed/shipped/delivered)
⏱️  TIMELINE: 6 hours
👥 TEAM: BA on requirements, Engineer on architecture, Ops on infrastructure
🎯 DECISIONS: SQS over Redis (pattern from past sessions), Handlebars templates
📋 DELIVERABLES: Notification service, email worker, monitoring, runbooks

[View full meeting log | Execute plan | Modify scope]"
```

**What happens behind the scenes:**
1. Manager convenes full team meeting (simulated, 15-30 sec)
2. All agents discuss scope, approach, timeline
3. Complete meeting log saved to `praxis/sessions/*/team_meeting.md`
4. Unified plan delivered to you
5. Strategic decisions escalated, everything else handled by team

**Benefits:**
- One command = Full team coordination
- Complete transparency (read meeting log)
- No micromanagement needed
- Fully interruptible (`@manager Wait, change scope...`)
- Zero API costs

**Learn more**: [COORDINATION.md](COORDINATION.md)

### Custom Agents (in `custom/extra-agents/`)

Create your own agents:

```bash
python praxis/custom/generate-agent.py
```

Then use them: `@security-reviewer`, `@ux-designer`, etc.

## Directory Structure

```
praxis/
├── templates/              # Default agent definitions (can commit)
│   ├── manager.md          # + Autonomous Coordination Mode
│   ├── business-analyst.md
│   ├── software-engineer.md
│   ├── ops-specialist.md
│   └── specialist.md       # POCs & Documentation
│
├── custom/                 # Your personal agents (gitignored)
│   ├── generate-agent.py   # Create new agents
│   ├── extra-agents/       # Your custom agents
│   │   └── security-reviewer.md
│   └── README.md
│
├── sessions/               # Active work (gitignored)
│   └── 2025-01-25-user-notifications/
│       ├── session.yml
│       ├── assignments.yml
│       ├── messages.yml
│       ├── decisions.yml
│       ├── conflicts.yml
│       ├── briefing.md
│       └── team_meeting.md    # Full collaboration transcript (Autonomous Mode)
```

## Session Lifecycle

### 1. Autonomous Coordination Mode (Recommended)

**One command → Full team coordination → Complete plan**

```
You: @manager Build user notifications for order updates

Manager (Autonomous Coordination Mode):
"I've coordinated the team. Here's our plan:

🎯 SCOPE: Order notifications (confirmed/shipped/delivered)
⏱️  TIMELINE: 6 hours total
👥 TEAM ASSIGNMENTS:
   • BA: 3 user stories, API contract (2h)
   • Engineer: SQS-based architecture (4h)
   • Ops: Infrastructure provisioned (2h parallel)

🎯 KEY DECISIONS:
   • SQS over Redis (pattern from past sessions)
   • Handlebars templates in S3 (marketing editable)

📋 DELIVERABLES:
   • Notification service API
   • Email worker
   • Monitoring dashboards  
   • Runbooks

⚠️  ESCALATIONS: None (full team consensus)

[View full meeting log: praxis/sessions/.../team_meeting.md]
[Execute plan | Modify scope | Hold another meeting]"

[Behind the scenes: Full 15-second team meeting simulated,
 all agents coordinated, complete log saved]
```

### 2. Traditional: Sequential Agent Control

For granular control, talk to agents individually:

```
You: @manager Start feature: user notifications

Manager: "Briefing team..."

You: @ba What are the requirements?
BA: "3 user stories identified..."

You: @engineer What's the architecture?
Engineer: "I recommend SQS..."

You: @ops Cost estimate?
Ops: "$42/mo including monitoring..."
```

### 3. Work Phase (Both Modes)

```
Manager coordinates:
- Monitors assignments.yml (tracking progress)
- Detects conflicts in conflicts.yml
- Updates briefing.md with status

You can check in anytime:
You: @manager Status?
Manager: "BA complete, Engineer 60% done, Ops standing by."
```

### 4. Interrupt / Modify Scope

```
You: @manager Wait, also add SMS notifications

Manager: "SCOPE CHANGE NOTED at 14:30

Reconvening team with updated scope...
[Re-runs coordination meeting]

Updated plan:
• Timeline: +2 hours (8h total)
• Budget impact: +$30/mo
• New Specialist assignment: SMS gateway POC

Proceed?"
```

### 5. Agent Handoff (Traditional Mode Only)

In traditional mode, talk to individual agents directly:

```
You: @engineer What architecture did you choose?

Engineer (Claude with software-engineer.md):
"I recommend SQS over Redis. Here's why..."

You: @ba Are the requirements clear?

Business Analyst:
"Yes, 3 user stories documented. One question about..."

You: @specialist Build POC for SMS gateway

Specialist:
"POC complete. Twilio integration works, costs $0.0075/SMS..."
```

### 6. Conflict Resolution

Manager detects disagreements and either resolves or escalates:

```
Manager detects conflict in conflicts.yml:
"⚠️ Decision needed: Redis vs SQS

Engineer: Redis (simpler, $0)
Ops: SQS (reliability, $50/mo)

Team couldn't reach consensus after 3 rounds.

My recommendation: SQS
- Pattern from past session showed Redis fails at scale
- Notifications are business-critical
- Cost is within budget

Your call?
[1] Redis (Engineer's choice)
[2] SQS (Ops' choice + my recommendation)  
[3] Redis dev / SQS prod (compromise, adds complexity)"

You: "Go with SQS"

Manager: "Decision logged (DECISION-001). Updating assignments..."
```

### 7. Completion

```
Engineer: "Implementation complete. All quality checks passed."
Ops: "Deployed successfully to production. Monitoring active."
Specialist: "Documentation complete. Runbooks tested."
Manager: "Feature live. 

Summary:
✅ All acceptance criteria met
✅ 99.2% delivery rate (monitoring)
✅ Documentation complete
✅ Runbooks ready

Session complete. Patterns learned saved to memory."

Session moves to memory:
- Patterns learned added to patterns.yml
- Agent performance updated
- Available for future reference
```

Session moves to memory:
- Patterns learned added to patterns.yml
- Agent performance updated
```

## State Files Explained

### session.yml
Overall session status and metadata.

```yaml
session_id: "2025-01-25-user-notifications"
created_at: "2025-01-25T10:00:00Z"
status: active  # active | paused | completed
current_phase: implementation  # discovery | design | implementation | review
team_members: ["manager", "business_analyst", "software_engineer", "ops_specialist", "specialist"]
original_request: "Build user notifications for order updates"
success_criteria: "20% reduction in 'where is my order' tickets"
```

### assignments.yml
Who's doing what.

```yaml
assignments:
  manager:
    status: monitoring
    current_task: "Coordinating deployment"
    
  business_analyst:
    status: done
    current_task: "Requirements documentation"
    deliverables:
      - "docs/requirements.md"
      - "docs/api-contract.yml"
    
  software_engineer:
    status: active
    current_task: "Building notification service"
    blocked_by: null
    deliverables:
      - "src/notifications/api.py"
    
  ops_specialist:
    status: standby
    current_task: "Awaiting handoff"
    
  specialist:
    status: done
    current_task: "Documentation complete"
    deliverables:
      - "docs/internal/notifications.md"
      - "docs/runbooks/notifications.md"
```

### messages.yml
Inter-agent communication.

```yaml
messages:
  - id: "msg-001"
    from: "manager"
    to: "business_analyst"
    timestamp: "2025-01-25T10:05:00Z"
    message: "New feature: User notifications..."
    requires_response: true
    
  - id: "msg-002"
    from: "business_analyst"
    to: "software_engineer"
    timestamp: "2025-01-25T10:30:00Z"
    message: "Requirements complete. See docs/..."
    requires_response: true
```

### decisions.yml
Decision log for accountability.

```yaml
decisions:
  - id: "dec-001"
    timestamp: "2025-01-25T11:00:00Z"
    made_by: "manager"
    decision: "Scope limited to order status only"
    rationale: "Time constraint"
    alternatives_considered:
      - option: "Full scope"
        pros: ["Complete feature"]
        cons: ["3 week timeline"]
```

### conflicts.yml
Active disputes.

```yaml
conflicts:
  - id: "conflict-001"
    timestamp: "2025-01-25T14:00:00Z"
    topic: "Redis vs SQS for queue"
    agent_a: "software_engineer"
    agent_b: "ops_specialist"
    status: resolved
    resolution: "Use SQS (human decision)"
```

### briefing.md
Manager's report to you.

```markdown
# Session Briefing: user-notifications

## Status
🟡 In Progress - Implementation phase

## Completed
✅ BA: Requirements documented
✅ Engineer: Architecture finalized
⏳ Engineer: Coding 60% complete

## Blockers
⚠️ None currently

## Next 4 Hours
- Engineer completes implementation
- Ops provisions infrastructure
- Integration testing
```

### team_meeting.md
**Autonomous Coordination Mode only.** Complete transcript of simulated team meeting.

```markdown
# Team Meeting: User Notifications
Date: 2025-01-25 10:00-10:15
Duration: 15 minutes

## Attendees
Manager, Business Analyst, Software Engineer, Ops Specialist

## Agenda
1. Scope clarification
2. Technical approach
3. Infrastructure requirements
4. Timeline and assignments

## Key Discussion Points

### Scope
- BA asked: "What notification types?"
- Human clarified: "Order confirmed, shipped, delivered"
- Resolution: 3 user stories identified

### Technical Decisions
- Engineer proposed: "SQS or Redis for queue?"
- Ops concern: "Redis had issues at scale in past session"
- Resolution: Consensus on SQS

## Decisions Made
- DECISION-001: Use SQS over Redis
  - Rationale: Managed service, past session success, has DLQ
  - Proposed by: Engineer
  - Approved by: Team consensus

## Action Items
| Agent | Task | Time | Status |
|-------|------|------|--------|
| BA | User stories & API contract | 2h | Pending |
| Engineer | SQS architecture | 4h | Pending |
| Ops | Provision SQS | 2h | Pending |

## Escalations to Human
- None (full consensus reached)

## Meeting Outcome
✅ Success - Team aligned, ready to execute
```

**Purpose:** Complete transparency. Debug by reviewing exactly what the team discussed and why decisions were made.

**Access:** `cat praxis/sessions/*/team_meeting.md`

## Creating Custom Agents

### Option 1: Use the Generator (Recommended)

```bash
cd your-project
python praxis/custom/generate-agent.py
```

Answer the questions, get a template, edit to refine.

### Option 2: Copy and Modify

```bash
cp praxis/templates/manager.md praxis/custom/extra-agents/my-agent.md
# Edit with your requirements
```

### Agent Template Structure

Every agent template has:

1. **Role definition** - What this agent does
2. **Core responsibilities** - 3-5 key tasks
3. **Collaboration** - Who they work with
4. **State management** - Files they read/write
5. **Intelligence layer** - Reflection guidelines
6. **Communication patterns** - How to talk to others
7. **Work process** - Step-by-step workflow
8. **Personality** - Traits and style

## Memory System

Cross-session learning in `praxis/memory/patterns.yml`:

### What Gets Remembered

- **Patterns**: What technical approaches worked
- **Failures**: What went wrong and why
- **Decisions**: Architectural choices and outcomes
- **Agent performance**: How well each agent performs

### Example Usage

```yaml
patterns:
  - id: "queue-choice-sqs-over-redis"
    what_worked: "SQS with DLQ for notification systems"
    what_failed: "Redis memory pressure at scale"
    recommendation: "Always use managed queues for business-critical async work"
    used_in: ["2024-12-10-auth-emails", "2025-01-25-user-notifications"]
```

Manager reads this and says:
> "Based on past sessions, I recommend SQS over Redis for reliability."

## Tips for Best Results

### 1. Be Explicit About Scope

```
Good: "Build user notifications for order updates only"
Bad: "Build notifications"

Good: "Deploy to staging, not production"
Bad: "Deploy this"
```

### 2. Use @mentions for Direct Access

```
@manager Status?           # Quick check-in
@engineer Why SQS?          # Technical question
@ops Cost estimate?         # Infrastructure question
```

### 3. Review State Files

You can always read session files directly:

```bash
cat praxis/sessions/2025-01-25-user-notifications/briefing.md
```

### 4. Refine Over Time

Agents learn from your feedback. Edit templates:

```bash
# Edit manager to be more proactive
Edit praxis/templates/manager.md

# Or create custom version
Edit praxis/custom/manager.md  # Overrides template
```

### 5. Clean Up Old Sessions

Sessions accumulate. Archive or delete:

```bash
# Archive completed sessions
mv praxis/sessions/2024-* praxis/archive/

# Or delete if no longer needed
rm -rf praxis/sessions/2025-01-old-feature/
```

## Troubleshooting

### "Agent not responding correctly"

1. Check agent template loaded: `Read praxis/templates/manager.md`
2. Check session exists: `List praxis/sessions/`
3. Provide more context in your message

### "State not updating"

1. Check file permissions: Sessions folder must be writable
2. Explicitly ask agent to update: "@manager Update the briefing"

### "Conflicts not resolved"

1. Check conflicts.yml: `Read praxis/sessions/{id}/conflicts.yml`
2. Make the decision yourself: "Use SQS"
3. Manager will log and implement

### "Want to start fresh"

```bash
# Archive all sessions
mkdir -p praxis/archive
mv praxis/sessions/* praxis/archive/

# Or reset everything
rm -rf praxis/sessions/*
rm praxis/memory/patterns.yml
```

## Advanced Usage

### Multi-Session Context

Manager can coordinate multiple features:

```
You: @manager We have 3 features in progress:
  1. User notifications (60% done)
  2. Payment retry logic (not started)
  3. Admin dashboard (20% done)
  
  Prioritize payment retry - it's blocking revenue.

Manager: "Understood. Reprioritizing...
- Pausing admin dashboard
- Accelerating payment retry
- User notifications continues as planned

New assignments:
[Updated in assignments.yml]"
```

### Cross-Project Learning

Patterns from one project apply to another:

```yaml
# In praxis/memory/patterns.yml
patterns:
  - id: "notification-system"
    used_in:
      - "project-a/sessions/2025-01-notifications"
      - "project-b/sessions/2025-02-alerts"
```

### Team Sharing

To share with teammates:

1. **Commit templates/** to git (default agents)
2. **Share custom agents** via copy/paste
3. **Share patterns** by syncing patterns.yml

Keep sessions/ gitignored - they're personal.

## Why This Approach?

| Traditional | This System |
|-------------|-------------|
| External APIs ($$$) | Local Claude Code (free) |
| Complex infrastructure | Simple files |
| Rigid workflows | Flexible, editable |
| Black box AI | Transparent state |
| One-size-fits-all | Personal, customizable |

## Contributing

This is your personal system. Modify freely:

- Edit templates to match your style
- Create new agents for your needs
- Add patterns as you learn
- Share improvements with team

## License

MIT - Use freely, modify completely.

---

**Questions? Issues?**

This is a local, file-based system. Debug by:
1. Reading state files
2. Checking agent templates
3. Testing agent responses

No external dependencies, no vendor lock-in.
