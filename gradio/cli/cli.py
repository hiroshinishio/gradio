import sys

from gradio_client.cli import deploy_discord  # type: ignore
import typer

from .commands import deploy
from .commands import print_environment_info
from .commands import reload
from .commands import create_component

app = typer.Typer()

def cli():
    args = sys.argv[1:]
    if len(args) == 0:
        raise ValueError("No file specified.")
    elif args[0] == "deploy":
        deploy()
    elif args[0] == "environment":
        print_environment_info()
    elif args[0] == "deploy-discord":
        deploy_discord.main()
    else:
        reload()