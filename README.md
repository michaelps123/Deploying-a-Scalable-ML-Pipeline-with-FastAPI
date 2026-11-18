# Census Income Classification — FastAPI ML Inference

A machine-learning project demonstrating the process of training, evaluating, serializing, and serving a classification model through a REST API.

Built with **Python, scikit-learn, pandas, and FastAPI** as part of Udacity's Machine Learning DevOps coursework.

## Project Overview

This project uses the Census Income dataset to predict whether an individual's annual income exceeds $50,000 based on demographic and employment-related features.

The objective is to demonstrate a practical ML workflow, from data preprocessing and model training through evaluation and API-based inference.

### Key Capabilities

- **Model Training:** Random Forest classifier using scikit-learn.
- **Data Processing:** One-hot encoding of categorical features, with preprocessing reused during inference.
- **Model Evaluation:** Precision, recall, and F1 score, including analysis across categorical data slices.
- **Model Serialization:** Save and reload trained model and encoder artifacts.
- **REST API:** FastAPI application providing prediction requests.
- **Testing:** Pytest coverage for model training, inference, metrics, and serialization.

## Model Performance

The model was evaluated using a stratified 80/20 train-test split of 32,561 census records.

| Metric | Result |
|---|---:|
| Precision | 0.7353 |
| Recall | 0.6378 |
| F1 Score | 0.6831 |

Metrics are for the income `>50K` class.

Additional evaluation details and limitations are documented in [model_card.md](model_card.md). Performance across categorical subsets is recorded in [slice_output.txt](slice_output.txt).

## Running Locally

The project was developed with Python 3.10 dependencies.

### 1. Clone and install

```bash
git clone https://github.com/michaelps123/Deploying-a-Scalable-ML-Pipeline-with-FastAPI.git
cd Deploying-a-Scalable-ML-Pipeline-with-FastAPI

python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Train the model

The training script expects the Census Income dataset at `data/census.csv`.

```bash
python train_model.py
```

This trains and evaluates the classifier, saves the model and encoder under `model/`, and generates categorical-slice evaluation results.

### 3. Start the API

```bash
uvicorn main:app --reload
```

The API runs locally at:

`http://127.0.0.1:8000`

Interactive FastAPI documentation:

`http://127.0.0.1:8000/docs`

### 4. Test predictions

The application exposes two endpoints:

| Endpoint | Purpose |
|---|---|
| `GET /` | Returns a welcome message |
| `POST /data/` | Accepts census features and returns an income classification |

An example API client is included:

```bash
python local_api.py
```

The inference endpoint returns JSON containing a `result` field with either `>50K` or `<=50K`.

### 5. Run unit tests

```bash
pytest -q
```

## Repository Structure

| File or Directory | Purpose |
|---|---|
| `train_model.py` | Training and model evaluation |
| `main.py` | FastAPI application |
| `ml/` | Preprocessing and ML functions |
| `local_api.py` | Example API client |
| `test_ml.py` | Unit tests |
| `model_card.md` | Model documentation and limitations |
| `slice_output.txt` | Evaluation across categorical slices |

## Limitations and Responsible Use

This is an educational demonstration, not a production decision-making system.

The underlying dataset is historical and includes sensitive demographic attributes. Predictions may reflect existing biases in the data.

The model should not be used to make employment, financial, or other consequential decisions about individuals. Additional validation, fairness analysis, and monitoring would be necessary for real-world applications.

## Project Background

This project was completed as part of the Udacity Machine Learning DevOps curriculum, using the [original Udacity starter repository](https://github.com/udacity/Deploying-a-Scalable-ML-Pipeline-with-FastAPI).

The completed coursework implementation includes the model training and evaluation workflow, test cases, serialized model handling, and FastAPI inference service.


***
Local Verification — November 17, 2026

Successfully validated on Linux using Python 3.10:
- Dependencies installed successfully.
- All three existing unit tests passed.
- FastAPI application started successfully.
- GET and POST endpoints returned HTTP 200.
- Example API client successfully returned a model prediction.

***
The repository is retained as a demonstration of foundational ML engineering and model-serving skills.
