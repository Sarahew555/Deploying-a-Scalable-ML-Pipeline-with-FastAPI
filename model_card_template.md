# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

The model I have used is a Support Vector Machine. It is provided by sklearn. I have used all the default parameters, and set a random seed of 4.

## Intended Use

This model is intended to predict individuals with a salary greater than $50,000. This is a supervised classification task. 

## Training Data

Our training data comes from the 1994 Census database. Barry Becker extracted a set of reasonable clean records. 

## Evaluation Data

The evaluation data accounts for 20% of our data has been split from the Census dataset.

## Metrics

The evaluation metrics used are fbeta, precision, and recall score.
Our models performance for said metrics are as follows:
Precision - 0.9683
Recall - 0.1583
F1 - 0.2722

## Ethical Considerations

The ethical considerations of our supervised learning model are the possibility of wrong predictions and descrimination which could lead to less donations as well as many other adverse effect. 

## Caveats and Recommendations

If we had more time to spend on this project, we could evaluate further hyperparameters to advance our model.
