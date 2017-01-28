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
        if 'text' in jtweet:
            return jtweet['text'].encode('utf-8')
    #print jtweet[u'text'].encode('utf-8')

def sent_calc(tweet,sent_dict):
    score = 0
    for word in tweet.split(" "):
        if word in sent_dict:
            score += sent_dict[word]
    print score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentdict = sent_dict(sent_file)
    tweet = 'this is just a test of good faith'
    sent_calc(tweet,sentdict)

#    read_tweets(tweet_file)


if __name__ == '__main__':
    main()
