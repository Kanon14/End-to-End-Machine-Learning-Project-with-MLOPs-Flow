# End-to-End-Machine-Learning-Project-with-MLOPs-Flow

This project integrates comprehensive Machine Learning operations (MLOps) to streamline the development and deployment of ML models. By using this template, you can ensure consistent project configuration, automate data processing, model training, and deployment steps, all controlled through an efficient MLOps workflow.

## Table of Contents
- Project Setup
- Workflows
- How to Run
- ML Flow Integration

## Project Setup
Before diving into the workflows, ensure that your development environment is ready.

### Prerequisites
- Anaconda or Miniconda installed on your machine.

### Installation
1. Clone the repository:
```bash
git clone https://github.com/Kanon14/End-to-End-Machine-Learning-Project-with-MLOPs-Flow.git
cd End-to-End-Machine-Learning-Project-with-MLOPs-Flow
```

2. Create and activate a Conda environment:
```bash
conda create -n mlproj python=3.8 -y
conda activate mlproj
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Workflows
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

## How to run
To execute the project's, follow these steps:
1. Run the pipeline:
```bash
python app.py
```

2. Access the application:
```bash
open up your local host and port
```

## ML Flow Integration
ML Flow is used to track experiments, manage model versions, and deploy models. Learn more about integrating ML Flow by visiting the [ML Flow documentation](https://mlflow.org/docs/latest/index.html).

# Author Information
Name: [Kanon14](https://github.com/Kanon14)
Note: This project was created by Kanon14. If you find any issues, have questions, or want to provide feedback, please don't hesitate to reach out. Thank you for exploring this project!