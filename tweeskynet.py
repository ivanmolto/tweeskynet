import siaskynet
import pyinputplus as pyip
import pathlib
from datetime import datetime
import webbrowser
import tweepy

api_key = 'Your API Key here'
api_key_secret = 'Your API Key secret here'
access_token = 'Your Access Token here'
access_token_secret = 'Your Access Token secret here'

blurb_prompt_handle = 'Please enter a correct twitter handle: '
blurb_prompt_hashtag = 'Please enter a hashtag: '
blurb_generating_snapshot = 'Generating your twitter snapshot for '
blurb_saved_locally = 'Your twitter snapshot has been saved locally as: '
blurb_current_directory = 'You will find it at the current directory: '
blurb_uploading_snapshot = 'Now uploading your twitter snapshot to Skynet...'
blurb_description = 'This is the Skylink that you can share with anyone to retrieve your twitter snapshot on any Skynet Webportal:'
blurb_url = 'Please check at the follow link: '
blurb_host = 'https://siasky.net/'
blurb_latest_tweets = 'Latest five tweets: \n'
blurb_hash_appearance = 'Latest five hashtag appearances: \n'


auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

file = open('twitter_snapshot.txt', 'w', encoding='utf-8')

search_handle = pyip.inputStr(prompt=blurb_prompt_handle)
search_hashtag = pyip.inputStr(prompt=blurb_prompt_hashtag)

print(blurb_generating_snapshot + search_handle + '\n')

now = datetime.now()
file.write(str(now))
print(now)
file.write('\n')
file.write('\n')

twee_handle = api.get_user(search_handle)

file.write('Twitter Id:' + str(twee_handle.id))
print(f'Twitter Id: {twee_handle.id}')
file.write('\n')
file.write('Name: ' + twee_handle.name)
print(f'Name: {twee_handle.name}')
file.write('\n')
file.write('Twitter handle: ' + twee_handle.screen_name)
print(f'Twitter handle: {twee_handle.screen_name} \n')
file.write('\n')
file.write('Description: ' + twee_handle.description)
print(f'Description: {twee_handle.description} \n')
file.write('\n')
file.write('Twitter status: ' + twee_handle.status.text)
print(f'Twitter status: {twee_handle.status.text} \n')
file.write('\n')
file.write('\n')
file.write(str('Followers: ' + str(twee_handle.followers_count)))
print(f'Followers: {twee_handle.followers_count}')
file.write('\n')
file.write(str('Following: ' + str(twee_handle.friends_count)))
print(f'Following: {twee_handle.friends_count} \n')
file.write('\n')
file.write('\n')

file.write(blurb_latest_tweets)
print(blurb_latest_tweets)
handle_tweets = api.user_timeline(screen_name=search_handle, count=5)
for tweet in handle_tweets:
    file.write(tweet.user.screen_name + ':' + tweet.text)
    print(f'{tweet.user.screen_name}: {tweet.text}\n')
    file.write('\n')
file.write('\n')
file.write(blurb_hash_appearance)
print(blurb_hash_appearance)
hash_tweets = api.search(q=search_hashtag, count=5)
for tweet in hash_tweets:
    file.write(tweet.user.screen_name + ': ')
    print(f'{tweet.user.screen_name}: ')
    file.write(tweet.text)
    print(f'{tweet.text}\n')
    file.write('\n')
file.close()

print(blurb_saved_locally + 'twitter_snapshot.txt')
path_to_txt = pathlib.Path().absolute()
print(blurb_current_directory + str(path_to_txt))
print()
print(blurb_uploading_snapshot)
print(blurb_description)
skylink = siaskynet.upload_file('twitter_snapshot.txt')
print(skylink)
print()
url_link = blurb_host + skylink[6:]
print(blurb_url + url_link)

webbrowser.open_new(url_link)
