import load
import jieba

exclusion_list = '，。、！？：；「」'

# 1. load file
news = load.load('6be5022461f84565aca6f2ec24e8b1ca')
# print(news.get_content())
text = news.get_content()

# 2. 用結巴斷詞
seg_list = list(jieba.cut(text))
# print('總共 %d 個詞' % len(seg_list))

# 3. 取得詞與數量的 dictionary，並計算 total frequency
total_frequency = 0
word_dict = dict()
for word in seg_list:
    if word in exclusion_list:
        continue

    total_frequency += 1
    if word not in word_dict:
        word_dict[word] = 1
    else:
        count = word_dict[word]
        word_dict[word] = count + 1

# 4.
c = 0

tf_dict = dict()
for w in word_dict:
    count = word_dict[w]
    tf = count / total_frequency
    tf_dict[w] = tf
    print('%s: %.3f' % (w, tf))
    c += tf
# tf_dict[w] = freq

print('c=', c)

# 4. get total frequency
# total_frequency = 0
# for i in word_dict:
    # print('%s: %d' % (i, word_dict[i]))

# total_frequency += word_dict[i]
print('total frequency=%d' % total_frequency)

# 4. 計算 term frequency




'''
class WordCount:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def get_word(self):
        return self.word

    def get_count(self):
        return self.count

word_list = list()
for word, count in word_dict.items():
    word_list.append(WordCount(word, count))

print(word_list)
word_list.sort(key=lambda x: x.count, reverse=True)


for w in word_list:
    print(w.get_word(), w.get_count())
'''
