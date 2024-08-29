/**
 * Likhon Sheikh 
 *
 * @author Likhon Sheikh <https://likhonsheikh.com>
 * @copyright 2023-2024 Likhon Sheikh
 * @mail  <me@likhonsheikh.com>
 * @telegram Likhon Sheikh  <https://t.me/likhondotxyz>
 */



import click
from jinja2 import Environment, FileSystemLoader
import os

@click.command()
@click.option('--name', prompt='Project name', help='The name of the project')
@click.option('--version', prompt='Project version', default='', help='The version of the project')
@click.option('--description', prompt='Project description', help='A short description of the project')
@click.option('--homepage', prompt='Project homepage', default='', help='The homepage URL of the project')
@click.option('--demo', prompt='Project demo URL', default='', help='The demo URL of the project')
@click.option('--docs', prompt='Project documentation URL', default='', help='The documentation URL of the project')
@click.option('--author', prompt='Author name', help='The name of the author')
@click.option('--github', prompt='GitHub username', default='', help='The GitHub username of the author')
@click.option('--website', prompt='Author website', default='', help='The website of the author')
@click.option('--twitter', prompt='Twitter username', default='', help='The Twitter username of the author')
@click.option('--linkedin', prompt='LinkedIn username', default='', help='The LinkedIn username of the author')
@click.option('--patreon', prompt='Patreon username', default='', help='The Patreon username of the author')
@click.option('--license', prompt='License name', default='', help='The name of the license')
@click.option('--issues', prompt='Issues page URL', default='', help='The URL of the issues page')
@click.option('--contributing', prompt='Contributing guide URL', default='', help='The URL of the contributing guide')
@click.option('--install', prompt='Install command', default='', help='The command to install the project')
@click.option('--usage', prompt='Usage command or instruction', default='', help='The command or instruction to use the project')
@click.option('--test', prompt='Test command', default='', help='The command to run tests')
@click.option('--use-html', prompt='Use HTML in README.md?', type=bool, default=False, help='Whether to use HTML in README.md')
@click.option('--template', type=click.Choice(['default', 'minimal']), default='default', help='Choose a README template')
def main(**kwargs):
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
    template = env.get_template(f"{kwargs['template']}.md")
    
    readme_content = template.render(**kwargs)
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    click.echo("README.md has been generated successfully!")

if __name__ == '__main__':
    main()
