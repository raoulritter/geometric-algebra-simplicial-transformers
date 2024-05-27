# clifford-group-equivariant-simplicial-transformers



## Description
This repository contains code and resources for the "Clifford Group Equivariant Simplicial Transformers" (CGESTs) project. The project aims to develop a new class of equivariant transformers by leveraging simplicial complexes and Clifford algebra to achieve equivariance to the full symmetry group. The codebase includes implementations of the proposed model, experiments, and evaluation scripts.

We introduce an extension to the domain of geometric deep learning with CGESTs, enhancing the expressivity of Transformers to match that of Simplicial Message Passing Neural Networks (MPNNs). This facilitates efficient and scalable solutions for geometric graph data, including triangles and higher-level graph structures. Our model has been successfully implemented on the three-dimensional N-body problem, aiming to establish a foundation for broader applications in physics, chemistry, robotics, and computer vision. 

## Report
Find a detailed report on the project [here](/blogpost.md).

## Requirements
- Python 3.8+
- Anaconda or Miniconda
   
## Code Organization
├── media/
│   └── diagram_1.png
├── results/
│   ├── hyperparameter_search/
│   ├── fin_model_6388474.out
│   ├── model_edges_zeros_6388476.out
│   └── model_nodes_6388473.out
├── src/
│   ├── algebra/
│   ├── data/
│   │   ├── nbody_dataset/
│   │   └── nbody.py
│   ├── lib/
│   │   ├── nbody_model/
│   │   │   ├── modules/
│   │   │   ├── __init__.py
│   │   │   ├── transformer.py
│   │   │   └── hyperparameter_testing.py
│   │   └── env.yaml
│   │   ├── main.py
│   │   ├── unit_test_model.py
│   ├── models/
│   ├── scripts/
│   │   └── __init__.py
│   ├── __init__.py
├── .gitignore
├── LICENSE
├── README.md
├── blogpost.md
└── demo.ipynb


## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:raoulritter/clifford-group-equivariant-simplicial-transformers.git 
   ```
2. Install the conda environment:
   ```bash
   conda env create -f src/lib/env.yaml
   conda activate cgest_env
   ```
3. Run the main script:
   ```bash
   python nbody_main.py
   ```
   or use other scripts provided in the repository under *scripts*.


## Usage
To use the scripts, ensure you have installed the required dependencies and activated the conda environment. You can then run the main script or any other scripts provided in the repository.

For example, to run the main script:
```bash
python nbody_main.py
```
## Demo and Reproducibility
% use pretrained models
% run scripts 

## Data
Data for the n-body problem and other experiments can be found in the `nbody_dataset` directory. 
Ensure that you have the necessary data files before running the scripts.
% Add info on where data comes from and what it is

## References
% Fill in
## Acknowledgements
% Fill in with TA and DavidRuhe

## Citation
% fill in
If you use this code or find it helpful in your research, please cite it as follows:
```
@misc{,
  author = {Your Name},
  title = {},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/bellavg/dl_on_the_dl}}
}
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

