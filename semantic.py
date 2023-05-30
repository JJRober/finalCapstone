# Load the 'en_core_web_sm' model from spacy
import spacy
nlp = spacy.load('en_core_web_md')

# Create tokens for specific words using the 'nlp' model
word1 = nlp("bat")
word2 = nlp("ball")
word3 = nlp("diamond")

# Print the similarity score
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Create tokens for the given text using the 'nlp' model
tokens = nlp('bat ball diamond car')

# Iterate through each token in 'tokens
for token1 in tokens:
    # Iterate through each token in 'tokens' again
    for token2 in tokens:
         # Print the text of 'token1', the text of 'token2', and their similarity score
        print(token1.text, token2.text, token1.similarity(token2))

# Using the model 'en_core_web_md' and 'en_core_web_sm' you get different similarity score as the model sm is a small English model where the md model is a medium size model and has a larger vocabulary
# therefore it will depend on the number of vectors related to that word based on the model used.

