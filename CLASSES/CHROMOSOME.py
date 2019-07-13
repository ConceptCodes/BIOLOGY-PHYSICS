# A class representing a chromosome, which has a collection of SNP's
class CHROMOSOME:
    def __init__(self, chrname):
        self.chrname = chrname
        self.locations_to_snps = dict()
    
    def get_name(self):
        return self.name

    