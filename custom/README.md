# Custom Agents

Personal agent templates and modifications.

## Extra Agents

Create your own agents using the generator:

```bash
python praxis/custom/generate-agent.py
```

Or manually create `.md` files in this directory.

## Modifying Default Agents

To override a default agent, create a file with the same name:

```
praxis/templates/manager.md           # Default
praxis/custom/manager.md              # Your version (takes precedence)
```

## Usage

After creating an agent, use it with:

```
@agent-id your request
```

Example: If you create `security-reviewer.md`, use `@security-reviewer`.

## Agent Ideas

- **Security Reviewer**: Audits code for vulnerabilities
- **UX Designer**: Reviews UI/UX, suggests improvements  
- **Performance Engineer**: Optimizes slow code
- **Documentation Writer**: Creates user docs
- **QA Engineer**: Designs test plans
- **Data Analyst**: Analyzes metrics, suggests improvements

## Sharing Agents

1. Copy `.md` file to teammate
2. They put it in their `praxis/custom/extra-agents/`
3. Now you both have the same agent
