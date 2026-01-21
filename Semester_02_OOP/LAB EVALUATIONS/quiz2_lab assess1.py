from abc import ABC, abstractmethod
class ForensicEvidence(ABC):
    def __init__(self, evidence_id):
        self.evidence_id = evidence_id

    @abstractmethod
    def analyze(self):
        pass

    @staticmethod
    def is_valid_id(evidence_id):
        if evidence_id.startswith("B"):
            return True
        else:
            return False
        
class BallisticEvidence(ForensicEvidence):
    def analyze(self):
        return f"Ballistic analysis completed with ID: {self.evidence_id}"
    
evidence_id = "A12345"
is_valid = BallisticEvidence.is_valid_id(evidence_id)  
print(is_valid) 

if is_valid:
    evidence1 = BallisticEvidence(evidence_id)
    print(evidence1.analyze())
else:
    print(f"Analysis not completed due to invalid ID {evidence_id}")


