import heapq
import nltk
import re
import pyttsx3
# nltk.download('punkt')
# nltk.download('stopwords')
# f=open(f"Recognized/myfile_20230716053406.txt","w")
# f.write("Hello World")
# f.close()
# import os

# os.chdir("../")
# with open("../Recognized/myfile_20230716053406.txt","r") as f:
#     text = f.read()
#     print(text)


def summarize(filename="D:\\Local Files\\Code For Good\\main\\Integrated\\Team-66_0315\\Team-66\\sample.txt"):
    file_name = r"{}".format(filename)
    # print(filename)
    #Open the file
    with open(file_name, "r") as f:
        article_text = f.read()

    # article_text = text
    #print(article_text,"\n")
    # Removing Square Brackets and Extra Spaces
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)
    # Removing special characters and digits
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
    sentence_list = nltk.sent_tokenize(article_text)
    stopwords = nltk.corpus.stopwords.words('english')

    word_frequencies = {}
    for word in nltk.word_tokenize(formatted_article_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                # print("Here1")
                word_frequencies[word] = 1
            else:
                # print("Here2")
                word_frequencies[word] += 1
        maximum_frequncy = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]
    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(summary_sentences)

    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 200)
    engine.say(summary)
    # engine.runAndWait()
    #with open("summarized_text.txt", "w") as f:
        # Write the text to the file
        #f.write(summary)


    
