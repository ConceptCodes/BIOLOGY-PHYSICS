import SNP


# Transition Test, should pass
snp1 = SNP("1", 12352, "rs11345", "C", "T")
assert snp1.is_transition() == True, "Failed Test"

# Transversion Test
snp2 = SNP("1", 36654, "rs22541", "A", "T")
assert snp2.is_transversion() == True, "Failed Test"

# Error Test, should give me Error: ref == alt at pos 69835
snp3 = SNP("1", 69835, "rs53482", "A", "A")