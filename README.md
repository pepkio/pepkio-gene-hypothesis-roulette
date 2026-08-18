# Pepkio Gene Hypothesis Roulette

Python client for the Pepkio `gene-hypothesis-roulette` tool over the REST API.

## Installation

```bash
pip install pepkio-gene-hypothesis-roulette
```

## Quick Start

```python
from pepkio_gene_hypothesis_roulette import PepkioClient

client = PepkioClient(api_key="your-api-key")

# Fetch gene data for TP53
result = client.run({"action": "fetch_gene", "gene_symbol": "TP53"})
print(result.status, result.result)
```
