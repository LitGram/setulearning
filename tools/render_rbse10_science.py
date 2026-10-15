"""Draw original readable process schematics plus a checked ray diagram and circuit."""
from pathlib import Path
import runpy
from PIL import Image, ImageDraw, ImageFont
import math

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/images'
FONT = Path('C:/Windows/Fonts/segoeui.ttf')
BOLD = Path('C:/Windows/Fonts/segoeuib.ttf')
BG, INK, BLUE, TEAL = '#F8FAFC', '#172B4D', '#2563EB', '#0D766E'

def font(size, bold=False):
    return ImageFont.truetype(str(BOLD if bold else FONT), size)

def text(draw, xy, value, size=30, fill=INK, bold=False, anchor='mm'):
    draw.text(xy, value, font=font(size, bold), fill=fill, anchor=anchor)

def arrow(draw, start, end, fill=BLUE, width=5):
    draw.line([start, end], fill=fill, width=width)
    angle = math.atan2(end[1]-start[1], end[0]-start[0])
    points = [end, (end[0]-16*math.cos(angle-.5), end[1]-16*math.sin(angle-.5)), (end[0]-16*math.cos(angle+.5), end[1]-16*math.sin(angle+.5))]
    draw.polygon(points, fill=fill)

def card(draw, xy, label):
    x,y=xy
    draw.rounded_rectangle((x-460,y-45,x+460,y+45), radius=18, fill='white', outline='#CBD5E1', width=3)
    text(draw,(x,y),label,32,bold=True)

def flow(draw, labels):
    positions=[(700,190+i*125) for i in range(len(labels))]
    for p,label in zip(positions,labels): card(draw,p,label)
    for a,b in zip(positions,positions[1:]): arrow(draw,(a[0],a[1]+48),(b[0],b[1]-49))

def branches(draw, center, products):
    card(draw,(700,205),center)
    xs=[270,700,1130] if len(products)==3 else [400,1000]
    for x, lines in zip(xs, products):
        arrow(draw,(700,253),(x,455))
        draw.rounded_rectangle((x-195,455,x+195,610),radius=20,fill='white',outline=TEAL,width=3)
        for j,line in enumerate(lines):text(draw,(x,505+j*55),line,29,bold=j==0)

def lens(draw):
    cy,ox,scale=455,700,4
    # f=40 diagram units, object u=-120 => image v=+60; m=-0.5.
    f=160; obj=(220,295); img=(940,535)
    draw.line((80,cy,1320,cy),fill='#64748B',width=3)
    draw.ellipse((675,170,725,745),outline=BLUE,width=6)
    text(draw,(700,780),'Convex lens',28)
    for x,label in [(380,'2F'),(540,'F'),(860,'F'),(1020,'2F')]:
        draw.line((x,cy-12,x,cy+12),fill=INK,width=3);text(draw,(x,cy+35),label,26)
    arrow(draw,(220,cy),obj,TEAL,7);text(draw,(220,245),'Object',29,TEAL,bold=True)
    arrow(draw,(940,cy),img,'#B45309',7);text(draw,(1130,525),'Image',29,'#B45309',bold=True)
    # parallel ray to lens then through far focus; center ray intersects at same image top.
    arrow(draw,obj,(700,295));arrow(draw,(700,295),(1100,695))
    arrow(draw,obj,(700,455),'#7C3AED');arrow(draw,(700,455),(1180,615),'#7C3AED')
    draw.ellipse((932,527,948,543),fill='#B45309')
    text(draw,(700,130),'Beyond 2F → between F and 2F',32,bold=True)
    text(draw,(700,825),'Real • inverted • diminished | Thin-lens, paraxial schematic',27)

def circuit(draw):
    # Closed low-voltage loop, ammeter series; voltmeter only across resistor terminals.
    draw.line([(260,500),(260,240),(1120,240),(1120,500)],fill=INK,width=5)
    draw.line([(260,500),(625,500)],fill=INK,width=5)
    draw.line([(675,500),(1120,500)],fill=INK,width=5)
    draw.line((625,460,625,540),fill=INK,width=5);draw.line((675,475,675,525),fill=INK,width=5)
    text(draw,(650,590),'Low-voltage DC source',29)
    draw.ellipse((375,195,465,285),fill=BG,outline=BLUE,width=4);text(draw,(420,240),'A',36,BLUE,bold=True)
    draw.rectangle((720,211,960,269),fill=BG,outline=TEAL,width=4);text(draw,(840,240),'R',32,TEAL,bold=True)
    draw.line([(690,240),(690,370),(990,370),(990,240)],fill=INK,width=4)
    draw.ellipse((795,325,885,415),fill=BG,outline='#7C3AED',width=4);text(draw,(840,370),'V',36,'#7C3AED',bold=True)
    text(draw,(420,150),'Series current',27)
    text(draw,(840,460),'Voltage across R',27)
    text(draw,(700,725),'Ammeter in series • Voltmeter in parallel',32,bold=True)
    text(draw,(700,800),'Teaching circuit only — never connect this to household mains.',25)

def rules(draw):
    for x,title,labels in [(390,'RIGHT-HAND THUMB',['Thumb: current','Fingers: field']), (1010,'FLEMING LEFT-HAND',['First: field','Middle: current','Thumb: force'])]:
        draw.rounded_rectangle((x-280,205,x+280,620),radius=24,fill='white',outline=BLUE,width=4)
        text(draw,(x,275),title,27,BLUE,bold=True)
        for j,label in enumerate(labels):text(draw,(x,375+j*70),label,32)
    text(draw,(700,750),'Field created by current ≠ Force on current in a field',29,bold=True)

def render():
    chapters=runpy.run_path(str(ROOT/'10th rbse/02_science/source.py'))['CHAPTERS']
    OUT.mkdir(parents=True,exist_ok=True)
    for c in chapters:
        im=Image.new('RGB',(1400,960),BG);d=ImageDraw.Draw(im)
        title=c['english']
        text(d,(700,65),title,35 if len(title)<45 else 29,bold=True)
        n=c['number']
        if n==2:branches(d,'Brine electrolysis',[['Anode','Cl₂'],['Cathode','H₂'],['Solution','NaOH']])
        elif n==7:
            branches(d,'After fertilisation',[['Ovule','Seed'],['Ovary','Fruit']])
            text(d,(700,735),'Pollination precedes fertilisation; the two are different events.',27)
        elif n==9:lens(d)
        elif n==11:circuit(d)
        elif n==12:rules(d)
        else:flow(d,c['diagram'])
        if n==13:text(d,(700,810),'10% onward at each step; other energy dissipates (approximation).',24)
        text(d,(700,920),f'SETU LEARNING • RBSE 10 SCIENCE • CHAPTER {n:02} • ORIGINAL SCHEMATIC',21,'#64748B')
        im.save(OUT/f'rbse10_sci_{n:02}.png',optimize=True)
    print(f'Rendered {len(chapters)} diagrams.')

if __name__=='__main__':render()
