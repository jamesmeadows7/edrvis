# edrvis

A terminal user interface for visualising [GROMACS](https://www.gromacs.org/) edr files.
Made using [pyedr](https://github.com/MDAnalysis/panedr) and [textual](https://github.com/Textualize/textual).

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