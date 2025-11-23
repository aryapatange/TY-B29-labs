# Simple Medical Diagnosis Expert System (Forward Chaining)

class ExpertSystem:
    def __init__(self):
        self.facts = {}
        self.rules = []
        self.derived = []

    def add_fact(self, fact, val):
        self.facts[fact] = val

    def add_rule(self, conds, concl):
        self.rules.append((conds, concl))

    def apply_rules(self):
        changed = True
        while changed:
            changed = False
            for conds, concl in self.rules:
                if concl not in self.derived and all(
                    fact in self.facts and self.facts[fact] == val
                    for fact, val in conds.items()
                ):
                    self.derived.append(concl)
                    changed = True
        return self.derived

# Rules
system = ExpertSystem()
system.add_rule({'fever': True, 'cough': True, 'sore_throat': True}, "Common Cold")
system.add_rule({'fever': True, 'cough': True, 'body_ache': True, 'chills': True}, "Flu")
system.add_rule({'fever': True, 'cough': True, 'shortness_of_breath': True, 'chest_pain': True}, "Pneumonia")
system.add_rule({'fever': True, 'cough': True}, "Respiratory Infection")
system.add_rule({'fever': True}, "Monitor Temperature")
system.add_rule({'cough': True}, "Drink Warm Liquids")

# Patient symptoms
symptoms = {
    'fever': True,
    'cough': True,
    'sore_throat': True,
    'body_ache': False,
    'chills': False,
    'shortness_of_breath': False,
    'chest_pain': False
}

# Add facts
for s, v in symptoms.items():
    system.add_fact(s, v)

# Run inference
print("\nDiagnoses:", system.apply_rules())
