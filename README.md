# ChatGLM + RAG PDF QA

本项目是一个基于 ChatGLM + RAG 的本地 PDF 文档问答系统。  
支持对本地 PDF 文档进行分块、向量化索引、检索以及问答和总结。

---

## Project Structure

```text
chatglm-rag-pdf/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
│
├── notebooks/
│   └── 01_prototype.ipynb
│
├── data/
│   ├── docs/
│   └── index/
│
├── src/
│   └── chatglm_rag/
│        ├── __init__.py
│        ├── config.py
│        ├── parser/
│        │     └── pdf_parser.py
│        ├── index/
│        │     └── faiss_index.py
│        └── rag/
│              └── chatglm_rag.py
│
├── scripts/
│   ├── build_index.py
│   └── query.py
│
├── tests/
│   └── test_index.py
│
├── examples/
│   └── sample_run.sh
│
├── .github/
│   └── workflows/ci.yml
└── setup.py / pyproject.toml
```

---

## Quick Start

```bash
pip install -e .
pip install -r requirements.txt
```

