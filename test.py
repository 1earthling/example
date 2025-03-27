graph TD
    A["CEO"]
    B["CTO"] --> C1["Lead Dev"]
    B --> C2["QA Manager"]
    A --> B
    A --> D["CFO"]
    A --> E["COO"]
    
    E --> E1["HR Manager"]
    E --> E2["Marketing Manager"]

    subgraph Development Team
        C1
        C2
    end

    subgraph Operations Team
        E1
        E2
    end
