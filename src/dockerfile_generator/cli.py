import click
from datetime import datetime
from pathlib import Path
from .generator import generate_dockerfile

@click.group()
def cli():
    """Dockerfile Generator CLI."""
    pass

@cli.command()
@click.argument(
    'language', 
    type=click.Choice(['python', 'nodejs'], case_sensitive=False), 
    required=True
)
@click.option(
    '-lv', '--language-version', 
    default='latest', 
    help='Version of NodeJS or Python (default: latest).'
)
@click.option(
    '--flavor',
    default='',
    help='Flavor of the language distribution (e.g., slim, alpine). (default: none)'
)
@click.option(
    '-o', '--output-file', 
    type=click.Path(), 
    help='Output file path for the generated Dockerfile. (default: <timestamp>.Containerfile)'
)
@click.help_option('-h', '--help')
def create(language: str, language_version: str, flavor: str, output_file: str):
    """Create a new Dockerfile for the specified language.
    
    LANGUAGE: Programming language for the Dockerfile (python or nodejs).

    Example usage:
        dockerfile-generator create python -lv 3.12 --flavor slim 
        dockerfile-generator create nodejs -lv 18 -o MyNodeImage.Containerfile
    """
    try:
        # Determine Output File Path
        if output_file is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = f"{timestamp}.Containerfile"
        
        output_path = Path(output_file)
        
        # Generate Dockerfile Content
        click.echo(f"Generating Dockerfile for {language.upper()} Docker image...")
        click.echo(f"Language Version: {language_version}")
        if flavor:
            click.echo(f"Using flavor: {flavor}")
        click.echo(f"Output File: {output_path}")

        content = generate_dockerfile(
            language=language.lower(),
            version=language_version,
            flavor=flavor
        )

        # Write data
        output_path.write_text(content, encoding='utf-8')

        click.secho(f"\n Dockerfile successfully created at {output_path}", fg='green')

    except ValueError as e:
        click.secho(f"Error: {e}", fg='red', err=True)
        raise click.Abort()
    except Exception as e:
        click.secho(f"An unexpected error occurred: {e}", fg='red', err=True)
        raise click.Abort()

if __name__ == '__main__':
    cli()