import os
from dotenv import load_dotenv
load_dotenv()

import click
import json

from miab.client import MailInABox

MAILINABOX_HOST=os.getenv("MAILINABOX_HOST", "")
MAILINABOX_EMAIL=os.getenv("MAILINABOX_EMAIL", "")
MAILINABOX_PASSWORD=os.getenv("MAILINABOX_PASSWORD", "")

mb = MailInABox(MAILINABOX_HOST, MAILINABOX_EMAIL, MAILINABOX_PASSWORD)

@click.group()
def cli():
    pass

@click.command()
@click.option("--format", "-f", default="json")
def users(format):
    click.echo(json.dumps(mb.mail_users(format)))

@click.command()
@click.option("--format", "-f",  default="json")
def aliases(format):
    click.echo(json.dumps(mb.mail_aliases(format)))

@click.command()
@click.argument("address")
@click.argument("forwards_to")
@click.option("--update-if-exists", default=0)
@click.option("--permitted-senders", default=None)
def add_alias(address, forwards_to, update_if_exists, permitted_senders):
    click.echo(mb.mail_aliases_add(update_if_exists, address, forwards_to, permitted_senders))

@click.command()
@click.argument("address")
def remove_alias(address):
    click.echo(mb.mail_aliases_remove(address))

cli.add_command(users)
cli.add_command(aliases)
cli.add_command(add_alias)
cli.add_command(remove_alias)

if __name__=="__main__":
    cli()
