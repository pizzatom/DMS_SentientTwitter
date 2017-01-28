import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def sent_dict(file_name):
    afinnfile = file_name
    scores = {} # initialize dictionary
    for line in afinnfile:
            term, score = line.split("\t")  # the file is tab-deliminated
            scores[term] = int(score)  # convert score to integer
    return scores

def read_tweets(tweet_file):
    for line in tweet_file:
        jtweet = json.loads(line)
        print jtweet
    #print jtweet[u'text'].encode('utf-8')

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentdict = sent_dict(sent_file)
    read_tweets(tweet_file)


if __name__ == '__main__':
    main()
