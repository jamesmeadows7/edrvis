# edrvis

A terminal user interface for visualising [GROMACS](https://www.gromacs.org/) edr files.
Made using [pyedr](https://github.com/MDAnalysis/panedr) and [textual](https://github.com/Textualize/textual).

<div style="display: flex; gap: 10px;">
  <img width="49%" src="https://github.com/user-attachments/assets/7e08d169-257f-4243-9ffe-9e2e472984c6" alt="edrvis-light" />
  <img width="49%" src="https://github.com/user-attachments/assets/10b39de3-8178-44bc-91e5-072860314057" alt="edrvis-dark" />
</div>

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

- [ ] Add tests
- [ ] Compute block average, error, RMSD and total drift
