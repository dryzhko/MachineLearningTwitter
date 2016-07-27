from twitter_machine_learning import load_tweets, TweetFeaturizer, create_train_set, cross_validate
import json
from optparse import OptionParser
import io
import codecs

parser = OptionParser()
parser.add_option("-c", "--classifier", dest="classifier")
(options, args) = parser.parse_args()

#train_file = r".\train_set_1.json"
train_file = r"train_set_1.json"
if options.classifier == "N":
    name = "naive_bayes"
elif options.classifier == "L":
    name = "logistic"
elif options.classifier == "S":
    name = "SVC"
#result_file = r".data\{}_results.json".format(name)
result_file = r"./data/{}_results.json".format(name)

out = codecs.open(result_file, "w", encoding="utf8")

print("Loading tweets")
tweets = load_tweets(train_file)
print("Done")

for i in range(1,6):
    for j in range(1,11):
        print("Creating featurizer")
        tf = TweetFeaturizer(tweets, i, j)
        print("Done")
        
        print("Creating training set")
        train_set = create_train_set(tf, tweets)
        print("Done")
        
        results = cross_validate(options.classifier, train_set, 10)
        results["features"] = len(tf.all_ngrams)
        results["ngrams"] = i
        results["removed"] = j
        print("Number of features: {}".format(results["features"]))
        print("ngrams: {}".format(i))
        print("Removed: {}".format(j))
        print("Accuracy: {}".format(results["average"]["accuracy"]))
        print("Precision: {}".format(results["average"]["precision"]))
        print("Recall: {}".format(results["average"]["recall"]))    
        out.write(json.JSONEncoder().encode(results) + "\n")    