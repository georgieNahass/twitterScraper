from tweetScrape import Scrape
import argparse

def main(args):
    scrape = Scrape(args)
    args = parser.parse_args()

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--Q', '--query', help = 'text query to be matched', type =str)
    parser.add_argument('--I', '--initial_date', help = 'initial date of search "YYYY-MM-DD"', type =str)
    parser.add_argument('--F', '--final_date', help = 'Final date of search "YYYY-MM-DD"',type =str)
    parser.add_argument('--T', '--top_tweets', help = 'show the top tweets from query')
    parser.add_argument('--P', '--place', help = 'Location to base search from i.e. "Berlin, Germany"',type =str, default = "Palo Alto, USA")
    parser.add_argument('--D', '--distance', help = 'distance from desired location i,e "30km"',type =str, default = "10mi")
    parser.add_argument('--X', '--total_results', help = 'number of results to be shown', type =int, default = 20)

    args = parser.parse_args()
    main(args)