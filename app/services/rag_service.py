from typing import Any, Dict, List, Union, Optional

import numpy as np
import re

from bson import ObjectId
from pythainlp import word_tokenize

from langfuse.decorators import observe

from app import collection, search_index_name
from app.services.llm_calls import generate_query_embedding


def weighted_reciprocal_rank(doc_lists: List[List[dict]]) -> List[dict]:
    """
    Perform weighted Reciprocal Rank Fusion on multiple rank lists.
    From https://medium.com/@rossashman/the-art-of-rag-with-atlas-part-2-hybrid-retrieval-77631457b565

    Args:
        doc_lists (List[List[dict]]): A list of ranked documents from different search sources.

    Returns:
        List[dict]: The aggregated list of documents sorted by their RRF scores in descending order.
    """
    c = 60
    weights = [1] * len(doc_lists)

    if len(doc_lists) != len(weights):
        raise ValueError('Number of rank lists must be equal to the number of weights.')

    # Create a union of all unique documents in the input doc_lists
    all_documents = set()
    for doc_list in doc_lists:
        for doc in doc_list:
            all_documents.add(doc['_id'])

    # Initialize the RRF score dictionary for each document
    rrf_score_dic = {doc: 0.0 for doc in all_documents}

    # Calculate RRF scores for each document
    for doc_list, weight in zip(doc_lists, weights, strict=False):
        for rank, doc in enumerate(doc_list, start=1):
            rrf_score = weight * (1 / (rank + c))
            rrf_score_dic[doc['_id']] += rrf_score

    # Sort documents by their RRF scores in descending order
    sorted_documents = sorted(rrf_score_dic.keys(), key=lambda x: rrf_score_dic[x], reverse=True)

    # Map the sorted page_content back to the original document objects
    page_content_to_doc_map = {doc['_id']: doc for doc_list in doc_lists for doc in doc_list}
    sorted_docs = [page_content_to_doc_map[page_content] for page_content in sorted_documents]

    return sorted_docs


async def perform_hybrid_search(
        query: str,
) -> list[dict[str, Any]]:
    """
    Perform hybrid search, combining vector and keyword search using RRF.

    Args:
        query (str): The input search query.

    Returns:
        List[dict]: A list of reranked article documents based on hybrid search.
    """
    print(f"--- Performing Article Search for: '{query}' ---")

    top_k = 7
    vector_results, keyword_results = [], []

    # Perform Vector Search
    try:
        query_vector = await generate_query_embedding(query)
        vector_cursor = collection.aggregate([
            {
                '$vectorSearch': {
                    'queryVector': query_vector,
                    'path': 'embedding',
                    'numCandidates': top_k * 2,
                    'limit': top_k * 2,
                    'index': search_index_name,
                }
            },
            {'$project': {
                '_id': 1,
                'chunk_id': 1,
                'source_document': 1,
                'contextual_summary': 1,
                'chunk_content': 1,
                'score': {'$meta': 'vectorSearchScore'},
                }
            }
        ])
        vector_results = list(vector_cursor)
        # print(f"[Vector Search] Retrieved {len(vector_results)} results.")
        # for i in vector_results: print(f"Vector search results: {i.get('chunk_content', 'No Content')[:40]} - Score: {i.get('score', 'No Score')}")
    except Exception as e:
        print(f"[Error] Article Semantic Search failed: {e}")

    # Perform Keyword Search
    try:
        tokenized_query = word_tokenize(query)
        print(f"Tokenized query for keyword search: {tokenized_query}")
        
        keyword_cursor = collection.aggregate([
            {
                '$search': {
                    'index': search_index_name,
                    'compound': {
                        'should': [
                            {'text': {'query': tokenized_query, 'path': 'tokenized_content', 'score': {'boost': {'value': 1}}}},
                        ],
                        'minimumShouldMatch': 1
                    }
                }
            },
            {'$project': {
                '_id': 1,
                'chunk_id': 1,
                'contextual_summary': 1,
                'source_document': 1,
                'chunk_content': 1,
                'score': {'$meta': 'searchScore'},
                }
            },
            {'$limit': top_k * 2}
        ])
        keyword_results = list(keyword_cursor)
        # print(f"[Keyword Search] Retrieved {len(keyword_results)} results.")
        # for i in keyword_results: print(f"Keyword search results: {i.get('chunk_content', 'No Content')[:40]} - Score: {i.get('score', 'No Score')}")
    except Exception as e:
        print(f"[Error] Article Keyword Search failed: {e}")

    # Perform Rank Fusion
    try:
        doc_lists = []
        if vector_results:
            doc_lists.append(vector_results)
        if keyword_results:
            doc_lists.append(keyword_results)
        
        if not doc_lists:
            print("No results from any search source to fuse.")
            return []

        # Apply rank fusion
        fused_documents = weighted_reciprocal_rank(doc_lists)[:top_k]
        return fused_documents[:top_k]

    except Exception as e:
        print(f"Error fetching full article documents: {e}")
        return []
