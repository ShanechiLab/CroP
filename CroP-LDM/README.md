# CroP-LDM

**CroP-LDM** (cross-population prioritized linear dynamical model) is a method for linear
dynamical modeling of interactions between two simultaneously recorded neural populations. Given
the activity of a source population Y and a target population Z, CroP-LDM learns a dynamical model
of population Y while prioritizing the dynamics that are predictive of population Z.

For details, see our manuscript: Jha T, Sani O G, Pesaran B and Shanechi M M 2025 Prioritized
learning of cross-population neural dynamics J. Neural Eng. 22 046040.

## Installation

Tested on **Python 3.11**

```bash
conda create -n cropldm python=3.11
conda activate cropldm
pip install -r requirements.txt
```

## Running the tutorial

Open `source/CroPLDM/example/CroPLDM_tutorial.ipynb` and run it. It walks through a complete
worked example on simulated cross-population data.

CroP-LDM is implemented as a wrapper layer over the [PSID](https://github.com/ShanechiLab/PyPSID)
codebase (Sani et al., *Nature Neuroscience*, 2021). PSID is bundled unmodified under
`source/PSID/`, fixed at commit `24c6a1261eba43f246d117f468bfbfa3dfc4d3e7` of its `dev` branch, so
the exact version that CroP-LDM builds on does not change as PSID is updated upstream.

## License

Copyright © 2025 The University of Southern California. All Rights Reserved.
See [LICENSE](./LICENSE) for the terms of use.
