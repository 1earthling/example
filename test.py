# render_markdown.py

from rich.console import Console
from rich.markdown import Markdown

def render_markdown(file_path):
    console = Console()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        markdown = Markdown(content)
        console.print(markdown)
    except FileNotFoundError:
        console.print(f"[bold red]Error:[/bold red] The file '{file_path}' was not found.")
    except Exception as e:
        console.print(f"[bold red]An error occurred:[/bold red] {e}")

# Example usage:
if __name__ == "__main__":
    # Replace 'example.md' with the path to your markdown file
    render_markdown('example.md')
