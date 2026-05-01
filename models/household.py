class Household:
    def __init__(self, household_id, num_people, income, tenure_type):
        self.household_id = household_id
        self.num_people = num_people
        self.income = income
        self.tenure_type = tenure_type

    def calculate_total_income(self):
        return self.income

    def describe(self):
        return (
            f"Household {self.household_id}: "
            f"people={self.num_people}, income={self.income}, "
            f"tenure={self.tenure_type}"
        )
    