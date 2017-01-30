import sys
import json
import tweet_sentiment as twit

def freq(tweet_file):
    term_freq = {}  # initialize new dictionary for term frequency
    build_dict(tweet_file,term_freq)
    for key in term_freq:
        print key, term_freq[key]

def build_dict(tweet_file,term_freq):
    for line in tweet_file:
        tweet = twit.get_tweet(line)
        if tweet is not None:
            for term in tweet.split(" "):
                add_to_dict(term,term_freq)

def add_to_dict(word,new_dict):
    if word not in new_dict:
        new_dict[word] = 1
    else:
        new_dict[word] += 1


def main():
    tweet_file = open(sys.argv[2])
    freq(tweet_file)

if __name__ == '__main__':
    main()
