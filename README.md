# KWIC (Key Word In Context)
## Modularization 2
### Functional Decomposition:

### Modules:
-   Input Module: Reads and stores the input lines.
-   Circular Shifter Module: Generates circular shifts.
-   Alphabetizer Module: Sorts the shifts.
-   Output Module: Prints the sorted shifts.
### Communication:
-   Direct function calls between modules.
-   Data is passed directly between modules using function arguments and return values.
### Approach:

-   Modules are tightly coupled.
-   Each module relies on the specific implementation details of other modules.
-   Functional decomposition emphasizes the sequence of operations.
-   Inter-Module Interaction:

-   The data flow is explicit through function calls.
-   Each module performs its task and then passes data to the next module in the sequence.

## Modularization 2
###  Data-Centric Decomposition:

### Modules:
-   Line Storage Module: Manages storage of lines.
-   Circular Shifter Module: Generates circular shifts using the line storage.
-   Alphabetizer Module: Sorts the circular shifts.
-   Output Module: Prints the sorted shifts.
-   Master Control Module: Coordinates the overall process.
### Communication:
-   Indirect communication through a shared data structure (Line Storage).
-   Modules interact via a central data repository.

### Approach:

-   Modules are more loosely coupled.
-   Each module interacts with a central data repository, reducing dependencies on the implementation -   details of other modules.
-   Data-centric decomposition emphasizes the storage and management of data.
### Inter-Module Interaction:

-   Indirect interaction through shared data structures.
-   Each module focuses on manipulating and accessing the shared data structure rather than directly -   passing data between modules.

## Key Differences
### Decomposition Method:

- Modularization 1: Functional decomposition where modules are defined by specific functions and operations.
- Modularization 2: Data-centric decomposition where modules are defined by their role in managing and manipulating shared data.
Coupling:

Modularization 1: Tighter coupling between modules due to direct function calls and data passing.
-   Modularization 2: Looser coupling due to interaction via a shared data structure.
Communication:

-   Modularization 1: Direct communication through function arguments and return values.
Modularization 2: Indirect communication through shared data managed by the Line Storage module.
Flexibility and Maintainability:

-   Modularization 1: Changes in one module may necessitate changes in other modules due to tighter coupling.
-   Modularization 2: More flexible and maintainable as modules interact through a shared data structure, isolating changes to individual modules.