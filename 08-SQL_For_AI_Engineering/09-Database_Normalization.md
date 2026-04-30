
# Database Normalization (Notes)

## 0) What normalization is
- **Normalization** = organizing relational tables to **reduce redundancy** and **avoid update anomalies**, using rules based on **dependencies**.
- Goal: good schema design with:
	- **Less duplication**
	- **Fewer anomalies**
	- **Clear keys + constraints**
	- **Lossless** decompositions (can reconstruct original relation)
	- Preferably **dependency-preserving** decompositions (constraints still enforceable without joins)

## 1) Why normalize? (Anomalies)
When one table mixes multiple “subjects”, redundancy creates:
- **Insertion anomaly**: can’t add one fact without another (e.g., can’t add a new course until a student enrolls).
- **Update anomaly**: same fact repeated in many rows → inconsistent updates.
- **Deletion anomaly**: deleting a row removes unrelated facts (e.g., deleting last enrollment loses course info).

## 2) Key terms (must-know)
### Keys
- **Super key**: any attribute set that uniquely identifies a row.
- **Candidate key**: minimal super key.
- **Primary key**: chosen candidate key.
- **Composite key**: key with multiple attributes.
- **Prime attribute**: attribute that is part of some candidate key.

### Dependencies
#### Functional Dependency (FD)
- Notation: $X \rightarrow Y$
- Meaning: if two rows have the same $X$, they must have the same $Y$.
- Types (common language):
	- **Full FD**: $X \rightarrow Y$ and no proper subset of $X$ determines $Y$.
	- **Partial dependency**: $X \rightarrow Y$ but some subset of composite $X$ also determines $Y$.
	- **Transitive dependency**: $X \rightarrow Y$ and $Y \rightarrow Z$ (with $Z$ not a key attribute) ⇒ $X \rightarrow Z$.

#### Multivalued Dependency (MVD) (for 4NF)
- Notation: $X \twoheadrightarrow Y$
- Meaning: for a fixed $X$, the set of $Y$ values is independent of other attributes.

## 3) Normal Forms (NF) — quick rules

### 1NF (First Normal Form)
Rule:
- All attributes are **atomic** (no repeating groups, arrays, lists).

Typical fixes:
- Split repeating groups into a separate table.
- Use one value per cell.

Mini example:
- Bad: `Student(SID, Name, Phones)` where Phones = "987,654"
- 1NF: `StudentPhone(SID, Phone)` (one phone per row)

---

### 2NF (Second Normal Form)
Applies when the table has a **composite candidate key**.

Rule:
- In 1NF, and **no partial dependency** of a non-key attribute on part of a composite key.

How to spot:
- If PK = (A, B) and some non-key C depends only on A (or only on B) ⇒ violates 2NF.

Mini example:
- `Enroll(StudentID, CourseID, StudentName, CourseTitle)` with PK (StudentID, CourseID)
- FDs: `StudentID -> StudentName`, `CourseID -> CourseTitle`
- Fix:
	- `Student(StudentID, StudentName)`
	- `Course(CourseID, CourseTitle)`
	- `Enroll(StudentID, CourseID)`

---

### 3NF (Third Normal Form)
Rule:
- In 2NF, and **no transitive dependency** of non-key attributes on the key.

Formal (common) definition:
- For every FD $X \rightarrow A$, at least one holds:
	- $X$ is a **super key**, OR
	- $A$ is **prime** (part of some candidate key)

How to spot:
- PK determines some non-key, which determines another non-key (Key → NonKey → NonKey).

Mini example:
- `Employee(EmpID, EmpName, DeptID, DeptName)` with PK EmpID
- FDs: `EmpID -> EmpName, DeptID` and `DeptID -> DeptName`
- Transitive: `EmpID -> DeptName` via DeptID
- Fix:
	- `Employee(EmpID, EmpName, DeptID)`
	- `Department(DeptID, DeptName)`

---

### BCNF (Boyce–Codd Normal Form)
Stronger than 3NF.

Rule:
- For every FD $X \rightarrow Y$, $X$ must be a **super key**.

When 3NF passes but BCNF fails:
- Usually when a dependency has a determinant that isn’t a key, but RHS is a prime attribute (3NF allows it, BCNF doesn’t).

Quick example pattern:
- Relation `R(A, B, C)` with FDs: `A B -> C` and `C -> B`
- If `C` is not a super key, `C -> B` violates BCNF.

---

### 4NF (Fourth Normal Form)
Deals with **multivalued dependencies**.

Rule:
- In BCNF, and for every non-trivial MVD $X \twoheadrightarrow Y$, $X$ must be a **super key**.

Classic example:
- `StudentSkillHobby(Student, Skill, Hobby)`
- If skills and hobbies are independent for a student:
	- `Student \twoheadrightarrow Skill`
	- `Student \twoheadrightarrow Hobby`
- Fix:
	- `StudentSkill(Student, Skill)`
	- `StudentHobby(Student, Hobby)`

---

### 5NF (Fifth Normal Form / PJNF)
Deals with **join dependencies** where data must be split into 3+ tables to avoid redundancy.

Rule (intuitive):
- Every join dependency is implied by candidate keys.

Often appears in complex many-to-many-to-many business rules (rare in typical apps).

## 4) Decomposition properties (important)

### Lossless (non-additive) join
- Decomposition is **lossless** if joining decomposed tables reconstructs the original without spurious rows.
- For a binary decomposition of $R$ into $R_1$ and $R_2$:
	- Lossless if $(R_1 \cap R_2) \rightarrow R_1$ **or** $(R_1 \cap R_2) \rightarrow R_2$ (under the original FDs)

### Dependency preservation
- Decomposition is dependency-preserving if you can enforce all original FDs by enforcing constraints on each decomposed relation separately.
- Trade-off:
	- BCNF decomposition may be lossless but **not** dependency-preserving.
	- 3NF synthesis aims for both lossless + dependency preservation.

## 5) Practical normalization workflow
1. Identify **entities** and **attributes** (ER-style thinking).
2. Identify **candidate keys**.
3. Write down **FDs** you believe are true (from business rules).
4. Ensure **1NF** (atomic attributes).
5. Fix **2NF** issues (partial dependencies).
6. Fix **3NF** issues (transitive dependencies).
7. If needed, push to **BCNF** (watch dependency preservation).
8. For independent multi-valued facts, consider **4NF**.
9. Validate with:
	 - Lossless join check
	 - Dependency preservation check

## 6) Small end-to-end example (1NF → 3NF)
Suppose:

`OrderLine(OrderID, OrderDate, CustomerID, CustomerName, ProductID, ProductName, UnitPrice, Qty)`

Assume FDs:
- `OrderID -> OrderDate, CustomerID`
- `CustomerID -> CustomerName`
- `ProductID -> ProductName, UnitPrice`
- Key for line items: `(OrderID, ProductID) -> Qty` (plus other determined values via FDs)

Problems:
- `CustomerName` depends on `CustomerID` (transitive through OrderID).
- Product details repeated for each order line.

3NF decomposition:
- `Orders(OrderID, OrderDate, CustomerID)`
- `Customers(CustomerID, CustomerName)`
- `Products(ProductID, ProductName, UnitPrice)`
- `OrderItems(OrderID, ProductID, Qty)`

## 7) Normalization vs Denormalization (real-world note)
- **Normalize** for data integrity and consistency.
- **Denormalize** sometimes for performance (fewer joins), analytics, or caching — but accept redundancy and handle it carefully.

## 8) Quick revision checklist (exam-friendly)
- 1NF: atomic values, no repeating groups.
- 2NF: no partial dependency on part of composite key.
- 3NF: no transitive dependency of non-key on key.
- BCNF: every FD determinant is a super key.
- 4NF: no non-trivial MVD unless determinant is a super key.
- Lossless join: join gives exactly original.
- Dependency preservation: constraints enforceable without joins.

