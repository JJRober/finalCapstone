# finalCapstone
# Word Similarity using spaCy

This code demonstrates how to calculate similarity scores between words using the spaCy library in Python. The code utilizes the 'en_core_web_md' model provided by spaCy.

## Description

The code performs the following steps:

1. Load the 'en_core_web_md' model from spaCy.
2. Create tokens for specific words, such as "bat," "ball," and "diamond," using the loaded model.
3. Calculate and print the similarity scores between the words.
4. Create tokens for a given text containing multiple words.
5. Iterate through each token and calculate the similarity score with every other token in the text.
6. Print the text of each token, the text of the compared token, and their similarity scores.

## Usage

To use this code, you need to have spaCy installed. You can install it using pip.
After installing the necessary dependencies, you can run the code and observe the similarity scores between words.

## Notes

It's important to note that the similarity scores may vary depending on the model used. The code showcases the difference in similarity scores when using the 'en_core_web_md' model compared to the 'en_core_web_sm' model. The 'md' model has a larger vocabulary, resulting in potentially different vectors and similarity scores for words.

Please refer to the spaCy documentation for more information on word similarity and the available models.
