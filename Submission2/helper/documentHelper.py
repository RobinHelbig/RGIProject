import os
import re

from data.document import Document
from helper.textProcessingHelper import getSentences, getTerms
import nltk

from typing import List 

dirname = os.path.dirname(__file__)
rootDic = os.path.join(dirname, '../../BBC News Summary')
newsDic = 'News Articles'
summaryDic = 'Summaries'
#categories = Category._member_names_
categories_default = ['business', 'entertainment', 'politics', 'sport', 'tech']

def categoryToInt(category: str):
    return categories_default.index(category)

def intToCategory(number: int):
    return categories_default[number]

def extract_sentences(summary_text, news_text):
    point_locations = [m.start() for m in re.finditer('[.?!]', summary_text)]
    point_locations = point_locations[:-1]
    spaces_inserted = 0

    for point_location in point_locations:
        point_location += spaces_inserted
        if summary_text[point_location + 1] != " ":
            summary_part = summary_text[point_location - 10:point_location + 1]
            news_pos = news_text.find(summary_part)
            if news_pos != -1:
                if news_pos + 11 == len(news_text) or news_text[news_pos + 11] == " " or news_text[news_pos + 11] == "\n":
                    summary_text = summary_text[:point_location + 1] + ' ' + summary_text[point_location + 1:]
                    spaces_inserted += 1

    tokens = nltk.sent_tokenize(summary_text)
    return tokens


def read_files(prepcrocessing: bool, categories: list[str] = None) -> list[Document]:
    documents = list[Document]()
    doc_id = 1
    c = categories if categories else categories_default
    for category in c:
        news_folder_path = os.path.join(rootDic, newsDic, category)
        summary_folder_path = os.path.join(rootDic, summaryDic, category)
        for f in os.listdir(news_folder_path):
            news_path = os.path.join(news_folder_path, f)
            summary_path = os.path.join(summary_folder_path, f)
            if os.path.isfile(news_path) and os.path.isfile(summary_path):
                text = open(news_path, "r", encoding='iso-8859-15').read()
                text = text.split("\n\n", 1)[1]  # remove headline
                text_terms = list[str]()
                text_sentences = getSentences(text)
                text_sentences_terms: list[list[str]] = list()
                text_sentences_avg_length = 0.0
                for sentence in text_sentences:
                    terms = getTerms(sentence, prepcrocessing)
                    text_terms = text_terms + terms
                    text_sentences_terms.append(terms)
                    text_sentences_avg_length += len(sentence)

                text_sentences_avg_length = text_sentences_avg_length / len(text_sentences)
                reference_summary = extract_sentences(open(summary_path, "r", encoding='iso-8859-15').read(), text)
                document = Document(doc_id, category, text, text_terms, text_sentences, text_sentences_terms, text_sentences_avg_length, reference_summary, None)
                documents.append(document)
                doc_id += 1
    return documents


"""
id: int
    category: str
    text: str #actual text content of document from "News Articles" directory
    text_sentences: list[str] #actual text content of document from "News Articles" directory divided in sentences
    text_sentence_terms: list[list[str]]
    referenceSummary: list[str] #reference summary from "Summaries Folder"
    summary: 
"""