"""
Tyrone Payroll System (2026 Rates)
OOP Implementation - Company as Base Class
"""


class Company:
    """Base class with all payroll logic - Employee, Supervisor, Manager inherit from this"""

    WORKING_DAYS_PER_MONTH = 22
    HOURS_PER_DAY = 8
    OVERTIME_PREMIUM = 0.10
    BONUS_RATE = 0.15

    # 2026 Deduction Rates (Sprout Solutions)
    SSS_EMPLOYEE_RATE = 0.045
    SSS_MAX = 900.00
    PHILHEALTH_EMPLOYEE_RATE = 0.025
    PAGIBIG_RATE_LOW = 0.01
    PAGIBIG_RATE_HIGH = 0.02
    PAGIBIG_THRESHOLD = 1500.00
    PAGIBIG_MAX = 200.00

    # 2026 Income Tax Brackets (Monthly, max 30%)
    # 0% for ≤₱20,833; 15%-30% on excess
    TAX_BRACKETS = [
        (20833.00, 0, 0.00),
        (33333.00, 0, 0.15),
        (66667.00, 1875.00, 0.20),
        (166667.00, 8541.67, 0.25),
        (float('inf'), 33541.67, 0.30),
    ]

    def __init__(self, name: str, salary_15th: float, salary_30th: float, overtime_hours: float = 0):
        self.name = name
        self.salary_15th = salary_15th
        self.salary_30th = salary_30th
        self.overtime_hours = overtime_hours
        self.role = "Company"

    # --- EARNINGS METHODS ---

    @property
    def base_monthly_salary(self) -> float:
        """Combine 15th and 30th payouts for total base"""
        return self.salary_15th + self.salary_30th

    @property
    def hourly_rate(self) -> float:
        """Calculate hourly rate from monthly salary"""
        total_hours = self.WORKING_DAYS_PER_MONTH * self.HOURS_PER_DAY
        return self.base_monthly_salary / total_hours

    def calculate_overtime(self) -> float:
        """Overtime = hourly rate × hours × 1.10 (10% premium)"""
        return self.hourly_rate * self.overtime_hours * (1 + self.OVERTIME_PREMIUM)

    def calculate_bonus(self) -> float:
        """Bonus = Base Monthly × 0.15"""
        return self.base_monthly_salary * self.BONUS_RATE

    def calculate_gross_earnings(self) -> float:
        """Gross = Base + Overtime + Bonus"""
        return self.base_monthly_salary + self.calculate_overtime() + self.calculate_bonus()

    # --- 2026 DEDUCTION METHODS ---

    def calculate_sss(self) -> float:
        """SSS: Base × 4.5% (employee share), max ₱900"""
        contribution = self.base_monthly_salary * self.SSS_EMPLOYEE_RATE
        return min(contribution, self.SSS_MAX)

    def calculate_philhealth(self) -> float:
        """PhilHealth: Base × 0.025 (employee's half of 5%)"""
        return self.base_monthly_salary * self.PHILHEALTH_EMPLOYEE_RATE

    def calculate_pagibig(self) -> float:
        """Pag-IBIG: 1% if ≤₱1,500, else 2%, max ₱200"""
        if self.base_monthly_salary <= self.PAGIBIG_THRESHOLD:
            contribution = self.base_monthly_salary * self.PAGIBIG_RATE_LOW
        else:
            contribution = self.base_monthly_salary * self.PAGIBIG_RATE_HIGH
        return min(contribution, self.PAGIBIG_MAX)

    def calculate_taxable_income(self) -> float:
        """Taxable Income = Gross Earnings - SSS - PhilHealth - Pag-IBIG"""
        return self.calculate_gross_earnings() - self.calculate_sss() - self.calculate_philhealth() - self.calculate_pagibig()

    def calculate_income_tax(self) -> float:
        """2026 Graduated Income Tax (max 35%) - monthly computation"""
        monthly_taxable = self.calculate_taxable_income()

        previous_limit = 0
        for limit, base_tax, rate in self.TAX_BRACKETS:
            if monthly_taxable <= limit:
                return base_tax + (monthly_taxable - previous_limit) * rate
            previous_limit = limit
        return 0.0

    def calculate_total_deductions(self) -> float:
        """Sum of all 2026 deductions including income tax"""
        return self.calculate_sss() + self.calculate_philhealth() + self.calculate_pagibig() + self.calculate_income_tax()

    # --- FINAL OUTPUT ---

    def calculate_net_pay(self) -> float:
        """Net Pay = Gross Earnings - Total Deductions"""
        return self.calculate_gross_earnings() - self.calculate_total_deductions()

    def display_payslip(self):
        """Print detailed payslip breakdown"""
        print("\n" + "=" * 50)
        print(f"PAYSLIP - {self.role.upper()}")
        print("=" * 50)
        print(f"Name: {self.name}")
        print("-" * 50)

        print("\nEARNINGS:")
        print(f"  15th Payout:        PHP {self.salary_15th:>12,.2f}")
        print(f"  30th Payout:        PHP {self.salary_30th:>12,.2f}")
        print(f"  Base Monthly:       PHP {self.base_monthly_salary:>12,.2f}")
        print(f"  Overtime ({self.overtime_hours} hrs):  PHP {self.calculate_overtime():>12,.2f}")
        print(f"  Bonus (15%):        PHP {self.calculate_bonus():>12,.2f}")
        print(f"  GROSS EARNINGS:     PHP {self.calculate_gross_earnings():>12,.2f}")

        print("\n2026 DEDUCTIONS:")
        print(f"  SSS (4.5%):         PHP {self.calculate_sss():>12,.2f}")
        print(f"  PhilHealth (2.5%):  PHP {self.calculate_philhealth():>12,.2f}")
        print(f"  Pag-IBIG:           PHP {self.calculate_pagibig():>12,.2f}")
        print(f"  Income Tax:         PHP {self.calculate_income_tax():>12,.2f}")
        print(f"  TOTAL DEDUCTIONS:   PHP {self.calculate_total_deductions():>12,.2f}")

        print("-" * 50)
        print(f"  NET PAY:            PHP {self.calculate_net_pay():>12,.2f}")
        print("=" * 50)


class Employee(Company):
    """Employee subclass - inherits all payroll logic from Company"""

    def __init__(self, name: str, salary_15th: float, salary_30th: float, overtime_hours: float = 0):
        super().__init__(name, salary_15th, salary_30th, overtime_hours)
        self.role = "Employee"


class Supervisor(Company):
    """Supervisor subclass - inherits all payroll logic from Company"""

    def __init__(self, name: str, salary_15th: float, salary_30th: float, overtime_hours: float = 0):
        super().__init__(name, salary_15th, salary_30th, overtime_hours)
        self.role = "Supervisor"


class Manager(Company):
    """Manager subclass - inherits all payroll logic from Company"""

    def __init__(self, name: str, salary_15th: float, salary_30th: float, overtime_hours: float = 0):
        super().__init__(name, salary_15th, salary_30th, overtime_hours)
        self.role = "Manager"


# --- MAIN PROGRAM WITH USER INPUT ---

def get_float_input(prompt: str) -> float:
    """Helper to get validated float input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_int_input(prompt: str) -> int:
    """Helper to get validated int input"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def create_person_from_input(role_class, role_name: str):
    """Create a person object from user input"""
    print(f"\n--- Adding {role_name} ---")
    name = input("Enter name: ")
    salary_15th = get_float_input("Enter salary for 15th: PHP ")
    salary_30th = get_float_input("Enter salary for 30th: PHP ")
    overtime_hours = get_float_input("Enter overtime hours: ")

    return role_class(name, salary_15th, salary_30th, overtime_hours)


def main():
    """Main program entry point"""
    print("\n" + "=" * 60)
    print("  PHILIPPINE PAYROLL SYSTEM (2026 RATES)")
    print("  OOP Implementation")
    print("=" * 60)

    company_name = input("\nEnter company name: ")
    personnel = []

    # Fixed personnel count: 1 for each role
    num_employees = 1
    num_supervisors = 1
    num_managers = 1

    print("\nHow many personnel to add?")
    print(f"Number of Employee Personnel: {num_employees}")
    print(f"Number of Supervisor Personnel: {num_supervisors}")
    print(f"Number of Manager Personnel: {num_managers}")

    # Add Employees
    for i in range(num_employees):
        print(f"\n[Employee {i + 1} of {num_employees}]")
        employee = create_person_from_input(Employee, "Employee")
        personnel.append(employee)

    # Add Supervisors
    for i in range(num_supervisors):
        print(f"\n[Supervisor {i + 1} of {num_supervisors}]")
        supervisor = create_person_from_input(Supervisor, "Supervisor")
        personnel.append(supervisor)

    # Add Managers
    for i in range(num_managers):
        print(f"\n[Manager {i + 1} of {num_managers}]")
        manager = create_person_from_input(Manager, "Manager")
        personnel.append(manager)

    # Display all payslips
    print(f"\n{'#' * 60}")
    print(f"  {company_name.upper()} - PAYROLL SUMMARY")
    print(f"{'#' * 60}")

    for person in personnel:
        person.display_payslip()

    total_payroll = sum(p.calculate_net_pay() for p in personnel)
    print(f"\n{'=' * 50}")
    print(f"TOTAL COMPANY PAYROLL: PHP {total_payroll:>12,.2f}")
    print(f"{'=' * 50}")




if __name__ == "__main__":
    main()
