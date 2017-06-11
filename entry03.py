import os
import load
import term_frequency as tf

file_list = os.listdir('./corpus')

# 1. get all tf_dict for every file
tf_list = list()
for f in file_list:
    news = load.load(f)
    text = news.get_content()

    tf_dict = tf.get_term_requency_dict(text)
    tf_list.append(tf_dict)
    # print(tf_dict)

# 2. merge to one tf_dict
tf_dict = dict()
for d in tf_list:
    pass
