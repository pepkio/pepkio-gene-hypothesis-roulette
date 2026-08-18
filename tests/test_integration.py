"""Integration tests against live Pepkio Tools API."""

from __future__ import annotations

import os

import pytest

from pepkio_gene_hypothesis_roulette.client import PepkioClient

ENVIRONMENTS = [
    ("local", "https://tools.localtest.me"),
    ("production", "https://tools.pepkio.com"),
]


def _api_key_for(base_url: str) -> str | None:
    if "localtest.me" in base_url:
        return os.getenv("LOCAL_PEPKIO_API_KEY") or os.getenv("PEPKIO_API_KEY")
    return os.getenv("PEPKIO_API_KEY")


@pytest.fixture(params=ENVIRONMENTS, ids=["local", "production"])
def live_client(request):
    env_name, base_url = request.param
    api_key = _api_key_for(base_url)
    if not api_key:
        pytest.skip(f"No API key for {env_name} (set LOCAL_PEPKIO_API_KEY or PEPKIO_API_KEY)")
    with PepkioClient(api_key=api_key, base_url=base_url) as client:
        yield client


def test_get_manifest(live_client: PepkioClient):
    manifest = live_client.get_manifest(refresh=True)
    assert manifest["tool_id"] == "gene-hypothesis-roulette"
    names = live_client.list_examples()
    assert "suggest_brca" in names
    assert "fetch_tp53" in names


def test_run_suggest_example(live_client: PepkioClient):
    inp = live_client.get_example_input("suggest_brca")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.run_id
    assert result.permalink
    assert result.result is not None
    assert isinstance(result.result.get("suggestions"), list)


def test_run_fetch_tp53_example(live_client: PepkioClient):
    inp = live_client.get_example_input("fetch_tp53")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.run_id
    assert result.result is not None
    assert "gene" in result.result
    assert result.result["gene"].get("symbol") == "TP53"


def test_get_run_by_id(live_client: PepkioClient):
    inp = live_client.get_example_input("suggest_brca")
    result1 = live_client.run(inp)
    assert result1.run_id
    result2 = live_client.get_run(result1.run_id)
    assert result2.run_id == result1.run_id
    assert result2.status == "completed"
