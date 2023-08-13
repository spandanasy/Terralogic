import re

def validate_twitter_url(url):
    twitter_pattern = r'^https?://(?:www\.)?twitter\.com/([A-Za-z0-9_]{1,15})$'
    return bool(re.match(twitter_pattern, url))

def extract_twitter_urls(text):
    twitter_pattern = r'https?://[^\s/$.?#].[^\s]*'
    return re.findall(twitter_pattern, text)

def count_valid_twitter_urls(urls):
    valid_twitter_urls = filter(validate_twitter_url, urls)
    return len(list(valid_twitter_urls))

def count_invalid_twitter_urls(urls):
    return len(urls) - count_valid_twitter_urls(urls)

text = "Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk , more information on Tesla's products can be found at https://www.tesla.com/ . Also here are leading influencers for tesla related news, https://twitter.com/teslarati https://twitter.com/dummy_tesla https://twiter.com/dummy_2_tesla"

twitter_urls = extract_twitter_urls(text)
valid_twitter_count = count_valid_twitter_urls(twitter_urls)
invalid_twitter_count = count_invalid_twitter_urls(twitter_urls)
print('\n')
print(twitter_urls)
print('\n')
print("Valid Twitter URLs found in the text:")
for url in twitter_urls:
    if validate_twitter_url(url):
        print('->'+url)

print('\n')
print("Invalid Twitter URLs found in the text:")
for url in twitter_urls:
    if not validate_twitter_url(url):  
        print('->'+url)


print(f"\nTotal Valid Twitter URLs: {valid_twitter_count}")
print(f"Total Invalid Twitter URLs: {invalid_twitter_count}")