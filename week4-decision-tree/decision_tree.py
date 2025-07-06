"""Simple decision tree classifier for demonstration."""

from collections import Counter
from typing import Any, List, Dict, Tuple

Dataset = List[Dict[str, Any]]


def entropy(labels: List[Any]) -> float:
    total = len(labels)
    counts = Counter(labels)
    from math import log2
    return -sum((c / total) * log2(c / total) for c in counts.values())


def majority(labels: List[Any]) -> Any:
    return Counter(labels).most_common(1)[0][0]


def split(dataset: Dataset, feature: str) -> Dict[Any, Dataset]:
    result: Dict[Any, Dataset] = {}
    for row in dataset:
        key = row[feature]
        result.setdefault(key, []).append(row)
    return result


def choose_feature(dataset: Dataset, features: List[str]) -> str:
    base_labels = [row['label'] for row in dataset]
    base_entropy = entropy(base_labels)
    best_gain = -1
    best_feature = features[0]
    for f in features:
        groups = split(dataset, f)
        new_entropy = sum(
            len(group) / len(dataset) * entropy([r['label'] for r in group])
            for group in groups.values()
        )
        gain = base_entropy - new_entropy
        if gain > best_gain:
            best_gain = gain
            best_feature = f
    return best_feature


def build_tree(dataset: Dataset, features: List[str]):
    labels = [row['label'] for row in dataset]
    if len(set(labels)) == 1:
        return labels[0]
    if not features:
        return majority(labels)
    best = choose_feature(dataset, features)
    tree = {best: {}}
    for value, subset in split(dataset, best).items():
        remaining = [f for f in features if f != best]
        tree[best][value] = build_tree(subset, remaining)
    return tree


def predict(tree, sample: Dict[str, Any]):
    if not isinstance(tree, dict):
        return tree
    feature = next(iter(tree))
    value = sample.get(feature)
    subtree = tree[feature].get(value)
    if subtree is None:
        return None
    return predict(subtree, sample)


def main():
    data = [
        {'outlook': 'sunny', 'temp': 'hot', 'windy': False, 'label': 'no'},
        {'outlook': 'sunny', 'temp': 'hot', 'windy': True, 'label': 'no'},
        {'outlook': 'overcast', 'temp': 'hot', 'windy': False, 'label': 'yes'},
        {'outlook': 'rain', 'temp': 'mild', 'windy': False, 'label': 'yes'},
        {'outlook': 'rain', 'temp': 'cool', 'windy': False, 'label': 'yes'},
        {'outlook': 'rain', 'temp': 'cool', 'windy': True, 'label': 'no'},
    ]
    features = ['outlook', 'temp', 'windy']
    tree = build_tree(data, features)
    print('Decision tree:', tree)
    sample = {'outlook': 'sunny', 'temp': 'cool', 'windy': True}
    print('Prediction for', sample, ':', predict(tree, sample))


if __name__ == '__main__':
    main()
