from openpyxl import Workbook


def create_excel(test_cases):
    wb = Workbook()

    ws = wb.active
    ws.title = "Test Cases"

    ws.append([
        "Test Case ID",
        "Title",
        "Preconditions",
        "Data",
        "Steps",
        "Expected Result",
        "Actual Result",
        "Priority"
    ])

    for tc in test_cases:

        steps = "\n".join(tc["Steps"])

        ws.append([
            tc["Test Case ID"],
            tc["Title"],
            tc["Preconditions"],
            tc["Data"],
            steps,
            tc["Expected Result"],
            tc["Actual Result"],
            tc["Priority"]
        ])

    wb.save("generated_test_cases.xlsx")