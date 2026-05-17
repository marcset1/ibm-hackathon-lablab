import click
import os
from bobflow.bob_runner import run_bob

@click.command()
@click.argument("feature_name")
@click.option("--stack", "-s", default="Python FastAPI", help="Tech stack")
@click.option("--idea", "-i", required=True, help="What to build")
@click.option("--output", "-o", default=".", help="Output directory")
@click.option("--timeout", "-t", default=300, help="Timeout in seconds")
def scaffold(feature_name, stack, idea, output, timeout):
    """Scaffold a new feature into an existing project using IBM Bob.

    Example: bobflow scaffold chat-agent --idea 'Add Kevin AI assistant'
    """
    # Bob travaille depuis le projet existant (output)
    # et crée le feature dans un sous-dossier
    target_dir = os.path.abspath(output)
    feature_dir = os.path.join(target_dir, feature_name)
    os.makedirs(feature_dir, exist_ok=True)

    click.echo(f"\n⚡ BobFlow — Scaffolding '{feature_name}'")
    click.echo(f"   Stack   : {stack}")
    click.echo(f"   Context : {target_dir}")
    click.echo(f"   Output  : {feature_dir}\n")
    click.echo("🤖 IBM Bob is working...\n")

    prompt = f"""You are working in an existing project. Read the existing files to understand the context.

Your task: Create a new feature called '{feature_name}' using {stack}.

Feature description: {idea}

Instructions:
- Read existing code files first to understand the project structure
- Create all new files inside the subdirectory '{feature_name}/'
- Make sure your code integrates with existing code
- Include: main code, requirements or dependencies, basic tests, README for the feature
- Write complete, working code. No placeholders.

Create all files now."""

    # Bob run depuis le projet existant pour avoir le contexte
    result = run_bob(prompt, cwd=target_dir, mode="code", timeout=timeout)

    if result["success"]:
        click.echo(result["output"])
        click.echo(f"\n✅ Feature '{feature_name}' scaffolded!")
        if os.path.exists(feature_dir):
            files = os.listdir(feature_dir)
            if files:
                click.echo("📁 Files created:")
                for f in files:
                    click.echo(f"   └── {feature_name}/{f}")
    else:
        click.echo(f"❌ {result['error']}", err=True)
