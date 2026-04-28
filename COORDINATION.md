# Praxis Autonomous Coordination Mode

**One command. Full team coordination. Complete transparency.**

## What Is It?

Autonomous Coordination Mode simulates a complete team meeting with all your agents (Manager, BA, Engineer, Ops, Specialist) when you give a single command. You get a unified plan, and the full conversation is logged for review.

## How It Works

### 1. You Give One Command
```
@manager Build user notifications for order updates
```

### 2. Manager Convenes Team Meeting (15-30 seconds)
Behind the scenes, Manager simulates:
- Briefing all agents on the request
- BA asking clarifying questions
- Engineer proposing technical approaches
- Ops raising infrastructure concerns
- Team debating key decisions (up to 3 rounds)
- Reaching consensus or escalating to you

### 3. Full Meeting Log Created
```
praxis/sessions/2025-01-25-user-notifications/
├── team_meeting.md          # Complete transcript
├── assignments.yml          # Final task assignments
├── decisions_log.yml        # What was decided & why
└── manager_briefing.md      # Summary for you
```

### 4. You Get Unified Plan
```
"I've coordinated the team. Here's our plan:

🎯 SCOPE: Order notifications (confirmed/shipped/delivered)
⏱️  TIMELINE: 6 hours total
👥 TEAM ASSIGNMENTS:
   • BA: 3 user stories (2h)
   • Engineer: SQS-based architecture (4h)
   • Ops: Infrastructure (2h parallel)

🎯 KEY DECISIONS:
   • SQS over Redis (pattern from past sessions)
   • Handlebars templates in S3 (marketing editable)

📋 DELIVERABLES:
   • Notification service API
   • Email worker
   • Monitoring dashboards
   • Runbooks

[View full meeting log | Execute plan | Modify scope]"
```

## Commands

### Start Automatic Coordination
```
@manager Build [feature description]
```
Manager immediately runs team meeting and delivers plan.

### Request Deep Dive Meeting
```
@manager Hold team meeting on [specific topic]
```
Manager convenes focused meeting on just that topic.

### Interrupt / Change Scope
```
@manager Wait, change scope to [new scope]
```
Manager immediately updates meeting log, re-runs coordination with new scope, delivers updated plan.

### Review Meeting Log
```
@manager Show me the team meeting log
```

Or read directly:
```bash
cat praxis/sessions/*/team_meeting.md
```

## Meeting Log Format

### team_meeting.md Structure
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
- Specialist noted: "Pattern from 2024-12 shows SQS works"
- Resolution: Consensus on SQS

## Decisions Made
- DECISION-001: Use SQS over Redis
  - Rationale: Managed service, past session success, has DLQ
  - Proposed by: Engineer
  - Approved by: Team consensus
  - Alternatives considered: Redis (simpler but failed at scale before)

## Action Items
| Agent | Task | Time | Status |
|-------|------|------|--------|
| BA | User stories & API contract | 2h | Pending |
| Engineer | SQS architecture & implementation | 4h | Pending |
| Ops | Provision SQS, monitoring | 2h | Pending |

## Escalations to Human
- None (full consensus reached)

## Meeting Outcome
✅ Success - Team aligned, ready to execute
```

## When Human Input Is Needed

Manager escalates to you when:

1. **Scope unclear**
   ```
   "BA asks: What notification types? Full order lifecycle or specific events?"
   ```

2. **Team disagreement** (after 3 rounds of debate)
   ```
   "Team has differing views:
   • Engineer: Redis (simpler, $0)
   • Ops: SQS (reliable, $50/mo)
   
   My recommendation: SQS
   Impact: $50/mo but prevents scaling issues
   
   Your decision?"
   ```

3. **Budget/timeline exceeds thresholds**
   ```
   "Ops estimates: $150/mo infrastructure
   This exceeds our $100 tactical decision threshold.
   
   Options:
   1. Find cost savings (reduce redundancy)
   2. Approve $150/mo
   3. Defer non-critical components
   
   Your call?"
   ```

## Benefits

| Benefit | How It Works |
|-----------|--------------|
| **One command** | `@manager Build X` → Full team coordination |
| **Full transparency** | Complete meeting log shows all discussions |
| **Debuggable** | If plan is wrong, review log to understand why |
| **Educational** | Learn how multi-agent reasoning works |
| **Accountable** | Every decision logged with who proposed/approved |
| **Efficient** | 15 seconds of coordination vs. managing 4 agents individually |
| **Interruptible** | Change scope anytime, team re-coordinates |
| **No API costs** | All happens within Claude Code |

## Example: Complete Session Flow

### Step 1: Initial Request
```
You: @manager Build user notifications

Manager: "I've coordinated the team. Here's our plan:

🎯 SCOPE: Order notifications (confirmed/shipped/delivered)
⏱️  TIMELINE: 6 hours
👥 ASSIGNMENTS: [list]
🎯 DECISIONS: [list]
⚠️  NEED YOUR INPUT: Redis vs SQS - Team split, I recommend SQS

Your call?"
```

### Step 2: You Decide
```
You: Go with SQS

Manager: "Decision logged. Team proceeding with SQS.

Updated plan ready. Execute?"
```

### Step 3: Execution (or Review Log)
```
You: Show me the meeting log

Manager: [Displays full team_meeting.md]
```

Or skip to execution:
```
You: Execute

Manager: "Team activated. BA starting requirements. I'll update you in 2 hours."
```

### Step 4: Interrupt If Needed
```
You: @manager Wait, also add SMS notifications

Manager: "SCOPE CHANGE NOTED

Reconvening team with updated scope...
[Re-runs meeting simulation]

Updated plan: ...
Timeline adjusted: +2 hours
Budget impact: +$30/mo

New total: 8 hours, $72/mo

Proceed?"
```

## Collaboration Without Micromanagement

**What you DON'T do:**
- ❌ Talk to each agent individually
- ❌ Manage handoffs between agents
- ❌ Track who's doing what manually
- ❌ Resolve every team disagreement

**What you DO:**
- ✅ Give one high-level command
- ✅ Review unified plan
- ✅ Make strategic decisions when escalated
- ✅ Interrupt/change scope as needed
- ✅ Review meeting log if curious
- ✅ Let team execute autonomously

## Tips

### For Fast Execution
```
@manager Build [feature] - Quick mode
```
Shorter meeting, focuses on essential decisions only.

### For Complex Features
```
@manager Hold deep planning meeting for [complex feature]
```
Longer meeting (30-60 min simulation), covers edge cases, risks, alternatives.

### To Skip to Specific Agent
```
@manager Coordinate, then I want to talk to @engineer directly
```
Gets plan, then switches to Engineer mode for your questions.

## Troubleshooting

### "Plan seems wrong"
```
@manager Show meeting log
[Review discussion - see where reasoning went wrong]
@manager Reconvene team, reconsider [specific decision]
```

### "Need more detail on decision"
```
cat praxis/sessions/*/team_meeting.md
[Search for DECISION-00X to see full rationale]
```

### "Want different team composition"
```
@manager For this project, add @security-specialist to team
```
(See AGENT_CUSTOMIZATION.md for creating custom agents)

## Comparison: Old vs New Way

| Without Coordination Mode | With Coordination Mode |
|---------------------------|------------------------|
| You: "@manager Start feature" | You: "@manager Build feature" |
| Manager: "Briefing team..." | Manager: **[runs full meeting]** |
| You: "@ba What requirements?" | Manager: "Plan ready" |
| BA: "..." | You: "Execute" |
| You: "@engineer Architecture?" | **[team works autonomously]** |
| Engineer: "..." | Manager: "Update in 2h" |
| (30 min of coordination) | (30 seconds of coordination) |

## Advanced Usage

### Pattern: Iterative Refinement
```
You: @manager Build notifications
Manager: [plan with 6 hour estimate]
You: Too long, can we cut scope?
Manager: [re-runs meeting, suggests: drop SMS, keep email only]
You: Good, execute that
```

### Pattern: Deep Investigation
```
You: @manager Hold deep meeting on architecture options
Manager: [30-min simulated debate on 3 approaches]
You: [reviews log, understands tradeoffs]
You: @manager Go with option B
```

### Pattern: Autonomous Execution
```
You: @manager Build this, full autonomy, update me only if blocked
Manager: "Understood. Will coordinate and execute. Check in at milestones or if escalations needed."
[Team works, you get brief updates or escalation notifications only]
```

## Summary

**Autonomous Coordination Mode =**
- One command triggers full team collaboration
- Complete meeting log for transparency
- Strategic decisions escalated to you
- Everything else handled by team
- Fully interruptible and modifiable

**Ready to try it?**
```
@manager Build [your feature]
```
