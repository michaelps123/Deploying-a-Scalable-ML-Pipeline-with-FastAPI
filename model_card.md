# Model Card: Census Income Classification Model


## Model Details
This project uses a scikit-learn `RandomForestClassifier` with 100 decision trees to predict whether an individual's annual income is greater than $50,000. Categorical features are processed with a `OneHotEncoder`.


## Intended Use
The model was created for a Machine Learning DevOps project. It demonstrates model training, evaluation, serialization, categorical-slice analysis, and API inference. It is not intended for real-world decisions about individuals.


## Training Data
The supplied Census Income dataset contains 32,561 records. The model was trained on 26,048 records using a stratified 80/20 train-test split. Eight categorical features were one-hot encoded before training.


## Evaluation Data
The evaluation set contains 6,513 records not used to train the model. It was processed using the encoder fitted on the training data.


## Metrics
The model was evaluated using precision, recall, and F1 score for the `>50K` class.
- Precision: 0.7353
- Recall: 0.6378
- F1 score: 0.6831

Precision measures how often a `>50K` prediction was correct. 
Recall measures how many actual `>50K` records were identified. 
The F1 score balances precision and recall. Performance for categorical slices is recorded in `slice_output.txt`.


## Ethical Considerations
The dataset includes sensitive attributes such as race and sex. The model may reproduce historical social or economic biases in the data and should not be used for employment, lending, benefits, or other consequential decisions.


## Caveats and Recommendations
The dataset is historical and may not represent current conditions. Before real-world use, the model would require current data, additional validation, fairness testing, and ongoing monitoring.
