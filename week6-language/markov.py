"""Simple Markov chain text generator."""

import random
from collections import defaultdict
from typing import Dict, List


def build_model(text: str) -> Dict[str, List[str]]:
    model = defaultdict(list)
    words = text.split()
    for i in range(len(words) - 1):
        model[words[i]].append(words[i + 1])
    return model


def generate(model: Dict[str, List[str]], start: str, length: int = 20) -> str:
    word = start
    output = [word]
    for _ in range(length - 1):
        next_words = model.get(word)
        if not next_words:
            break
        word = random.choice(next_words)
        output.append(word)
    return ' '.join(output)


def main():
    text = "the quick brown fox jumps over the lazy dog the quick blue hare" \
           " jumps over the sleepy cat"
    model = build_model(text)
    print(generate(model, 'the', 10))


if __name__ == '__main__':
    main()
