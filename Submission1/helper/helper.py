import nltk
import re
import csv


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
                if news_pos + 11 == len(news_text) or news_text[news_pos + 11] == " " or news_text[
                    news_pos + 11] == "\n":
                    summary_text = summary_text[:point_location + 1] + ' ' + summary_text[point_location + 1:]
                    spaces_inserted += 1

    tokens = nltk.sent_tokenize(summary_text)
    return tokens


def write_to_csv(file_name, header, data):
    with open(f'${file_name}', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        writer.writerow(header)

        writer.writerows(data)
