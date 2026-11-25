# RiskSignal_v1 (for procurement and supply chain managers)
//Python-based vuln. intelligence and risk analysis tool; integrating NVD and OSV data sources

Public cyber risk signals designed for procurement, supplier risk, and supply chain teams who need a quick public-source signal before deeper due diligence.
(Japan & APAC focus)

A lightweight first-pass CLI tool that collects & analyzes public vulnerability data (NVD + OSV) related to a supplier or specific product/component.

## Features

_ Collects public vulnerability signals from:
  - NVD (National Vulnerability Database)
  - OSV (Open Source Vulnerabilities)
_ Supports supplier-level queries with optional product/component focus
_ Simple and clean CLI interface
_ Modular architecture (collectors → aggregator → analyzer → reporter)
_ Explicitly designed as a **first-pass** tool using public sources only

## Usage

Basic usage:

python mainlab.py --supplier "SupplierName"

With product/component focus:

python mainlab.py --supplier "SupplierName" --product "ComponentName"

Example:

python mainlab.py --supplier "ExampleVendor" --product "libxyz"


## Structure

```text
RiskSignal/
│
├── README.md
├── mainlab.py
├── risksignal.txt
│
└── src/
    ├── __init__.py
    ├── aggregator.py
    ├── analyzer.py
    ├── reporter.py
    │
    └── collectors/
        ├── __init__.py
        ├── nvd.py
        └── osv.py
```


## Outro

I developed this lightweight tool to accelerate the identification of sensitive areas related to suppliers background. It provides a preliminary screening process, helping narrow the scope (investigation) and establish a meaningful KPI-driven assessment of one or several suppliers.

The objective is to support better-informed procurement and SCM decisions through greater transparency (access to information). RiskSignal_v1 relies exclusively on publicly available data sources.
