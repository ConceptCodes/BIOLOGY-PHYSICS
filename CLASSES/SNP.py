import io
import sys
import re

# A class representing simple SNPs
class SNP:
    def __init__(self, chrname, pos, snp_id, ref_allele, alt_allele):
        assert ref_allele != alt_allele, "Error: ref == alt at pos " + str(pos)
        self.chrname = chrname
        self.pos = pos
        self.snpid = snpid
        self.ref_allele = ref_allele
        self.alt_allele = alt_allele

    # Returns True if ref_allele/alt_alt_allele is A/G, G/A, C/T, or T/C
    def is_transition(self):
        if self.ref_allele == "G" or self.ref_allele == "A":
            if self.alt_allele == "G" or self.alt_allele == "G":
                return True
        if self.ref_allele == "C" or self.ref_allele == "T":
            if self.alt_allele == "C" or self.alt_allele == "T":
                return True
        return False

    # Returs True if is a transversion
    def is_transversion(self):
        if self.is_transition():
            return False
        return True





























