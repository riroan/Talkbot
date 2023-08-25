from math import log
from collections import defaultdict

def get_tfidf(a, b):
    arr = a.split()
    brr = b.split()
    tf_a = defaultdict(int)
    tf_b = defaultdict(int)
    s = set()
    for i in arr:
        tf_a[i]+=1
        s.add(i)
    for i in brr:
        tf_b[i] += 1
        s.add(i)
    df = defaultdict(int)
    for i in arr + brr:
        df[i] += 1
    idf = {}
    for i in df:
        idf[i] = log(3 / (df[i] + 1)) + 1
    tfidf_a = {}
    tfidf_b = {}
    for i in s:
        tfidf_a[i] = tf_a[i] * idf[i]
        tfidf_b[i] = tf_b[i] * idf[i]
    return tfidf_a, tfidf_b

def get_cosinesimilarity(a, b):
    up = 0
    down = 0
    aa = 0
    bb = 0
    for i in a:
        up += a[i] * b[i]
        aa += a[i] ** 2
        bb += b[i] ** 2
    down = aa **.5 * bb**.5 + 1e-5
    return up / down

def get_score(a,b):
    tfidf_a, tfidf_b = get_tfidf(a,b)
    return get_cosinesimilarity(tfidf_a, tfidf_b)

document = []

with open("data/talk.txt", "r") as f:
    while 1:
        s = f.readline().strip()
        if s == "THE END":
            break
        arr = s.split(":")[2:]
        s = ":".join(arr)
        document.append(s)

def get_next_answer(inp):
    ma = 0
    ix = 0
    for i in range(len(document)):
        score = get_score(document[i], inp)
        if score > ma:
            ma = score
            ix = i
    return document[(ix+1)%len(document)].strip()

