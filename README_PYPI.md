# Pepkio Gene Hypothesis Roulette

Python client for the Pepkio `gene-hypothesis-roulette` tool over the REST API.

## Installation

```bash
pip install pepkio-gene-hypothesis-roulette
```

## Usage

```python
from pepkio_gene_hypothesis_roulette import PepkioClient

client = PepkioClient(api_key="your-api-key")
manifest = client.get_manifest()
print(manifest["title"])
```
