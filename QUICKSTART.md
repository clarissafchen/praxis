# 🚀 Quick Start Guide

Get your AI Operations team running in 5 minutes.

## Step 1: Verify Structure

```bash
# Check that praxis exists
ls -la praxis/

# Should show:
# - README.md
# - templates/
# - custom/
# - sessions/
# - memory/
```

## Step 2: Start Your First Session

In Claude Code, type:

```
@manager I want to build [your feature]
```

Example:
```
@manager I want to build user notifications for order updates
```

## Step 3: Watch It Work

Manager will:
1. Create a session folder in `praxis/sessions/`
2. Brief the team (BA, Engineer, Ops)
3. Report back with a plan
4. Start coordinating work

## Step 4: Interact With Your Team

```
@manager Status?                    # Check overall progress
@business-analyst Show requirements # See what BA documented
@engineer What architecture?        # Ask Engineer technical questions
@ops Is it deployed?                 # Check deployment status
```

## Step 5: Make Decisions

When Manager escalates:

```
Manager: "⚠️ Decision needed: Redis vs SQS"

You: "Go with SQS"

Manager: "Decision logged. Proceeding with SQS..."
```

## Step 6: Review Progress

Check files directly:

```bash
# Read the latest briefing
cat praxis/sessions/*/briefing.md

# Check current assignments
cat praxis/sessions/*/assignments.yml

# See what decisions were made
cat praxis/sessions/*/decisions.yml
```

## Common Commands

### Start New Feature
```
@manager Build [feature description]
```

### Check Status
```
@manager Status update?
```

### Switch to Specific Agent
```
@engineer How's the implementation going?
@ba Are requirements clear?
@ops Any deployment blockers?
```

### Ask About Past Sessions
```
@manager What did we learn about queue systems?
```
(Manager reads memory/patterns.yml and summarizes)

### Create Custom Agent
```bash
python praxis/custom/generate-agent.py
```

Then use it:
```
@my-new-agent Do something
```

## Tips

### Be Specific
```
Good: "Build notifications for order updates only"
Bad: "Build notifications"
```

### Provide Context
```
Good: "Must use existing SendGrid account, GDPR compliant"
Bad: [no constraints]
```

### Escalate When Needed
If agents are stuck, make the decision:
```
"Use SQS. Cost is acceptable."
```

### Review State
Always can read session files yourself:
```bash
cat praxis/sessions/[date-feature]/briefing.md
```

## Troubleshooting

### "@manager not responding correctly"
1. Check template loaded: `Read praxis/templates/manager.md`
2. Provide more context in your request

### "Want to start over"
```bash
# Archive current sessions
mv praxis/sessions/* praxis/archive/

# Start fresh
@manager [new request]
```

### "Agent is too verbose/conservative"
Edit the template:
```
Edit praxis/templates/manager.md
```

Change personality section to match your preference.

## Next Steps

1. ✅ Try your first session
2. ✅ Read the full README: `praxis/README.md`
3. ✅ Create a custom agent: `python praxis/custom/generate-agent.py`
4. ✅ Refine templates to match your style

## Example Session

See `praxis/sessions/2025-01-25-example-user-notifications/` for a complete example of:
- Session lifecycle
- Assignments
- Briefing format
- How decisions are logged

---

**Ready? Start with:**
```
@manager Build [your feature here]
```
