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

# get the 'tweet' content from a line of the twitter API
def get_tweet(line):
    jtweet = json.loads(line)
    if 'text' in jtweet:
        return jtweet['text'].encode('utf-8')
    else:
        return None

# calculate the sentiment in a string of text (aka text) according to a sentiment dictionary
def sent_calc(tweet,sent_dict):
    score = 0
    for word in tweet.split(" "):
        if word in sent_dict:
            score += sent_dict[word]
    return score

def tweet_score(tweet,sent_dict):
    if tweet is not None:
        score = sent_calc(tweet,sent_dict)
        return score

def score_tweets(tweet_file,sent_dict):
    for line in tweet_file:
        tweet = get_tweet(line)
        print tweet_score(line,sent_dict)


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentdict = sent_dict(sent_file)
    score_tweets(tweet_file,sentdict)

#    read_tweets(tweet_file)


if __name__ == '__main__':
    main()
