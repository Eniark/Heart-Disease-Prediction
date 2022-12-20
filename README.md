# Heart-Disease-Prediction

One of my first end-to-end ML projects. I tried applying some statistical tests like ANOVA, Chi2, Cramer V test, Shapiro-Wilk etc.

P.s. I have to note that I'm not that experienced in finding relationships between variables and have some questions regarding that. (Oddly enough, Shapiro-Wilk test outputted that most of my features are not normally distributed, but just from looking at the distributions I wouldn't say that __all__ of them are not normally distributed.)

I created a Baseline model with 82% using accuracy as metric.

But using accuracy was not a good thing because my main focus was to reduce the amount of False Negatives, so instead I focused on _recall_ for class #1(has disease). I performed hyperparameter tuning with respect to recall and later plotted the Precision-Recall Curve to find the optimal threshold for class split. Interestingly enough, the optimal value was near the 0.5 -> 0.46. It increased my base recall from __0.88 -> 0.97__ while maintaining decent precision and accuracy.  


Screenshots:



To use this project you can either:
a) Manually do these steps in a CLI:
  1. git clone https://github.com/Eniark/Heart-Disease-Prediction.git
  2. go to folder where requirements.txt is located
  3. pip install -r requirements.txt
  4. python -m flask run
b) Use a docker image:
  1. docker pull loc
  2. docker run -p 5000:5000 -d heart-disease-img

Dataset Metadata: https://archive.ics.uci.edu/ml/datasets/heart+disease

__Work in Progress...__
