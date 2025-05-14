import mdv

def render_markdown(file_path):
    try:
        output = mdv.main(file=file_path)
        print(output)
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    render_markdown("example.md")
