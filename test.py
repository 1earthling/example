%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#f4f4f4'}, 'flowchart': {'defaultRenderer': 'dagre'}}}%%
graph TD
    A["CEO"]
    
    subgraph Team1
        direction TB
        B1["Lead Dev"]
        B2["QA Manager"]
        B3["DevOps Manager"]
        B4["Security Lead"]
        B5["UX Designer"]
        B6["Data Engineer"]
    end

    A --> Team1
