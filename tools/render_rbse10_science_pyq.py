"""Original scientific schematics supporting the solved previous-year chapter."""
from pathlib import Path
from PIL import Image, ImageDraw
import math
from render_rbse10_science import text, arrow, BG, INK, BLUE, TEAL

ROOT=Path(__file__).resolve().parents[1]

def dashed(d,a,b,fill='#64748B'):
    dx,dy=b[0]-a[0],b[1]-a[1];length=math.hypot(dx,dy)
    for v in range(0,int(length),24):
        e=min(v+12,length)
        d.line([(a[0]+dx*v/length,a[1]+dy*v/length),(a[0]+dx*e/length,a[1]+dy*e/length)],fill=fill,width=3)

def water(d):
    d.rectangle((340,480,1060,780),fill='#DBEAFE')
    d.line([(340,320),(340,780),(1060,780),(1060,320)],fill=INK,width=5)
    for x,gas,volume,h in [(520,'O₂','1 volume',90),(880,'H₂','2 volumes',180)]:
        d.rectangle((x-46,300,x+46,300+h),fill='#99F6E4')
        d.line([(x-46,740),(x-46,300),(x+46,300),(x+46,740)],fill=BLUE,width=4)
        d.line((x,510,x,705),fill=INK,width=10)
        text(d,(x,260),gas+' • '+volume,30,bold=True)
        text(d,(x,830),'Anode (+)' if x==520 else 'Cathode (−)',28)
        d.line([(x,510),(x,150),(645 if x==520 else 715,150)],fill=INK,width=4)
    d.line((645,115,645,185),fill=INK,width=5);d.line((715,130,715,170),fill=INK,width=5)
    text(d,(680,215),'DC source',26)
    text(d,(700,600),'Acidified water',28)
    text(d,(700,885),'2H₂O → 2H₂ + O₂ | Supervised laboratory setup',25)

def uniform(d):
    for y in [280,380,480,580,680]:arrow(d,(200,y),(1200,y),TEAL,6)
    text(d,(700,815),'Parallel • equally spaced • same direction',32,bold=True)

def hydra(d):
    for i,x in enumerate([280,700,1100]):
        d.rounded_rectangle((x-30,380,x+30,720),radius=30,fill='#CCFBF1',outline=TEAL,width=4)
        for off in [-110,-55,55,110]:d.line([(x,380),(x+off,270),(x+off*1.2,250)],fill=TEAL,width=4)
        if i<2:
            bx=x+75;by=530
            d.ellipse((x+15,by-25,bx+35,by+25),fill='#CCFBF1',outline=TEAL,width=3)
            if i==1:
                for off in [-30,0,30]:d.line([(bx+15,by),(bx+45,by-55+off)],fill=TEAL,width=3)
            text(d,(x+75,620),'Bud',26)
        else:
            bx=x+160
            d.rounded_rectangle((bx-20,480,bx+20,700),radius=20,fill='#CCFBF1',outline=TEAL,width=3)
            for off in [-50,0,50]:d.line([(bx,480),(bx+off,410)],fill=TEAL,width=3)
            text(d,(bx,765),'New Hydra',25)
        text(d,(x,815),['Bud formation','Bud growth','Detachment'][i],28,bold=True)
    text(d,(700,165),'Simplified stages; body shapes are schematic.',27)

def slab(d):
    d.rectangle((450,210,900,810),fill='#E0F2FE',outline=BLUE,width=4)
    text(d,(675,255),'Glass slab',32,bold=True)
    a,b,c,e=(200,100),(450,350),(900,589),(1120,809)
    dashed(d,(230,350),(650,350));dashed(d,(740,589),(1230,589))
    arrow(d,a,b,TEAL);arrow(d,b,c,TEAL);arrow(d,c,e,TEAL)
    text(d,(320,300),'Incident',28,TEAL);text(d,(725,445),'Refracted',28,TEAL)
    text(d,(1150,735),'Emergent',28,TEAL)
    text(d,(300,390),'Normal',24);text(d,(1170,630),'Normal',24)
    text(d,(700,865),'Parallel faces → emergent ray parallel to incident ray',27,bold=True)

def dispersion(d):
    d.polygon([(700,220),(450,800),(950,800)],fill='#E0F2FE',outline=BLUE,width=5)
    arrow(d,(130,500),(580,500),INK,9);d.line((580,500,846,560),fill=INK,width=6)
    text(d,(280,450),'White light',29,bold=True)
    colors=['#DC2626','#EA580C','#CA8A04','#16A34A','#2563EB','#4338CA','#7C3AED']
    for j,color in enumerate(colors):arrow(d,(846,560),(1210,585+j*36),color,5)
    text(d,(1270,585),'Red',25,'#DC2626');text(d,(1270,801),'Violet',25,'#7C3AED')
    text(d,(700,850),'Red: least deviation • Violet: greatest deviation',29,bold=True)

def field(d,coil=False):
    # Nested nonintersecting half-ellipses from N (left) to S (right).
    for level,height in enumerate([110,200,290]):
        for sign in [-1,1]:
            pts=[]
            pole_y=480+sign*(45+level*15)
            for i in range(101):
                angle=math.pi*i/100
                pts.append((700-335*math.cos(angle),pole_y+sign*height*math.sin(angle)))
            d.line(pts,fill=TEAL,width=4);arrow(d,pts[48],pts[53],TEAL,4)
    if coil:
        for x in range(375,1036,45):d.ellipse((x-30,390,x+30,570),outline='#B45309',width=3)
        text(d,(700,635),'Current-carrying solenoid',29,bold=True)
        for y in [445,480,515]:arrow(d,(990,y),(410,y),BLUE,5)
    else:
        d.rectangle((365,405,700,555),fill='#FEE2E2',outline=INK,width=3)
        d.rectangle((700,405,1035,555),fill='#DBEAFE',outline=INK,width=3)
        arrow(d,(960,480),(440,480),INK,5)
    label_y=370 if coil else 445
    text(d,(500,label_y),'N',35,bold=True);text(d,(900,label_y),'S',35,bold=True)
    text(d,(700,875),'Outside: N → S | Inside: S → N | Closed field loops',27,bold=True)

def sex(d):
    text(d,(700,170),'Egg: X • Sperm: X or Y (school XX–XY model)',29,bold=True)
    d.rectangle((450,330,1110,730),outline=INK,width=4)
    d.line((780,330,780,730),fill=INK,width=3);d.line((450,530,1110,530),fill=INK,width=3)
    text(d,(615,275),'Sperm X',29);text(d,(945,275),'Sperm Y',29)
    text(d,(315,430),'Egg X',29);text(d,(315,630),'Egg X',29)
    for y in [430,630]:text(d,(615,y),'XX',42,TEAL,bold=True);text(d,(945,y),'XY',42,BLUE,bold=True)
    text(d,(700,830),'Expected XX : XY = 1 : 1 | Probability, not parental choice',27,bold=True)

def graph(d,inverse=False):
    origin=(230,745);arrow(d,origin,(1230,745),INK);arrow(d,origin,(230,160),INK)
    text(d,(1200,805),'A (area)' if inverse else 'I (ampere)',29)
    text(d,(135,200),'R (Ω)' if inverse else 'V (volt)',29)
    if inverse:
        pts=[(x,745-40000/(x-230)) for x in range(330,1190)]
        d.line(pts,fill=TEAL,width=5);text(d,(800,350),'R = ρl/A',35,TEAL,bold=True)
        text(d,(700,865),'Same material, length, temperature: R ∝ 1/A',28,bold=True)
    else:
        arrow(d,origin,(1130,205),TEAL,5)
        text(d,(840,450),'Slope = ΔV/ΔI = R',31,TEAL,bold=True)
        text(d,(700,865),'Ohmic conductor • temperature kept fixed',29,bold=True)

def main():
    figures={'water':('Water electrolysis',water),'uniform':('Uniform magnetic field',uniform),'budding':('Budding in Hydra',hydra),'slab':('Refraction through a glass slab',slab),'dispersion':('Dispersion through a prism',dispersion),'barfield':('Bar magnet: closed field lines',field),'solenoid':('Solenoid magnetic field',lambda d:field(d,True)),'sex':('Human chromosomal sex determination',sex),'ra':('Resistance versus cross-sectional area',lambda d:graph(d,True)),'vi':('Ohm law: voltage versus current',graph)}
    for key,(title,draw) in figures.items():
        im=Image.new('RGB',(1400,960),BG);d=ImageDraw.Draw(im);text(d,(700,65),title,35,bold=True)
        draw(d)
        text(d,(700,925),'SETU LEARNING • ORIGINAL TEACHING SCHEMATIC • SOLVED EXAMS',21,'#64748B')
        im.save(ROOT/f'assets/images/pyq_{key}.png',optimize=True)
    print('Rendered',len(figures),'PYQ figures.')

if __name__=='__main__':main()
