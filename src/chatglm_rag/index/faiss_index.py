# -*- coding: utf-8 -*-
"""
文本块 → 向量 → FAISS 索引
"""
from typing import List, Tuple
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer


def build_index(
    chunks: List[str],
    model_name: str = "shibing624/text2vec-base-chinese",
) -> Tuple[faiss.IndexFlatL2, SentenceTransformer]:
    """
    返回 (faiss 索引, 向量化模型)；索引用 L2
    """
    model = SentenceTransformer(model_name)
    embeddings = model.encode(chunks, show_progress_bar=True, batch_size=64)
    embeddings = np.asarray(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, model
