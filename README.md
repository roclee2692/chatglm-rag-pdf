# ChatGLM + RAG PDF QA

🚀 A local document QA system built on ChatGLM and Retrieval-Augmented Generation (RAG) architecture.  
It enables question answering and summarization over your own PDF documents, leveraging vector search (FAISS) and language models.

本项目是一个基于 ChatGLM + RAG 的本地 PDF 文档问答系统。  
支持对本地 PDF 文档进行分块、向量化索引、检索以及问答和总结。

---

## Features

✅ Parse PDF files into text  
✅ Split text into chunks for indexing  
✅ Vectorize text chunks using Sentence Transformers  
✅ Build a FAISS index for fast semantic search  
✅ Query relevant document fragments with natural language questions  
✅ Generate answers or summaries using ChatGLM  
✅ Fully local operation, keeping your data private

---
## Project Structure

<pre> ```text chatglm-rag-pdf/ ├── README.md ├── LICENSE ├── .gitignore ├── requirements.txt │ ├── notebooks/ │ └── 01_prototype.ipynb │ ├── data/ │ ├── docs/ │ └── index/ │ ├── src/ │ └── chatglm_rag/ │ ├── __init__.py │ ├── config.py │ ├── parser/ │ │ └── pdf_parser.py │ ├── index/ │ │ └── faiss_index.py │ └── rag/ │ └── chatglm_rag.py │ ├── scripts/ │ ├── build_index.py │ └── query.py │ ├── tests/ │ └── test_index.py │ ├── examples/ │ └── sample_run.sh │ ├── .github/ │ └── workflows/ci.yml └── setup.py / pyproject.toml ``` </pre>

---

## Quick Start

### Install

```bash
pip install -e .
pip install -r requirements.txt
Build Index
python scripts/build_index.py --pdf_path data/docs/your_pdf.pdf
Query
python scripts/query.py --question "这篇文章讲了什么？"



