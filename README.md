# Division & Replication of Data for Optimal Performance & Security

> Distributed Big Data Solution | Associated with Tech Mahindra

## Overview

Designed and implemented a distributed big data solution using **Apache Hadoop** and **Apache Spark** to divide large datasets into optimized fragments and replicate them across multiple cloud nodes. The system ensures improved fault tolerance, redundancy, and high availability for enterprise-scale data workloads.

## Key Features

- 🔀 **Data Partitioning** — Splits large datasets into fragments using optimized partitioning strategies
- 🔁 **Data Replication** — Replicates fragments across multiple cloud nodes for redundancy
- ⚡ **High Availability** — Ensures zero data loss with fault-tolerant distributed architecture
- 📈 **Scalability** — Designed to scale horizontally across cloud infrastructure
- 🔒 **Security** — Implements secure data distribution with access controls

## Tech Stack

![Apache Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white)
![Hadoop](https://img.shields.io/badge/Hadoop-FF652F?style=flat-square&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Cloud](https://img.shields.io/badge/Cloud-00b4d8?style=flat-square&logoColor=white)
![HDFS](https://img.shields.io/badge/HDFS-FF652F?style=flat-square&logoColor=white)

## Architecture

```
Raw Data Source
      │
      ▼
Data Partitioning Layer (Apache Spark)
      │
      ├──► Node 1 (Fragment A)
      ├──► Node 2 (Fragment B)
      ├──► Node 3 (Fragment C)
      └──► Node N (Fragment N)
            │
            ▼
    Replication Manager
            │
      ┌─────┴─────┐
      ▼           ▼
  Replica 1   Replica 2
  (Backup)    (Backup)
```

## Results

- ✅ Improved fault tolerance and high availability across distributed nodes
- ✅ Optimized data partitioning strategies for enhanced scalability
- ✅ Reduced data retrieval time through parallel processing
- ✅ Ensured reliable performance in distributed cloud environments

## Association

This project was developed as part of enterprise data engineering work at **Tech Mahindra**, focusing on scalable and secure data infrastructure for large-scale business operations.

---

*© 2024 Preethi Dommaraju*
