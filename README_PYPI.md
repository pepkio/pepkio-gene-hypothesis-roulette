# Pepkio Gene Hypothesis Roulette

A Python client and bioinformatic tool for aggregating multi-omics context, exploring non-obvious gene-disease relationships, and generating testable biological hypothesis cards for candidate gene lists.

# What It Does

High-throughput biological screens—such as bulk RNA-seq, single-cell RNA-seq, GWAS, and pooled CRISPR knockouts—regularly produce candidate gene lists containing poorly annotated or under-studied genes. Literature bias often concentrates research effort on well-characterized targets, making hypothesis formulation difficult.

The **Pepkio Gene Hypothesis Roulette** integrates multi-omics annotations from HGNC, Ensembl, UniProt, Gene Ontology (GO), KEGG, Reactome, ClinVar, and STRING protein interaction networks. It enables researchers to resolve gene identifiers, retrieve functional contexts, sample structured hypothesis cards ("roulette" mode) for pathway crosstalk and synthetic lethality, pin promising concepts to a research board, and export formatted validation briefs.

# Features

* **Gene Search & ID Resolution**: Search and resolve HGNC gene symbols, Ensembl gene IDs (`ENSG`), UniProt accessions, and synonyms (`suggest`).
* **Multi-Omics Context Aggregation**: Fetch unified gene summaries, sub-cellular localizations, tissue expression profiles, disease links, and pathways (`fetch_gene`).
* **Exploratory Hypothesis Generation**: Sample hypothesis cards exploring pathway crosstalk, synthetic lethality, and regulatory feedback loops ("roulette" mode).
* **Pinboard & Brief Export**: Collate selected hypothesis cards and export structured summaries (`export_txt`) for lab notebooks or experimental planning.
* **Python API & CLI**: Fully typed `PepkioClient` supporting synchronous execution, polling, and command-line execution (`pepkio-gene-hypothesis-roulette`).

# Installation

Install the package from PyPI using `pip`:

```bash
pip install pepkio-gene-hypothesis-roulette
```

# Quick Example

Query gene annotations and export a hypothesis brief using the Python client:

```python
from pepkio_gene_hypothesis_roulette import PepkioClient

# Initialize client (uses PEPKIO_API_KEY environment variable if set)
with PepkioClient() as client:
    # 1. Search for gene symbol suggestions
    suggestions = client.run({"action": "suggest", "query": "BRCA"})
    print("Suggestions:", suggestions.result)

    # 2. Fetch multi-omics annotations for TP53
    gene_data = client.run({
        "action": "fetch_gene",
        "gene_symbol": "TP53"
    }, label="tp53-analysis")

    print("Status:", gene_data.status)
    print("Gene Symbol:", gene_data.result["gene"]["symbol"])
    print("Pathways Found:", len(gene_data.result.get("pathways", [])))

    # 3. Export pinned hypothesis cards to a formatted text brief
    export_result = client.run({
        "action": "export_txt",
        "gene_symbol": "TP53",
        "pinned_cards": ["card_tp53_dna_repair"]
    })
    print("Exported File:", export_result.result.get("filename"))
```

# Typical Use Cases

* **RNA-seq & scRNA-seq Hit Follow-up**: Prioritize top differentially expressed genes or cell-type markers, focusing on uncharacterized target genes.
* **CRISPR & RNAi Screen Validation**: Formulate mechanistic hypotheses for top hits from functional genomics screens prior to secondary assays.
* **GWAS Locus Functional Annotation**: Connect non-coding or coding variants in GWAS loci to downstream disease pathways and regulatory networks.
* **Synthetic Lethality & Pathway Crosstalk**: Explore potential synthetic lethal interactions and compensatory signaling loops for drug target discovery.
* **Experimental Validation Assay Design**: Generate structured research briefs outlining candidate orthogonal validation experiments (RT-qPCR, Western blot, ChIP-seq).

# Scientific Background

### Multi-Omics Data Integration

Target prioritization relies on unifying distinct genomic abstraction layers: HGNC gene nomenclature, Ensembl genomic loci (`ENSG`), UniProt protein accessions, Gene Ontology terms (Biological Process, Molecular Function, Cellular Component), and KEGG/Reactome pathway models.

### Pathway Enrichment & Disease Odds Ratio

Over-representation analysis evaluates candidate gene enrichment within target pathways using the Hypergeometric distribution:

$$P(X \ge k) = \sum_{i=k}^{\min(n, M)} \frac{\binom{M}{i} \binom{N-M}{n-i}}{\binom{N}{n}}$$

Where $N$ is total background genes, $M$ is pathway gene set size, $n$ is candidate list size, and $k$ is overlap count. Gene-disease association strength is quantified via the 2x2 contingency table Odds Ratio $\text{OR} = \frac{a \cdot d}{b \cdot c}$.

### Synthetic Lethality Scoring

Synthetic lethal vulnerability $S_{ij}$ between target gene $i$ and partner gene $j$ quantifies deviations from additive viability loss:

$$S_{ij} = \Delta V_{i,j} - (\Delta V_i + \Delta V_j)$$

# Web Application

For researchers who prefer a graphical interface, an interactive web version is available:

Web Application: https://www.pepkio.com/tools/gene-hypothesis-roulette

The web application features interactive target search, visual pinboards for hypothesis cards, live pathway mapping, shareable permalinks, and downloadable ELN worksheets.

# Documentation and Resources

* GitHub Repository: https://github.com/pepkio/pepkio-gene-hypothesis-roulette
* Web Application: https://www.pepkio.com/tools/gene-hypothesis-roulette
* Source and Issue Tracker: https://github.com/pepkio/pepkio-gene-hypothesis-roulette

# About Pepkio

Pepkio (https://www.pepkio.com/) develops software tools and bioinformatics solutions for life science researchers, including laboratory calculators and analysis services (https://www.pepkio.com/cro). See https://www.pepkio.com for additional tools and services.

# Keywords

* gene hypothesis roulette
* gene hypothesis generator
* target gene discovery
* multi-omics aggregator
* pathway crosstalk
* candidate gene prioritization
* gene-disease association
* RNA-seq hit follow-up
* CRISPR screen hit validation
* GWAS locus annotation
* synthetic lethality
* functional genomics
* HGNC symbol resolution
* Ensembl gene lookup
* UniProt protein mapping
* Gene Ontology enrichment
* KEGG pathway analysis
* Reactome pathway mapping
* STRING protein interactions
* bioinformatic hypothesis builder
* drug repurposing ideation
* research pinboard
* experimental validation design
* bioinformatics python client
* exploratory hypothesis generation engine for gene discovery
* multi-omics target gene data aggregator python package
* automated RNA-seq candidate gene prioritization tool
* CRISPR knockout screen hit validation hypothesis builder
* GWAS locus non-coding variant pathway annotation tool
* synthetic lethality pathway crosstalk generator for target discovery
* HGNC symbol Ensembl ID UniProt accession resolution api
* Gene Ontology and KEGG pathway enrichment hypothesis cards
* bioinformatic research brief generator for electronic lab notebooks
* target gene disease association odds ratio calculation tool
* hypergeometric pathway enrichment over-representation analyzer
* python client for pepkio gene hypothesis roulette api
