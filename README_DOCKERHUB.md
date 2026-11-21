# Pepkio Gene Hypothesis Roulette

Run the Pepkio gene-hypothesis-roulette CLI in a container to aggregate multi-omics context and generate citation-backed hypothesis cards without a local Python setup.

# What It Does

The image runs `pepkio-gene-hypothesis-roulette`, a client for the Pepkio Gene Hypothesis Roulette REST API. Submit gene queries to resolve symbols and identifiers, retrieve unified multi-omics functional annotations (MyGene.info pathways, ClinGen diseases, STRING interactors), sample structured hypothesis cards exploring pathway crosstalk or synthetic lethality, pin concepts to a research board, and export structured validation briefs.

Typical workflows include RNA-seq and scRNA-seq hit follow-up, CRISPR screen candidate validation planning, GWAS locus functional annotation, and drug repurposing ideation. Calculator and aggregation logic runs on Pepkio servers; provide a network connection and API key for `run` commands.

# Features

- Gene search and identifier resolution across HGNC symbols, Ensembl IDs, and UniProt accessions (`suggest`)
- Multi-omics functional context aggregation covering diseases, pathways, and interactors (`fetch_gene`)
- Exploratory hypothesis cards sampling pathway crosstalk and synthetic lethality ("roulette" mode)
- Pinboard collator with structured validation brief export (`export_txt`)
- Named manifest examples (`suggest_brca`, `fetch_tp53`, `export_txt_empty`)
- Manifest inspection without an API key

# Quick Start

```bash
docker pull pepkio/gene-hypothesis-roulette:0.1.0
docker run --rm -e PEPKIO_API_KEY="your-key" pepkio/gene-hypothesis-roulette:0.1.0 \
  pepkio-gene-hypothesis-roulette run --example fetch_tp53
```

Manifest only (no API key):

```bash
docker run --rm pepkio/gene-hypothesis-roulette:0.1.0 \
  pepkio-gene-hypothesis-roulette manifest --examples
```

Set `PEPKIO_API_BASE_URL` to override the API host (default: `https://tools.pepkio.com`). Create an API key with **tools:run** scope at https://www.pepkio.com/account/api-keys.

# Quick Example

```bash
docker run --rm -e PEPKIO_API_KEY="$PEPKIO_API_KEY" pepkio/gene-hypothesis-roulette:0.1.0 \
  pepkio-gene-hypothesis-roulette run --input-json \
  '{"action":"fetch_gene","gene_symbol":"TP53"}'
```

# Typical Use Cases

- RNA-seq and single-cell transcriptomic hit prioritization for under-studied genes
- CRISPR-Cas9 functional screen follow-up and mechanistic hypothesis formulation
- GWAS locus functional annotation and disease-pathway linkage
- Synthetic lethality and compensatory signaling loop exploration
- Validation assay protocol planning (RT-qPCR, Western blot, ChIP-seq)

# Scientific Background

High-throughput screens often highlight candidate genes subject to literature bias ("streetlamp effect"). Multi-omics integration unifies HGNC nomenclature, Ensembl genomic loci, UniProt protein accessions, Gene Ontology classifications, and KEGG/Reactome pathway models. Over-representation analysis evaluates candidate gene enrichment in pathways using the hypergeometric distribution, while contingency odds ratios quantify gene-disease association strength.

# Web Application

For researchers who prefer a graphical interface, an interactive web version is available.

Web Application: https://www.pepkio.com/tools/gene-hypothesis-roulette

The web interface features interactive autocomplete, visual pinboards for hypothesis cards, live pathway mapping, shareable permalinks, and downloadable ELN worksheets.

# Documentation and Resources

GitHub Repository (source and Dockerfile): https://github.com/pepkio/pepkio-gene-hypothesis-roulette

Web Application: https://www.pepkio.com/tools/gene-hypothesis-roulette

# About Pepkio

Pepkio (https://www.pepkio.com/) develops software tools and bioinformatics solutions for life science researchers, including laboratory calculators and analysis services (https://www.pepkio.com/cro).

A semantic, AI-native version of this document in the K2F format is available at https://k2f.dev (https://k2f.dev/v/eef3ed31a168d2bcac19750d0f54f024caf8f89e9ea71ec2ef12fceed0254999)
