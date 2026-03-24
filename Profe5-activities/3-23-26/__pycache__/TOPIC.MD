# Four Pillars of OOP in Payroll System

## 1. Encapsulation
Bundling data (attributes) and methods that operate on that data within a single class.

**Where it's used:**
- `payroll_system.py:7-127` - `Company` class encapsulates employee data with payroll methods
- `payroll_system.py:30-35` - Private data (`self.name`, `self.salary_15th`, `self.salary_30th`, `self.overtime_hours`) bundled inside the class
- `payroll_system.py:10-13` - Class constants (`WORKING_DAYS_PER_MONTH`, `HOURS_PER_DAY`, etc.) kept within the class

---

## 2. Abstraction
Hiding complex implementation details and exposing only essential features.

**Where it's used:**
- `payroll_system.py:39-48` - `@property` decorators for `base_monthly_salary` and `hourly_rate` hide calculation logic
- `payroll_system.py:58-60` - `calculate_gross_earnings()` abstracts the complexity of summing all earnings
- `payroll_system.py:91-93` - `calculate_total_deductions()` hides the complexity of summing deductions
- `payroll_system.py:101-126` - `display_payslip()` abstracts complex formatting and display logic

---

## 3. Inheritance
Child classes inherit properties and methods from a parent class.

**Where it's used:**
- `payroll_system.py:129` - `class Employee(Company)` inherits from Company
- `payroll_system.py:137` - `class Supervisor(Company)` inherits from Company
- `payroll_system.py:145` - `class Manager(Company)` inherits from Company
- `payroll_system.py:133,141,149` - `super().__init__()` calls parent constructor to reuse initialization logic

---

## 4. Polymorphism
Objects of different classes can be treated through a common interface.

**Where it's used:**
- `payroll_system.py:227-228` - `for person in personnel: person.display_payslip()` treats Employee, Supervisor, and Manager uniformly
- `payroll_system.py:230` - `sum(p.calculate_net_pay() for p in personnel)` calls the same method on different class instances
- `payroll_system.py:173-181` - `create_person_from_input(role_class, role_name)` accepts any class as parameter (polymorphic instantiation)
