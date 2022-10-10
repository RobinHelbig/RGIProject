import os

from src.data.document import Document
from src.helper.helper import extract_sentences
from src.helper.textProcessingHelper import getSentences, getTerms

from typing import List 

rootDic = './BBC News Summary'
newsDic = 'News Articles'
summaryDic = 'Summaries'
#categories = Category._member_names_
# categories = ['business', 'entertainment', 'politics', 'sport', 'tech']
categories = ['business']

def read_files(prepcrocessing: bool) -> [Document]:
    documents = list[Document]()
    doc_id = 1
    for category in categories:
        news_folder_path = os.path.join(rootDic, newsDic, category)
        summary_folder_path = os.path.join(rootDic, summaryDic, category)
        for f in os.listdir(news_folder_path):
            news_path = os.path.join(news_folder_path, f)
            summary_path = os.path.join(summary_folder_path, f)
            if os.path.isfile(news_path) and os.path.isfile(summary_path):
                text = open(news_path, "r", encoding='iso-8859-15').read()
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

                reference_summary = extract_sentences(open(summary_path, "r", encoding='iso-8859-15').read())
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