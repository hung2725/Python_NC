import math
from pprint import pprint

train = [
    (4.6, 3.2, 1.4, 0.2, "Iris-setosa"),
    (5.3, 3.7, 1.5, 0.2, "Iris-setosa"),
    (5.0, 3.3, 1.4, 0.2, "Iris-setosa"),
    (7.0, 3.2, 4.7, 1.4, "Iris-versicolor"),
    (6.4, 3.2, 4.5, 1.5, "Iris-versicolor"),
    (6.9, 3.1, 4.9, 1.5, "Iris-versicolor"),
    (6.3, 3.3, 6.0, 2.5, "Iris-virginica"),
    (5.8, 2.7, 5.1, 1.9, "Iris-virginica"),
    (7.1, 3.0, 5.9, 2.1, "Iris-virginica")
]

queries = [
    (5.0, 2.4, 3.5, 1.1),
    (4.1, 3.0, 2.1, 1.0)
]

def euclid(a,b):
    return math.sqrt(sum((ai-bi)**2 for ai,bi in zip(a,b)))

def knn_predict(xq, train, k=3):
    dists = []
    for x1,x2,x3,x4,label in train:
        d = euclid(xq, (x1,x2,x3,x4))
        dists.append((d, label, (x1,x2,x3,x4)))
    dists.sort(key=lambda t: t[0])
    neighbors = dists[:k]
    votes = {}
    for d,label,_ in neighbors:
        votes[label] = votes.get(label,0) + 1
    pred = max(votes.items(), key=lambda t: t[1])[0]
    return pred, neighbors, votes
results = []
for q in queries:
    pred, neighbors, votes = knn_predict(q, train, k=3)
    results.append((q, pred, neighbors, votes))
for i,(q,pred,neighbors,votes) in enumerate(results, start=1):
    print(f"Query {i}: {q}")
    print("3 láng giềng gần nhất (distance, label, features):")
    pprint(neighbors)
    print("Votes:", votes,"\n")
    print("Dự đoán:", pred)
print("💵")