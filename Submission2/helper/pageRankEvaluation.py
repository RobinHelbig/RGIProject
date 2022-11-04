import matplotlib.pyplot as plt

def calculate_true_pos(summary_sentences, news_sentences):
    true_pos = []
    for t1 in summary_sentences:
        for t2 in news_sentences:
            if t1 == t2:
                true_pos.append(t2)
    return true_pos

def calculate_accuracy(document, news_sentences, summary_sentences):
    TP = 0
    TN = 0
    All = len(document.text_sentences)
    for sent in document.text_sentences:
        is_in_ref_summary = sent in summary_sentences
        is_in_summary = sent in news_sentences

        if is_in_summary and is_in_ref_summary:
            TP += 1
        if not is_in_summary and not is_in_ref_summary:
            TN += 1

    return (TP + TN) / All


def draw_MAP_chart(map0, map1, map2, DOCUMENTS):

    fig, ax = plt.subplots()

    ax.bar(x=DOCUMENTS,
           height=[map0, map1, map2],
           capsize=4)

    plt.title('Documents MAP - comparision')
    plt.xlabel('Document')
    plt.ylabel('MAP value')
    plt.show()