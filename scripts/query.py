#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
命令行查询：加载索引 → 检索相关片段
"""

import argparse
import pickle
from pathlib import Path
from sentence_transformers import SentenceTransformer
from chatglm_rag.rag.chatglm_rag import search_chunks

parser = argparse.ArgumentParser()
parser.add_argument(
    "--index_path",
    type=Path,
    default=Path("data/index/faiss_index.pkl"),
    help="build_index.py 生成的索引文件",
)
parser.add_argument("--question", "-q", required=True, help="你的问题")
args = parser.parse_args()

with open(args.index_path, "rb") as f:
    saved = pickle.load(f)

index = saved["index"]
chunks = saved["chunks"]

embedder = SentenceTransformer("shibing624/text2vec-base-chinese")

results = search_chunks(args.question, index, chunks, embedder, top_k=5)
print("\n=== 最相关片段 ===")
for i, seg in enumerate(results, 1):
    print(f"\n--- Top {i} ---\n{seg}")
