# coding=utf-8
import codecs
import math
import networkx as nx
import numpy as np
import re
import jieba

__author__ = 'jayvee'


def cal_sim(wordlist1, wordlist2):
    """
    给定两个句子的词列表，计算句子相似度。计算公式参考Textrank论文
    :param wordlist1:
    :param wordlist2:
    :return:
    """
    co_occur_sum = 0
    wordset1 = list(set(wordlist1))
    wordset2 = list(set(wordlist2))
    for word in wordset1:
        if word in wordset2:
            co_occur_sum += 1.0
    if co_occur_sum < 1e-12:  # 防止出现0的情况
        return 0.0
    denominator = math.log(len(wordset1)) + math.log(len(wordset2))
    if abs(denominator) < 1e-12:
        return 0.0
    return co_occur_sum / denominator


def text_rank(sentences, num=10, pagerank_config={'alpha': 0.85, }):
    """
    对输入的句子进行重要度排序
    :param sentences: 句子的list
    :param num: 希望输出的句子数
    :param pagerank_config: pagerank相关设置，默认设置阻尼系数为0.85
    :return:
    """
    sorted_sentences = []
    sentences_num = len(sentences)
    wordlist = []  # 存储wordlist避免重复分词，其中wordlist的顺序与sentences对应
    for sent in sentences:
        tmp = []
        cur_res = jieba.cut(sent)
        for i in cur_res:
            tmp.append(i)
        wordlist.append(tmp)
    graph = np.zeros((sentences_num, sentences_num))
    for x in xrange(sentences_num):
        for y in xrange(x, sentences_num):
            similarity = cal_sim(wordlist[x], wordlist[y])
            graph[x, y] = similarity
            graph[y, x] = similarity

    nx_graph = nx.from_numpy_matrix(graph)
    scores = nx.pagerank(nx_graph, **pagerank_config)  # this is a dict
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)

    for index, score in sorted_scores:
        item = {"sent": sentences[index], 'score': score, 'origin_index': index}
        sorted_sentences.append(item)

    return sorted_sentences[:num]


def split_sentences(full_text):
    sents = re.split(u'[。;；？!！\n\.\?]', full_text)
    sents = [sent for sent in sents if len(sent) > 0]  # 去除只包含\n或空白符的句子
    return sents


def extract_abstracts(full_text, sent_num=10):
    """
    摘要提取的入口函数，并根据textrank结果进行摘要组织
    :param full_text:
    :param sent_num:
    :return:
    """
    sents = split_sentences(full_text)
    trank_res = text_rank(sents, num=sent_num)
    sorted_res = sorted(trank_res, key=lambda x: x['index'], reverse=False)
    return sorted_res


if __name__ == '__main__':
    a = u'laksjfkajslf!dlkajdlkf！大分类。的刷.卡机奥拉夫；大声 ？附近空?大方。'
    split_sentences(a)
    raw_text = codecs.open('/Users/jayvee/github_project/DocumentsAbstractProject/static/text', 'r', 'utf8').read()
    res = extract_abstracts(raw_text, sent_num=5)
    ab = ''
    for s in res:
        print s['score'], s['sent']
        ab += s['sent'] + u'。'
    print ab
