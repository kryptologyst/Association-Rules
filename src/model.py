import numpy as np
import pandas as pd
from itertools import combinations
from loguru import logger


class AssociationRules:
    def __init__(self, min_support: float = 0.3, min_confidence: float = 0.5):
        self.min_support = min_support
        self.min_confidence = min_confidence
        self.frequent_itemsets_: dict = {}
        self.rules_: list = []

    def fit(self, transactions: list) -> "AssociationRules":
        n = len(transactions)
        items = sorted(set(item for t in transactions for item in t))
        freq1 = {}
        for item in items:
            support = sum(1 for t in transactions if item in t) / n
            if support >= self.min_support:
                freq1[frozenset([item])] = support
        self.frequent_itemsets_ = freq1
        k = 2
        current = freq1
        while current:
            candidates = {}
            itemsets = list(current.keys())
            for i in range(len(itemsets)):
                for j in range(i + 1, len(itemsets)):
                    candidate = itemsets[i] | itemsets[j]
                    if len(candidate) == k:
                        support = sum(1 for t in transactions if candidate.issubset(t)) / n
                        if support >= self.min_support:
                            candidates[candidate] = support
            if candidates:
                self.frequent_itemsets_.update(candidates)
            current = candidates
            k += 1
        self._generate_rules(n)
        logger.info(f"Association rules: {len(self.frequent_itemsets_)} itemsets, {len(self.rules_)} rules")
        return self

    def _generate_rules(self, n):
        for itemset, support in self.frequent_itemsets_.items():
            if len(itemset) < 2:
                continue
            for i in range(1, len(itemset)):
                for ant in combinations(itemset, i):
                    ant_set = frozenset(ant)
                    cons_set = itemset - ant_set
                    ant_support = self.frequent_itemsets_.get(ant_set, 0)
                    if ant_support > 0:
                        confidence = support / ant_support
                        if confidence >= self.min_confidence:
                            self.rules_.append({
                                "antecedent": set(ant_set),
                                "consequent": set(cons_set),
                                "support": round(support, 4),
                                "confidence": round(confidence, 4),
                            })

    def get_sample_transactions(self):
        return [
            ["bread", "milk"],
            ["bread", "diapers", "beer", "eggs"],
            ["milk", "diapers", "beer", "cola"],
            ["bread", "milk", "diapers", "beer"],
            ["bread", "milk", "diapers", "cola"],
        ]
