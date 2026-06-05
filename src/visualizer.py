import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from typing import Optional
from loguru import logger


class ARVisualizer:
    @staticmethod
    def plot_rules(rules, save_path=None):
        if not rules:
            return
        plt.figure(figsize=(10, 5))
        supports = [r["support"] for r in rules]
        confidences = [r["confidence"] for r in rules]
        plt.scatter(supports, confidences, s=100, c="steelblue", edgecolors="k")
        plt.xlabel("Support"); plt.ylabel("Confidence")
        plt.title("Association Rules — Support vs Confidence")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches="tight")
        plt.close()
