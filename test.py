import mdv

def render_markdown(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        rendered = mdv.main(string=content)
        print(rendered)
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    render_markdown("example.md")
