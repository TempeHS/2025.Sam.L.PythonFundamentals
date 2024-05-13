from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "", 50)
        self.cell(0, 60, "CS50 Shirtificate", align="C")
        self.image(
            "/workspaces/2025.Sam.L.PythonFundamentals/8-OOP/shirtificate/shirtificate.png",
            10,
            70,
            190,
        )
        self.set_font_size(30)
        self.ln(20)


def main():
    name = input("Your name: ")
    shirt(name)


def shirt(s):
    pdf = PDF()
    pdf.add_page(orientation="P", format="A4")
    pdf.output("shirtificate.pdf")
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 213, f"{s} took CS50", align="C")


if __name__ == "__main__":
    main()
