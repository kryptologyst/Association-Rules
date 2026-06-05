import typer
import sys
from loguru import logger

from .config import settings
from .data import load_data
from .model import AssociationRules
from .visualizer import ARVisualizer

app = typer.Typer(help="Association Rules CLI")
logger.remove()
logger.add(sys.stderr, level=settings.log_level)


@app.command()
def mine(min_support: float = typer.Option(0.3, help="Minimum support"),
         min_confidence: float = typer.Option(0.5, help="Minimum confidence")):
    logger.info(f"Mining association rules (support>={min_support}, confidence>={min_confidence})...")
    transactions = load_data()
    ar = AssociationRules(min_support=min_support, min_confidence=min_confidence)
    ar.fit(transactions)
    logger.info(f"Found {len(ar.rules_)} rules:")
    for r in ar.rules_:
        logger.info(f"  {r['antecedent']} → {r['consequent']} (s={r['support']:.2f}, c={r['confidence']:.2f})")
    ARVisualizer.plot_rules(ar.rules_, save_path=settings.plots_dir / "association_rules.png")
    logger.success("Done!")


if __name__ == "__main__":
    app()
