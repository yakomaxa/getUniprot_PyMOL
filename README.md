# getUniprot_PyMOL
fetch UniProt text from PyMOL

# requirement

* BeautifulSoup

# Usage 

Select any atoms of your AFDB model, and type
``` uniprot sele ```

This script assume that your object is named like AF-P42212-F1_model_v4 or P42212.

If your object is named like AF-XXXXX-F1_model_v4, run it as described above.

If you object is named as raw Uniprot accession like ```P42212```, select any of atoms and type

``` uniprot sele, 1```

