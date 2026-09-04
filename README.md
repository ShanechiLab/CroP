# CroP-Models: Modeling Cross-Population Neural Dynamics

This repository introduces two methods for modeling interactions across neural populations.
**CroP-LDM** (cross-population prioritized linear dynamical modeling) learns the cross-population
dynamics with a linear dynamical model. **CroP-DYNO** (cross-population prioritized dynamical
nonlinear interaction model) provides a nonlinear dynamical framework for the same objective, and
further allows individual components of the dynamical model to be independently specified as
nonlinear or linear.

## Getting started

The installation instructions and tutorial notebook for each method are below:

- **[CroP-LDM/](./CroP-LDM/)**: see [CroP-LDM/README.md](./CroP-LDM/README.md). Tutorial at
  `CroP-LDM/source/CroPLDM/example/CroPLDM_tutorial.ipynb`
- **[CroP-DYNO/](./CroP-DYNO/)**: see [CroP-DYNO/README.md](./CroP-DYNO/README.md). Tutorial at
  `CroP-DYNO/source/CroPDYNO/example/CroPDYNO_tutorial.ipynb`

## Citations

If you use CroP-LDM, please cite:

> Jha T, Sani O G, Pesaran B and Shanechi M M 2025 Prioritized learning of cross-population neural
> dynamics *J. Neural Eng.* **22** 046040. https://doi.org/10.1088/1741-2552/ade569

If you use CroP-DYNO, please cite:

> Jha T, Song D and Shanechi M M 2026 Prioritized nonlinear modeling of shared dynamics across
> neural populations *J. Neural Eng.* https://doi.org/10.1088/1741-2552/ae9bee

## License

Copyright © The University of Southern California. All Rights Reserved.
See the `LICENSE` file in each method's directory for the full notice and terms of use.
