# Heart-Disease-Prediction

One of my first end-to-end ML projects. I tried applying some statistical tests like ANOVA, Chi2, Cramer V test, Shapiro-Wilk etc.

P.s. I have to note that I'm not that experienced in finding relationships between variables and have some questions regarding that. (Oddly enough, Shapiro-Wilk test outputted that most of my features are not normally distributed, but just from looking at the distributions I wouldn't say that __all__ of them are not normally distributed.)

I created a Baseline model with 82% using accuracy as metric.

But using accuracy was not a good thing because my main focus was to reduce the amount of False Negatives, so instead I focused on _recall_ for class #1(has disease). I performed hyperparameter tuning with respect to recall and later plotted the Precision-Recall Curve to find the optimal threshold for class split. Interestingly enough, the optimal value was near the 0.5 -> 0.46. It increased my base recall from __0.88 -> 0.97__ while maintaining decent precision and accuracy.  

There were some variables I'm not familiar with (like _Thal_, _ST Depression test_, _Number of vessels_) because of lack of domain knowledge. So it was hard for me to find good causal relationships.

## Screenshots:
![image](https://user-images.githubusercontent.com/62321153/209288643-3bccf25d-ef61-4e1f-bc03-ca103fec924b.png)

![image](https://user-images.githubusercontent.com/62321153/209288681-1b19e441-6107-4b75-bc04-d4c32ffefc6e.png)

## Project evaluation

To run this project in __development mode__ you can either:
* Manually do these steps in a CLI:
  1. `git clone https://github.com/Eniark/Heart-Disease-Prediction.git`
  2. go to folder where requirements.txt is located
  3. `pip install -r requirements.txt`
  4. on first startup use _scripts/run_app.sh_ (next times you may run _app.py_ instead). This will configure your flask app; 
  4. go to directory with _app.py_ and run `python app.py`
* Use a docker image:
  1. `docker pull eniark/heart-disease-img:flask-app`
  2. `docker run -p 5000:5000 -d heart-disease-img`

## Summary
- [x] Created a classifier with stress on recall. Got 97% recall rate;
- [x] Created a responsive website for users to interact with the model;
- [x] Deployed code to github and dockerhub;

[Dataset Metadata Here](https://archive.ics.uci.edu/ml/datasets/heart+disease)
