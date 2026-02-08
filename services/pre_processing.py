import re
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")
STOPWORDS = set(stopwords.words('english'))
#cleaning the loaded text removing stopwords like the, if ,is the etc. and keeping only relevant info for analysis and further job matching process.
def clean_text(text):
    text = text.lower()
    text = re.sub(r"<[^>]+>", " ", text) #remove any html tags
    text = re.sub(r"\s+", " ",text).strip() # remove any white spaces    
    text = re.sub(r'\n+', ' ',text)
    text = re.sub(r'\(cid:\d+\)', '', text)# removes all he cid characters encoding with the phone no. and linkedin and github
    text = re.sub(r'[^\x00-\x7F]+',' ',text) #remove non ASCII Charcters
    Words = text.split()
    Words = [word for word in Words if word not in STOPWORDS ]
    return " ".join(Words)