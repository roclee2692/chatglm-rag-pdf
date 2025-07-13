# -*- coding: utf-8 -*-
"""
PDF → 纯文本提取
"""
import os
import pdfplumber
from pathlib import Path
from typing import List


def extract_text_from_pdf(pdf_path: str | Path) -> str:
    """
    读取文字版 PDF，返回全文文本。
    若为扫描件则抛异常（留给调用方决定是否 OCR）。
    """
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF 不存在: {pdf_path}")

    text: List[str] = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                pg_txt = page.extract_text()
                if pg_txt:
                    text.append(pg_txt)
    except Exception as e:
        raise RuntimeError(f"读取 PDF 失败: {e}")

    full_text = "\n\n".join(text).strip()
    if not full_text:
        raise ValueError("未提取到任何文字，可能是扫描版 PDF")
    return full_text
