from pathlib import Path
import base64
from PIL import Image as PILImage
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, Flowable
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'Documentation'
RENDERS = ROOT / 'Designs' / 'Mechanical_Design' / 'Renders'
PITCH_DIR = DOC / 'Pitch_Deck'
REPORT_DIR = DOC / 'Holistic_Build_Document'
PITCH_PDF = PITCH_DIR / 'SentinelT_Pitch_Deck.pdf'
REPORT_PDF = REPORT_DIR / 'SentinelT_Holistic_Build_Document.pdf'
PHOTO_B64 = PITCH_DIR / 'Thato_Glen_Assegaai_photo.b64'
PHOTO = PITCH_DIR / '.Thato_Glen_Assegaai.jpg'

FRONT = RENDERS / '01_SentinelT_FRONT_FINAL.png'
SIDE = RENDERS / '02_SentinelT_SIDE_FINAL.png'
TOP = RENDERS / '03_SentinelT_TOP_FINAL.png'
ISO = RENDERS / '04_SentinelT_ISOMETRIC_FINAL.png'

PAGE_W, PAGE_H = A4
M = 2.4 * cm
RED = HexColor('#8F1414')
DARK = HexColor('#202020')
MID = HexColor('#555555')
LIGHT = HexColor('#F5F5F5')
BORDER = HexColor('#D6D6D6')


def prepare_photo():
    PHOTO.write_bytes(base64.b64decode(PHOTO_B64.read_text().strip()))


def fit_image(path, max_w, max_h):
    im = PILImage.open(path)
    w, h = im.size
    scale = min(max_w / w, max_h / h)
    return w * scale, h * scale


def wrap_canvas(c, text, x, y, width, font='Helvetica', size=10.5, leading=14):
    c.setFont(font, size)
    words = text.split()
    line = ''
    yy = y
    for word in words:
        candidate = (line + ' ' + word).strip()
        if c.stringWidth(candidate, font, size) <= width:
            line = candidate
        else:
            c.drawString(x, yy, line)
            yy -= leading
            line = word
    if line:
        c.drawString(x, yy, line)
        yy -= leading
    return yy


def draw_power(c, x, y, w, h):
    c.saveState()
    c.setFillColor(DARK)
    c.setFont('Helvetica-Bold', 13)
    c.drawCentredString(x + w / 2, y + h - 18, 'SentinelT Power & E-Stop Architecture')
    labels = [
        ('3S LiPo Battery', 'Primary energy source', False),
        ('Main Fuse / Protection', 'Protects battery path', False),
        ('MAIN ON/OFF ISOLATOR', 'Accessible primary isolation', False),
        ('E-STOP PUSHBUTTON', 'Emergency command input', True),
        ('HIGH-CURRENT RELAY / CONTACTOR', 'Interrupts actuator power', True),
        ('POWER DISTRIBUTION', 'Drive, control and auxiliary branches', False),
    ]
    top = y + h - 48
    box_h = 47
    gap = 10
    box_w = w * 0.70
    bx = x + (w - box_w) / 2
    centres = []
    for title, subtitle, danger in labels:
        by = top - box_h
        c.setStrokeColor(RED if danger else DARK)
        c.setFillColor(HexColor('#FFF7F7') if danger else LIGHT)
        c.roundRect(bx, by, box_w, box_h, 7, fill=1, stroke=1)
        c.setFillColor(RED if danger else DARK)
        c.setFont('Helvetica-Bold', 8.5)
        c.drawCentredString(bx + box_w / 2, by + 28, title)
        c.setFillColor(MID)
        c.setFont('Helvetica', 6.7)
        c.drawCentredString(bx + box_w / 2, by + 13, subtitle)
        centres.append((bx + box_w / 2, by))
        top = by - gap
    for i in range(len(centres) - 1):
        cx = centres[i][0]
        c.setStrokeColor(DARK)
        c.line(cx, centres[i][1] - 2, cx, centres[i + 1][1] + box_h + 2)
    branch_y = y + 25
    branch_w = w * 0.25
    for label, cx in [('DRIVE BRANCH', x + w * .20), ('AUXILIARY BRANCH', x + w * .50), ('CONTROL BRANCH', x + w * .80)]:
        c.setStrokeColor(DARK)
        c.setFillColor(LIGHT)
        c.roundRect(cx - branch_w / 2, branch_y, branch_w, 38, 6, fill=1, stroke=1)
        c.setFillColor(DARK)
        c.setFont('Helvetica-Bold', 7.3)
        c.drawCentredString(cx, branch_y + 21, label)
    pd_bottom = centres[-1][1]
    pd_cx = centres[-1][0]
    c.setStrokeColor(DARK)
    c.line(pd_cx, pd_bottom - 2, pd_cx, branch_y + 68)
    for cx in (x + w * .20, x + w * .50, x + w * .80):
        c.line(pd_cx, branch_y + 68, cx, branch_y + 68)
        c.line(cx, branch_y + 68, cx, branch_y + 38)
    c.restoreState()


def draw_control(c, x, y, w, h):
    c.saveState()
    c.setFillColor(DARK)
    c.setFont('Helvetica-Bold', 13)
    c.drawCentredString(x + w / 2, y + h - 18, 'SentinelT 2.4 GHz RC Control Flow')
    safe_w = w * .27
    main_x = x + safe_w + 22
    main_w = w - safe_w - 22
    steps = [
        'POWER ON',
        'Initialize controller; outputs OFF',
        'Check hardware E-Stop condition',
        'Read and validate 2.4 GHz RC signal',
        'Read throttle / steering / auxiliary enable',
        'Apply differential drive + auxiliary control',
        'Continue only while safety conditions remain valid',
    ]
    box_h = 41
    gap = 11
    top = y + h - 54
    boxes = []
    for s in steps:
        by = top - box_h
        c.setFillColor(LIGHT)
        c.setStrokeColor(DARK)
        c.roundRect(main_x, by, main_w, box_h, 6, fill=1, stroke=1)
        c.setFillColor(DARK)
        c.setFont('Helvetica-Bold', 7.2)
        c.drawCentredString(main_x + main_w / 2, by + 17, s)
        boxes.append((main_x, by, main_w, box_h))
        top = by - gap
    for i in range(len(boxes) - 1):
        cx = main_x + main_w / 2
        c.line(cx, boxes[i][1] - 2, cx, boxes[i + 1][1] + box_h + 2)
    sy = boxes[2][1] - 95
    c.setStrokeColor(RED)
    c.setFillColor(HexColor('#FFF7F7'))
    c.roundRect(x, sy, safe_w, 105, 7, fill=1, stroke=1)
    c.setFillColor(RED)
    c.setFont('Helvetica-Bold', 9.2)
    c.drawCentredString(x + safe_w / 2, sy + 72, 'SAFE DISABLED')
    c.setFont('Helvetica-Bold', 7.4)
    c.drawCentredString(x + safe_w / 2, sy + 48, 'Drive OFF | Auxiliary OFF')
    c.setFillColor(MID)
    c.setFont('Helvetica', 6.3)
    c.drawCentredString(x + safe_w / 2, sy + 22, 'Re-check E-Stop and RC link')
    for idx, lab in [(2, 'E-STOP ACTIVE'), (3, 'RC INVALID / LOST')]:
        by = boxes[idx][1] + box_h / 2
        c.setStrokeColor(RED)
        c.line(main_x, by, x + safe_w, by)
        c.setFillColor(RED)
        c.setFont('Helvetica-Bold', 5.8)
        c.drawRightString(main_x - 3, by + 5, lab)
    c.restoreState()


def make_pitch():
    c = canvas.Canvas(str(PITCH_PDF), pagesize=A4, pageCompression=1)
    c.setTitle('SentinelT Pitch Deck')
    c.setAuthor('Thato Glen Assegaai')

    def head(title, subtitle=''):
        c.setFillColor(white); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
        c.setFillColor(RED); c.rect(M, PAGE_H - 1.55 * cm, PAGE_W - 2 * M, .07 * cm, fill=1, stroke=0)
        c.setFillColor(DARK); c.setFont('Helvetica-Bold', 23); c.drawString(M, PAGE_H - 2.55 * cm, title)
        if subtitle:
            c.setFillColor(MID); c.setFont('Helvetica', 10.5); c.drawString(M, PAGE_H - 3.12 * cm, subtitle)

    def foot(n):
        c.setFillColor(MID); c.setFont('Helvetica', 8.4)
        c.drawString(M, .9 * cm, 'SentinelT | Thato Glen Assegaai')
        c.drawRightString(PAGE_W - M, .9 * cm, f'{n} / 7')

    def bullets(items, x, y, width, size=12, leading=16, gap=5):
        yy = y
        c.setFillColor(DARK)
        for item in items:
            c.setFont('Helvetica', size)
            words, line, lines = item.split(), '', []
            for word in words:
                candidate = (line + ' ' + word).strip()
                if c.stringWidth(candidate, 'Helvetica', size) <= width - 16: line = candidate
                else: lines.append(line); line = word
            if line: lines.append(line)
            c.drawString(x, yy, u'\u2022')
            for j, line in enumerate(lines): c.drawString(x + 14, yy - j * leading, line)
            yy -= len(lines) * leading + gap
        return yy

    def card(y, label, value, height=1.75 * cm):
        c.setFillColor(LIGHT); c.setStrokeColor(BORDER); c.roundRect(M, y, PAGE_W - 2 * M, height, 7, fill=1, stroke=1)
        c.setFillColor(MID); c.setFont('Helvetica-Bold', 8.8); c.drawString(M + 12, y + height - 17, label)
        c.setFillColor(RED); c.setFont('Helvetica-Bold', 18); c.drawString(M + 12, y + 14, value)

    head('SENTINELT', 'Robo Wars RC Combat Robot')
    c.setFillColor(RED); c.setFont('Helvetica-Bold', 15); c.drawString(M, PAGE_H - 4.25 * cm, 'Designed and developed by Thato Glen Assegaai')
    c.setFillColor(MID); c.setFont('Helvetica', 10.5); c.drawString(M, PAGE_H - 4.85 * cm, 'Independent mechanical, control, safety and documentation development')
    iw, ih = fit_image(ISO, PAGE_W - 2 * M, 13.7 * cm); c.drawImage(str(ISO), (PAGE_W - iw) / 2, 4.1 * cm, iw, ih, preserveAspectRatio=True, mask='auto')
    c.setFillColor(DARK); c.setFont('Helvetica-Bold', 10.5); c.drawCentredString(PAGE_W / 2, 2.35 * cm, 'Verified CAD envelope: 318.16 mm x 495.00 mm x 255.41 mm')
    c.setFillColor(MID); c.setFont('Helvetica', 9.5); c.drawCentredString(PAGE_W / 2, 1.85 * cm, 'Footprint audit: 180 / 180 frames PASS'); foot(1); c.showPage()

    head('Robo Wars Design Requirements', 'Engineering limits built directly into SentinelT')
    bullets(['Maximum footprint: 500 mm x 500 mm.', 'Robot mass: strictly below 5 kg.', 'Human-operated remote control limited to 2.4 GHz.', 'Accessible main ON/OFF power isolation.', 'Emergency Stop mechanism that disables actuator power.', 'No projectiles, flames or liquids.'], M + .64 * cm, PAGE_H - 4.2 * cm, PAGE_W - 2 * M - .64 * cm, 13.2, 18, 7)
    card(7.0 * cm, 'VERIFIED SENTINELT FOOTPRINT', '318.16 mm x 495.00 mm', 2.0 * cm)
    card(4.45 * cm, 'ENGINEERING MASS ALLOCATION', '4.650 kg', 2.0 * cm)
    c.setFillColor(MID); c.setFont('Helvetica', 9.5); c.drawString(M, 3.55 * cm, 'The mass value is an engineering budget and will be physically verified after fabrication.'); foot(2); c.showPage()

    head('SentinelT Solution & Buildability', 'Compact, serviceable and safety-focused Robo Wars architecture')
    iw, ih = fit_image(FRONT, PAGE_W - 2 * M, 10 * cm); c.drawImage(str(FRONT), (PAGE_W - iw) / 2, PAGE_H - 14.3 * cm, iw, ih, preserveAspectRatio=True, mask='auto')
    bullets(['Armored HDPE chassis with protected wheel and drive areas.', 'Sloped front and side protection with removable service panels.', 'Direct-drive 12 V geared motors with 125 mm wheels.', 'Accessible internal packaging for battery, receiver, ESC and safety hardware.', '2.4 GHz human-operated control with safe-state logic.', 'Guarded active-mechanism provision integrated into the chassis layout.'], M + .64 * cm, 8.2 * cm, PAGE_W - 2 * M - .64 * cm, 11.7, 16, 5); foot(3); c.showPage()

    head('Mechanical CAD & Verification', 'Blender CAD and Python-based dimensional auditing')
    iw, ih = fit_image(TOP, PAGE_W - 2 * M, 9.5 * cm); c.drawImage(str(TOP), (PAGE_W - iw) / 2, PAGE_H - 13.9 * cm, iw, ih, preserveAspectRatio=True, mask='auto')
    card(7.25 * cm, 'MAXIMUM CAD WIDTH (X)', '318.16 mm', 1.65 * cm); card(5.15 * cm, 'MAXIMUM CAD LENGTH (Y)', '495.00 mm', 1.65 * cm); card(3.05 * cm, 'ANIMATION-RANGE FOOTPRINT RESULT', '180 / 180 frames PASS', 1.65 * cm); foot(4); c.showPage()

    head('Electronics, Control & Safety', 'Main isolation, E-Stop and 2.4 GHz RC architecture')
    draw_power(c, M, 6.1 * cm, PAGE_W - 2 * M, 17.8 * cm)
    bullets(['3S 11.1 V LiPo power architecture.', '2.4 GHz receiver and safe-state control logic.', 'Main ON/OFF isolation is upstream of actuator distribution.', 'Emergency pushbutton commands a separate high-current isolation device.'], M + .64 * cm, 4.2 * cm, PAGE_W - 2 * M - .64 * cm, 10.3, 14, 4); foot(5); c.showPage()

    head('Mass, Components & Cost', 'Current engineering procurement plan')
    card(20.0 * cm, 'ENGINEERING MASS BUDGET', '4.650 kg'); card(17.75 * cm, 'DESIGN MARGIN BELOW 5 KG', '0.350 kg'); card(15.30 * cm, 'CURRENT PRICED COMPONENT SUBTOTAL', 'R 8,039.15', 1.95 * cm)
    bullets(['Priced: HDPE chassis / armor stock, drive motors, wheels, RC system, battery, ESC, isolation, E-Stop hardware, power distribution, wiring and fasteners.', 'The guarded active-mechanism motor / controller remains marked TBD until its mass and electrical compatibility are finalized.', 'The Bill of Materials records quantity, unit cost, supplier, stock code, direct URL and total line cost.'], M + .64 * cm, 13.5 * cm, PAGE_W - 2 * M - .64 * cm, 11.5, 15.8, 6)
    c.setFillColor(MID); c.setFont('Helvetica', 9.2); c.drawString(M, 3.2 * cm, 'R8,039.15 is a priced subtotal, not the final implementation total.'); foot(6); c.showPage()

    head('Project Owner & Responsibilities', 'Thato Glen Assegaai')
    iw, ih = fit_image(PHOTO, 8.3 * cm, 8.6 * cm); c.drawImage(str(PHOTO), (PAGE_W - iw) / 2, PAGE_H - 12.2 * cm, iw, ih, preserveAspectRatio=True, mask='auto')
    bullets(['Robo Wars system concept and engineering architecture.', 'Blender CAD modelling and mechanical packaging.', 'Python-based footprint and mass-budget tools.', '2.4 GHz RC control framework and safe-state logic.', 'Main ON/OFF and E-Stop safety architecture.', 'Component research, Bill of Materials and procurement planning.', 'Technical documentation and GitHub repository organisation.'], M + .64 * cm, 9.15 * cm, PAGE_W - 2 * M - .64 * cm, 10.8, 14.6, 4)
    c.setFillColor(MID); c.setFont('Helvetica', 8.9); c.drawString(M, 2.45 * cm, 'Third-party commercial components are identified by manufacturer and supplier in the Bill of Materials.'); foot(7); c.showPage(); c.save()


class PowerFlowable(Flowable):
    def __init__(self, width, height):
        super().__init__(); self.width = width; self.height = height
    def draw(self): draw_power(self.canv, 0, 0, self.width, self.height)


class ControlFlowable(Flowable):
    def __init__(self, width, height):
        super().__init__(); self.width = width; self.height = height
    def draw(self): draw_control(self.canv, 0, 0, self.width, self.height)


def make_report():
    styles = getSampleStyleSheet()
    body = ParagraphStyle('BodyX', parent=styles['BodyText'], fontName='Helvetica', fontSize=10.5, leading=14, textColor=DARK, leftIndent=.64 * cm, rightIndent=0, spaceBefore=0, spaceAfter=8)
    h1 = ParagraphStyle('H1X', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=16, leading=19, textColor=RED, leftIndent=.64 * cm, spaceBefore=0, spaceAfter=8)
    h2 = ParagraphStyle('H2X', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=12.5, leading=15, textColor=DARK, leftIndent=.64 * cm, spaceBefore=0, spaceAfter=8)
    cap = ParagraphStyle('CapX', parent=body, fontName='Helvetica-Oblique', fontSize=9, leading=11, textColor=MID, alignment=TA_CENTER, leftIndent=0, spaceAfter=8)
    cover = ParagraphStyle('CoverX', parent=body, fontName='Helvetica-Bold', fontSize=28, leading=32, textColor=RED, alignment=TA_CENTER, leftIndent=0, spaceAfter=10)
    cover2 = ParagraphStyle('Cover2X', parent=body, fontName='Helvetica-Bold', fontSize=17, leading=21, textColor=DARK, alignment=TA_CENTER, leftIndent=0, spaceAfter=10)

    def hf(c, doc):
        c.saveState(); c.setFont('Helvetica', 8); c.setFillColor(MID)
        c.drawCentredString(PAGE_W / 2, PAGE_H - 1.35 * cm, 'SentinelT | Robo Wars RC Combat Robot | Thato Glen Assegaai')
        c.drawCentredString(PAGE_W / 2, 1.0 * cm, f'SentinelT - Independent engineering design | Page {doc.page}'); c.restoreState()

    def img(path, mw, mh):
        w, h = fit_image(path, mw, mh); return Image(str(path), width=w, height=h)

    def table(data, widths):
        t = Table(data, colWidths=widths, repeatRows=1, hAlign='CENTER')
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),LIGHT),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTNAME',(0,1),(-1,-1),'Helvetica'),('FONTSIZE',(0,0),(-1,-1),9),('LEADING',(0,0),(-1,-1),11),('GRID',(0,0),(-1,-1),.5,BORDER),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)])); return t

    S = [Spacer(1,1.1*cm), Paragraph('SENTINELT',cover), Paragraph('Robo Wars RC Combat Robot',cover2), Paragraph('Holistic Build Document',ParagraphStyle('subx',parent=cover2,fontSize=14,textColor=MID)), Paragraph('Designed and developed by Thato Glen Assegaai',ParagraphStyle('ownx',parent=body,fontName='Helvetica-Bold',fontSize=12,alignment=TA_CENTER,leftIndent=0)), Spacer(1,.25*cm), img(ISO,15.5*cm,10.8*cm), Paragraph('Verified CAD envelope: 318.16 mm x 495.00 mm x 255.41 mm | Footprint audit: 180/180 frames PASS',cap), PageBreak()]
    S += [Paragraph('1. Project Ownership and Overview',h1), Paragraph('SentinelT is my independently designed Robo Wars RC combat robot. I developed the mechanical concept, Blender CAD model, dimensional-verification scripts, 2.4 GHz control framework, power and safety architecture, component plan and technical documentation represented in this repository.',body), Paragraph('The current build is complete as a digital engineering design. Physical fabrication and hardware validation remain separate implementation stages, so measured mass, current draw, thermal performance and physical E-Stop response are not claimed as completed results.',body), table([['Design item','Current verified state'],['CAD width (X)','318.16 mm'],['CAD length (Y)','495.00 mm'],['CAD height (Z)','255.41 mm'],['Footprint verification','180 / 180 frames PASS'],['Engineering mass budget','4.650 kg'],['Design margin below 5 kg','0.350 kg'],['Control architecture','Human-operated 2.4 GHz RC']],[7*cm,8*cm]), Spacer(1,.2*cm), Paragraph('2. Robo Wars Design Requirements',h1), Paragraph('SentinelT is engineered around the Robo Wars operating envelope and safety requirements: a maximum 500 mm x 500 mm footprint, mass below 5 kg, 2.4 GHz human-operated RC, accessible main ON/OFF isolation, an Emergency Stop power-disable mechanism and no projectiles, flames or liquids.',body), PageBreak()]
    S += [Paragraph('3. Mechanical Design',h1), Paragraph('SentinelT uses a compact armored lower chassis with protected drive areas, sloped external protection, a central service volume, removable access panels and an articulated upper structure.',body), img(FRONT,15.5*cm,11.2*cm), Paragraph('Figure 1. Front CAD view of SentinelT.',cap), Paragraph('3.1 Fabrication and materials',h2), Paragraph('The current material plan uses 6 mm HDPE sheet for the chassis and shared armor panels, with metal hardware used where load transfer, motor housings, shafts, brackets, electrical terminals and fasteners require it. Bolted construction keeps the design serviceable and compatible with the 4.650 kg engineering mass budget.',body), PageBreak()]
    S += [Paragraph('4. Electronic Design',h1), Paragraph('The electronic system is organized around a 3S battery, high-current power distribution, 2.4 GHz RC control and independent safety isolation. The component plan is treated as a matched engineering system and remains subject to final physical validation.',body), table([['Subsystem','Selected / planned component'],['Drive motors','2 x Pololu 4743 50:1 12 V 200 RPM 37D metal gearmotors'],['Drive wheels','125 mm all-terrain pair with 6 mm shaft fittings'],['Drive controller','HobbyWing QuicRun WP 880 dual brushed ESC'],['RC link','FlySky FS-i6X transmitter + X6B receiver, 2.4 GHz'],['Battery','BEAT 5000 mAh 11.1 V 3S LiPo, XT60'],['Power distribution','100 A 4-way terminal block'],['Main isolation','12 V 100 A battery isolator candidate'],['E-Stop control','Emergency pushbutton + separate high-current relay / contactor candidate'],['Power wiring','10 mm2 silicone red / black high-current wiring set']],[5.1*cm,9.9*cm]), PageBreak()]
    S += [Paragraph('5. Power and E-Stop Safety Architecture',h1), Paragraph('The main ON/OFF function and Emergency Stop function are explicit parts of the power path. The emergency pushbutton is not assumed to interrupt full traction or auxiliary current directly; it commands a separate high-current power-isolation device.',body), PowerFlowable(15.4*cm,18.6*cm), Paragraph('Figure 2. SentinelT power, control and E-Stop architecture.',cap), PageBreak()]
    S += [Paragraph('6. 2.4 GHz RC Control',h1), Paragraph('SentinelT is human-operated through a 2.4 GHz transmitter and receiver. The operator provides throttle, steering and auxiliary-enable commands. Throttle and steering are converted into differential-drive commands, while auxiliary actuation remains disabled by default.',body), Paragraph('7. Programming and Framework Design',h1), Paragraph('The software architecture is written specifically for Robo Wars operation. Human RC input is always gated by hardware safety state, signal validity and the auxiliary-enable command.',body), ControlFlowable(15.4*cm,18.2*cm), Paragraph('Figure 3. SentinelT safe-state control-flow logic.',cap), PageBreak()]
    S += [Paragraph('8. Simulation and Digital Verification',h1), Paragraph('I used Blender and Python-based auditing to verify SentinelT before fabrication. The footprint script evaluates visible mesh world-space bounds across frames 1-180 and compares the X and Y dimensions with the 500 mm x 500 mm Robo Wars footprint.',body), table([['Audit parameter','Verified result'],['Maximum X','318.16 mm'],['Maximum Y','495.00 mm'],['Maximum Z','255.41 mm'],['Frames checked','180'],['Failed frames','0'],['Result','PASS']],[7*cm,8*cm]), Spacer(1,.35*cm), img(TOP,15.5*cm,10*cm), Paragraph('Figure 4. Top CAD view used as part of dimensional verification.',cap), PageBreak()]
    S += [Paragraph('9. Engineering Mass Budget',h1), Paragraph('The CAD meshes do not contain verified physical mass metadata, so I use an explicit engineering subsystem allocation rather than claiming a false simulated mass.',body), table([['Subsystem','Planned mass'],['Chassis and lower armor','1.10 kg'],['Drive motors and gearboxes','0.75 kg'],['Wheels, hubs and shafts','0.30 kg'],['Battery and power system','0.60 kg'],['RC electronics, ESC and wiring','0.25 kg'],['Guarded active mechanism + drive / mount','0.70 kg'],['Upper structure, arms and outer shells','0.50 kg'],['Bearings, brackets and fasteners','0.25 kg'],['Contingency allowance','0.20 kg'],['TOTAL','4.650 kg']],[10.5*cm,4.5*cm]), Paragraph('The remaining design allowance is 0.350 kg below 5.000 kg. The completed physical robot must be weighed on a calibrated scale before operational use.',body), PageBreak()]
    S += [Paragraph('10. Bill of Materials and Cost',h1), Paragraph('The Bill of Materials records component name, quantity, unit cost, supplier, supplier stock code, direct purchase URL and total line cost. The current priced component subtotal is R8,039.15. The guarded active-mechanism motor / controller remains intentionally marked TBD until its electrical and mass compatibility is finalized.',body), table([['Core item','Cost status'],['6 mm HDPE chassis / armor stock','Priced'],['Drive motors and wheels','Priced'],['2.4 GHz transmitter + receiver','Priced'],['3S LiPo battery','Priced'],['Dual brushed drive ESC','Priced'],['Main isolation, E-Stop, relay, fuse and distribution','Priced'],['High-current wiring and fasteners','Priced'],['Guarded active-mechanism motor / controller','TBD'],['Current priced component subtotal','R8,039.15']],[10.5*cm,4.5*cm]), Paragraph('BOM file: <link href="../BOM/SentinelT_Bill_of_Materials.xlsx" color="#0000CC">SentinelT_Bill_of_Materials.xlsx</link>',body), PageBreak()]
    S += [Paragraph('11. Buildability and Serviceability',h1), Paragraph('SentinelT is designed as a modular build. Removable panels provide access to the battery, receiver, ESC, power distribution, main isolation and E-Stop control hardware. The selected direct-drive wheels mount to 6 mm motor shafts, reducing separate drivetrain parts.',body), img(SIDE,15.5*cm,10.2*cm), Paragraph('Figure 5. Side CAD view showing the compact chassis envelope.',cap), Paragraph('12. Current Development Status',h1), Paragraph('The digital robot design, external CAD geometry, dimensional simulation, control framework, safety architecture and procurement plan are documented. The next CAD revision adds simplified internal component models, wiring paths, a separate 2.4 GHz transmitter model, a cutaway view and an exploded internal-layout view.',body), Paragraph('Physical claims remain separated from digital results. Final physical mass, current draw, thermal behaviour, drivetrain response and E-Stop interruption performance will be measured after fabrication and bench testing.',body), Paragraph('13. Project Ownership and Responsibilities',h1), Paragraph('SentinelT is independently designed and developed by Thato Glen Assegaai. My responsibilities include system concept, Blender CAD modelling, mechanical packaging, Python-based verification tools, 2.4 GHz RC control framework, safety architecture, component research, Bill of Materials development, technical documentation and repository organisation.',body), Paragraph('Third-party commercial components are identified by manufacturer and supplier names in the Bill of Materials. Their inclusion does not imply ownership of those products; the SentinelT system design, integration plan, CAD work, control framework and documentation are presented as my project work.',body)]
    doc = SimpleDocTemplate(str(REPORT_PDF), pagesize=A4, leftMargin=M, rightMargin=M, topMargin=2.4*cm, bottomMargin=2.4*cm, title='SentinelT Holistic Build Document', author='Thato Glen Assegaai')
    doc.build(S, onFirstPage=hf, onLaterPages=hf)


if __name__ == '__main__':
    prepare_photo()
    make_pitch()
    make_report()
    PHOTO.unlink(missing_ok=True)
    print(PITCH_PDF)
    print(REPORT_PDF)
