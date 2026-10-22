import json, math, cmath, os, sys
import numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lib import *
P=[]
def add(**k):
    k.setdefault("chapter",3); P.append(k)
D=lambda s:"$$"+s+"$$"          # display math
GAMMA_DEF=r"\Gamma_L=\frac{Z_L-Z_0}{Z_L+Z_0}"
ZIN_DEF=r"Z_{in}=Z_0\,\frac{Z_L+jZ_0\tan\beta\ell}{Z_0+jZ_L\tan\beta\ell}"
VSWR_DEF=r"\mathrm{VSWR}=\frac{1+|\Gamma_L|}{1-|\Gamma_L|}"
deg=lambda x:f"{tr(x)}^\\circ"

# ================= COURSE PRACTICE PROBLEMS =================
add(id="pp-3.1-1",source="course",set="PP LO 3.1",lo="3.1",difficulty=2,title="Derive the second telegrapher's equation",
 prompt="Using the lumped-element model of a transmission line (series $R'\\Delta z$ and $L'\\Delta z$, shunt $G'\\Delta z$ and $C'\\Delta z$), apply KCL to derive"+D(r"-\frac{\partial i(z,t)}{\partial z}=G'v(z,t)+C'\frac{\partial v(z,t)}{\partial t}"),
 hints=["Write KCL at the node after the series elements: the current in equals the current through the shunt branch plus the current continuing down the line.",
        "The shunt branch current is $G'\\Delta z\\,v + C'\\Delta z\\,\\dfrac{\\partial v}{\\partial t}$.",
        "Divide by $\\Delta z$ and take the limit $\\Delta z\\to 0$."],
 steps=["KCL at the node at $z+\\Delta z$:"+D(r"i(z,t)=i(z+\Delta z,t)+i_{shunt}"),
        "The shunt current is"+D(r"i_{shunt}=G'\Delta z\,v(z+\Delta z,t)+C'\Delta z\,\frac{\partial v(z+\Delta z,t)}{\partial t}"),
        "Rearrange and divide by $\\Delta z$:"+D(r"-\frac{i(z+\Delta z,t)-i(z,t)}{\Delta z}=G'v(z+\Delta z,t)+C'\frac{\partial v(z+\Delta z,t)}{\partial t}"),
        "Let $\\Delta z\\to 0$. The left side becomes $-\\dfrac{\\partial i}{\\partial z}$ and $v(z+\\Delta z)\\to v(z)$:"+D(r"-\frac{\partial i(z,t)}{\partial z}=G'v(z,t)+C'\frac{\partial v(z,t)}{\partial t}")],
 answers=[{"label":"Result","value":r"-\frac{\partial i}{\partial z}=G'v+C'\frac{\partial v}{\partial t}"}],widget=None)
add(id="pp-3.1-2",source="course",set="PP LO 3.1",lo="3.1",difficulty=2,title="Wave equation for the current",
 prompt="Using the phasor telegrapher's equations, derive the governing equation for $I(z)$ on a lossy line, define $\\gamma$, and give the solution for the lossless case. Identify the real and imaginary parts of $\\gamma=\\alpha+j\\beta$.",
 hints=["The phasor forms are $-\\dfrac{dV}{dz}=(R'+j\\omega L')I$ and $-\\dfrac{dI}{dz}=(G'+j\\omega C')V$.",
        "Differentiate the second equation with respect to $z$ and substitute the first."],
 steps=["Differentiate the current equation:"+D(r"-\frac{d^2I}{dz^2}=(G'+j\omega C')\frac{dV}{dz}"),
        "Substitute $\\dfrac{dV}{dz}=-(R'+j\\omega L')I$:"+D(r"\frac{d^2I}{dz^2}=(R'+j\omega L')(G'+j\omega C')\,I"),
        "So"+D(r"\frac{d^2I}{dz^2}-\gamma^2 I=0,\qquad \gamma=\sqrt{(R'+j\omega L')(G'+j\omega C')}=\alpha+j\beta"),
        "General solution:"+D(r"I(z)=I_0^+e^{-\gamma z}+I_0^-e^{\gamma z}"),
        "Lossless ($R'=G'=0$): $\\gamma=j\\omega\\sqrt{L'C'}$, so $\\alpha=0$ and $\\beta=\\omega\\sqrt{L'C'}$."+D(r"I(z)=I_0^+e^{-j\beta z}+I_0^-e^{j\beta z}")],
 answers=[{"label":"I(z)","value":r"I_0^+e^{-j\beta z}+I_0^-e^{j\beta z}"},{"label":r"\beta","value":r"\omega\sqrt{L'C'}"},{"label":r"\alpha","value":"0"}],
 note="The course answer key writes $I_0^+ + e^{-j\\beta z}$; the plus sign between the amplitude and the exponential is a typo.",widget="params")
add(id="pp-3.1-3",source="course",set="PP LO 3.1",lo="3.1",difficulty=1,title="Verify the wave solution",
 prompt="Show that $\\tilde V(z)=V_0^+e^{-\\gamma z}+V_0^-e^{\\gamma z}$ solves"+D(r"\frac{d^2\tilde V}{dz^2}-\gamma^2\tilde V=0"),
 hints=["Differentiate twice and substitute."],
 steps=[D(r"\frac{d\tilde V}{dz}=-\gamma V_0^+e^{-\gamma z}+\gamma V_0^-e^{\gamma z}"),D(r"\frac{d^2\tilde V}{dz^2}=\gamma^2V_0^+e^{-\gamma z}+\gamma^2V_0^-e^{\gamma z}=\gamma^2\tilde V"),"So $\\dfrac{d^2\\tilde V}{dz^2}-\\gamma^2\\tilde V=0$. ✓"],
 answers=[{"label":"Check","value":r"\frac{d^2\tilde V}{dz^2}=\gamma^2\tilde V"}],widget=None)

up=c/math.sqrt(5)
add(id="pp-3.2-1",source="course",set="PP LO 3.2–3.3",lo="3.2",difficulty=1,title="Wave speed in a dielectric",
 prompt="A wave travels in a material with relative permittivity $\\varepsilon_r=5$. What is its speed?",
 hints=["For a non-magnetic material, $u_p=\\dfrac{c}{\\sqrt{\\varepsilon_r}}$."],
 steps=[D(f"u_p=\\frac{{c}}{{\\sqrt{{5}}}}={teng(up,'m/s')}={tr(1/math.sqrt(5))}c")],
 answers=[{"label":"u_p","value":f"{teng(up,'m/s')}={tr(1/math.sqrt(5))}c"}],widget="calc")
g=G(20,60)
add(id="pp-3.2-2",source="course",set="PP LO 3.2–3.3",lo="3.2",difficulty=1,title="Reflected voltage wave",
 prompt="A $7\\ \\mathrm{mV}\\angle 180^\\circ$ voltage wave travels on a lossless $60\\ \\Omega$ line terminated in a $20\\ \\Omega$ load. Find the magnitude and phase of the reflected wave.",
 hints=["$V^-=\\Gamma_L V^+$.","$\\Gamma_L$ is real and negative here, which adds $180^\\circ$."],
 steps=[D(f"\\Gamma_L=\\frac{{20-60}}{{20+60}}={tr(g)}=0.5\\angle 180^\\circ"),D(r"V^-=\Gamma_LV^+=(0.5\angle 180^\circ)(7\ \mathrm{mV}\angle 180^\circ)=3.5\ \mathrm{mV}\angle 0^\circ")],
 answers=[{"label":"V^-","value":r"3.5\ \mathrm{mV}\angle 0^\circ"}],note="The course solution writes $\\Gamma_L=\\dfrac{Z_L-Z_0}{Z_L-Z_0}$; the denominator should be $Z_L+Z_0$.",widget="waves")
g=G(60,72)
add(id="pp-3.2-3",source="course",set="PP LO 3.2–3.3",lo="3.2",difficulty=1,title="Γ and VSWR for a 60 Ω load on a 72 Ω line",
 prompt="A $72\\ \\Omega$ line is terminated in a $60\\ \\Omega$ load. (a) Sketch the system. (b) Find $\\Gamma_L$. (c) Find the VSWR.",
 hints=["Put the load at $z=0$ and the input at $z=-\\ell$.","$"+VSWR_DEF+"$"],
 steps=[D(f"\\Gamma_L=\\frac{{60-72}}{{60+72}}={tr(g)}"),D(f"\\mathrm{{VSWR}}=\\frac{{1+{tr(abs(g))}}}{{1-{tr(abs(g))}}}={tr(vswr(g))}")],
 answers=[{"label":r"\Gamma_L","value":tr(g)},{"label":r"\mathrm{VSWR}","value":tr(vswr(g))}],widget="waves")
zl=20-35j; g=G(zl,50); Z3=zin(zl,50,0.3)
add(id="pp-3.2-4",source="course",set="PP LO 3.2–3.3",lo="3.3",difficulty=2,title="Γ, VSWR and impedance at z = −0.3λ",
 prompt="A lossless $50\\ \\Omega$ line is terminated in $Z_L=20-j35\\ \\Omega$. Find (a) $\\Gamma_L$, (b) the VSWR, and (c) the impedance at $z=-0.3\\lambda$.",
 hints=["$"+GAMMA_DEF+"$","Use"+D(ZIN_DEF)+"with $\\beta\\ell=2\\pi(0.3)=108^\\circ$."],
 steps=[D(f"\\Gamma_L=\\frac{{-30-j35}}{{70-j35}}={tc(g)}={tp(g)}"),D(f"\\mathrm{{VSWR}}=\\frac{{1+{tr(abs(g))}}}{{1-{tr(abs(g))}}}={tr(vswr(g))}"),
        f"$\\tan 108^\\circ={tr(math.tan(2*math.pi*0.3))}$, so"+D(f"Z(-0.3\\lambda)=50\\,\\frac{{Z_L+j50\\tan 108^\\circ}}{{50+jZ_L\\tan 108^\\circ}}={tc(Z3)}\\ \\Omega"),
        "Check with $\\Gamma$:"+D(f"\\Gamma(-0.3\\lambda)=\\Gamma_Le^{{-j2\\beta(0.3\\lambda)}}={tp(g*cmath.exp(-4j*math.pi*0.3))},\\qquad Z=Z_0\\frac{{1+\\Gamma}}{{1-\\Gamma}}={tc(Z3)}\\ \\Omega")],
 answers=[{"label":r"\Gamma_L","value":tp(g)},{"label":r"\mathrm{VSWR}","value":tr(vswr(g))},{"label":r"Z(-0.3\lambda)","value":tc(Z3)+r"\ \Omega"}],
 note="The course solution shows $|\\Gamma|=0.636$ in an intermediate step; it should be $0.589$. The final answer is unaffected.",widget="calc")
add(id="pp-3.2-5",source="course",set="PP LO 3.2–3.3",lo="3.3",difficulty=1,title="Input impedance of a 1.5λ line",
 prompt="A lossless $50\\ \\Omega$ line, $1.5\\lambda$ long, is terminated in $72+j42\\ \\Omega$. What is the input impedance?",
 hints=["What is $\\tan\\beta\\ell$ when $\\ell$ is a multiple of $\\lambda/2$?"],
 steps=["$\\beta\\ell=2\\pi(1.5)=3\\pi$, so $\\tan\\beta\\ell=0$.",D(r"Z_{in}=Z_0\,\frac{Z_L+0}{Z_0+0}=Z_L"),"A half-wavelength line repeats the load impedance."],
 answers=[{"label":"Z_{in}","value":r"72+j42\ \Omega"}],note="The course solution substitutes $72+j45\\ \\Omega$ in one line; the load is $72+j42\\ \\Omega$.",widget="smith")
rts=[(d,zin(25+25j,50,d)) for d in roots(lambda d:zin(25+25j,50,d).imag,0.001,0.499)]
g=G(25+25j,50)
add(id="pp-3.2-6",source="course",set="PP LO 3.2–3.3",lo="3.3",difficulty=2,title="When is $Z_{in}$ purely real?",
 prompt="A lossless $50\\ \\Omega$ coax is terminated in $25+j25\\ \\Omega$. (a) Plot $Z_{in}$ in the complex plane for $\\ell$ from $0$ to $0.45\\lambda$. (b) For what lengths is $Z_{in}$ purely real, and what is $Z_{in}$ there?",
 hints=["$Z_{in}$ is real where the point on the Smith chart crosses the real axis.","Those crossings are the voltage maximum and minimum positions."],
 steps=[f"$\\Gamma_L={tp(g)}$ and $\\mathrm{{VSWR}}={tr(vswr(g))}$."]+[f"$\\ell={tr(d)}\\lambda$: $Z_{{\\mathrm{{in}}}}={tr(z.real,4)}\\ \\Omega$, which is {'$Z_0\\cdot\\mathrm{VSWR}$ (a voltage maximum)' if z.real>50 else '$Z_0/\\mathrm{VSWR}$ (a voltage minimum)'}." for d,z in rts],
 answers=[{"label":f"\\ell_{i+1}","value":f"{tr(d)}\\lambda,\\ Z_{{\\mathrm{{in}}}}={tr(z.real,4)}\\ \\Omega"} for i,(d,z) in enumerate(rts)],widget="smith")
lam=0.55*c/900e6; l=0.13/lam; Zo=-1j*75/math.tan(2*math.pi*l)
add(id="pp-3.2-7",source="course",set="PP LO 3.2–3.3",lo="3.3",difficulty=2,title="Open-circuited coax at 900 MHz",
 prompt="A $13\\ \\mathrm{cm}$ section of $75\\ \\Omega$ coax is open at the far end. With velocity factor $0.55$, what is the input impedance at $900\\ \\mathrm{MHz}$?",
 hints=["$\\lambda=\\dfrac{u_p}{f}$.","For an open load, $Z_{in}=-jZ_0\\cot\\beta\\ell$."],
 steps=[D(f"\\lambda=\\frac{{0.55c}}{{900\\ \\mathrm{{MHz}}}}={teng(lam,'m')}"),D(f"\\ell=\\frac{{0.13}}{{{tr(lam,4)}}}\\lambda={tr(l,4)}\\lambda,\\qquad \\beta\\ell={deg(math.degrees(2*math.pi*l))}"),
        D(f"Z_{{\\mathrm{{in}}}}=-j75\\cot({deg(math.degrees(2*math.pi*l))})=-j{tr(abs(Zo.imag),4)}\\ \\Omega")],
 answers=[{"label":"Z_{in}","value":f"-j{tr(abs(Zo.imag),4)}\\ \\Omega"}],note="The course key gives $-j19.26\\ \\Omega$ because $\\ell$ is rounded to $0.71\\lambda$; carrying full precision gives $-j19.47\\ \\Omega$.",widget="calc")

w=2*math.pi*1e9; sp=series_pts(35-50j,100)
spC=[s for s in sp if s[1]>0][0]; spL=[s for s in sp if s[1]<0][0]
Cs=1/(w*spC[1]*100); Ls=-spL[1]*100/w
add(id="pp-3.4-1",source="course",set="PP LO 3.4–3.6",lo="3.4",difficulty=3,title="Series element match without a Smith chart",
 prompt="Without a Smith chart, match a $35-j50\\ \\Omega$ load to a $100\\ \\Omega$ source at $1\\ \\mathrm{GHz}$ using a length $\\ell$ of $100\\ \\Omega$ line followed by a series reactive element. Find $\\ell$ and the element value for (a) a series capacitor and (b) a series inductor.",
 hints=["Find $\\ell$ where $\\mathrm{Re}\\{z_{in}\\}=1$ using the transmission-line equation, normalized to $100\\ \\Omega$.","The series element must cancel $\\mathrm{Im}\\{z_{in}\\}$.","A capacitor cancels positive reactance; an inductor cancels negative reactance."],
 steps=[f"$z_L=0.35-j0.5$ and $\\Gamma_L={tp(G(35-50j,100))}$.",
        f"(a) $\\mathrm{{Re}}\\{{z_{{\\mathrm{{in}}}}\\}}=1$ at $\\ell={tr(spC[0])}\\lambda$, where $z_{{\\mathrm{{in}}}}=1+j{tr(spC[1])}$. The capacitor must provide $-j{tr(spC[1]*100,4)}\\ \\Omega$:"+D(f"C=\\frac{{1}}{{\\omega X}}=\\frac{{1}}{{2\\pi(10^9)({tr(spC[1]*100,4)})}}={teng(Cs,'F')}"),
        f"(b) $\\mathrm{{Re}}\\{{z_{{\\mathrm{{in}}}}\\}}=1$ at $\\ell={tr(spL[0])}\\lambda$, where $z_{{\\mathrm{{in}}}}=1-j{tr(-spL[1])}$. The inductor must provide $+j{tr(-spL[1]*100,4)}\\ \\Omega$:"+D(f"L=\\frac{{X}}{{\\omega}}=\\frac{{{tr(-spL[1]*100,4)}}}{{2\\pi(10^9)}}={teng(Ls,'H')}")],
 answers=[{"label":"(a)","value":f"\\ell={tr(spC[0])}\\lambda,\\ C={teng(Cs,'F')}"},{"label":"(b)","value":f"\\ell={tr(spL[0])}\\lambda,\\ L={teng(Ls,'H')}"}],
 note="The course key lists $L=221\\ \\mu\\mathrm{H}$. At $1\\ \\mathrm{GHz}$ a $139\\ \\Omega$ reactance needs $22.1\\ \\mathrm{nH}$, so $\\mu\\mathrm{H}$ appears to be a units slip.",widget="smith")
yp=[(d,(1/zin(35-50j,100,d))) for d in roots(lambda d:(100/zin(35-50j,100,d)).real-1)]
ypC=[x for x in yp if x[1].imag<0][0]; ypL=[x for x in yp if x[1].imag>0][0]
Cp=-ypC[1].imag/w; Lp=1/(w*ypL[1].imag)
add(id="pp-3.6-1",source="course",set="PP LO 3.4–3.6",lo="3.6",difficulty=3,title="Four ways to match 35 − j50 Ω with a Smith chart",
 prompt="Using a Smith chart, match a $35-j50\\ \\Omega$ load to a $100\\ \\Omega$ source at $1\\ \\mathrm{GHz}$ with a length of $100\\ \\Omega$ line and one reactive element: (a) series capacitor, (b) series inductor, (c) shunt capacitor, (d) shunt inductor.",
 hints=["Series elements: rotate on the Z chart to the $r=1$ circle.","Shunt elements: convert to admittance and rotate to the $g=1$ circle.","Read the leftover reactance or susceptance and pick the element that cancels it."],
 steps=[f"Plot $z_L=0.35-j0.5$ and draw its VSWR circle ($\\mathrm{{VSWR}}={tr(vswr(G(35-50j,100)))}$).",
        f"(a) Reach $r=1$ at $\\ell={tr(spC[0])}\\lambda$: $z=1+j{tr(spC[1])}$, so a series $C={teng(Cs,'F')}$.",
        f"(b) Reach $r=1$ at $\\ell={tr(spL[0])}\\lambda$: $z=1-j{tr(-spL[1])}$, so a series $L={teng(Ls,'H')}$.",
        f"(c) On the Y chart, reach $g=1$ at $\\ell={tr(ypC[0])}\\lambda$: $y=1-j{tr(-ypC[1].imag*100)}$. A shunt capacitor supplies $B={tr(-ypC[1].imag*100)}/100\\ \\mathrm{{S}}$:"+D(f"C=\\frac{{B}}{{\\omega}}={teng(Cp,'F')}"),
        f"(d) Reach $g=1$ at $\\ell={tr(ypL[0],2)}\\lambda$: $y=1+j{tr(ypL[1].imag*100)}$. A shunt inductor cancels it:"+D(f"L=\\frac{{1}}{{\\omega B}}={teng(Lp,'H')}")],
 answers=[{"label":"(a)","value":f"\\ell={tr(spC[0])}\\lambda,\\ C={teng(Cs,'F')}"},{"label":"(b)","value":f"\\ell={tr(spL[0])}\\lambda,\\ L={teng(Ls,'H')}"},
          {"label":"(c)","value":f"\\ell={tr(ypC[0])}\\lambda,\\ C={teng(Cp,'F')}"},{"label":"(d)","value":f"\\ell={tr(ypL[0],2)}\\lambda,\\ L={teng(Lp,'H')}"}],
 note="The course key gives $L=221.2\\ \\mu\\mathrm{H}$ for (b) and $113.7\\ \\mu\\mathrm{H}$ for (d). The reactances at $1\\ \\mathrm{GHz}$ correspond to $22.1\\ \\mathrm{nH}$ and $11.5\\ \\mathrm{nH}$.",widget="smith")
st=shunt_stub(170,50)
add(id="pp-3.6-2",source="course",set="PP LO 3.4–3.6",lo="3.4",difficulty=2,title="170 Ω load: quarter-wave transformer and shorted stub",
 prompt="Match a $170\\ \\Omega$ load to a $50\\ \\Omega$ source. (a) What characteristic impedance does a quarter-wave transformer need? (b) Using $50\\ \\Omega$ line, find the through-line length and shorted shunt-stub length.",
 hints=["$Z_{in}(\\lambda/4)=\\dfrac{Z_1^2}{Z_L}$.","For the stub, work in admittance: $y_L=\\dfrac{50}{170}$.","Rotate $y_L$ toward the generator until it meets the $g=1$ circle."],
 steps=["(a)"+D(f"Z_1=\\sqrt{{(170)(50)}}={tr(math.sqrt(170*50))}\\ \\Omega"),f"(b) $y_L={tr(50/170)}$ and $|\\Gamma_L|={tr(abs(G(170,50)))}$."]+
       [f"Solution {i+1}: at $d={tr(d)}\\lambda$, $y=1{'+' if b>0 else '-'}j{tr(abs(b))}$. The shorted stub must add ${'-' if b>0 else '+'}j{tr(abs(b))}$, so $\\ell_{{\\mathrm{{stub}}}}={tr(ls)}\\lambda$." for i,(d,b,ls,lo) in enumerate(st)],
 answers=[{"label":"Z_1","value":f"{tr(math.sqrt(170*50))}\\ \\Omega"}]+[{"label":f"\\text{{Stub }}{i+1}","value":f"d={tr(d)}\\lambda,\\ \\ell_{{\\mathrm{{stub}}}}={tr(ls)}\\lambda"} for i,(d,b,ls,lo) in enumerate(st)],
 note="The course key lists $y_{stub}=\\pm j1.07$ with $d=0.086\\lambda$ and $0.4125\\lambda$. For a $170\\ \\Omega$ load on $50\\ \\Omega$ line the $g=1$ crossings are at $1\\pm j1.30$, which gives the values here.",widget="stub")
st=shunt_stub(200+160j,100)
o=min(st,key=lambda s:s[3]); sh=min(st,key=lambda s:s[2])
add(id="pp-3.6-3",source="course",set="PP LO 3.4–3.6",lo="3.6",difficulty=3,title="Open shunt stub for 200 + j160 Ω",
 prompt="Match $Z_L=200+j160\\ \\Omega$ to a $100\\ \\Omega$ source with an open shunt stub on $100\\ \\Omega$ line. Find the solution with the shortest stub.",
 hints=["$y_L=\\dfrac{100}{200+j160}$.","Find both $g=1$ crossings, compute both stub lengths, and keep the shorter one.","An open stub has $y=+j\\tan\\beta\\ell$."],
 steps=[f"$y_L={tc(100/(200+160j))}$"]+[f"At $d={tr(d)}\\lambda$: $y=1{'+' if b>0 else '-'}j{tr(abs(b))}$, so the open stub is $\\ell={tr(lo)}\\lambda$." for d,b,ls,lo in st]+[f"The shortest open stub is $\\ell_{{\\mathrm{{stub}}}}={tr(o[3])}\\lambda$ with $d={tr(o[0])}\\lambda$."],
 answers=[{"label":"d","value":f"{tr(o[0])}\\lambda"},{"label":r"\ell_{stub}","value":f"{tr(o[3])}\\lambda"}],widget="stub")
add(id="pp-3.6-4",source="course",set="PP LO 3.4–3.6",lo="3.6",difficulty=3,title="Shorted shunt stub for 200 + j160 Ω",
 prompt="Repeat the previous problem with a shorted shunt stub. Find the solution with the shortest stub.",
 hints=["A shorted stub has $y=-j\\cot\\beta\\ell$.","The two $g=1$ crossings are the same as before; only the stub length changes."],
 steps=[f"At $d={tr(d)}\\lambda$ the stub must supply ${'-' if b>0 else '+'}j{tr(abs(b))}$, so the shorted stub is $\\ell={tr(ls)}\\lambda$." for d,b,ls,lo in st]+[f"The shortest shorted stub is $\\ell_{{\\mathrm{{stub}}}}={tr(sh[2])}\\lambda$ with $d={tr(sh[0])}\\lambda$."],
 answers=[{"label":"d","value":f"{tr(sh[0])}\\lambda"},{"label":r"\ell_{stub}","value":f"{tr(sh[2])}\\lambda"}],
 note="The course key gives $d=0.221\\lambda$ and $\\ell_{stub}=0.100\\lambda$, which agree with these values to Smith-chart reading accuracy.",widget="stub")
GL,Gs,V1,A=bounce(10,30,50,150,1); T=0.08/(0.67*c)
vs=lambda x,t:tr(vstep(A,x,t,1),4)
add(id="pp-3.7-1",source="course",set="PP LO 3.7",lo="3.7",difficulty=2,title="Bounce diagram: 30 Ω source, 150 Ω load",
 prompt="A $10\\ \\mathrm{V}$ step source with $30\\ \\Omega$ internal resistance drives an $8\\ \\mathrm{cm}$, $50\\ \\Omega$ line ($u_p=0.67c$) terminated in $150\\ \\Omega$. (a) Draw the bounce diagram. Sketch the voltage out to $2\\ \\mathrm{ns}$ at (b) the source end, (c) the midpoint, and (d) the load.",
 hints=["$T=\\dfrac{\\ell}{u_p}$.","$V_1^+=V_s\\dfrac{Z_0}{R_s+Z_0}$.","Each new wave is the previous one times $\\Gamma_L$ or $\\Gamma_s$."],
 steps=[D(f"T=\\frac{{0.08}}{{0.67c}}={teng(T,'s')}"),D(f"\\Gamma_L=\\frac{{150-50}}{{150+50}}={tr(GL)},\\qquad \\Gamma_s=\\frac{{30-50}}{{30+50}}={tr(Gs)}"),D(f"V_1^+=10\\cdot\\frac{{50}}{{30+50}}={tr(V1)}\\ \\mathrm{{V}}"),
        "Wave amplitudes in order (volts): "+", ".join(f"${tr(a)}$" for a in A[:6])+".",
        f"Source end: ${vs(0,.5)}\\ \\mathrm{{V}}$ for $0<t<2T$, then ${vs(0,2.5)}\\ \\mathrm{{V}}$, then ${vs(0,4.5)}\\ \\mathrm{{V}}$ after $4T$.",
        f"Midpoint: $0$ until $T/2$, then ${vs(.5,1)}$, ${vs(.5,2)}$ at $1.5T$, ${vs(.5,3)}$ at $2.5T$, ${vs(.5,4)}$ at $3.5T$, ${vs(.5,4.9)}\\ \\mathrm{{V}}$ at $4.5T$.",
        f"Load: $0$ until $T$, then ${vs(1,1.5)}\\ \\mathrm{{V}}$, ${vs(1,3.5)}\\ \\mathrm{{V}}$ at $3T$, ${vs(1,5.5)}\\ \\mathrm{{V}}$ at $5T$.",
        "Steady state:"+D(f"V_\\infty=10\\cdot\\frac{{150}}{{30+150}}={tr(10*150/180,4)}\\ \\mathrm{{V}}")],
 answers=[{"label":"T","value":teng(T,'s')},{"label":"V_1^+","value":f"{tr(V1)}\\ \\mathrm{{V}}"},{"label":r"V_L\ (T<t<3T)","value":f"{vs(1,1.5)}\\ \\mathrm{{V}}"},{"label":r"V_\infty","value":f"{tr(10*150/180,4)}\\ \\mathrm{{V}}"}],widget="bounce")

# ================= ORIGINAL PROBLEMS =================
bt=60; f=2e9; upv=2*math.pi*f/bt
add(id="ox-3.2-1",source="original",lo="3.2",difficulty=1,title="Reading a traveling wave",
 prompt="A voltage on a lossless line is"+D(r"v(z,t)=5\cos\!\left(4\pi\times10^{9}\,t-60z\right)\ \mathrm{V}")+"Find the frequency, $\\beta$, the phase velocity, the wavelength, and the relative permittivity of the dielectric.",
 hints=["Match the form $\\cos(\\omega t-\\beta z)$.","$u_p=\\dfrac{\\omega}{\\beta}$ and $\\varepsilon_r=\\left(\\dfrac{c}{u_p}\\right)^2$."],
 steps=[f"$\\omega=4\\pi\\times10^9\\ \\mathrm{{rad/s}}$, so $f={teng(f,'Hz')}$, and $\\beta=60\\ \\mathrm{{rad/m}}$.",D(f"u_p=\\frac{{\\omega}}{{\\beta}}={teng(upv,'m/s')}={tr(upv/c)}c"),D(f"\\lambda=\\frac{{2\\pi}}{{\\beta}}={teng(2*math.pi/bt,'m')}"),D(f"\\varepsilon_r=\\left(\\frac{{c}}{{u_p}}\\right)^2={tr((c/upv)**2)}"),"The wave travels in $+z$ because $\\omega t$ and $\\beta z$ have opposite signs."],
 answers=[{"label":"f","value":teng(f,'Hz')},{"label":"u_p","value":f"{tr(upv/c)}c"},{"label":r"\lambda","value":teng(2*math.pi/bt,'m')},{"label":r"\varepsilon_r","value":tr((c/upv)**2)}],widget="waves")
L_,C_=300e-9,120e-12; f=500e6
add(id="ox-3.2-2",source="original",lo="3.2",difficulty=1,title="Line constants from L′ and C′",
 prompt="A lossless line has $L'=300\\ \\mathrm{nH/m}$ and $C'=120\\ \\mathrm{pF/m}$. At $500\\ \\mathrm{MHz}$, find $Z_0$, $u_p$, $\\beta$, and $\\lambda$.",
 hints=["For a lossless line, $Z_0=\\sqrt{\\dfrac{L'}{C'}}$ and $u_p=\\dfrac{1}{\\sqrt{L'C'}}$."],
 steps=[D(f"Z_0=\\sqrt{{\\frac{{300\\ \\mathrm{{nH/m}}}}{{120\\ \\mathrm{{pF/m}}}}}}={tr(math.sqrt(L_/C_))}\\ \\Omega"),D(f"u_p=\\frac{{1}}{{\\sqrt{{L'C'}}}}={teng(1/math.sqrt(L_*C_),'m/s')}"),D(f"\\beta=\\frac{{\\omega}}{{u_p}}={tr(2*math.pi*f*math.sqrt(L_*C_))}\\ \\mathrm{{rad/m}},\\qquad \\lambda=\\frac{{u_p}}{{f}}={teng(1/math.sqrt(L_*C_)/f,'m')}")],
 answers=[{"label":"Z_0","value":f"{tr(math.sqrt(L_/C_))}\\ \\Omega"},{"label":"u_p","value":teng(1/math.sqrt(L_*C_),'m/s')},{"label":r"\beta","value":f"{tr(2*math.pi*f*math.sqrt(L_*C_))}\\ \\mathrm{{rad/m}}"},{"label":r"\lambda","value":teng(1/math.sqrt(L_*C_)/f,'m')}],widget="params")
R_,L_,G_,C_=2,250e-9,0.5e-3,100e-12; f=50e6; w_=2*math.pi*f
gam=cmath.sqrt((R_+1j*w_*L_)*(G_+1j*w_*C_)); Z0c=cmath.sqrt((R_+1j*w_*L_)/(G_+1j*w_*C_))
add(id="ox-3.2-3",source="original",lo="3.2",difficulty=2,title="A lossy line at 50 MHz",
 prompt="A line has $R'=2\\ \\Omega/\\mathrm{m}$, $L'=250\\ \\mathrm{nH/m}$, $G'=0.5\\ \\mathrm{mS/m}$, and $C'=100\\ \\mathrm{pF/m}$. At $50\\ \\mathrm{MHz}$, find $\\gamma$, $\\alpha$ in dB/m, $\\beta$, and $Z_0$. How much does a wave's amplitude drop over $20\\ \\mathrm{m}$?",
 hints=["$\\gamma=\\sqrt{(R'+j\\omega L')(G'+j\\omega C')}$.","$\\alpha_{dB}=8.686\\,\\alpha$ when $\\alpha$ is in Np/m.","The amplitude ratio over a length $\\ell$ is $e^{-\\alpha\\ell}$."],
 steps=[D(f"R'+j\\omega L'={tc(R_+1j*w_*L_)}\\ \\Omega/\\mathrm{{m}},\\qquad G'+j\\omega C'={tc(G_+1j*w_*C_,3)}\\ \\mathrm{{S/m}}"),D(f"\\gamma=\\sqrt{{(R'+j\\omega L')(G'+j\\omega C')}}={tc(gam,4)}\\ \\mathrm{{m}}^{{-1}}"),
        f"$\\alpha={tr(gam.real,4)}\\ \\mathrm{{Np/m}}={tr(8.686*gam.real,4)}\\ \\mathrm{{dB/m}}$ and $\\beta={tr(gam.imag,4)}\\ \\mathrm{{rad/m}}$.",D(f"Z_0=\\sqrt{{\\frac{{R'+j\\omega L'}}{{G'+j\\omega C'}}}}={tc(Z0c)}\\ \\Omega"),
        D(f"e^{{-20\\alpha}}={tr(math.exp(-20*gam.real))}")+f"That is a ${tr(20*8.686*gam.real)}\\ \\mathrm{{dB}}$ loss over $20\\ \\mathrm{{m}}$."],
 answers=[{"label":r"\alpha","value":f"{tr(8.686*gam.real)}\\ \\mathrm{{dB/m}}"},{"label":r"\beta","value":f"{tr(gam.imag,4)}\\ \\mathrm{{rad/m}}"},{"label":"Z_0","value":tc(Z0c)+r"\ \Omega"},{"label":r"e^{-20\alpha}","value":tr(math.exp(-20*gam.real))}],widget="params")
zl=30+45j; g=G(zl,75); th=cmath.phase(g); dmax=th/(4*math.pi); dmax=dmax+0.5 if dmax<0 else dmax; dmin=dmax+0.25 if dmax<0.25 else dmax-0.25
add(id="ox-3.2-4",source="original",lo="3.2",difficulty=2,title="Where are the peaks and nulls?",
 prompt="A $75\\ \\Omega$ line is terminated in $30+j45\\ \\Omega$. Find $\\Gamma_L$, the VSWR, and the distances from the load to the first voltage maximum and minimum.",
 hints=["Voltage maxima occur where the phase of $\\Gamma(d)=\\Gamma_Le^{-j2\\beta d}$ is zero.","Maxima and minima are $\\lambda/4$ apart."],
 steps=[D(f"\\Gamma_L=\\frac{{-45+j45}}{{105+j45}}={tc(g)}={tp(g)}"),f"$\\mathrm{{VSWR}}={tr(vswr(g))}$",D(f"d_{{\\mathrm{{max}}}}=\\frac{{\\theta_\\Gamma}}{{4\\pi}}\\lambda=\\frac{{{deg(math.degrees(th))}}}{{720^\\circ}}\\lambda={tr(dmax)}\\lambda"),D(f"d_{{\\mathrm{{min}}}}=d_{{\\mathrm{{max}}}}{'+' if dmax<0.25 else '-'}\\frac{{\\lambda}}{{4}}={tr(dmin)}\\lambda")],
 answers=[{"label":r"\Gamma_L","value":tp(g)},{"label":r"\mathrm{VSWR}","value":tr(vswr(g))},{"label":"d_{max}","value":f"{tr(dmax)}\\lambda"},{"label":"d_{min}","value":f"{tr(dmin)}\\lambda"}],widget="waves")
zl=100-100j; g=G(zl,50); vp=4*cmath.exp(1j*math.radians(30))
add(id="ox-3.2-5",source="original",lo="3.2",difficulty=1,title="Reflected and transmitted voltage",
 prompt="An incident wave $V_0^+=4\\ \\mathrm{V}\\angle 30^\\circ$ on a $50\\ \\Omega$ line reaches a $100-j100\\ \\Omega$ load. Find the reflected wave $V_0^-$ and the load voltage $V_L$.",
 hints=["$V_0^-=\\Gamma_LV_0^+$.","$V_L=V_0^++V_0^-=V_0^+(1+\\Gamma_L)=\\tau V_0^+$."],
 steps=[D(f"\\Gamma_L=\\frac{{50-j100}}{{150-j100}}={tp(g)}"),D(f"V_0^-=\\Gamma_LV_0^+={tp(g*vp)}\\ \\mathrm{{V}}"),D(f"\\tau=1+\\Gamma_L={tp(1+g)},\\qquad V_L=\\tau V_0^+={tp(vp*(1+g))}\\ \\mathrm{{V}}")],
 answers=[{"label":"V_0^-","value":tp(g*vp)+r"\ \mathrm{V}"},{"label":"V_L","value":tp(vp*(1+g))+r"\ \mathrm{V}"}],widget="calc")
zl=40+70j; Zi=zin(zl,50,0.18); w0=((math.pi-cmath.phase(G(zl,50)))/(4*math.pi))%0.5
add(id="ox-3.3-1",source="original",lo="3.3",difficulty=2,title="Input impedance at 0.18λ",
 prompt="Find the input impedance of a $0.18\\lambda$ length of $50\\ \\Omega$ line terminated in $40+j70\\ \\Omega$. Check your answer on the Smith chart.",
 hints=["$\\beta\\ell=2\\pi(0.18)=64.8^\\circ$.","On the Smith chart, rotate $0.18\\lambda$ toward the generator."],
 steps=[f"$\\tan 64.8^\\circ={tr(math.tan(2*math.pi*0.18),4)}$",D(f"Z_{{\\mathrm{{in}}}}=50\\,\\frac{{Z_L+j50\\tan\\beta\\ell}}{{50+jZ_L\\tan\\beta\\ell}}={tc(Zi)}\\ \\Omega"),f"Smith chart: $z_L=0.8+j1.4$ sits at ${tr(w0)}\\lambda$ WTG. Moving $0.18\\lambda$ lands at ${tr((w0+0.18)%0.5)}\\lambda$ WTG."],
 answers=[{"label":"Z_{in}","value":tc(Zi)+r"\ \Omega"}],widget="smith")
lam=0.7*c/2.4e9; ls=math.atan(2)/(2*math.pi)
add(id="ox-3.3-2",source="original",lo="3.3",difficulty=2,title="A shorted stub that acts like an inductor",
 prompt="At $2.4\\ \\mathrm{GHz}$ you need $+j100\\ \\Omega$ from a shorted $50\\ \\Omega$ stub with $u_p=0.7c$. What is the shortest stub length, in wavelengths and millimeters? What inductor would give the same reactance?",
 hints=["A shorted line has $Z_{in}=jZ_0\\tan\\beta\\ell$.","Solve $\\tan\\beta\\ell=\\dfrac{100}{50}$."],
 steps=["$jZ_0\\tan\\beta\\ell=j100$, so $\\tan\\beta\\ell=2$.",D(f"\\beta\\ell=\\tan^{{-1}}2={deg(math.degrees(math.atan(2)))}\\quad\\Rightarrow\\quad \\ell={tr(ls,4)}\\lambda"),D(f"\\lambda=\\frac{{0.7c}}{{2.4\\ \\mathrm{{GHz}}}}={teng(lam,'m')}\\quad\\Rightarrow\\quad \\ell={teng(ls*lam,'m')}"),D(f"L=\\frac{{X}}{{\\omega}}=\\frac{{100}}{{2\\pi(2.4\\times10^9)}}={teng(100/(2*math.pi*2.4e9),'H')}")],
 answers=[{"label":r"\ell","value":f"{tr(ls,4)}\\lambda={teng(ls*lam,'m')}"},{"label":"L","value":teng(100/(2*math.pi*2.4e9),'H')}],widget="smith")
X=1/(2*math.pi*1e9*2e-12); lo=math.atan(50/X)/(2*math.pi)
add(id="ox-3.3-3",source="original",lo="3.3",difficulty=2,title="An open stub that acts like a capacitor",
 prompt="What is the shortest length of open-circuited $50\\ \\Omega$ line that looks like a $2\\ \\mathrm{pF}$ capacitor at $1\\ \\mathrm{GHz}$?",
 hints=["An open line has $Z_{in}=-jZ_0\\cot\\beta\\ell$.","A capacitor has $Z=\\dfrac{-j}{\\omega C}$."],
 steps=[D(f"X_C=\\frac{{1}}{{\\omega C}}={tr(X,4)}\\ \\Omega"),D(f"Z_0\\cot\\beta\\ell={tr(X,4)}\\quad\\Rightarrow\\quad\\tan\\beta\\ell=\\frac{{50}}{{{tr(X,4)}}}={tr(50/X,4)}"),D(f"\\beta\\ell={deg(math.degrees(math.atan(50/X)))}\\quad\\Rightarrow\\quad\\ell={tr(lo,4)}\\lambda")],
 answers=[{"label":r"\ell","value":f"{tr(lo,4)}\\lambda"}],widget="smith")
Vs=12; Zs=50; Z0=50; zl=25-40j; l=0.35
Zi=zin(zl,Z0,l); Vin=Vs*Zi/(Zs+Zi); g=G(zl,Z0); b=2*math.pi*l; V0=Vin/(cmath.exp(1j*b)+g*cmath.exp(-1j*b)); Pin=0.5*(Vin*np.conj(Vin/Zi)).real
add(id="ox-3.3-4",source="original",lo="3.3",difficulty=3,title="Generator, line and load",
 prompt="A $12\\ \\mathrm{V}$ (amplitude) source with $50\\ \\Omega$ internal impedance drives a $0.35\\lambda$, $50\\ \\Omega$ lossless line terminated in $25-j40\\ \\Omega$. Find $Z_{in}$, $V_{in}$, $V_0^+$, the load voltage, and the average power delivered to the load.",
 hints=["Find $Z_{in}$ first, then use a voltage divider at the input.","$V(z)=V_0^+\\left(e^{-j\\beta z}+\\Gamma_Le^{j\\beta z}\\right)$; evaluate it at $z=-\\ell$ to find $V_0^+$.","On a lossless line, all the power entering the line reaches the load."],
 steps=[f"$\\Gamma_L={tp(g)}$ and $Z_{{\\mathrm{{in}}}}={tc(Zi)}\\ \\Omega$.",D(f"V_{{\\mathrm{{in}}}}=12\\cdot\\frac{{Z_{{\\mathrm{{in}}}}}}{{50+Z_{{\\mathrm{{in}}}}}}={tp(Vin)}\\ \\mathrm{{V}}"),D(f"V_0^+=\\frac{{V_{{\\mathrm{{in}}}}}}{{e^{{j\\beta\\ell}}+\\Gamma_Le^{{-j\\beta\\ell}}}}={tp(V0)}\\ \\mathrm{{V}}"),"$|V_0^+|=6\\ \\mathrm{V}$ because $Z_s=Z_0$: the source launches $V_s/2$ whatever the load.",
        D(f"V_L=V_0^+(1+\\Gamma_L)={tp(V0*(1+g))}\\ \\mathrm{{V}}"),D(f"P_{{\\mathrm{{av}}}}=\\frac{{|V_0^+|^2}}{{2Z_0}}\\left(1-|\\Gamma_L|^2\\right)={teng(abs(V0)**2*(1-abs(g)**2)/100,'W')}"),f"Check: $\\tfrac12\\mathrm{{Re}}\\{{V_{{\\mathrm{{in}}}}I_{{\\mathrm{{in}}}}^*\\}}={teng(Pin,'W')}$."],
 answers=[{"label":"Z_{in}","value":tc(Zi)+r"\ \Omega"},{"label":"V_0^+","value":tp(V0)+r"\ \mathrm{V}"},{"label":"V_L","value":tp(V0*(1+g))+r"\ \mathrm{V}"},{"label":"P_{av}","value":teng(Pin,'W')}],widget="calc")
Vs=20; Zs=75; Z0=50; zl=150; l=0.2
Zi=zin(zl,Z0,l); Vin=Vs*Zi/(Zs+Zi); g=G(zl,Z0); Pin=0.5*(Vin*np.conj(Vin/Zi)).real; Pmax=Vs**2/(8*Zs)
add(id="ox-3.3-5",source="original",lo="3.3",difficulty=3,title="Mismatched at both ends",
 prompt="A $20\\ \\mathrm{V}$ source with $75\\ \\Omega$ internal resistance drives a $0.2\\lambda$, $50\\ \\Omega$ line terminated in $150\\ \\Omega$. Find $Z_{in}$ and the power delivered to the load, and compare it with the source's available power $\\dfrac{V_s^2}{8R_s}$.",
 hints=["Find $Z_{in}$ first, then treat the input as a voltage divider.","Available power is what a conjugate-matched load would get."],
 steps=[f"$\\Gamma_L={tr(g)}$ and $\\beta\\ell=72^\\circ$.",D(f"Z_{{\\mathrm{{in}}}}={tc(Zi)}\\ \\Omega"),D(f"V_{{\\mathrm{{in}}}}={tp(Vin)}\\ \\mathrm{{V}},\\qquad I_{{\\mathrm{{in}}}}={tp(Vin/Zi)}\\ \\mathrm{{A}}"),D(f"P_{{\\mathrm{{load}}}}=\\tfrac12\\mathrm{{Re}}\\{{V_{{\\mathrm{{in}}}}I_{{\\mathrm{{in}}}}^*\\}}={teng(Pin,'W')}"),D(f"P_{{\\mathrm{{avail}}}}=\\frac{{20^2}}{{8(75)}}={teng(Pmax,'W')}")+f"The load receives ${tr(100*Pin/Pmax)}\\%$ of the available power."],
 answers=[{"label":"Z_{in}","value":tc(Zi)+r"\ \Omega"},{"label":"P_{load}","value":teng(Pin,'W')},{"label":r"P_{load}/P_{avail}","value":f"{tr(100*Pin/Pmax)}\\%"}],widget="calc")
Z1=math.sqrt(300*75); lamq=c/math.sqrt(2.2)/600e6
add(id="ox-3.4-1",source="original",lo="3.4",difficulty=1,title="Quarter-wave transformer",
 prompt="Match a $300\\ \\Omega$ antenna to a $75\\ \\Omega$ line at $600\\ \\mathrm{MHz}$ with a quarter-wave transformer built on a dielectric with $\\varepsilon_r=2.2$. Find $Z_1$ and the physical length.",
 hints=["$Z_1=\\sqrt{Z_0Z_L}$.","Inside the transformer, $\\lambda=\\dfrac{c}{f\\sqrt{\\varepsilon_r}}$."],
 steps=[D(f"Z_1=\\sqrt{{(75)(300)}}={tr(Z1)}\\ \\Omega"),D(f"\\lambda=\\frac{{c}}{{(600\\ \\mathrm{{MHz}})\\sqrt{{2.2}}}}={teng(lamq,'m')}\\quad\\Rightarrow\\quad\\ell=\\frac{{\\lambda}}{{4}}={teng(lamq/4,'m')}"),"The match is exact only at $600\\ \\mathrm{MHz}$; at other frequencies the section is no longer $\\lambda/4$."],
 answers=[{"label":"Z_1","value":f"{tr(Z1)}\\ \\Omega"},{"label":r"\ell","value":teng(lamq/4,'m')}],widget="calc")
zl=60+40j; g=G(zl,50); S=vswr(g); th=cmath.phase(g); dmax=(th/(4*math.pi))%0.5; dmin=(dmax+0.25)%0.5
add(id="ox-3.4-2",source="original",lo="3.4",difficulty=3,title="Quarter-wave transformer for a complex load",
 prompt="A $60+j40\\ \\Omega$ load sits on a $50\\ \\Omega$ line. A quarter-wave transformer only matches real impedances. Find where on the line to insert it (at a voltage maximum or minimum) and the $Z_1$ needed in each case.",
 hints=["At a voltage maximum the line impedance is real and equals $Z_0\\cdot\\mathrm{VSWR}$.","At a voltage minimum it is real and equals $\\dfrac{Z_0}{\\mathrm{VSWR}}$."],
 steps=[f"$\\Gamma_L={tp(g)}$ and $\\mathrm{{VSWR}}={tr(S)}$.",f"First voltage maximum at $d={tr(dmax)}\\lambda$, where $Z=50({tr(S)})={tr(50*S)}\\ \\Omega$:"+D(f"Z_1=\\sqrt{{(50)({tr(50*S)})}}={tr(math.sqrt(2500*S))}\\ \\Omega"),
        f"First voltage minimum at $d={tr(dmin)}\\lambda$, where $Z=\\dfrac{{50}}{{{tr(S)}}}={tr(50/S)}\\ \\Omega$:"+D(f"Z_1=\\sqrt{{(50)({tr(50/S)})}}={tr(math.sqrt(2500/S))}\\ \\Omega")],
 answers=[{"label":r"\text{At }V_{max}","value":f"d={tr(dmax)}\\lambda,\\ Z_1={tr(math.sqrt(2500*S))}\\ \\Omega"},{"label":r"\text{At }V_{min}","value":f"d={tr(dmin)}\\lambda,\\ Z_1={tr(math.sqrt(2500/S))}\\ \\Omega"}],widget="smith")
st=shunt_stub(30-40j,50)
add(id="ox-3.6-1",source="original",lo="3.6",difficulty=3,title="Shorted shunt stub for 30 − j40 Ω",
 prompt="Design a shorted shunt-stub match for $Z_L=30-j40\\ \\Omega$ on $50\\ \\Omega$ line. Give both solutions ($d$ and $\\ell_{stub}$).",
 hints=["$y_L=\\dfrac{50}{30-j40}=0.6+j0.8$.","Rotate on the VSWR circle until $g=1$.","A shorted stub has $y=-j\\cot\\beta\\ell$."],
 steps=[f"$y_L={tc(50/(30-40j))}$ and $|\\Gamma_L|={tr(abs(G(30-40j,50)))}$."]+[f"Solution {i+1}: at $d={tr(d)}\\lambda$, $y=1{'+' if b>0 else '-'}j{tr(abs(b))}$. The stub adds ${'-' if b>0 else '+'}j{tr(abs(b))}$, so $\\ell_{{\\mathrm{{stub}}}}={tr(ls)}\\lambda$." for i,(d,b,ls,lo) in enumerate(st)],
 answers=[{"label":f"\\text{{Solution }}{i+1}","value":f"d={tr(d)}\\lambda,\\ \\ell_{{\\mathrm{{stub}}}}={tr(ls)}\\lambda"} for i,(d,b,ls,lo) in enumerate(st)],widget="stub")
sp=series_pts(100+80j,50); w2=2*math.pi*2e9
el_=lambda x:(f"C={teng(1/(w2*x*50),'F')}" if x>0 else f"L={teng(-x*50/w2,'H')}")
add(id="ox-3.6-2",source="original",lo="3.6",difficulty=3,title="Series element match at 2 GHz",
 prompt="Match $Z_L=100+j80\\ \\Omega$ to $50\\ \\Omega$ at $2\\ \\mathrm{GHz}$ using a length of $50\\ \\Omega$ line followed by a series lumped element. Give both solutions, each with its element type and value.",
 hints=["Rotate $z_L=2+j1.6$ to the $r=1$ circle.","Cancel the leftover reactance with a capacitor if it is $+jx$, or an inductor if it is $-jx$."],
 steps=[f"$z_L=2+j1.6$ and $\\Gamma_L={tp(G(100+80j,50))}$."]+[f"At $\\ell={tr(d)}\\lambda$: $z=1{'+' if x>0 else '-'}j{tr(abs(x))}$, so use a series ${el_(x)}$." for d,x in sp],
 answers=[{"label":f"\\text{{Solution }}{i+1}","value":f"\\ell={tr(d)}\\lambda,\\ {el_(x)}"} for i,(d,x) in enumerate(sp)],widget="smith")
GL,Gs,V1,A=bounce(12,25,75,225,1); T=300/2e8
vs=lambda x,t:tr(vstep(A,x,t,1),4)
add(id="ox-3.7-1",source="original",lo="3.7",difficulty=2,title="Step response on a 300 m line",
 prompt="A $12\\ \\mathrm{V}$ step with $25\\ \\Omega$ source resistance drives a $300\\ \\mathrm{m}$, $75\\ \\Omega$ line ($u_p=2\\times10^8\\ \\mathrm{m/s}$) terminated in $225\\ \\Omega$. Find $T$, $\\Gamma_s$, $\\Gamma_L$, and $V_L$ at $t=2$, $5$, and $8\\ \\mu\\mathrm{s}$. What is the steady-state load voltage?",
 hints=["$T=\\dfrac{\\ell}{u_p}=1.5\\ \\mu\\mathrm{s}$.","The load first sees the incident wave plus its own reflection at $t=T$."],
 steps=[f"$T={teng(T,'s')}$, $\\Gamma_L={tr(GL)}$, $\\Gamma_s={tr(Gs)}$.",D(f"V_1^+=12\\cdot\\frac{{75}}{{25+75}}={tr(V1)}\\ \\mathrm{{V}}"),f"For $T<t<3T$ ($1.5$–$4.5\\ \\mu\\mathrm{{s}}$): $V_L=V_1^+(1+\\Gamma_L)={vs(1,2/1.5)}\\ \\mathrm{{V}}$.",
        f"For $3T<t<5T$ ($4.5$–$7.5\\ \\mu\\mathrm{{s}}$): $V_L={vs(1,5/1.5)}\\ \\mathrm{{V}}$.",f"For $5T<t<7T$: $V_L={vs(1,8/1.5)}\\ \\mathrm{{V}}$.","Steady state:"+D(r"V_\infty=12\cdot\frac{225}{25+225}=10.80\ \mathrm{V}")],
 answers=[{"label":r"V_L(2\ \mu\mathrm{s})","value":f"{vs(1,2/1.5)}\\ \\mathrm{{V}}"},{"label":r"V_L(5\ \mu\mathrm{s})","value":f"{vs(1,5/1.5)}\\ \\mathrm{{V}}"},{"label":r"V_L(8\ \mu\mathrm{s})","value":f"{vs(1,8/1.5)}\\ \\mathrm{{V}}"},{"label":r"V_\infty","value":r"10.80\ \mathrm{V}"}],widget="bounce")
GL,Gs,V1,A=bounce(9,150,50,np.inf,1)
vs=lambda x,t:tr(vstep(A,x,t,1),4)
add(id="ox-3.7-2",source="original",lo="3.7",difficulty=2,title="Open-circuited line",
 prompt="A $9\\ \\mathrm{V}$ step source with $150\\ \\Omega$ resistance is connected to an open-circuited $50\\ \\Omega$ line with one-way delay $T$. Sketch the voltage at the source end from $0$ to $6T$ and say where it settles.",
 hints=["$\\Gamma_L=+1$ for an open.","The source-end voltage only changes at $t=0,\\,2T,\\,4T,\\dots$"],
 steps=[D(f"\\Gamma_L=1,\\qquad\\Gamma_s=\\frac{{150-50}}{{150+50}}={tr(Gs)},\\qquad V_1^+=9\\cdot\\frac{{50}}{{200}}={tr(V1)}\\ \\mathrm{{V}}"),f"$0<t<2T$: ${vs(0,1)}\\ \\mathrm{{V}}$",f"$2T<t<4T$: ${vs(0,3)}\\ \\mathrm{{V}}$",f"$4T<t<6T$: ${vs(0,5)}\\ \\mathrm{{V}}$","It climbs toward $9\\ \\mathrm{V}$: with no load current, nothing drops across $R_s$."],
 answers=[{"label":"0<t<2T","value":f"{vs(0,1)}\\ \\mathrm{{V}}"},{"label":"2T<t<4T","value":f"{vs(0,3)}\\ \\mathrm{{V}}"},{"label":"4T<t<6T","value":f"{vs(0,5)}\\ \\mathrm{{V}}"},{"label":r"V_\infty","value":r"9\ \mathrm{V}"}],widget="bounce")
gm=10**(-14/20)
add(id="ox-3.8-1",source="original",lo="3.8",difficulty=1,title="Reading a VNA return loss",
 prompt="A VNA shows a return loss of $14\\ \\mathrm{dB}$ ($S_{11}=-14\\ \\mathrm{dB}$) for an antenna on a $50\\ \\Omega$ system. What are $|\\Gamma|$, the VSWR, and the fraction of incident power reflected?",
 hints=["$|\\Gamma|=10^{-RL/20}$.","The reflected power fraction is $|\\Gamma|^2$."],
 steps=[D(f"|\\Gamma|=10^{{-14/20}}={tr(gm)}"),D(f"\\mathrm{{VSWR}}=\\frac{{1+{tr(gm)}}}{{1-{tr(gm)}}}={tr(vswr(gm))}"),D(f"|\\Gamma|^2={tr(gm**2)}={tr(100*gm**2)}\\%")],
 answers=[{"label":r"|\Gamma|","value":tr(gm)},{"label":r"\mathrm{VSWR}","value":tr(vswr(gm))},{"label":r"|\Gamma|^2","value":f"{tr(100*gm**2)}\\%"}],widget="calc")
S=3; dmin=0.12; gm=(S-1)/(S+1); th=4*math.pi*dmin-math.pi; g=gm*cmath.exp(1j*th); ZL=50*(1+g)/(1-g)
add(id="ox-3.2-6",source="original",lo="3.2",difficulty=3,title="Find the load from standing-wave measurements",
 prompt="On a $50\\ \\Omega$ line you measure $\\mathrm{VSWR}=3$, with the first voltage minimum $0.12\\lambda$ from the load. What is $Z_L$?",
 hints=["$|\\Gamma|=\\dfrac{\\mathrm{VSWR}-1}{\\mathrm{VSWR}+1}$.","At a voltage minimum the phase of $\\Gamma(d)$ is $-180^\\circ$, so $\\theta_\\Gamma-\\dfrac{4\\pi d_{min}}{\\lambda}=-\\pi$."],
 steps=[D(f"|\\Gamma|=\\frac{{3-1}}{{3+1}}={tr(gm)}"),D(f"\\theta_\\Gamma=4\\pi(0.12)-\\pi={deg(math.degrees(th))}"),D(f"\\Gamma_L={tp(g)}={tc(g)}"),D(f"Z_L=50\\,\\frac{{1+\\Gamma_L}}{{1-\\Gamma_L}}={tc(ZL)}\\ \\Omega"),"Smith chart check: start at the $V_{min}$ point ($z=1/3$ on the real axis) and rotate $0.12\\lambda$ toward the load."],
 answers=[{"label":"Z_L","value":tc(ZL)+r"\ \Omega"}],widget="smith")

json.dump(roman({"chapter":3,"title":"Transmission lines","format":"Text with inline TeX in $...$ and display TeX in $$...$$. Answer label and value fields are TeX without delimiters.","problems":P}),open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","content","ch03-practice.json"),"w"),ensure_ascii=False,indent=1)
print(len(P))
