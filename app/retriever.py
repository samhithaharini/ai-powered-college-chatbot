"""
RAG Retrieval Engine — Optimized for Engineering Student Assistant
Uses enhanced keyword matching and category-specific boosting.
"""

import math
import re
from typing import List, Dict

def _tokenize(text: str) -> List[str]:
    """Lowercase, strip punctuation, split into tokens, and handle basic plurals."""
    tokens = re.findall(r"\b[a-z]{2,}\b", text.lower())
    # Basic stemming: Remove 's' at the end of words to match singular/plural (e.g., courses -> course)
    stemmed = []
    for t in tokens:
        if t.endswith('s') and len(t) > 3:
            stemmed.append(t[:-1])
        stemmed.append(t)
    return stemmed

def _score_chunk(query_tokens: List[str], chunk: Dict, idf: Dict[str, float]) -> float:
    """Enhanced scoring logic with Title priority and Engineering boosts."""
    title_tokens = _tokenize(chunk["title"])
    content_tokens = _tokenize(chunk["content"])
    keyword_tokens = _tokenize(" ".join(chunk.get("keywords", [])))
    doc_tokens = title_tokens + content_tokens + keyword_tokens
    
    tf: Dict[str, float] = {}
    for t in doc_tokens:
        tf[t] = tf.get(t, 0) + 1
    
    total = len(doc_tokens) or 1
    score = 0.0
    
    for qt in query_tokens:
        if qt in tf:
            # Base TF-IDF score
            term_score = (tf[qt] / total) * idf.get(qt, 1.0)
            
            # HIGH BOOST: If query term is in the TITLE or KEYWORDS
            if qt in title_tokens or qt in keyword_tokens:
                term_score *= 4.0
            
            score += term_score

    # ── Category & Engineering Logic ──
    category_keywords = {
        "courses": ["course", "program", "degree", "study", "branch", "department", "btech", "be", "engg", "engineering"],
        "admissions": ["admission", "apply", "fee", "eligibility", "enroll", "join"],
        "placements": ["placement", "job", "salary", "recruit", "company", "package", "career"],
    }
    
    cat = chunk.get("category", "")
    for kw in category_keywords.get(cat, []):
        if kw in query_tokens:
            score *= 2.0  # Category match boost
            break
            
    # ENGINEERING SPECIFIC BOOST
    is_eng_query = any(q in ["engineering", "btech", "be", "engineer"] for q in query_tokens)
    is_eng_chunk = "engineering" in chunk["title"].lower() or "engineering" in chunk["content"].lower()
    
    if is_eng_query and is_eng_chunk:
        score *= 3.0 # Prioritize engineering content for engineering queries
        
    return score

def _build_idf(chunks: List[Dict]) -> Dict[str, float]:
    """Compute inverse-document-frequency for all tokens in the knowledge base."""
    N = len(chunks)
    df: Dict[str, int] = {}
    for chunk in chunks:
        tokens = set(_tokenize(chunk["title"] + " " + chunk["content"]))
        for t in tokens:
            df[t] = df.get(t, 0) + 1
    return {t: math.log(N / (1 + freq)) for t, freq in df.items()}

class RAGRetriever:
    def __init__(self, chunks: List[Dict]):
        self.chunks = chunks
        self.idf = _build_idf(chunks)

    def retrieve(self, query: str, top_k: int = 8) -> List[Dict]:
        """Return the top_k most relevant chunks for the query with high recall."""
        query_tokens = _tokenize(query)
        if not query_tokens:
            return self.chunks[:top_k]
            
        scored = [
            (_score_chunk(query_tokens, chunk, self.idf), chunk)
            for chunk in self.chunks
        ]
        
        # Sort by score descending
        scored.sort(key=lambda x: x[0], reverse=True)
        
        # Return top K results that actually matched (score > 0)
        results = [chunk for score, chunk in scored[:top_k] if score > 0]
        
        # Fallback: if no matches, return top k anyway
        return results if results else self.chunks[:top_k]

    def build_context(self, query: str, top_k: int = 8) -> str:
        """Return a formatted context string from the top relevant chunks."""
        chunks = self.retrieve(query, top_k)
        parts = []
        for c in chunks:
            parts.append(f"[{c['title']}]\n{c['content']}")
        return "\n\n".join(parts)
