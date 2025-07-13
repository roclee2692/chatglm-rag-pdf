# -*- coding: utf-8 -*-
"""
RAG 查询：检索 + 生成
这里只给检索 + 返回片段，后续可接 ChatGLM。
"""
from typing import List
import faiss
from sentence_transformers import SentenceTransformer


def search_chunks(
    query: str,
    index: faiss.Index,
    chunks: List[str],
    embedder: SentenceTransformer,
    top_k: int = 5,
) -> List[str]:
    """
    返回最相关的 top_k 文本块
    """
    q_emb = embedder.encode([query]).astype("float32")
    distances, indices = index.search(q_emb, k=top_k)
    return [chunks[i] for i in indices[0]]
