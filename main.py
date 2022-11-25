import os
from dotenv import load_dotenv
load_dotenv()

MAILINABOX_HOST=os.getenv("MAILINABOX_HOST", "")
MAILINABOX_EMAIL=os.getenv("MAILINABOX_EMAIL", "")
MAILINABOX_PASSWORD=os.getenv("MAILINABOX_PASSWORD", "")

import click
from miab.client import MailInABox

mb = MailInABox(MAILINABOX_HOST, MAILINABOX_EMAIL, MAILINABOX_PASSWORD)

@click.group()
def cli():
    pass

@click.command()
@click.option("--format", default="json")
def mail_users(format):
    click.echo(mb.mail_users(format))

cli.add_command(mail_users)

if __name__=="__main__":
    cli()
