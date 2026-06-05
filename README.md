# Association Rules

**Market basket analysis** with Apriori-like frequent itemset mining.

## Overview

- Frequent itemset discovery with configurable support
- Association rule generation with confidence threshold
- Support vs confidence scatter plot
- **Streamlit dashboard**

## Quick Start

```bash
pip install -r requirements.txt
streamlit run app.py
# CLI: python -m src.main mine --min-support 0.3
pytest tests/ -v
```

## Docker

```bash
docker compose up --build
```

## License

MIT
# Association-Rules
