import tweepy
from tweepy_info import consumer_key, consumer_secret, access_token, access_token_secret
import matplotlib.pyplot as plt
from collections import Counter
from PIL import Image 
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator, color_from_image

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

text = ""
for tweet in tweepy.Cursor(api.user_timeline, id = 'NASAClimate', include_rts = False).items(500):
    text += "".join(tweet.text)

# image to be used
earth = np.array(Image.open("earth.jpg"))

# removes unneccessary words
STOPWORDS.update(["https", "t", "s","co", "U", "NASA", "help", "data", "amp", "year"])

# create the wordcloud object
wordcloud = WordCloud(mask = earth, max_words = 400, background_color = "white").generate(text)

# display the generated image
image_color = ImageColorGenerator(earth)

plt.imshow(wordcloud.recolor(color_func = image_color), interpolation = "bilinear")
plt.axis("off")
plt.show()