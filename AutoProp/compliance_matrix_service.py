import csv

def create_compliance_matrix(summary_dict):
    matrix = []

    for section_label, summary in summary_dict.items():
        requirements = extract_requirements(summary)
        for requirement in requirements:
            matrix.append({"Section": section_label, "Requirement": requirement})

    return matrix

def extract_requirements(summary):
    # Implement a custom function to extract requirements from the summary
    # For now, we return the summary as a single requirement
    return [summary]

def export_to_csv(matrix, file_name="compliance_matrix.csv"):
    with open(file_name, "w", newline="") as csvfile:
        fieldnames = ["Section", "Requirement"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in matrix:
            writer.writerow(row)
