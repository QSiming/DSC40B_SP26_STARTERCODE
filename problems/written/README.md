# Written Problems

These problems are written in LaTeX and designed for homeworks and discussion
worksheets.

Run `make previews` to build a PDF preview of each problem. Run `make jpg` to
make JPG preview images.

Each subdirectory is a *category*. Within each category is a *problem
directory*. A problem directory must have one or more *versions* of the form
`v01`, `v02`, etc. The actual problem source is stored in these version
directories.

## Version Directory Structure

A problem version directory should have the following structure:

- `problem.tex`: the problem as a LaTeX file
- `rubric.md`: the problem's rubric
- `include/`: (optional) a directory containing data used in the student-facing
  version of the problem
- `include-solution/`: (optional) a directory containing data used in the
  problem's solution
- `dev/`: (optional) a directory containing materials used in the creation of
  the problem

## Example

Below is an example of what the directory tree for the `bst/` category may look
like:

```
bst
├── order_statistic
│  └── v01
│     ├── include
│     │  └── order_statistic.py
│     ├── outcomes.yaml
│     ├── problem.tex
│     └── rubric.md
└── time_of_operations
   └── v01
      ├── include
      │  ├── bar.py
      │  ├── baz.py
      │  └── foo.py
      ├── outcomes.yaml
      ├── problem.tex
      └── rubric.md
```
