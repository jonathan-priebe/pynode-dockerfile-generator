from pathlib import Path

from jinja2 import (Environment, PackageLoader, TemplateNotFound,
                    select_autoescape)


def generate_dockerfile(language: str, version: str, flavor: str) -> str:
    """Generate a Dockerfile content based on the specified language, version, and flavor.

    Args:
        language (str): Programming language (e.g., 'python', 'nodejs').
        version (str): Version of the programming language.
        flavor (str): Flavor of the language distribution (e.g., 'slim', 'alpine').

    Returns:
        Generated Dockerfile content as a string.

    Raises:
        ValueError: If the specified language is not supported.
    """
    try:
        # Jinja2 Environment Setup
        env = Environment(
            loader=PackageLoader("dockerfile_generator", "templates"),
            autoescape=select_autoescape(),
            trim_blocks=True,
            lstrip_blocks=True,
        )

        # Template loader
        template_name = f"{language}.dockerfile.j2"
        template = env.get_template(template_name)

        # Build Image-Tag
        if flavor:
            image_tag = f"{version}-{flavor}"
        else:
            image_tag = version

        # Render Template
        content = template.render(
            language=language, version=version, flavor=flavor, image_tag=image_tag
        )

        return content

    except TemplateNotFound:
        raise ValueError(f"Unsupported language '{language}'. No template found.")
    except Exception as e:
        raise ValueError(f"Error generating Dockerfile: {e}")
