import sys
import json
import tweet_sentiment as twit


def new_score(term,score,new_dict):
        if term not in new_dict:
            new_dict[term] = score, 1
        else: # term in new_dict:
            new_dict[term] = tuple(map(lambda x, y: x + y, new_dict[term], (score,1)))  #there must be a better way to do this

def score_terms(tweet,new_dict,sent_dict):
    score = twit.tweet_score(tweet,sent_dict)
    if score is not None: # assign a score to the rest of the terms
        for term in tweet.split(" "):
            if term not in sent_dict: # add it to new_dict
                new_score(term,score,new_dict)

def terms(tweet_file,new_dict,sent_dict):
    for line in tweet_file:
        tweet = twit.get_tweet(line)
        score_terms(tweet,new_dict,sent_dict)

def term_scores(new_dict):
    for key in new_dict:
        print key, new_dict[key][0]/new_dict[key][1]

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentdict = twit.sent_dict(sent_file)
    tweet = "this is is just an awesome test!"
    new_dict = {} # initialize scores dict
    #score_terms(tweet,new_dict,sentdict)
    terms(tweet_file,new_dict,sentdict)
    term_scores(new_dict)

if __name__ == '__main__':
    main()
