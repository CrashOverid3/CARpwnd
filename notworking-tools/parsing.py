import click

@click.group()
def cli():pass

@cli.command()
def inject_one():
    click.echo("parse")

@cli.command()
def inject_two():
    click.echo("parse parse")

