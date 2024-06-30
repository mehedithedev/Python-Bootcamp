from fpdf import FPDFimport pandas as pdpdf = FPDF(orientation="P", unit="mm", format = "A4")pdf.set_auto_page_break(auto=False, margin=0)df = pd.read_csv("topics.csv")for index, row in df.iterrows():    pdf.add_page() # Master page    pdf.set_font(family="Times", style='B', size=24)    pdf.set_text_color(100,100,100)    pdf.cell(w=0, h=24, txt=row['Topic'], align="L", ln=1)    for i in range(27, 265, 5):        pdf.line(x1=10, y1=i, x2=200, y2=i)    pdf.ln(265)    # Set the footer    pdf.set_font(family="Times", style="I", size=8)    pdf.set_text_color(180,180,180)    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")    for i in range(row["Pages"] - 1):        pdf.add_page() # Extra page according to the csv file        # Set the footer        pdf.ln(277)        pdf.set_font(family="Times", style="I", size=8)        pdf.set_text_color(180, 180, 180)        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")        for i in range(27, 265, 5):            pdf.line(x1=10, y1=i, x2=200, y2=i)pdf.output("output.pdf")