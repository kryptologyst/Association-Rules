from loguru import logger

def load_data():
    from .model import AssociationRules
    ar = AssociationRules()
    transactions = ar.get_sample_transactions()
    logger.info(f"Loaded {len(transactions)} transactions")
    return transactions
