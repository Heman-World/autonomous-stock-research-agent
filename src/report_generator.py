from config import REPORT_FOLDER
import logging
def generate_report(company, results):
    try:
        report = f"""
Stock Analysis REPORT
=====================

company: {company}

Highest Close: {results['highest_close']:.2f}
Lowest Close: {results['lowest_close']:.2f}
Average Volume: {results['average_volume']:.0f}
"""

        with open (f"{REPORT_FOLDER}/{company}_summary.txt", "w") as file:
            file.write(report)
    except Exception as e:
        logging.error(f"Error while generating report: {e}")
        return None