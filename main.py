import pandas as pd
from fpdf import FPDF

df = pd.read_csv("data/energy_log.csv")

pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", size=12)

pdf.cell(
    200,
    10,
    txt="Smart Home Energy Report",
    ln=True,
    align="C"
)

for _, row in df.tail(30).iterrows():

    line = (
        f"{row['Timestamp']} | "
        f"{row['Appliance']} | "
        f"{row['Power']}W | "
        f"₹{row['Cost']}"
    )

    pdf.cell(200, 8, txt=line, ln=True)

pdf.output("outputs/energy_report.pdf")

print("Report Generated")