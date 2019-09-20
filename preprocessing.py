import nltk
# nltk.download('all')
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords

def text_data(textlist):

    title_clean_word_tokens = []
    title_filtered_clean_word_tokens = []
    title_tagged_filtered_clean_word_tokens = []
    title_word_tokens  = []
    title_sent_tokens = []
    title_words_fdist = []
    title_namedEnt = []

    for text in textlist:
        
        text = text.lower()

        title_word_tokens.append(word_tokenize(text))
        title_sent_tokens.append(sent_tokenize(text))

        # Remove punctuation and retain words
        title_clean_word_tokens.append(RegexpTokenizer(r'\w+').tokenize(text))

        # Let's filter the stopwords
        stop_words = set(stopwords.words("english"))
        title_filtered_clean_word_tokens.append([word for word in title_clean_word_tokens if word not in stop_words])

        # Let's tag the Parts of Speech
        title_tagged_filtered_clean_word_tokens.append(nltk.pos_tag(title_filtered_clean_word_tokens))

        # Let's look at the frequency of distribution
        title_words_fdist.append(FreqDist(title_tagged_filtered_clean_word_tokens))

        # Named Entity Recognition for the tagged_filtered_clean_word_tokens
        title_namedEnt.append(nltk.ne_chunk(title_tagged_filtered_clean_word_tokens))

    return title_clean_word_tokens, title_filtered_clean_word_tokens, title_tagged_filtered_clean_word_tokens, title_word_tokens, title_sent_tokens, title_words_fdist, title_namedEnt

