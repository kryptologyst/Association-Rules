import streamlit as st
import pandas as pd
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from src.data import load_data
from src.model import AssociationRules

st.set_page_config(page_title="Association Rules", page_icon="🔍", layout="wide")
st.title("🔍 Association Rules")
st.markdown("Market basket analysis — discover frequent itemsets and association rules.")

transactions = load_data()
st.write("Sample transactions:", transactions)

c1, c2 = st.columns(2)
with c1:
    min_support = st.slider("Min Support", 0.1, 1.0, 0.3, 0.05)
with c2:
    min_confidence = st.slider("Min Confidence", 0.1, 1.0, 0.5, 0.05)

if st.button("Mine Rules", type="primary"):
    ar = AssociationRules(min_support=min_support, min_confidence=min_confidence)
    ar.fit(transactions)
    st.metric("Frequent Itemsets", len(ar.frequent_itemsets_))
    st.metric("Rules Found", len(ar.rules_))
    if ar.rules_:
        df = pd.DataFrame(ar.rules_)
        df["antecedent"] = df["antecedent"].apply(str)
        df["consequent"] = df["consequent"].apply(str)
        st.dataframe(df, use_container_width=True)
