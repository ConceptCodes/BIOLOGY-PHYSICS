# Class Object to Represent a Gene
class GENE:
    # Constructor that takes the gene id and sequence
    def __init__(self, _id, seq):
        self.id = _id
        self.sequence = seq
    # Print ID
    def get_id(self):
        return str(self.id)
    # Override the default 'len()' property to return sequence length
    def __len__(self):
        return len(self.sequence)
    # Override default '=' 
    def __eq__(self, other):
        if self.sequence == other.get_seq():
            return True
        return False
    # Override default '<'
    def __lt__(self, other):
        if self.sequence < other.get_seq():
            return True
        return False
    # Override default '<='
    def __le__(self, other):
        if self.sequence <= other.get_seq():
            return True
        return False
    # Override default '>'
    def __gt__(self, other):
        if self.sequence > other.get_seq():
            return True
        return False
    # Override default '>='
    def __ge__(self, other):
        if self.sequence >= other.get_seq():
            return True
        return False
    # Override default '!='
    def __ne__(self, other):
        if self.sequence != other.get_seq():
            return True
        return False
    # Get base count for given base
    def get_base_count(self, base):
        base_count = 0
        for i in range(0, len(self.sequence)):
            _base = self.sequence[i]
            if _base == base:
                base_count = base_count + 1 
        return base_count
    # Return percentage of the amount of given base
    def get_base_content(self, base):
        return (self.get_base_count(str(base))) / float(len(self.sequence))
    # Return gene sequence
    def get_seq(self):
        return self.sequence
    # Set Gene Sequence
    def set_seq(self, _seq):
        assert _seq.get_base_count("U") == 0, 'Sorry No RNA allowed'
        self.sequence = _seq































