# twitterScraper
Search twitter for tweets based on user inputted preferences. Uses GetOldTweets3 library. Only detects tweets from hourly intervals but fixing soon

### Dependencies

 ```pip install GetOldTweets3 pandas```

### Basic usage

Command line arguments are used to parse parameters. See main.py for default values. Here is a description of the parameters: 

```
python main.py \
        --Q --query        
        --I --initial_date        
        --F --final_date        
        --T --top_tweets      
        --P --place 
        --D --distance        
        --X --total_results    
```

  Argument              | Usage          
----------------------- | ------------------
query                   | Text string to search for REQUIRED FLAG
initial_date            | Initial start date to search from YYYY-MM-DD REQUIRED FLAG
final_date              | Initial end date to search from YYYY-MM-DD REQUIRED FLAG
top_tweets              | Show top tweets only or not (boolean) REQUIRED FLAG
place                   | Tweet location city, country
distance                | Radius from listed city
total_results           | How many results to show


### Example

Runs scrape from tweets posted from 09/08/2020-09/09/2020 with the word "Woodward" in them. Shows tweets from a 60 mile radius around San Francisco and will list 20 results (not neccesarily top tweeets due to '--T False'

``` python main.py --I "2020-09-08" --F "2020-09-10" --Q "Woodward" --P "San Francisco, USA" --D "60mi" --X 20 --T False```

Output will be in HTML file in working directory



### References
[1] https://medium.com/@AIY/getoldtweets3-830ebb8b2dab \
[2] https://pypi.org/project/GetOldTweets3/ 
