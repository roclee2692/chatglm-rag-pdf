#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
解析 PDF → 切分 → 构建 FAISS 索引，保存到磁盘
"""

import argparse
import pickle
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter

from chatglm_rag.parser.pdf_parser import extract_text_from_pdf
from chatglm_rag.index.faiss_index import build_index

parser = argparse.ArgumentParser()
parser.add_argument(
    "--pdf_path",
    type=Path,
    default=r"D:\Pythonmodel\chatglm-rag-pdf\data\docs\全球股市投资研究报告.pdf",
    help="PDF 文件路径",
)
parser.add_argument(
    "--out_path",
    type=Path,
    default=Path("data/index/faiss_index.pkl"),
    help="索引文件保存路径",
)
args = parser.parse_args()

# 1. 解析 PDF
text = extract_text_from_pdf(args.pdf_path)
print(f"[√] PDF 提取完成，长度 {len(text)} 字符")

# 2. 文本切块
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=75)
chunks = splitter.split_text(text)
print(f"[√] 切分得到 {len(chunks)} 个块")

# 3. 构建索引
index, embedder = build_index(chunks)
args.out_path.parent.mkdir(parents=True, exist_ok=True)
with open(args.out_path, "wb") as f:
    pickle.dump({"index": index, "chunks": chunks}, f)
print(f"[√] 索引已保存到 {args.out_path}")
