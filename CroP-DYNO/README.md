# CroP-DYNO

**CroP-DYNO** (cross-population prioritized dynamical nonlinear interaction model) is a method
for nonlinear dynamical modeling of interactions between two simultaneously recorded neural
populations. Given the activity of a source population Y and a target population Z, CroP-DYNO
learns a dynamical model of population Y while prioritizing the dynamics that are predictive of
population Z.

For details, see our manuscript: Jha T, Song D and Shanechi M M 2026 Prioritized nonlinear
modeling of shared dynamics across neural populations *J. Neural Eng.*
https://doi.org/10.1088/1741-2552/ae9bee

## Installation

Tested on **Python 3.11** 

```bash
conda create -n cropdyno python=3.11
conda activate cropdyno
pip install -r requirements.txt
```

## Running the tutorial

Open `source/CroPDYNO/example/CroPDYNO_tutorial.ipynb` and run it. It walks
through a complete worked example on simulated cross-population data, covering:

1. Fitting CroP-DYNO with a nonlinear target-population readout and comparing against the true
   (ideal)  model and a fully linear baseline.
2. Flexible search over which model mappings should be nonlinear.
3. Causal vs. noncausal (smoothing) inference.

CroP-DYNO builds on the [DPAD](https://github.com/ShanechiLab/DPAD) codebase.

DPAD is bundled under `source/DPAD/`, and CroP-DYNO is implemented as a wrapper layer over it
(`source/CroPDYNO/`). Bundling a copy keeps CroP-DYNO self-contained and ensures it runs against
the same DPAD version it was developed with. To update DPAD, replace the contents of
`source/DPAD/` with the newer version.

## License

Copyright © 2026 The University of Southern California. See [LICENSE](./LICENSE) for the full
notice.
