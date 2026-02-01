# CLI Implementation

## Architecture

The CLI is built using **Click** (Python CLI framework) with a command-group structure.

### Structure

```
cli.py
├── cli() - Main command group
└── create() - Subcommand for generating Dockerfiles
```

### Key Decisions

**Framework: Click**
- Declarative decorator-based syntax
- Built-in help generation
- Type validation and error handling
- Wide adoption in Python ecosystem

**Command Structure**
- `@click.group()` for main entry point
- `@click.command()` for subcommands
- Extensible for future commands (e.g., `list`, `validate`)

**Arguments & Options**
- `language` - Positional argument with choices validation
- `-lv/--language-version` - Optional with default
- `--flavor` - Optional for distribution variants
- `-o/--output-file` - Optional with timestamp fallback
- `-h/--help` - Custom help flag on both levels

### Template Engine

**Jinja2** for dynamic Dockerfile generation:
- Clean separation of logic and templates
- Easy to maintain and extend
- Standard templating syntax

### Error Handling

- `ValueError` for user input errors (red output)
- `Exception` for unexpected errors
- `click.Abort()` for graceful exits

### Output

- Colored output using `click.secho()`
- Timestamps for unique filenames
- `.Containerfile` extension (OCI-compliant)

## Future Enhancements

- Add `list` command for available templates
- Add `validate` command for Dockerfile linting
- Support custom template paths
