from tqdm import tqdm
import nltk
# nltk.download('all')
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords

def text_list(textlist):

    word_tokens_list = []
    sent_tokens_list = []
    clean_word_tokens_list = []
    for text in tqdm(textlist, desc="Remove Punctuation"):

        text = ' '.join(text).strip().lower()

        word_tokens_list.append(word_tokenize(text))
        sent_tokens_list.append(sent_tokenize(text))

        # Remove punctuation and retain words
        clean_word_tokens_list.append(RegexpTokenizer(r'\w+').tokenize(text))

    # Let's filter the stopwords
    stop_words = set(stopwords.words("english"))
    filtered_clean_word_tokens_list = []
    for clean_word_tokens in tqdm(clean_word_tokens_list, desc="Removing Stopwords"):
        filtered_clean_word_tokens = []
        for clean_word_token in clean_word_tokens:
            if clean_word_token not in stop_words:
                filtered_clean_word_tokens.append(clean_word_token)
        filtered_clean_word_tokens_list.append(filtered_clean_word_tokens)

    # Let's tag the Parts of Speech
    tagged_filtered_clean_word_tokens_list = []
    for filtered_clean_word_tokens in tqdm(filtered_clean_word_tokens_list, desc="POS Tagging"):
        tagged_filtered_clean_word_tokens_list.append(nltk.pos_tag(filtered_clean_word_tokens))

    # Let's look at the frequency of distribution
    words_fdist_list = []
    for tagged_filtered_clean_word_tokens in tqdm(tagged_filtered_clean_word_tokens_list, desc="Word Frequency Distribution"):
        words_fdist_list.append(FreqDist(tagged_filtered_clean_word_tokens))

    # Named Entity Recognition for the tagged_filtered_clean_word_tokens
    namedEnts_list = []
    for tagged_filtered_clean_word_tokens in tqdm(tagged_filtered_clean_word_tokens_list, desc="Named Entity Recognition"):
        namedEnts_list.append(nltk.ne_chunk(tagged_filtered_clean_word_tokens))

    return word_tokens_list, sent_tokens_list, clean_word_tokens_list, filtered_clean_word_tokens_list, tagged_filtered_clean_word_tokens_list, words_fdist_list, namedEnts_list
