## Project Title
In-silico Identification and Functional Characterization of a Hypothetical Protein (A0A8S4BTT0) from Menidia menidia Using Sequence Analysis and Homology-Based Annotation

## Author
**Swathi PS**  
BS Chemistry  
SRM Institute of Science and Technology (SRMIST)
Email : swathips415@gmail.com

## Project Description
Hypothetical proteins constitute a large portion of sequenced genomes, yet their biological roles remain unknown. This project aims to predict the function of a hypothetical protein from *Menidia menidia* using in-silico sequence analysis and homology-based annotation.

## Objective
To assign a putative biological function to the hypothetical protein A0A8S4BTT0 through sequence analysis and BLAST-based homology search using BioPython.

## Methodology
- Retrieval of protein sequence from UniProt
- Sequence quality assessment and validation
- BLASTP analysis against the Swiss-Prot database
- Identification of closest homologs
- Alignment interpretation and functional region mapping
- Functional annotation based on conserved domains and homologous proteins

## Tools and Databases Used
- BioPython
- BLASTP
- Swiss-Prot database
- UniProt

## Results
BLAST analysis revealed strong homology between the hypothetical protein A0A8S4BTT0 and the MHC class II invariant chain (CD74). High alignment scores, low E-values, conserved regions, and functional domain mapping indicate that the query protein is likely involved in antigen processing and immune regulation.

## Repository Structure
- `input_sequence.fasta` – Hypothetical protein sequence from UniProt  
- `blast_run.py` – Python script to perform BLASTP using BioPython  
- `blast_result.xml` – BLASTP output file  
- `homology_analysis.py` – Script for BLAST result parsing and homology analysis  
- `sequence_qc.py` – Sequence quality and amino acid composition analysis  
- `Report.pdf` – Detailed capstone project report

## Conclusion
This study demonstrates that homology-based computational analysis can successfully predict the function of hypothetical proteins. The findings suggest that the analyzed protein may participate in immune-related processes in *Menidia menidia*.

Limitations of the Study
The functional prediction of A0A8S4BTT0 is based entirely on in-silico homology analysis using sequence similarity and BLAST results. Although strong alignment scores and conserved regions support the predicted function, no experimental validation was performed in this study. Therefore, the assigned function remains a computational prediction and requires further experimental confirmation.

## Keywords
Hypothetical protein, BLASTP, Functional annotation, BioPython, Menidia menidia

