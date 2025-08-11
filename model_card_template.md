# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

The model I chose to use to complete this project is XGBoost or Extreme Gradient Boosting. XGBoost is a highly efficient implementation of gradient boosted decision trees.

## Intended Use

XGBoost can be used for classification tasks and handles complex data well. In this project, we will be using this model to determine if an individuals salary is less than or greater than $50k. 

## Training Data

The training data we will use was extracted from the 1994 US Census database by Barry Becker. This dataset contains 14 features that we will use to classify salary. The original dataset contains 48,842 instances and includes multiple data types. We used 80% of the data to train the model.

## Evaluation Data

Our evaluation data is from the same dataset as our training data, but we used the remaining 20% of data for testing the models performance metrics.

## Metrics
_Please include the metrics used and your model's performance on those metrics._
The metrics from our model are: Precision 0.7328, Recall 0.6690, F1 0.6995

## Ethical Considerations

The ethical considerations of this model include possible bias and incorrect predictions which could lead to people groups feeling marginalized depending on the use of this model.

## Caveats and Recommendations

I would recommend using further hyperparameter tuning to achieve better metrics.
