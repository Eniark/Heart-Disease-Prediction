# Heart-Disease-Prediction

One of my first end-to-end ML projects. I tried applying some statistical tests like ANOVA, Chi2, Cramer V test, Shapiro-Wilk etc.

P.s. I have to note that I'm not that experienced in finding relationships between variables and have some questions regarding that. (Oddly enough, Shapiro-Wilk test outputted that most of my features are not normally distributed, but just from looking at the distributions I wouldn't say that __all__ of them are not normally distributed.)

I created a Baseline model with 82% using accuracy as metric.

But using accuracy was not a good thing because my main focus was to reduce the amount of False Negatives, so instead I focused on _recall_ for class #1(has disease). I performed hyperparameter tuning with respect to recall and later plotted the Precision-Recall Curve to find the optimal threshold for class split. Interestingly enough, the optimal value was near the 0.5 -> 0.51. It increased my base recall from __0.88 -> 0.95__ while maintaining intermediate precision and accuracy.  



Dataset Metadata: https://archive.ics.uci.edu/ml/datasets/heart+disease

__Work in Progress...__
