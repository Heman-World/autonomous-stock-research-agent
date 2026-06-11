def generate_report(company, results):
    report = f"""
Stock Analysis REPORT
=====================

company: {company}

Highest Close: {results['highest_close']:.2f}
Lowest Close: {results['lowest_close']:.2f}
Average Volume: {results['average_volume']:.0f}
"""

    with open (f"reports/{company}_summary.txt", "w") as file:
        file.write(report)