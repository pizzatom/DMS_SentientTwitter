import sys
import json
import tweet_sentiment as twit

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


def new_dict(tweet_file,sent_dict)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentdict = twit.sent_dict(sent_file)
    tweet = "this is just an awesome test!"
    print twit.sent_calc(tweet,sentdict)


if __name__ == '__main__':
    main()
