import numpy as np
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.model import AssociationRules


class TestAssociationRules:
    def test_fit(self):
        ar = AssociationRules(min_support=0.3, min_confidence=0.5)
        transactions = ar.get_sample_transactions()
        ar.fit(transactions)
        assert len(ar.frequent_itemsets_) > 0
        assert len(ar.rules_) > 0
