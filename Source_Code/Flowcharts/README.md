# SentinelT Control Flowcharts

The primary control-flow diagram is available as a clear, scalable vector graphic:

![SentinelT 2.4 GHz RC Control Flow](./SentinelT_Control_Flow.svg)

## Main Operating Logic

```mermaid
flowchart TD
    A[Power ON] --> B[Initialize controller]
    B --> C[Disable all actuator outputs]
    C --> D{E-Stop safe?}
    D -->|No| E[Remain in SAFE DISABLED state]
    E --> D
    D -->|Yes| F[Initialize 2.4 GHz RC receiver]
    F --> G{Valid RC signal?}
    G -->|No| H[Disable drive and auxiliary outputs]
    H --> G
    G -->|Yes| I[Read operator commands]
    I --> J[Apply differential-drive command]
    J --> K{Auxiliary enable commanded?}
    K -->|No| L[Keep auxiliary disabled]
    K -->|Yes| M[Enable auxiliary controller]
    L --> N{E-Stop active or RC lost?}
    M --> N
    N -->|Yes| H
    N -->|No| I
```

## Safety Principle

The software never treats motion as the default state. Startup, reset, signal loss and invalid command data all return SentinelT to a disabled state. The physical E-Stop remains a separate hardware safety layer.
