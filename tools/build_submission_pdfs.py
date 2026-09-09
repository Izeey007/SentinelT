from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, Table, TableStyle, PageBreak
from reportlab.pdfgen import canvas
from PIL import Image as PILImage, ImageDraw
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
PW, PH = A4
M = 2.4 * cm
RED = HexColor('#8F1414')
DARK = HexColor('#202020')
MID = HexColor('#555555')
LIGHT = HexColor('#F4F4F4')
BORDER = HexColor('#D1D5DB')

renders = ROOT / 'Designs' / 'Mechanical_Design' / 'Renders'
pictures = ROOT / 'Designs' / 'Electronic_Design' / 'Pictures'
schematics = ROOT / 'Designs' / 'Schematics'
flowcharts = ROOT / 'Source_Code' / 'Flowcharts'
docs = ROOT / 'Documentation'

front = renders / '01_SentinelT_FRONT.png'
top = renders / '03_SentinelT_TOP.png'
iso = renders / '04_SentinelT_ISOMETRIC.png'
photo = docs / 'Pitch_Deck' / 'Thato_Glen_Assegaai.jpg'

# Render repository-native SVG evidence to PNG for the PDF builder.
power_png = pictures / 'SentinelT_Power_Architecture.png'
estop_png = pictures / 'SentinelT_EStop_Integration.png'
internal_png = pictures / 'SentinelT_Internal_Layout.png'
exploded_png = pictures / 'SentinelT_Exploded_Layout.png'
flow_png = flowcharts / 'SentinelT_Control_Flow.png'

cairosvg.svg2png(url=str(schematics/'SentinelT_Power_Architecture.svg'), write_to=str(power_png), output_width=1350, output_height=1800)
cairosvg.svg2png(url=str(pictures/'SentinelT_EStop_Integration.svg'), write_to=str(estop_png), output_width=1500, output_height=875)
cairosvg.svg2png(url=str(pictures/'SentinelT_Internal_Layout.svg'), write_to=str(internal_png), output_width=1500, output_height=1000)
cairosvg.svg2png(url=str(pictures/'SentinelT_Exploded_Layout.svg'), write_to=str(exploded_png), output_width=1500, output_height=1000)
cairosvg.svg2png(url=str(flowcharts/'SentinelT_Control_Flow.svg'), write_to=str(flow_png), output_width=1350, output_height=1800)

# Build a clean robot + 2.4 GHz remote presentation image using the real isometric CAD render.
remote_png = renders / 'SentinelT_Remote.png'
base = PILImage.new('RGB', (1500, 900), '#0c1015')
robot = PILImage.open(iso).convert('RGB')
robot.thumbnail((900, 760), PILImage.Resampling.LANCZOS)
base.paste(robot, (40, 80))
d = ImageDraw.Draw(base)
d.rounded_rectangle((1050, 220, 1400, 680), radius=35, fill='#20262e', outline='#9ca3af', width=5)
d.line((1225, 220, 1225, 95), fill='#9ca3af', width=10)
d.ellipse((1110, 345, 1160, 395), fill='#9ca3af')
d.ellipse((1290, 345, 1340, 395), fill='#9ca3af')
d.rounded_rectangle((1130, 455, 1320, 550), radius=12, fill='#144a7a', outline='#9ca3af', width=4)
d.line((930, 390, 1040, 390), fill='#69c8ff', width=6)
d.text((1075, 720), '2.4 GHz RC TRANSMITTER', fill='white')
base.save(remote_png, quality=92)


def fit(path, max_w, max_h):
    im = PILImage.open(path)
    w, h = im.size
    s = min(max_w / w, max_h / h)
    return w * s, h * s


def img(path, max_w, max_h):
    w, h = fit(path, max_w, max_h)
    return RLImage(str(path), width=w, height=h)

styles = getSampleStyleSheet()
body = ParagraphStyle('Body', parent=styles['BodyText'], fontName='Helvetica', fontSize=10.2, leading=14, textColor=DARK, leftIndent=0.64*cm, rightIndent=0, spaceBefore=0, spaceAfter=8)
h1 = ParagraphStyle('H1', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=16, leading=19, textColor=RED, leftIndent=0.64*cm, spaceBefore=0, spaceAfter=8)
cap = ParagraphStyle('Cap', parent=body, fontName='Helvetica-Oblique', fontSize=8.7, leading=10.5, textColor=MID, alignment=TA_CENTER, leftIndent=0, spaceAfter=8)
cover = ParagraphStyle('Cover', parent=body, fontName='Helvetica-Bold', fontSize=28, leading=32, textColor=RED, alignment=TA_CENTER, leftIndent=0, spaceAfter=10)
cover2 = ParagraphStyle('Cover2', parent=body, fontName='Helvetica-Bold', fontSize=16, leading=20, textColor=DARK, alignment=TA_CENTER, leftIndent=0, spaceAfter=8)


def table(data, widths):
    t = Table(data, colWidths=widths, repeatRows=1, hAlign='CENTER')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), LIGHT), ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'), ('FONTSIZE', (0,0), (-1,-1), 8.8),
        ('LEADING', (0,0), (-1,-1), 11), ('GRID', (0,0), (-1,-1), 0.5, BORDER),
        ('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6), ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5)
    ]))
    return t


def hf(c, doc):
    c.saveState()
    c.setFillColor(MID); c.setFont('Helvetica', 8)
    c.drawString(M, 0.9*cm, 'SentinelT | Project Developer: TG Assegaai')
    c.drawRightString(PW-M, 0.9*cm, f'Page {doc.page}')
    c.restoreState()

# ---------------- Holistic Build Document ----------------
holistic = docs / 'Holistic_Build_Document' / 'SentinelT_Holistic_Build_Document.pdf'
S = [Spacer(1, 1.0*cm), Paragraph('SENTINELT', cover), Paragraph('Robo Wars RC Combat Robot', cover2), Paragraph('Holistic Build Document', ParagraphStyle('Sub', parent=cover2, fontSize=13, textColor=MID)), Paragraph('<b>Project Developer:</b> TG Assegaai', ParagraphStyle('Dev', parent=body, alignment=TA_CENTER, leftIndent=0, fontSize=11.5)), Spacer(1, 0.25*cm), img(iso, 15.2*cm, 10.7*cm), Paragraph('Verified digital envelope: 318.16 mm x 495.00 mm x 405.99 mm | Footprint audit: 180/180 frames PASS', cap), PageBreak()]
S += [Paragraph('1. Context and Robo Wars Design Constraints', h1), Paragraph('SentinelT is a human-operated 2.4 GHz RC combat robot. The design addresses the Robo Wars constraints: maximum footprint 500 mm x 500 mm, mass strictly below 5 kg, an accessible ON/OFF switch, a mandatory Emergency Stop power-cut mechanism, 2.4 GHz remote control, and no projectiles, flames or liquids.', body), table([['Constraint','SentinelT response'],['Footprint','318.16 mm x 495.00 mm; 180/180 frames PASS'],['Mass','4.650 kg engineering allocation; 0.350 kg design margin'],['Control','Human-operated 2.4 GHz RC'],['Main power','Accessible ON/OFF battery isolation'],['E-Stop','Mushroom E-Stop controlling a separate high-current isolation stage'],['Restricted weapon types','No projectiles, flames or liquids']], [5.2*cm, 9.8*cm]), Paragraph('2. Solution Overview', h1), Paragraph('I am building SentinelT as a compact armored Robo Wars robot with protected drive components, sloped external protection, a serviceable electronics bay, an articulated upper structure, a guarded active-mechanism provision, and a fail-safe power architecture. The design combines a 3S battery system, brushed drive control, 2.4 GHz RC input, safe-state logic, main battery isolation and an E-Stop-controlled high-current power cut.', body), PageBreak()]
S += [Paragraph('3. Mechanical Design', h1), Paragraph('The chassis uses a 6 mm HDPE structural/armor material plan, with metal hardware where shafts, motor mounts, brackets, terminals and fasteners require greater strength. Bolted construction supports repair, inspection and component replacement.', body), img(front, 15.2*cm, 10.4*cm), Paragraph('Figure 1. SentinelT front CAD view.', cap), table([['Mechanical feature','Design intent'],['HDPE chassis/armor','Impact-resistant, machinable and serviceable structure'],['Protected drive zones','Reduce direct exposure of motors and wheels'],['Sloped guards','Deflect contact away from flat vulnerable faces'],['Bolted joints','Support repair and internal access'],['Metal hardware','Carry concentrated drivetrain and fastening loads']], [5.2*cm, 9.8*cm]), PageBreak()]
S += [Paragraph('4. Internal Packaging and Buildability', h1), Paragraph('The service bay reserves space for the 3S battery, drive ESC, X6B receiver, fuse, power distribution, E-Stop relay/contactor, XT60 connector, main ON/OFF isolator, auxiliary controller and left/right drive motors.', body), img(internal_png, 15.2*cm, 10.4*cm), Paragraph('Figure 2. Internal electronics and wiring layout.', cap), img(exploded_png, 15.2*cm, 9.2*cm), Paragraph('Figure 3. Exploded component layout.', cap), PageBreak()]
S += [Paragraph('5. Electronic Design', h1), Paragraph('The electronic architecture uses a 3S LiPo source, high-current protection and isolation, a 2.4 GHz RC receiver, brushed drive control and a separate auxiliary branch. The main ON/OFF isolator and E-Stop are hardware safety functions rather than software-only controls.', body), table([['Subsystem','Selected / planned hardware'],['Battery','3S 11.1 V 5000 mAh LiPo, XT60'],['RC system','FlySky FS-i6X transmitter + X6B receiver, 2.4 GHz'],['Drive controller','HobbyWing QuicRun WP-880 dual brushed ESC'],['Drive motors','2 x 12 V 37D 50:1 geared motors'],['Main isolation','12 V high-current battery isolator'],['E-Stop','Mushroom pushbutton controlling a high-current relay/contactor'],['Distribution','High-current distribution block and fused branches'],['Auxiliary branch','Guarded active-mechanism controller/actuator; final selection after hardware matching']], [5.0*cm,10.0*cm]), img(power_png, 14.0*cm, 10.8*cm), Paragraph('Figure 4. SentinelT power and E-Stop architecture.', cap), PageBreak()]
S += [Paragraph('6. E-Stop Integration and Wiring', h1), Paragraph('The Emergency Stop is designed as an independent power-disable path. The mushroom switch opens the control circuit of a suitably rated relay/contactor; the contactor main contacts then interrupt actuator power downstream of the main isolator. Software safe-state behavior is an additional layer and is not the only means of stopping powered actuators.', body), img(estop_png, 15.0*cm, 8.8*cm), Paragraph('Figure 5. Mandatory E-Stop integration.', cap), img(internal_png, 15.0*cm, 9.0*cm), Paragraph('Figure 6. Internal wiring/component placement evidence.', cap), PageBreak()]
S += [Paragraph('7. Programming and Framework Design', h1), Paragraph('The control framework uses C/C++ with Arduino framework conventions and a deterministic state model: SAFE_DISABLED, RC_READY and OPERATING. Human RC input is checked for validity before motion is allowed. Differential drive mixing uses throttle and steering commands. Startup, reset, invalid command data, RC signal loss and an active E-Stop force the software to the disabled state.', body), table([['Programming element','Implementation'],['Language / framework','C/C++ using Arduino framework conventions'],['Input method','2.4 GHz RC receiver channel data'],['Drive method','Differential mixing: left = throttle + steering; right = throttle - steering'],['RC safety timeout','250 ms validity timeout'],['Default state','All actuator commands disabled'],['Auxiliary logic','Explicit operator enable; default OFF'],['Hardware parameters','Receiver protocol, pin mapping and ESC calibration verified after hardware implementation']], [5.0*cm,10.0*cm]), img(flow_png, 14.4*cm, 11.9*cm), Paragraph('Figure 7. SentinelT RC control and safe-state flow.', cap), PageBreak()]
S += [Paragraph('8. Simulation and Digital Verification', h1), Paragraph('Blender and Python-based dimensional auditing are used before physical fabrication. The current audit evaluates the world-space bounds of 204 physical mesh objects over frames 1-180 and compares the X and Y extents with the 500 mm x 500 mm limit.', body), table([['Audit result','Value'],['Physical mesh objects','204'],['Maximum X','318.16 mm at frame 1'],['Maximum Y','495.00 mm at frame 1'],['Maximum Z','405.99 mm'],['Frames checked','180'],['Failed frames','0'],['Status','PASS - 180/180 frames']], [7.0*cm,8.0*cm]), img(top, 15.2*cm, 10.0*cm), Paragraph('Figure 8. Top CAD view supporting footprint verification.', cap), PageBreak()]
S += [Paragraph('9. Engineering Mass Budget', h1), Paragraph('The 4.650 kg value is an engineering allocation, not a measured physical mass. It leaves a 0.350 kg design margin below the 5.000 kg limit. Physical weighing will be completed after hardware implementation.', body), table([['Subsystem','Allocated mass'],['Chassis and lower armor','1.10 kg'],['Drive motors and gearboxes','0.75 kg'],['Wheels, hubs and shafts','0.30 kg'],['Battery and power system','0.60 kg'],['RC electronics, ESC and wiring','0.25 kg'],['Guarded active mechanism + mount','0.70 kg'],['Upper structure and outer shells','0.50 kg'],['Bearings, brackets and fasteners','0.25 kg'],['Contingency','0.20 kg'],['TOTAL','4.650 kg']], [10.2*cm,4.8*cm]), Paragraph('10. BOM Summary', h1), Paragraph('The full Bill of Materials is stored in Documentation/BOM/SentinelT_Bill_of_Materials.xlsx. It records component name, quantity, cost per unit, supplier, supplier stock code, direct purchase URL and line/total cost information. The current priced component subtotal is R8,039.15. The guarded active-mechanism motor/controller remains to be finalized after hardware matching.', body), PageBreak()]
S += [Paragraph('11. Current Implementation Status', h1), Paragraph('The digital engineering package contains CAD geometry, footprint verification, internal component layout, electronic architecture, E-Stop integration, control framework, flowchart, BOM structure, pitch deck and holistic report. After hardware implementation, the remaining physical evidence will verify measured mass, current draw, thermal behavior, battery runtime, drivetrain response, cable routing and E-Stop interruption performance.', body), Paragraph('12. Project Development Responsibility', h1), Paragraph('SentinelT is developed by TG Assegaai. Development responsibilities cover the system concept, Blender CAD modelling, mechanical packaging, dimensional verification scripts, 2.4 GHz control architecture, safe-state framework, power and E-Stop design, component research, Bill of Materials and technical documentation.', body), Spacer(1,1.0*cm), Paragraph('<b>Project Developer:</b> TG Assegaai', body), Spacer(1,0.35*cm), Paragraph('<b>Signature:</b> Thato Glen Assegaai', body)]
SimpleDocTemplate(str(holistic), pagesize=A4, leftMargin=M, rightMargin=M, topMargin=2.4*cm, bottomMargin=2.4*cm, title='SentinelT Holistic Build Document', author='TG Assegaai').build(S, onFirstPage=hf, onLaterPages=hf)

# ---------------- Electronic Design ----------------
electronic = ROOT / 'Designs' / 'Electronic_Design' / 'Electronic_Design.pdf'
E = [Spacer(1,1.0*cm), Paragraph('SENTINELT', cover), Paragraph('Electronic Design', cover2), Paragraph('<b>Project Developer:</b> TG Assegaai', ParagraphStyle('EDev', parent=body, alignment=TA_CENTER, leftIndent=0, fontSize=11.5)), Spacer(1,0.4*cm), img(internal_png, 15.2*cm, 10.5*cm), Paragraph('Electronic architecture, wiring, circuit safety and E-Stop integration', cap), PageBreak(), Paragraph('1. Electronic Architecture', h1), Paragraph('SentinelT uses a 3S DC power system with protected high-current distribution, a 2.4 GHz radio-control link, brushed drive control and a separate auxiliary branch. The accessible main ON/OFF isolator and the E-Stop-controlled high-current isolation stage are upstream of the drive and auxiliary actuator buses.', body), table([['Function','Hardware / method'],['RC link','FlySky FS-i6X + X6B receiver, 2.4 GHz'],['Battery','3S 11.1 V LiPo with XT60'],['Drive ESC','HobbyWing QuicRun WP-880 dual brushed ESC'],['Drive motors','Two 12 V brushed 37D gearmotors'],['Protection','Main fuse / fused distribution'],['Main power control','Accessible battery isolator'],['Emergency stop','Mushroom E-Stop controlling a high-current relay/contactor'],['Auxiliary branch','Guarded active-mechanism controller/actuator; finalized after hardware matching']], [5.0*cm,10.0*cm]), PageBreak(), Paragraph('2. Circuit Schematic and Power Flow', h1), img(power_png, 14.5*cm, 18.0*cm), Paragraph('Figure 1. SentinelT power and control architecture.', cap), PageBreak(), Paragraph('3. E-Stop Integration', h1), Paragraph('The E-Stop is integrated as a hardware power-disable function. The emergency pushbutton opens the relay/contactor control loop. The contactor main contacts then interrupt the actuator supply. This design does not depend on the microcontroller or RC software to remove motor power.', body), img(estop_png, 15.0*cm, 8.9*cm), Paragraph('Figure 2. Mandatory E-Stop integration.', cap), Paragraph('The main ON/OFF switch remains a separate accessible isolation device. When hardware is implemented, the selected relay/contactor, fuse, conductor size and connector ratings will be verified against measured current.', body), PageBreak(), Paragraph('4. Wiring and Internal Placement', h1), img(internal_png, 15.2*cm, 10.7*cm), Paragraph('Figure 3. Internal wiring/component layout.', cap), Paragraph('High-current battery/actuator wiring is separated conceptually from low-current RC/control wiring. Final routing, strain relief and wire sizing will be verified after hardware implementation.', body), PageBreak(), Paragraph('5. Component Justification', h1), table([['Component','Reason for selection'],['3S LiPo','Matches the 12 V-class drivetrain and current power architecture'],['WP-880 dual brushed ESC','Provides brushed drivetrain control in one protected controller package'],['FS-i6X + X6B','2.4 GHz human-operated RC link with multiple channels'],['37D gearmotors','Compact geared drive units with 6 mm shafts'],['Main isolator','Provides accessible primary ON/OFF control'],['E-Stop + relay/contactor','Provides independent actuator power cut'],['Fuse / distribution','Protects and organizes the high-current battery path']], [5.0*cm,10.0*cm]), Spacer(1,0.8*cm), Paragraph('<b>Project Developer:</b> TG Assegaai', body), Paragraph('<b>Signature:</b> Thato Glen Assegaai', body)]
SimpleDocTemplate(str(electronic), pagesize=A4, leftMargin=M, rightMargin=M, topMargin=2.4*cm, bottomMargin=2.4*cm, title='SentinelT Electronic Design', author='TG Assegaai').build(E, onFirstPage=hf, onLaterPages=hf)

# ---------------- 7-page Pitch Deck ----------------
pitch = docs / 'Pitch_Deck' / 'SentinelT_Pitch_Deck.pdf'
c = canvas.Canvas(str(pitch), pagesize=A4, pageCompression=1)
c.setTitle('SentinelT Pitch Deck'); c.setAuthor('TG Assegaai')

def slide_header(title, sub=None):
    c.setFillColor(white); c.rect(0,0,PW,PH,fill=1,stroke=0)
    c.setFillColor(RED); c.rect(M,PH-1.5*cm,PW-2*M,0.07*cm,fill=1,stroke=0)
    c.setFillColor(DARK); c.setFont('Helvetica-Bold',22); c.drawString(M,PH-2.5*cm,title)
    if sub:
        c.setFillColor(MID); c.setFont('Helvetica',10.2); c.drawString(M,PH-3.05*cm,sub)

def slide_footer(n):
    c.setFillColor(MID); c.setFont('Helvetica',8); c.drawString(M,0.85*cm,'SentinelT | Project Developer: TG Assegaai'); c.drawRightString(PW-M,0.85*cm,f'{n} / 7')

def draw_image(path, y, max_h, max_w=None):
    max_w = max_w or PW-2*M
    w,h = fit(path,max_w,max_h)
    c.drawImage(str(path),(PW-w)/2,y,w,h,preserveAspectRatio=True,mask='auto')

def bullets(items, y, size=11.6, leading=15.2):
    x=M+0.64*cm; max_w=PW-2*M-0.64*cm; c.setFillColor(DARK); c.setFont('Helvetica',size); yy=y
    for item in items:
        words=item.split(); line=''; lines=[]
        for wd in words:
            test=(line+' '+wd).strip()
            if c.stringWidth(test,'Helvetica',size) <= max_w-16: line=test
            else: lines.append(line); line=wd
        if line: lines.append(line)
        c.drawString(x,yy,u'\u2022')
        for j,txt in enumerate(lines): c.drawString(x+14,yy-j*leading,txt)
        yy -= len(lines)*leading+6

slide_header('SENTINELT','Robo Wars RC Combat Robot'); c.setFillColor(RED); c.setFont('Helvetica-Bold',15); c.drawString(M,PH-4.1*cm,'Project Developer: TG Assegaai'); draw_image(iso,4.0*cm,14.0*cm); c.setFillColor(DARK); c.setFont('Helvetica-Bold',10.5); c.drawCentredString(PW/2,2.2*cm,'318.16 mm x 495.00 mm footprint | 180/180 frames PASS'); slide_footer(1); c.showPage()
slide_header('Robo Wars Design Constraints','Requirements translated directly into the SentinelT design'); bullets(['Maximum footprint: 500 mm x 500 mm.','Mass strictly below 5 kg.','Human-operated remote control limited to 2.4 GHz.','Accessible main ON/OFF power isolation.','Mandatory Emergency Stop / immediate power-cut mechanism.','No projectiles, flames or liquids.'],PH-4.2*cm,13); c.setFillColor(RED); c.setFont('Helvetica-Bold',20); c.drawString(M,7.0*cm,'Verified: 318.16 mm x 495.00 mm'); c.setFillColor(DARK); c.setFont('Helvetica-Bold',18); c.drawString(M,5.6*cm,'Engineering mass budget: 4.650 kg'); c.setFillColor(MID); c.setFont('Helvetica',10); c.drawString(M,4.7*cm,'Physical mass will be verified after hardware implementation.'); slide_footer(2); c.showPage()
slide_header('Solution & Buildability','Compact armor, protected drive layout and serviceable packaging'); draw_image(front,PH-15.0*cm,10.4*cm); bullets(['6 mm HDPE chassis and armor concept with metal shafts, brackets and fasteners where required.','Protected drivetrain and sloped guards reduce exposure to direct impacts.','Bolted construction supports repair, inspection and component replacement.','Internal service bay packages battery, ESC, receiver, fuse, E-Stop hardware and distribution.','Guarded active-mechanism provision is integrated into the chassis concept.'],7.6*cm,11.1); slide_footer(3); c.showPage()
slide_header('Mechanical CAD & Simulation','Blender model with repeatable Python footprint verification'); draw_image(top,PH-14.5*cm,10.2*cm); bullets(['Verified CAD envelope: 318.16 mm x 495.00 mm x 405.99 mm.','204 physical mesh objects audited.','Frames 1-180 checked.','0 failed frames; PASS 180/180.','Digital verification completed before physical fabrication.'],7.0*cm,11.4); slide_footer(4); c.showPage()
slide_header('Electronics, Control & Safety','2.4 GHz RC with hardware isolation and E-Stop integration'); draw_image(power_png,PH-20.6*cm,16.4*cm,14.1*cm); bullets(['3S LiPo power system and brushed drive controller.','FlySky FS-i6X + X6B 2.4 GHz human-operated RC.','Accessible main ON/OFF isolator.','Mushroom E-Stop controls a separate high-current relay/contactor.','RC signal loss and invalid commands return software to SAFE_DISABLED.'],4.2*cm,9.7,13.2); slide_footer(5); c.showPage()
slide_header('Components, Mass & Cost','Current engineering implementation plan'); c.setFillColor(RED); c.setFont('Helvetica-Bold',22); c.drawString(M,PH-5.0*cm,'4.650 kg'); c.setFillColor(MID); c.setFont('Helvetica',11); c.drawString(M,PH-5.55*cm,'Engineering mass allocation'); c.setFillColor(RED); c.setFont('Helvetica-Bold',22); c.drawString(M,PH-7.1*cm,'R 8,039.15'); c.setFillColor(MID); c.setFont('Helvetica',11); c.drawString(M,PH-7.65*cm,'Current priced component subtotal'); draw_image(exploded_png,3.4*cm,13.1*cm); c.setFillColor(MID); c.setFont('Helvetica',8.8); c.drawString(M,2.35*cm,'Final active-mechanism motor/controller and implementation total are verified after hardware matching.'); slide_footer(6); c.showPage()
slide_header('Project Developer','TG Assegaai'); draw_image(photo,PH-13.4*cm,8.6*cm,7.4*cm); bullets(['System concept and engineering architecture.','Blender CAD modelling and mechanical packaging.','Python footprint and mass-budget verification tools.','2.4 GHz RC control framework and safe-state logic.','Main ON/OFF and E-Stop safety architecture.','Component research, BOM development and technical documentation.'],8.1*cm,10.7,14.0); c.setFillColor(DARK); c.setFont('Helvetica-Bold',10.5); c.drawString(M,2.3*cm,'Signature: Thato Glen Assegaai'); slide_footer(7); c.showPage(); c.save()

print('Generated:', holistic, electronic, pitch)
