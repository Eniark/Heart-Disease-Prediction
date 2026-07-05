# Heart Disease Prediction

An end-to-end machine learning project for predicting the presence of heart disease using clinical data. The project covers data exploration, statistical analysis, feature evaluation, model training, hyperparameter tuning, and deployment through a Flask web application.

## Highlights

* Performed exploratory data analysis and statistical feature evaluation using:

  * ANOVA
  * Chi-Square Test
  * Cramer's V
  * Shapiro-Wilk Test
* Built a baseline classification model with **82% accuracy**.
* Optimized the model for **recall** rather than accuracy to reduce false negatives.
* Performed hyperparameter tuning and decision-threshold optimization using the Precision-Recall curve.
* Improved recall for the positive (heart disease) class from **0.88 → 0.97** while maintaining good precision and overall performance.
* Built and deployed a Flask web application for interactive predictions.
* Containerized the application with Docker.

## Tech Stack

* Python
* scikit-learn
* Pandas
* NumPy
* Matplotlib
* Flask
* Docker


## Screenshots
![image](https://user-images.githubusercontent.com/62321153/209288643-3bccf25d-ef61-4e1f-bc03-ca103fec924b.png) 
![image](https://user-images.githubusercontent.com/62321153/209288681-1b19e441-6107-4b75-bc04-d4c32ffefc6e.png)

## Results

| Metric                            |   Value |
| --------------------------------- | ------: |
| Baseline Accuracy                 |     82% |
| Optimized Recall (Positive Class) | **97%** |

## Dataset

The project uses the **UCI Heart Disease Dataset**.

Dataset: [https://archive.ics.uci.edu/ml/datasets/heart+disease](https://archive.ics.uci.edu/ml/datasets/heart+disease)

## Running the Project

```bash
git clone https://github.com/Eniark/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction
pip install -r requirements.txt
python app.py
```

Alternatively, run the Docker image:

```bash
docker pull eniark/heart-disease-image:flask-app
docker run -p 5000:5000 eniark/heart-disease-image:flask-app
```
