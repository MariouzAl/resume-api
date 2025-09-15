from src.resume.application.use_cases.i_resume_generator import IResumeGenerator
from src.resume.domain.entities.resume import ResumeEntity

from fpdf import FPDF, text_region, enums


def get_skill_level(level: int):
    if level > 80:
        return "Advanced"
    if level > 50:
        return "Intermediate"
    return "Basic"


class PDFResumeGenarator(IResumeGenerator):
    def generate(self, data: ResumeEntity) -> bytes:
        # this will define the ELEMENTS that will compose the template.
        margin_left = 20
        margin_top = 20
        margin_right = 20
        margin_bottom = 20
        pdf = FPDF(format="Letter", unit="mm")
        pdf.set_margins(margin_left, margin_top, margin_right)
        pdf.set_font(family="Helvetica", size=int(16 * 0.352778))
        pdf.set_auto_page_break(auto=True, margin=margin_bottom)

        pdf.add_page()

        pdf.set_font("Helvetica", "B", 16)
        pdf.set_text_color(69, 151, 211)
        pdf.cell(0, 8, text=data.focus, ln=True, align="L")
        pdf.set_text_color(0, 85, 150)
        pdf.cell(0, 8, text=f"{data.profile.name}", ln=True, align="L")
        pdf.set_font_size(9)
        pdf.cell(0, 4, text=f"{data.profile.city}", ln=True, align="L")
        pdf.cell(0, 4, text=f"{data.profile.email}", ln=True, align="L")
        pdf.cell(0, 4, text=f"{data.profile.phone}", ln=True, align="L")
        pdf.ln()
        cols: text_region.TextColumns = pdf.text_columns(
            text_align="JUSTIFY", ncols=2, gutter=5
        )
        with cols:
            pdf.set_font_size(12)
            cols.write("PROFESSIONAL SUMMARY")
            cols.ln()
            cols.ln()
            pdf.set_font("Helvetica", "", 9)
            pdf.set_text_color(26, 27, 38)
            cols.write(text=data.tech_profile.description)
            cols.new_column()
            # cols.multi_cell(210/2,None,text=data.tech_profile.description,ln=True)
            pdf.set_font("Helvetica", "B", 16)
            pdf.set_font_size(12)
            pdf.set_text_color(0, 85, 150)
            cols.write(text="INDUSTRIES")
            cols.ln()
            cols.ln()
            pdf.set_font("Helvetica", "", 9)
            pdf.set_text_color(26, 27, 38)
            cols.write(text="- Healthcare")
            cols.ln()
            cols.write(text="- Education")
            cols.ln()
            cols.write(text="- Business Intelligence")
            cols.ln()
            cols.write(text="- Military")
            cols.ln()
            cols.write(text="- International Trade")
            cols.ln()
            cols.write(text="- Scientific Research")
            cols.ln()
            cols.ln()
            pdf.set_font("Helvetica", "B", 16)
            pdf.set_font_size(12)
            pdf.set_text_color(0, 85, 150)
            cols.write('LANGUAGES')
            cols.ln()
            cols.ln()
            pdf.set_font("Helvetica", "", 9)
            pdf.set_text_color(26, 27, 38)
            for lang in data.languages:
                cols.write(f'-{lang.language}: {lang.level} ')
                cols.ln()
            

        pdf.set_xy(pdf.l_margin, pdf.get_y() + pdf.font_size * 1.5)

        pdf.set_font("Helvetica", "B", 16)
        pdf.set_font_size(12)
        pdf.set_text_color(0, 85, 150)
        pdf.cell(0, 4, text="TECHNICAL SKILLS", ln=True, align="L")
        pdf.ln()
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(26, 27, 38)
        ypos = pdf.get_y()
        xpos = pdf.get_x()
        midpoint = len(data.skills) // 2
        skills_list = [data.skills[:midpoint], data.skills[midpoint:]]
        with pdf.table(
            col_widths=(2, 1, 1),
            width=85,
            borders_layout=enums.TableBordersLayout.HORIZONTAL_LINES,
            align="LEFT",
        ) as table:
            row = table.row()
            row.cell(align="L", text="Skill")
            row.cell(text="Level")
            row.cell(align="R", text="Years")
            for skill in skills_list[0]:
                row = table.row()
                row.cell(align="L", text=skill.skill)
                row.cell(text=get_skill_level(skill.level))
                row.cell(align="R", text=f"{skill.get_years_of_experience()}")

        pdf.set_xy(115, ypos)
        with pdf.table(
            col_widths=(2, 1, 1),
            width=85,
            borders_layout=enums.TableBordersLayout.HORIZONTAL_LINES,
            align="LEFT",
        ) as table:
            row = table.row()
            row.cell(align="L", text="Skill")
            row.cell(text="Level")
            row.cell(align="R", text="Years")
            for skill in skills_list[1]:
                row = table.row()
                row.cell(align="L", text=skill.skill)
                row.cell(text=get_skill_level(skill.level))
                row.cell(align="R", text=f"{skill.get_years_of_experience()}")

        pdf.set_x(xpos)
        pdf.ln()
        pdf.set_font("Helvetica", "B", 16)
        pdf.set_font_size(12)
        pdf.set_text_color(0, 85, 150)
        pdf.cell(0, 4, text="PROFESSIONAL EXPERIENCE", ln=True, align="L")
        pdf.ln()
        initial_x = pdf.get_x()
        for pe in data.professional_experiences:
            pdf.ln()
            if pe.projects is None:
                break
            for pro in pe.projects:
                pdf.set_font("Helvetica", "B", 16)
                pdf.set_font_size(11)
                pdf.set_text_color(0, 85, 150)
                pdf.set_x(initial_x)
                pdf.write(
                    text=f"{pro.start_date.year}-{pro.end_date.year} | Project: {pro.project} - {pe.position} at {pe.company.name} ",
                )
                pdf.ln(pdf.font_size * 2)

                PADDING_LEFT = 50
                pdf.set_x(initial_x + PADDING_LEFT)
                pdf.set_font("Helvetica", "BU", 10)
                pdf.set_text_color(26, 27, 38)
                pdf.write(text="About:")
                pdf.set_font("Helvetica", "", 9)
                pdf.set_x(pdf.get_x() + 3)
                pdf.multi_cell(
                    w=pdf.w - pdf.l_margin - pdf.r_margin - PADDING_LEFT - 5,
                    ln=True,
                    text=f"{pro.shortDescription}",
                )
                pdf.ln(pdf.font_size * 1.5)
                pdf.set_font("Helvetica", "BU", 10)
                pdf.set_x(initial_x + PADDING_LEFT)
                pdf.cell(text="Responsibilities:", ln=True)
                pdf.ln(pdf.font_size * 1.2)
                pdf.set_font("Helvetica", "", 9)
                for resp in pro.responsibilities:
                    pdf.set_x(initial_x + PADDING_LEFT)
                    pdf.cell(text=f"-{resp}", ln=True)
                pdf.ln(pdf.font_size * 1.5)
                pdf.set_font("Helvetica", "BU", 10)
                pdf.set_x(initial_x + PADDING_LEFT)
                pdf.cell(text="Tecnologies:", ln=True)
                pdf.ln(pdf.font_size * 1.2)
                pdf.set_font("Helvetica", "", 9)
                for tech in pro.builtWith:
                    pdf.set_x(initial_x + PADDING_LEFT)
                    pdf.cell(text=f"-{tech}", ln=True)
                pdf.ln(pdf.font_size * 1.5)

        pdf.set_font("Helvetica", "B", 16)
        pdf.set_font_size(12)
        pdf.set_text_color(0, 85, 150)
        pdf.cell(0, 4, text="EDUCATION", ln=True, align="L")
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(26, 27, 38)
        for ed_item in data.education:
            pdf.set_x(initial_x + PADDING_LEFT)
            pdf.multi_cell(
                w=pdf.w - pdf.l_margin - pdf.r_margin - PADDING_LEFT - 5,
                ln=True,
                text=f"- {ed_item.title} | {ed_item.institute} ({ed_item.dateStart.year}-{ed_item.dateFinished.year})",
            )
            pdf.ln()

        return bytes(pdf.output())
