import click
from bobflow.commands.scaffold import scaffold
from bobflow.commands.explain import explain
from bobflow.commands.test_gen import test
from bobflow.commands.docs import docs
from bobflow.commands.review import review

@click.group()
def cli():
    """
    \b
    ██████╗  ██████╗ ██████╗ ███████╗██╗      ██████╗ ██╗    ██╗
    ██╔══██╗██╔═══██╗██╔══██╗██╔════╝██║     ██╔═══██╗██║    ██║
    ██████╔╝██║   ██║██████╔╝█████╗  ██║     ██║   ██║██║ █╗ ██║
    ██╔══██╗██║   ██║██╔══██╗██╔══╝  ██║     ██║   ██║██║███╗██║
    ██████╔╝╚██████╔╝██████╔╝██║     ███████╗╚██████╔╝╚███╔███╔╝
    \b
    AI-powered developer workflow CLI — Powered by IBM Bob
    IBM Bob Hackathon 2026 — lablab.ai
    """
    pass

cli.add_command(scaffold)
cli.add_command(explain)
cli.add_command(test)
cli.add_command(docs)
cli.add_command(review)
