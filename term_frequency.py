import jieba

exclusion_list = '，。、！？：；「」'


def get_term_requency_dict(content):
    # 1. 用結巴斷詞
    seg_list = list(jieba.cut(content))

    # 2. 取得詞與數量的 dictionary，並計算 total frequency
    total_frequency = 0
    word_count_dict = dict()
    for word in seg_list:
        if word in exclusion_list:
            continue

        total_frequency += 1
        if word not in word_count_dict:
            word_count_dict[word] = 1
        else:
            count = word_count_dict[word]
            word_count_dict[word] = count + 1

    # 3. 計算
    tf_dict = dict()
    for w in word_count_dict:
        count = word_count_dict[w]
        tf = count / total_frequency
        tf_dict[w] = tf
        # print('%s: %.3f' % (w, tf))

    return tf_dict
