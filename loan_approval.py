# Loan Approval System using Propositional Logic
# Discrete Mathematics - Logic, Propositions, Truth Tables

def get_applicant():
    print("\nEnter applicant details:")
    name = input("  Applicant name: ")
    age = int(input("  Age: "))
    income = float(input("  Monthly income (Rs.): "))
    credit_score = int(input("  Credit score (300-900): "))
    employed = input("  Currently employed? (yes/no): ").strip().lower() == "yes"
    existing_loans = int(input("  Number of existing loans: "))
    return {
        "name": name,
        "age": age,
        "income": income,
        "credit_score": credit_score,
        "employed": employed,
        "existing_loans": existing_loans
    }

def evaluate_propositions(applicant):
    P1 = applicant["age"] >= 21 and applicant["age"] <= 60
    P2 = applicant["income"] >= 25000
    P3 = applicant["credit_score"] >= 650
    P4 = applicant["employed"] == True
    P5 = applicant["existing_loans"] <= 2
    return P1, P2, P3, P4, P5

def print_propositions(P1, P2, P3, P4, P5):
    print("\n--- PROPOSITIONS ---")
    print(f"  P1 (Age between 21-60)         : {P1}")
    print(f"  P2 (Income >= Rs. 25,000)       : {P2}")
    print(f"  P3 (Credit score >= 650)        : {P3}")
    print(f"  P4 (Currently employed)         : {P4}")
    print(f"  P5 (Existing loans <= 2)        : {P5}")

def apply_logic(P1, P2, P3, P4, P5):
    basic_eligibility = P1 and P4
    financial_score = sum([P2, P3, P5])
    financial_ok = financial_score >= 2
    approved = basic_eligibility and financial_ok
    return approved, basic_eligibility, financial_score

def print_truth_table():
    print("\n--- TRUTH TABLE (All possible cases for P2, P3, P5) ---")
    print("Assuming P1=True, P4=True (basic eligibility met)")
    print(f"{'P2':<6} {'P3':<6} {'P5':<6} {'Financial Score':<18} {'Approved'}")
    print("-" * 50)
    for p2 in [True, False]:
        for p3 in [True, False]:
            for p5 in [True, False]:
                score = sum([p2, p3, p5])
                approved = score >= 2
                print(f"  {str(p2):<6} {str(p3):<6} {str(p5):<6} {score:<18} {approved}")

def print_result(applicant, approved, basic_eligibility, financial_score):
    print(f"\n--- RESULT FOR {applicant['name'].upper()} ---")
    if not basic_eligibility:
        print("  Basic eligibility FAILED (Age or Employment condition not met)")
    else:
        print("  Basic eligibility PASSED")
        print(f"  Financial conditions met: {financial_score} out of 3 (need at least 2)")
    if approved:
        print("\n  ✓ LOAN APPROVED")
    else:
        print("\n  ✗ LOAN REJECTED")

def main():
    print("=== LOAN APPROVAL SYSTEM (Propositional Logic) ===")
    while True:
        applicant = get_applicant()
        P1, P2, P3, P4, P5 = evaluate_propositions(applicant)
        print_propositions(P1, P2, P3, P4, P5)
        approved, basic_eligibility, financial_score = apply_logic(P1, P2, P3, P4, P5)
        print_truth_table()
        print_result(applicant, approved, basic_eligibility, financial_score)
        again = input("\nCheck another applicant? (yes/no): ").strip().lower()
        if again != "yes":
            break
    print("\n=== DONE ===")

main()
