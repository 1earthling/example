from rich.console import Console
from rich.markdown import Markdown

def render_markdown(file_path):
    # Force left-justification by using a wide console and soft wrapping
    console = Console(width=120, soft_wrap=True)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        markdown = Markdown(content)
        console.print(markdown, justify="left")
    except FileNotFoundError:
        console.print(f"[bold red]Error:[/bold red] The file '{file_path}' was not found.")
    except Exception as e:
        console.print(f"[bold red]An error occurred:[/bold red] {e}")

# Example usage:
if __name__ == "__main__":
    render_markdown('example.md')
