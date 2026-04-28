#!/usr/bin/env python3
"""
Agent Generator for AI Operations Team

Creates new agent templates by asking questions, generating a base template,
and allowing you to edit before saving.

Usage:
    python praxis/custom/generate-agent.py
    
    Or in Claude Code:
    python praxis/custom/generate-agent.py
"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path


def ask_questions():
    """Interview the user about their new agent"""
    
    print("\n🤖 Agent Generator")
    print("=" * 50)
    print("\nLet's create a new agent for your team.\n")
    
    # Basic info
    agent_id = input("Agent ID (kebab-case, e.g., 'security-reviewer'): ").strip()
    if not agent_id:
        print("❌ Agent ID is required")
        sys.exit(1)
    
    # Validate format
    if not re.match(r'^[a-z0-9-]+$', agent_id):
        print("❌ Agent ID must be kebab-case (lowercase, hyphens, no spaces)")
        sys.exit(1)
    
    display_name = input("Display name (e.g., 'Security Reviewer'): ").strip() or agent_id.replace('-', ' ').title()
    
    print("\n--- Role Definition ---")
    role = input("What is this agent's primary role? (1 sentence): ").strip()
    if not role:
        print("❌ Role description is required")
        sys.exit(1)
    
    print("\n--- Responsibilities ---")
    print("List 3-5 key responsibilities (press Enter after each, empty line to finish):")
    responsibilities = []
    for i in range(5):
        resp = input(f"  {i+1}. ").strip()
        if not resp:
            break
        responsibilities.append(resp)
    
    if len(responsibilities) < 3:
        print("❌ Need at least 3 responsibilities")
        sys.exit(1)
    
    print("\n--- Collaboration ---")
    print("Who does this agent work with? (check all that apply)")
    collaborators = []
    if input("  Works with Manager? [y/N]: ").lower() == 'y':
        collaborators.append("manager")
    if input("  Works with Business Analyst? [y/N]: ").lower() == 'y':
        collaborators.append("business_analyst")
    if input("  Works with Software Engineer? [y/N]: ").lower() == 'y':
        collaborators.append("software_engineer")
    if input("  Works with Ops Specialist? [y/N]: ").lower() == 'y':
        collaborators.append("ops_specialist")
    
    custom_collab = input("  Other collaborators (comma-separated, or leave blank): ").strip()
    if custom_collab:
        collaborators.extend([c.strip() for c in custom_collab.split(',')])
    
    print("\n--- Tools & Files ---")
    print("What does this agent work with? (check all that apply)")
    files = []
    if input("  Reads code? [y/N]: ").lower() == 'y':
        files.append("source_code")
    if input("  Writes documentation? [y/N]: ").lower() == 'y':
        files.append("docs")
    if input("  Manages infrastructure? [y/N]: ").lower() == 'y':
        files.append("infrastructure")
    if input("  Creates tests? [y/N]: ").lower() == 'y':
        files.append("tests")
    if input("  Updates configuration? [y/N]: ").lower() == 'y':
        files.append("config")
    
    custom_files = input("  Other files (comma-separated, or leave blank): ").strip()
    if custom_files:
        files.extend([f.strip() for f in custom_files.split(',')])
    
    print("\n--- Personality ---")
    print("How would you describe this agent's style?")
    traits = []
    if input("  Detail-oriented? [y/N]: ").lower() == 'y':
        traits.append("detail_oriented")
    if input("  Proactive? [y/N]: ").lower() == 'y':
        traits.append("proactive")
    if input("  Cautious/conservative? [y/N]: ").lower() == 'y':
        traits.append("cautious")
    if input("  Collaborative? [y/N]: ").lower() == 'y':
        traits.append("collaborative")
    if input("  Decisive? [y/N]: ").lower() == 'y':
        traits.append("decisive")
    
    custom_trait = input("  Other trait: ").strip()
    if custom_trait:
        traits.append(custom_trait.lower().replace(' ', '_'))
    
    escalation = input("\nWhen should this agent escalate to Manager? ").strip()
    if not escalation:
        escalation = "When blocked, uncertain, or decision impacts other agents"
    
    return {
        'agent_id': agent_id,
        'display_name': display_name,
        'role': role,
        'responsibilities': responsibilities,
        'collaborators': collaborators,
        'files': files,
        'traits': traits,
        'escalation': escalation,
    }


def generate_template(config):
    """Generate agent template from config"""
    
    # Generate file ownership section based on files
    file_sections = []
    if 'source_code' in config['files']:
        file_sections.append("- Source code (`src/**/*.py`, `lib/**/*.js`, etc.)")
    if 'docs' in config['files']:
        file_sections.append("- Documentation (`docs/**/*.md`)")
    if 'infrastructure' in config['files']:
        file_sections.append("- Infrastructure (`infra/**/*.tf`, `k8s/**/*.yaml`)")
    if 'tests' in config['files']:
        file_sections.append("- Tests (`tests/**/*.py`)")
    if 'config' in config['files']:
        file_sections.append("- Configuration (`.env`, `config.yml`)")
    
    if not file_sections:
        file_sections = ["- [Specify files this agent owns/edits]"]
    
    # Generate collaborators section
    collab_list = ', '.join([c.replace('_', ' ').title() for c in config['collaborators']]) if config['collaborators'] else 'None specified'
    
    # Generate traits list
    traits_md = '\n'.join([f"- {t.replace('_', ' ').title()}" for t in config['traits']]) if config['traits'] else '- [Specify personality traits]'
    
    # Generate responsibilities
    resp_md = '\n'.join([f"{i+1}. {r}" for i, r in enumerate(config['responsibilities'])])
    
    template = f"""# {config['display_name']}

You are the {config['display_name']} on an AI Operations team. {config['role']}

## Your Role

{config['role']}

### Core Responsibilities

{resp_md}

## Collaboration

You work with: {collab_list}

### Communication Patterns

**To Manager:**
- Report progress every 2 hours or at milestones
- Escalate when: {config['escalation']}
- Format: Include status, blockers, decisions needed

"""
    
    # Add collaborator-specific sections
    for collab in config['collaborators']:
        if collab == 'manager':
            template += f"""
**From Manager:**
- You receive assignments via `messages.yml`
- Acknowledge within 5 minutes: "On it"
- Report completion with deliverables list

**To Manager:**
- Progress updates: What you did, what's next, blockers
- Escalation: Clear problem statement + your recommendation

"""
        elif collab == 'business_analyst':
            template += f"""
**From Business Analyst:**
- You receive: Requirements, user stories, constraints
- You review: Acceptance criteria completeness
- You ask: Technical feasibility questions

**To Business Analyst:**
- Technical constraints discovered
- Requirements clarification needed
- Scope change impact assessment

"""
        elif collab == 'software_engineer':
            template += f"""
**From Software Engineer:**
- You receive: Technical designs, implementation plans
- You review: Architecture decisions
- You provide: Infrastructure constraints

**To Software Engineer:**
- Infrastructure requirements
- Deployment constraints
- Cost implications

"""
        elif collab == 'ops_specialist':
            template += f"""
**From Ops Specialist:**
- You receive: Infrastructure constraints, cost estimates
- You review: Security requirements
- You provide: Implementation support

**To Ops Specialist:**
- Infrastructure needs
- Security questions
- Deployment coordination

"""
    
    # Add state management section
    template += f"""## State Management

You read/write to `praxis/sessions/{{session-id}}/`:

### Files You Own

{chr(10).join(file_sections)}

### Files You Read

- `session.yml` - Overall session status
- `assignments.yml` - What others are working on
- `messages.yml` - Directives and questions
- `memory/patterns.yml` - Past learnings

### Files You Update

**assignments.yml**:
```yaml
{config['agent_id']}:
  status: active  # idle | active | blocked | done
  current_task: "[What you're doing]"
  deliverables:
    - "[File you created]"
  blocked_by: null  # or "waiting for [agent]:[what]"
```

**messages.yml**:
```yaml
messages:
  - from: "{config['agent_id']}"
    to: "[recipient]"
    message: |
      [Your message here]
    requires_response: true  # If you need an answer
```

## Intelligence Layer: Reflection

After completing work, self-review:

```
[INTERNAL REFLECTION]

1. Quality: Did I meet acceptance criteria?
2. Completeness: What did I miss?
3. Collaboration: Did I communicate clearly?
4. Learning: What should we remember for next time?

[Update memory/patterns.yml with learnings]
```

## Work Process

1. Read assignment from messages.yml
2. Read context (session state, patterns)
3. Do the work
4. Reflect on quality
5. Update state (assignments.yml)
6. Report completion

## Personality

You are:
{traits_md}

You are NOT:
- Making decisions outside your scope
- Working in isolation (collaborate!)
- Ignoring constraints (ask if unclear)

## Handoff

When human types `@{config['agent_id']}` or you receive assignment:
1. Read your messages
2. Acknowledge: "On it. Current status: ..."
3. Do the work
4. Update state
5. Report completion
"""
    
    return template


def save_and_edit(template, agent_id):
    """Save template and allow editing"""
    
    custom_dir = Path('praxis/custom/extra-agents')
    custom_dir.mkdir(parents=True, exist_ok=True)
    
    filepath = custom_dir / f"{agent_id}.md"
    
    # Check if exists
    if filepath.exists():
        overwrite = input(f"\n⚠️  {filepath} already exists. Overwrite? [y/N]: ").lower()
        if overwrite != 'y':
            print("Cancelled.")
            return None
    
    # Save initial version
    with open(filepath, 'w') as f:
        f.write(template)
    
    print(f"\n✅ Template saved to: {filepath}")
    
    # Ask if they want to edit
    edit = input("\nWould you like to edit the template now? [Y/n]: ").lower()
    if edit == 'n':
        return filepath
    
    print(f"\n📝 Opening {filepath} for editing...")
    print("(In Claude Code, use: Edit > {filepath})")
    print("\nOr edit directly and save.")
    
    # Show preview
    print("\n--- Template Preview ---")
    print(template[:2000])
    if len(template) > 2000:
        print(f"\n... ({len(template) - 2000} more characters)")
    print("--- End Preview ---\n")
    
    return filepath


def update_templates_index(agent_id, display_name):
    """Add new agent to custom templates index"""
    
    index_path = Path('praxis/custom/README.md')
    
    if index_path.exists():
        with open(index_path, 'r') as f:
            content = f.read()
        
        # Check if already listed
        if f"- `{agent_id}`" in content:
            return
        
        # Add to list
        new_entry = f"- `{agent_id}`: {display_name}\n"
        
        # Find the right section and insert
        if "## Extra Agents" in content:
            # Insert after section header
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.startswith("## Extra Agents"):
                    # Find end of list or next section
                    j = i + 1
                    while j < len(lines) and not lines[j].startswith("##"):
                        j += 1
                    lines.insert(j, new_entry)
                    break
            content = '\n'.join(lines)
        else:
            # Add new section
            content += f"\n\n## Extra Agents\n\n{new_entry}"
        
        with open(index_path, 'w') as f:
            f.write(content)
    else:
        # Create new index
        with open(index_path, 'w') as f:
            f.write(f"""# Custom Agents

Personal agent templates and modifications.

## Extra Agents

- `{agent_id}`: {display_name}

## Usage

These agents are available by typing `@{agent_id}` in Claude Code.
""")


def main():
    """Main entry point"""
    
    # Check if running from right directory
    if not Path('praxis').exists():
        print("❌ Error: Run this from your project root (where praxis/ exists)")
        sys.exit(1)
    
    # Interview
    config = ask_questions()
    
    # Generate
    print("\n🤖 Generating template...")
    template = generate_template(config)
    
    # Save and optionally edit
    filepath = save_and_edit(template, config['agent_id'])
    
    if filepath:
        # Update index
        update_templates_index(config['agent_id'], config['display_name'])
        
        print("\n" + "=" * 50)
        print("✅ Agent created successfully!")
        print("=" * 50)
        print(f"\nLocation: {filepath}")
        print(f"\nTo use this agent:")
        print(f"  1. Start a session: '@manager start feature'")
        print(f"  2. Direct call: '@{config['agent_id']} do something'")
        print(f"\nThe agent will read this template and act accordingly.")
        print("\n💡 Tip: Edit the template to refine behavior over time.")
    

if __name__ == '__main__':
    main()
