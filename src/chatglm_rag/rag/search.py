# -*- coding: utf-8 -*-
"""
检索模块：给定 query → 返回最相关的文本块
"""
from typing import List
import numpy as np
import faiss
from chatglm_rag.index.faiss_index import HFEmbedder


def search_chunks(
    query: str,
    index: faiss.Index,
    chunks: List[str],
    embedder: HFEmbedder,
    top_k: int = 5,
) -> List[str]:
    """
    :return: 按相关度排序后的 top_k 文本片段
    """
    q_emb: np.ndarray = embedder.encode([query]).astype("float32")
    _, idx = index.search(q_emb, k=top_k)
    return [chunks[i] for i in idx[0]]
