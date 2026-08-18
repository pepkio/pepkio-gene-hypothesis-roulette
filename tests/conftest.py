"""Test fixtures for pepkio-gene-hypothesis-roulette."""

from __future__ import annotations

import pytest
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(usecwd=True))


@pytest.fixture
def mock_manifest():
    return {
        "schema_version": "1.0",
        "tool_id": "gene-hypothesis-roulette",
        "title": "Gene Hypothesis Roulette",
        "description": "Hypothesis generator",
        "execution_mode": "sync",
        "examples": [
            {
                "name": "suggest_brca",
                "input": {"action": "suggest", "query": "BRCA"},
                "output": {"suggestions": []},
            },
            {
                "name": "fetch_tp53",
                "input": {"action": "fetch_gene", "gene_symbol": "TP53"},
                "output": {"gene": {"symbol": "TP53"}},
            },
            {
                "name": "export_txt_empty",
                "input": {"action": "export_txt", "gene_symbol": "TP53", "pinned_cards": []},
                "output": {"filename": "gene-hypothesis-pinboard-TP53.txt"},
            },
        ],
    }


@pytest.fixture
def mock_run_response():
    return {
        "run_id": "test_run_123",
        "status": "completed",
        "result": {
            "gene": {"symbol": "TP53"},
            "diseases": [],
            "pathways": [],
        },
        "error": None,
        "result_url": "https://tools.pepkio.com/api/tools/v1/runs/test_run_123",
        "permalink": "https://tools.pepkio.com/r/test_run_123",
        "duration_ms": 150,
    }
