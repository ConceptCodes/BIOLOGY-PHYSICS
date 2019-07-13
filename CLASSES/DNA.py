class DNA:
    """Class representing DNA as a string sequence."""
    
    basecomplement = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    
    codon2aa = {"TTT":"F","TTC":"F","TTA":"L","TTG":"L","TCT":"S","TCC":"S",
                "TCA":"S","TCG":"S","TAT":"Y","TAC":"Y","TAA":"*","TAG":"*",
                "TGT":"C","TGC":"C","TGA":"*","TGG":"W","CTT":"L","CTC":"L",
                "CTA":"L","CTG":"L","CCT":"P","CCC":"P","CCA":"P","CCG":"P",
                "CAT":"H","CAC":"H","CAA":"Q","CAG":"Q","CGT":"R","CGC":"R",
                "CGA":"R","CGG":"R","ATT":"I","ATC":"I","ATA":"I","ATG":"M",
                "ACT":"T","ACC":"T","ACA":"T","ACG":"T","AAT":"N","AAC":"N",
                "AAA":"K","AAG":"K","AGT":"S","AGC":"S","AGA":"R","AGG":"R",
                "GTT":"V","GTC":"V","GTA":"V","GTG":"V","GCT":"A","GCC":"A",
                "GCA":"A","GCG":"A","GAT":"D","GAC":"D","GAA":"E","GAG":"E",
                "GGT":"G","GGC":"G","GGA":"G","GGG":"G"}
            
    def __init__(self, s):
        """Create DNA instance initialized to string s."""
        self.seq = s
        
    def transcribe(self):
        """Return as rna string."""
        return self.seq.replace('T', 'U')
        
    def reverse(self):
        """Return dna string in reverse order."""
        letters = list(self.seq)
        letters.reverse()
        return ''.join(letters)
        
    def complement(self):
        """Return the complementary dna string."""
        letters = list(self.seq)
        letters = [self.basecomplement[base] for base in letters]
        return ''.join(letters)
        
    def reversecomplement(self):
        """Return the reverse of complement of the dna string."""
        letters = list(self.seq)
        letters.reverse()
        letters = [self.basecomplement[base] for base in letters]
        return ''.join(letters)
        
    def gc(self):
        """Return the % of dna composed of G+C."""
        s = self.seq
        gc = s.count('G') + s.count('C')
        return gc * 100.0 / len(s)
        
    def codons(self):
        """Return list of codons for the dna string,"""
        s = self.seq
        end = len(s) - (len(s) % 3) - 1
        codons = [s[i:i+3] for i in range(0, end, 3)]
        return codons
        
    def translate(self):
        """Return amino acid sequence translating dna seq."""
        s = self.seq
        codons = self.codons()
        aa = [self.codon2aa[aa] for aa in codons]
        return ''.join(aa)