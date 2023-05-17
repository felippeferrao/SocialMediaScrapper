from src.InstagramScrapper import InstagramScrapper
from src.TwitterScrapper import TwitterScrapper

if __name__ == '__main__':

    print("Starting Social Media Scrapper...")
    keyword = str(input("Enter keyword to search for: "))
    insta_limit = int(input("Enter how many posts to scrape from Instagram: "))
    twitter_limit = int(input("Enter how many posts to scrape from Twitter: "))

    consumerKey = ''
    consumerSecret = ''
    accessToken = ''
    accessTokenSecret = ''


    scrapper = InstagramScrapper()
    scrapper.Scrape_Instagram(tag=keyword,
                              limit=insta_limit,
                              browser='chrome') # 'chrome' or 'firefox'


    twitter = TwitterScrapper()
    twitter.Scrape_Twitter(Consumer_Key=consumerKey,
                           Consumer_Secret=consumerSecret,
                           Access_Token=accessToken,
                           Access_Token_Secret=accessTokenSecret,
                           tag=keyword,
                           limit=twitter_limit,
                           lang='en')  # Language codes: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes


    print("Stopping Social Media Scrapper...")
