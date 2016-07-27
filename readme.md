Machine Learning for Flu Related Tweets
Program utilizes Supervised Learning to learn from pre-labeled tweets to accurately label new input. Classifier_test is used to compare three classifiers, ultimately using logistic for new classification.
Tweets are marked as irrelivent(irr) by the classifier if they do not mention getting a flu shot, and relevant(rel) if they do.

classifier_test:
tests classifiers, naive bayes, svc, and logistic, 10 fold cross validation, gives scores for accuracy, precision, and recall.

classify_new_data:
opens train_set_1.json to train classifier
loops through files in new_dir, classifies, outputs in classified_tweets


compare_official_classified:
not yet working




