# Hack, Law and Ethics: A Case Study Presentation
# Topics: Cyber Laws, Cybercrime Incidents, and Ethical Dilemmas

case_studies = {
    1: {
        "title": "The WannaCry Ransomware Attack (2017)",
        "incident": (
            "WannaCry was a worldwide ransomware cyberattack that targeted computers "
            "running Microsoft Windows. It encrypted data and demanded ransom payments "
            "in Bitcoin, affecting over 200,000 computers across 150 countries."
        ),
        "law": (
            "Applicable Laws:\n"
            "  - Computer Fraud and Abuse Act (CFAA) - USA\n"
            "  - Information Technology Act, 2000 (Section 66) - India\n"
            "  - Budapest Convention on Cybercrime - International"
        ),
        "ethics": (
            "Ethical Dilemma:\n"
            "  - Should victims pay the ransom to recover critical data?\n"
            "  - Paying ransom funds future criminal activity.\n"
            "  - Not paying may result in permanent loss of sensitive data."
        ),
    },
    2: {
        "title": "The Facebook-Cambridge Analytica Data Scandal (2018)",
        "incident": (
            "Cambridge Analytica harvested personal data from millions of Facebook "
            "profiles without consent and used it for political advertising. "
            "Up to 87 million Facebook users were affected."
        ),
        "law": (
            "Applicable Laws:\n"
            "  - General Data Protection Regulation (GDPR) - EU\n"
            "  - Federal Trade Commission Act (FTC Act) - USA\n"
            "  - Information Technology (Amendment) Act, 2008 - India"
        ),
        "ethics": (
            "Ethical Dilemma:\n"
            "  - Is it ethical to use personal data for political influence?\n"
            "  - Who bears responsibility: the platform, the data broker, or the user?\n"
            "  - Tension between targeted advertising and individual privacy rights."
        ),
    },
    3: {
        "title": "The Sony Pictures Hack (2014)",
        "incident": (
            "A hacker group calling themselves 'Guardians of Peace' leaked confidential "
            "data from Sony Pictures, including personal employee information, salary details, "
            "unreleased films, and embarrassing emails. The attack was linked to North Korea."
        ),
        "law": (
            "Applicable Laws:\n"
            "  - Computer Fraud and Abuse Act (CFAA) - USA\n"
            "  - Economic Espionage Act - USA\n"
            "  - UN Convention against Transnational Organized Crime - International"
        ),
        "ethics": (
            "Ethical Dilemma:\n"
            "  - Is it ethical for journalists to publish stolen confidential data?\n"
            "  - Should corporations share threat intelligence with governments?\n"
            "  - How should states respond to state-sponsored cyberattacks?"
        ),
    },
}

def display_case_study(case):
    print("-" * 60)
    print(f"Case Study: {case['title']}")
    print("-" * 60)
    print(f"\nIncident:\n  {case['incident']}\n")
    print(f"{case['law']}\n")
    print(f"{case['ethics']}\n")

def main():
    print("=" * 60)
    print("   HACK, LAW AND ETHICS: A CASE STUDY PRESENTATION")
    print("=" * 60)
    print("\nSelect a case study to explore:")
    for key, case in case_studies.items():
        print(f"  {key}. {case['title']}")
    print("  4. View All Case Studies")
    print("  0. Exit")

    while True:
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 0:
            print("Thank you for exploring Hack, Law and Ethics case studies!")
            break
        elif choice in case_studies:
            display_case_study(case_studies[choice])
        elif choice == 4:
            for case in case_studies.values():
                display_case_study(case)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
