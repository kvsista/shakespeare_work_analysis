import nltk
# nltk.download('all')
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords

def text_data(text):

    text = text.lower()

    word_tokens = word_tokenize(text)
    sent_tokens = sent_tokenize(text)

    # Remove punctuation and retain words
    clean_word_tokens = RegexpTokenizer(r'\w+').tokenize(text)

    # Let's filter the stopwords
    stop_words = set(stopwords.words("english"))
    filtered_clean_word_tokens = [word for word in clean_word_tokens if word not in stop_words]

    # Let's tag the Parts of Speech
    tagged_filtered_clean_word_tokens = nltk.pos_tag(filtered_clean_word_tokens)

    # Let's look at the frequency of distribution
    words_fdist = FreqDist(tagged_filtered_clean_word_tokens)

    # Named Entity Recognition for the tagged_filtered_clean_word_tokens
    namedEnt = nltk.ne_chunk(tagged_filtered_clean_word_tokens)

    return clean_word_tokens, filtered_clean_word_tokens, tagged_filtered_clean_word_tokens, word_tokens, sent_tokens, words_fdist, namedEnt
