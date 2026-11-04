# Skill++ v1 — evidence restoration

The public research is [the citation page](../zhang--skill-plus-plus.md) and [lifelong skill routing](../../concepts/lifelong-skill-routing.md). [capture.json](capture.json) pins the version, provenance, read coverage and SHA-256 hashes.

The full paper and derived reproductions live in local, ignored `raw/`. They are not included in GitHub or restored by the repository-clone setup script. The arXiv record uses its [nonexclusive distribution license](https://arxiv.org/licenses/nonexclusive-distrib/1.0/); the public wiki publishes its own analysis rather than a complete reprint.

## Restore the primary evidence

From the repository root, these commands download the pinned v1 PDF, HTML and metadata. Do not overwrite an existing capture; check its manifest first.

```sh
mkdir -p sources/zhang--skill-plus-plus/raw
curl --fail --location --no-clobber https://arxiv.org/pdf/2611.00544v1 --output sources/zhang--skill-plus-plus/raw/paper.pdf
curl --fail --location --no-clobber https://arxiv.org/html/2611.00544v1 --output sources/zhang--skill-plus-plus/raw/paper.html
curl --fail --location --no-clobber https://arxiv.org/abs/2611.00544v1 --output sources/zhang--skill-plus-plus/raw/abstract.html
```

Compare file hashes with the manifest (`shasum -a 256 <file>`). HTML wrappers can change even for a pinned paper version; a hash mismatch means this is not the original captured byte stream. Record a separate capture instead of changing the manifest to hide it.

## Reading map

- PDF pp. 1–9: main argument, formulation, method, results and limitations.
- pp. 9–11: references (read as references, not independently verified papers).
- pp. 12–13: implementation details and Algorithm 1.
- pp. 13–15: dataset construction, router protocol, metrics and baselines; Table A1 on p. 14.
- pp. 15–20: stability/plasticity, error taxonomy, ablations, other benchmarks/models, native harness, actual task-success check and robustness.

The initial local capture also includes all 20 page-text files, combined page-labeled text, PDF links and six inspected page images. These are convenience derivatives, not required to follow the public source map. Use the PDF/HTML for math or table-layout ambiguity. Capturing and reading the paper does not reproduce the experiments.
