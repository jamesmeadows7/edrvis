# edrvis

[![PyPI version](https://img.shields.io/pypi/v/edrvis)](https://pypi.org/project/edrvis/)
[![Python versions](https://img.shields.io/pypi/pyversions/edrvis)](https://pypi.org/project/edrvis/)
[![License](https://img.shields.io/pypi/l/edrvis)](https://github.com/jamesmeadows7/edrvis/blob/main/LICENSE)

A terminal user interface for visualising [GROMACS](https://www.gromacs.org/) edr files.
Made using [pyedr](https://github.com/MDAnalysis/panedr) and [textual](https://github.com/Textualize/textual).

<img width="1211" height="830" alt="image" src="https://github.com/user-attachments/assets/888b5697-5de5-4bb1-afd1-fa1e0fb95bd7" />
<img width="1211" height="830" alt="image" src="https://github.com/user-attachments/assets/74c77c5b-5d2d-4f3f-885e-ee977fafdff0" />



## Installation

As a standalone tool:
```bash
uv tool install edrvis
```

In a project environment:
```bash
uv add edrvis
```

## Usage
```bash
edrvis path/to/file.edr
```

### Keyboard Actions

| Key | Action |
|-----|--------|
| `j` / `k` | Navigate energy quantities |
| `d` | Toggle dark mode |
| `q` | Quit |


## Development

```bash
git clone https://github.com/jamesmeadows7/edrvis.git
cd edrvis
uv sync
uv run edrvis path/to/file.edr
```


## Roadmap

- [x] Add tests
- [x] Compute block average, error, RMSD and total drift
