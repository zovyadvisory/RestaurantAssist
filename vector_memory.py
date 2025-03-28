import faiss
import numpy as np

class VectorMemory:
    def __init__(self, dim=384):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.vectors = []
        self.text_store = []

    def embed_text(self, text):
        # Dummy embedding: convert each character to ASCII, pad/truncate to dim
        vector = np.zeros((self.dim,), dtype='float32')
        raw = [ord(c) for c in text][:self.dim]
        vector[:len(raw)] = raw
        return vector

    def add(self, text):
        vector = self.embed_text(text)
        self.index.add(np.array([vector]))
        self.vectors.append(vector)
        self.text_store.append(text)

    def search(self, query, top_k=3):
        query_vector = self.embed_text(query).reshape(1, -1)
        D, I = self.index.search(query_vector, top_k)
        results = []
        for idx in I[0]:
            if idx < len(self.text_store):
                results.append(self.text_store[idx])
        return results

    def clear(self):
        self.index.reset()
        self.vectors = []
        self.text_store = []