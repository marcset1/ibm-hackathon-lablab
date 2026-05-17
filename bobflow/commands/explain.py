import click
import os
from bobflow.bob_runner import run_bob

@click.command()
@click.argument("path", default=".")
@click.option("--depth", "-d", default="overview",
              type=click.Choice(["overview", "detailed"]),
              help="Level of explanation")
def explain(path, depth):
    """Explain a codebase and suggest the next BobFlow command.

    Example: bobflow explain ./my-project
    """
    abs_path = os.path.abspath(path)

    if not os.path.exists(abs_path):
        click.echo(f"❌ Path not found: {abs_path}", err=True)
        return

    click.echo(f"\n🔍 BobFlow — Analyzing '{abs_path}'\n")
    click.echo("🤖 IBM Bob is analyzing your codebase...\n")

    prompt = f"""Analyze all files in the current directory carefully.

Provide a {depth} analysis:

1. PROJECT PURPOSE — What does this project do?
2. CURRENT STATE — What is already implemented? List actual files.
3. TECH STACK — What languages, frameworks, libraries are used?
4. WHAT IS MISSING — What features are incomplete or absent based on the README and code?
5. RECOMMENDED NEXT STEP — One clear, specific feature to build next.

END your response with this exact block:

---SUGGESTED BOBFLOW COMMAND---
bobflow scaffold <feature-name> --stack "<detected stack>" --idea "<specific, detailed description of exactly what to build next, based on what is missing>"
---

Make the idea precise enough that IBM Bob can build it immediately."""

    result = run_bob(prompt, cwd=abs_path, mode="ask")

    if result["success"]:
        click.echo(result["output"])
        click.echo("\n💡 Copy the suggested command above and run it!")
    else:
        click.echo(f"❌ {result['error']}", err=True)
