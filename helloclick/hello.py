import click


@click.command()
@click.option('--string', default='World',
              help='This is the thing that is greeted.')
@click.option('--repeat', default=1,
              help='How many times you should be greeted.')
def cli(string, repeat):
    '''This scripts greets you.'''
    for x in range(repeat):
        click.echo('Hello %s' % string)
