# Magnetostatics: flashcards, glossary and practice problems.
# Every number in the steps and answers is computed here. Run: python3 tools/make_magnetostatics.py
import math, os, sys
import numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lib import *
D=lambda s:"$$"+s+"$$"
deg=lambda x:f"{tr(x)}^\\circ"
MU0=4e-7*math.pi
T=["magnetostatics"]

C=[
("Magnetic force on a moving charge?",D(r"\mathbf{F}_m=q\,\mathbf{u}\times\mathbf{B}")+"It is perpendicular to the velocity, so it does no work.","equation",T),
("Lorentz force?",D(r"\mathbf{F}=q\mathbf{E}+q\,\mathbf{u}\times\mathbf{B}"),"equation",T),
("Force on a straight wire of length $\\ell$ carrying $I$ in a uniform $\\mathbf{B}$?",D(r"\mathbf{F}=I\,\boldsymbol{\ell}\times\mathbf{B}")+"$\\boldsymbol{\\ell}$ points along the current.","equation",T),
("Biot–Savart law?",D(r"d\mathbf{H}=\frac{I}{4\pi}\,\frac{d\mathbf{l}\times\hat{\mathbf{R}}}{R^2}")+"$\\hat{\\mathbf{R}}$ points from the current element to the field point.","equation",T),
("$\\mathbf{H}$ of an infinitely long straight wire?",D(r"\mathbf{H}=\hat{\boldsymbol{\phi}}\,\frac{I}{2\pi r}")+"Circles the wire by the right-hand rule.","equation",T),
("$\\mathbf{H}$ at the center of a circular loop of radius $a$?",D(r"H=\frac{I}{2a}"),"equation",T),
("$\\mathbf{H}$ on the axis of a circular loop?",D(r"\mathbf{H}=\hat{\mathbf{z}}\,\frac{Ia^2}{2(a^2+z^2)^{3/2}}"),"equation",T),
("$\\mathbf{H}$ of a finite straight segment, at distance $r$?",D(r"H=\frac{I}{4\pi r}\left(\cos\alpha_1-\cos\alpha_2\right)")+"$\\alpha_1$ and $\\alpha_2$ are the angles from the wire's direction to the lines joining its two ends to the point.","equation",T),
("Gauss's law for magnetism?",D(r"\oint_S\mathbf{B}\cdot d\mathbf{s}=0,\qquad\nabla\cdot\mathbf{B}=0")+"There are no magnetic charges; field lines always close.","equation",T),
("Ampère's law, integral form?",D(r"\oint_C\mathbf{H}\cdot d\mathbf{l}=I_{\mathrm{enc}}"),"equation",T),
("Ampère's law, differential form (statics)?",D(r"\nabla\times\mathbf{H}=\mathbf{J}"),"equation",T),
("$\\mathbf{H}$ inside a long solenoid with $n$ turns per meter?",D(r"\mathbf{H}=\hat{\mathbf{z}}\,nI")+"Uniform inside and nearly zero outside.","equation",T),
("$\\mathbf{H}$ inside a toroid with $N$ turns?",D(r"H=\frac{NI}{2\pi r}")+"Zero outside the windings.","equation",T),
("$\\mathbf{H}$ inside a solid round wire carrying uniform current?",D(r"H=\frac{Ir}{2\pi a^2}\qquad(r\le a)"),"equation",T),
("Force per unit length between two parallel wires?",D(r"F'=\frac{\mu_0I_1I_2}{2\pi d}")+"Currents in the same direction attract; opposite currents repel.","equation",T),
("Magnetic flux through a surface?",D(r"\Phi=\int_S\mathbf{B}\cdot d\mathbf{s}")+"In webers (Wb).","equation",T),
("Definition of inductance?",D(r"L=\frac{\Lambda}{I}=\frac{N\Phi}{I}"),"equation",T),
("Inductance of a long solenoid?",D(r"L=\frac{\mu N^2A}{\ell}"),"equation",T),
("Energy stored in an inductor, and the magnetic energy density?",D(r"W_m=\tfrac12LI^2,\qquad w_m=\tfrac12\mu H^2"),"equation",T),
("Boundary condition on normal $\\mathbf{B}$?",D(r"B_{1n}=B_{2n}"),"equation",T),
("Boundary condition on tangential $\\mathbf{H}$?",D(r"\hat{\mathbf{n}}_2\times(\mathbf{H}_1-\mathbf{H}_2)=\mathbf{J}_s")+"With no surface current, $H_{1t}=H_{2t}$.","equation",T),
("What happens to $\\mathbf{B}$ leaving iron into air?","It leaves almost exactly normal to the surface: tangential $H$ is continuous, so tangential $B$ drops by $\\mu_r$.","concept",T),
("Diamagnetic, paramagnetic and ferromagnetic?","Diamagnetic: $\\mu_r$ slightly below 1 (copper). Paramagnetic: slightly above 1 (aluminum). Ferromagnetic: $\\mu_r\\gg1$ and nonlinear (iron, nickel).","concept",T),
("Magnetic vector potential?",D(r"\mathbf{B}=\nabla\times\mathbf{A}")+"Possible because $\\nabla\\cdot\\mathbf{B}=0$.","equation",T),
]

G=[
("Magnetic force","","","$\\mathbf{F}_m=q\\mathbf{u}\\times\\mathbf{B}$ on a moving charge, or $I\\,d\\mathbf{l}\\times\\mathbf{B}$ on a current element. Always perpendicular to the motion.",None,T),
("Lorentz force","","","The total electromagnetic force on a charge: $\\mathbf{F}=q(\\mathbf{E}+\\mathbf{u}\\times\\mathbf{B})$.",None,T),
("Biot–Savart law","","","Gives the magnetic field of a current element: $d\\mathbf{H}=\\dfrac{I\\,d\\mathbf{l}\\times\\hat{\\mathbf{R}}}{4\\pi R^2}$. Integrate over the current to get $\\mathbf{H}$.","biot",T),
("Ampère's law","","","The circulation of $\\mathbf{H}$ around a closed loop equals the current through it: $\\oint\\mathbf{H}\\cdot d\\mathbf{l}=I_{\\mathrm{enc}}$.","ampere",T),
("Amperian loop","","","A closed path chosen so that $\\mathbf{H}$ is constant and tangent along it, which turns Ampère's law into algebra.","ampere",T),
("Right-hand rule","","","Point the thumb along the current; the fingers curl the way $\\mathbf{H}$ circles it. Also gives the direction of $\\mathbf{A}\\times\\mathbf{B}$.","biot",T),
("Magnetic flux","\\Phi","\\mathrm{Wb}","$\\Phi=\\int_S\\mathbf{B}\\cdot d\\mathbf{s}$. Through any closed surface it is zero.",None,T),
("Magnetic dipole","\\mathbf{m}=I\\mathbf{A}","\\mathrm{A\\,m^2}","A small current loop. Far away its field looks like an electric dipole's field.","biot",T),
("Solenoid","","","A helical coil. Inside a long one, $H=nI$ along the axis, where $n$ is turns per meter.","biot",T),
("Toroid","","","A solenoid bent into a ring. $H=\\dfrac{NI}{2\\pi r}$ inside the windings and zero outside.","ampere",T),
("Inductance","L","\\mathrm{H}","Flux linkage per unit current: $L=N\\Phi/I$. Depends only on geometry and $\\mu$.",None,T),
("Mutual inductance","M_{12}","\\mathrm{H}","Flux linking circuit 2 per unit current in circuit 1.",None,T),
("Magnetic energy","W_m","\\mathrm{J}","Energy stored in the field: $W_m=\\tfrac12\\int\\mu H^2\\,dV=\\tfrac12LI^2$.",None,T),
("Ferromagnetic material","","","A material such as iron with $\\mu_r$ in the hundreds or thousands, which concentrates magnetic flux. Its $B$–$H$ curve is nonlinear and shows hysteresis.","mboundary",T),
("Magnetic boundary conditions","","","Normal $\\mathbf{B}$ is continuous. Tangential $\\mathbf{H}$ is continuous unless a surface current $\\mathbf{J}_s$ flows on the boundary.","mboundary",T),
("Magnetic vector potential","\\mathbf{A}","\\mathrm{Wb/m}","A vector field with $\\mathbf{B}=\\nabla\\times\\mathbf{A}$.",None,T),
]

P=[]
def add(**k): k.setdefault("source","original"); k.setdefault("topics",T); P.append(k)
def vec(v,u=("\\mathbf{x}","\\mathbf{y}","\\mathbf{z}"),n=3):
    s=""
    for k,a in zip(u,v):
        if abs(a)<1e-15: continue
        s+=("-" if a<0 else ("+" if s else ""))+f"\\hat{{{k}}}\\,{tr(abs(a),n)}"
    return s or "0"

q=2e-6; u=np.array([3e5,0,0]); B=np.array([0,0,0.5]); F=q*np.cross(u,B)
add(difficulty=1,title="Force on a moving charge",
 prompt="A $2\\ \\mu\\mathrm{C}$ charge moves with $\\mathbf{u}=\\hat{\\mathbf{x}}\\,3\\times10^5\\ \\mathrm{m/s}$ through $\\mathbf{B}=\\hat{\\mathbf{z}}\\,0.5\\ \\mathrm{T}$. Find the force on it.",
 hints=["$\\mathbf{F}=q\\,\\mathbf{u}\\times\\mathbf{B}$ and $\\hat{\\mathbf{x}}\\times\\hat{\\mathbf{z}}=-\\hat{\\mathbf{y}}$."],
 steps=[D(r"\mathbf{F}=(2\times10^{-6})(3\times10^5)(0.5)\,(\hat{\mathbf{x}}\times\hat{\mathbf{z}})"),D(f"\\mathbf{{F}}={vec(F)}\\ \\mathrm{{N}}")],
 answers=[{"label":r"\mathbf{F}","value":vec(F)+r"\ \mathrm{N}"}])

F=5*np.cross([0,0,2],[0.2,0,0])
add(difficulty=1,title="Force on a current-carrying wire",
 prompt="A $2\\ \\mathrm{m}$ straight wire along $+\\hat{\\mathbf{z}}$ carries $5\\ \\mathrm{A}$ in a uniform field $\\mathbf{B}=\\hat{\\mathbf{x}}\\,0.2\\ \\mathrm{T}$. Find the force on the wire.",
 hints=["$\\mathbf{F}=I\\boldsymbol{\\ell}\\times\\mathbf{B}$ and $\\hat{\\mathbf{z}}\\times\\hat{\\mathbf{x}}=\\hat{\\mathbf{y}}$."],
 steps=[D(r"\mathbf{F}=(5)(2)(0.2)\,(\hat{\mathbf{z}}\times\hat{\mathbf{x}})"),D(f"\\mathbf{{F}}={vec(F)}\\ \\mathrm{{N}}")],
 answers=[{"label":r"\mathbf{F}","value":vec(F)+r"\ \mathrm{N}"}])

I,r=10,0.05; H=I/(2*math.pi*r)
add(difficulty=1,title="Field of a long wire",
 prompt="A long straight wire carries $10\\ \\mathrm{A}$. Find $H$ and $B$ in air $5\\ \\mathrm{cm}$ from it, and compare $B$ with Earth's field of about $50\\ \\mu\\mathrm{T}$.",
 hints=["$H=\\dfrac{I}{2\\pi r}$ and $B=\\mu_0H$."],
 steps=[D(f"H=\\frac{{10}}{{2\\pi(0.05)}}={teng(H,'A/m')}"),D(f"B=\\mu_0H={teng(MU0*H,'T')}"),f"That is {tr(100*MU0*H/50e-6)}% of Earth's field, enough to deflect a compass."],
 answers=[{"label":"H","value":teng(H,'A/m')},{"label":"B","value":teng(MU0*H,'T')}],widget="ampere")

I,L,r=2,0.5,0.2; c1=L/math.hypot(r,L); H=I/(4*math.pi*r)*2*c1
add(difficulty=2,title="Finite wire segment",
 prompt="A straight wire $1\\ \\mathrm{m}$ long carries $2\\ \\mathrm{A}$. Find $H$ at a point $20\\ \\mathrm{cm}$ from its midpoint, on the perpendicular bisector. How much does treating it as infinitely long overestimate the field?",
 hints=["$H=\\dfrac{I}{4\\pi r}(\\cos\\alpha_1-\\cos\\alpha_2)$.","By symmetry $\\cos\\alpha_1=-\\cos\\alpha_2=\\dfrac{0.5}{\\sqrt{0.5^2+0.2^2}}$."],
 steps=[D(f"\\cos\\alpha_1=\\frac{{0.5}}{{\\sqrt{{0.29}}}}={tr(c1)}"),D(f"H=\\frac{{2}}{{4\\pi(0.2)}}(2)({tr(c1)})={teng(H,'A/m')}"),D(f"H_\\infty=\\frac{{2}}{{2\\pi(0.2)}}={teng(I/(2*math.pi*r),'A/m')}"),f"The infinite-wire formula is {tr(100*(1/c1-1))}% too high here."],
 answers=[{"label":"H","value":teng(H,'A/m')},{"label":r"H_\infty","value":teng(I/(2*math.pi*r),'A/m')}],widget="biot")

I,a,z=3,0.1,0.1; H0=I/(2*a); Hz=I*a*a/(2*(a*a+z*z)**1.5)
add(difficulty=2,title="Circular loop: center and axis",
 prompt="A loop of radius $10\\ \\mathrm{cm}$ carries $3\\ \\mathrm{A}$. Find $H$ at its center and on its axis $10\\ \\mathrm{cm}$ away.",
 hints=["On the axis the radial parts of $d\\mathbf{H}$ cancel; only $H_z$ remains.",D(r"H_z=\frac{Ia^2}{2(a^2+z^2)^{3/2}}")],
 steps=[D(f"H(0)=\\frac{{I}}{{2a}}=\\frac{{3}}{{0.2}}={teng(H0,'A/m')}"),D(f"H(0.1)=\\frac{{3(0.1)^2}}{{2(0.02)^{{3/2}}}}={teng(Hz,'A/m')}"),f"At $z=a$ the field is $1/2^{{3/2}}={tr(Hz/H0)}$ of its value at the center."],
 answers=[{"label":"H(0)","value":teng(H0,'A/m')},{"label":r"H(10\ \mathrm{cm})","value":teng(Hz,'A/m')}],widget="biot")

I,w=1,0.2; d=w/2; Hs=4*I*d/(2*math.pi*d*math.hypot(d,d))
add(difficulty=3,title="Square loop at its center",
 prompt="A square loop $20\\ \\mathrm{cm}$ on a side carries $1\\ \\mathrm{A}$. Find $H$ at its center, and compare with a circular loop of the same perimeter.",
 hints=["Add four finite segments. Each is $d=10\\ \\mathrm{cm}$ from the center and runs from $-d$ to $d$ along its length.","Same perimeter: $2\\pi a=0.8\\ \\mathrm{m}$."],
 steps=[D(r"H_{\text{side}}=\frac{I}{4\pi d}\cdot2\cdot\frac{d}{\sqrt{2}\,d}=\frac{I}{2\sqrt2\,\pi d}"),D(f"H=4H_{{\\text{{side}}}}=\\frac{{\\sqrt2\\,I}}{{\\pi d}}={teng(Hs,'A/m')}"),D(f"a=\\frac{{0.8}}{{2\\pi}}={teng(0.8/(2*math.pi),'m')},\\qquad H_{{\\text{{circle}}}}=\\frac{{I}}{{2a}}={teng(I/(2*0.8/(2*math.pi)),'A/m')}")],
 answers=[{"label":r"H_{\text{square}}","value":teng(Hs,'A/m')},{"label":r"H_{\text{circle}}","value":teng(I/(2*0.8/(2*math.pi)),'A/m')}],widget="biot")

N,l,I,mr=500,0.25,2,200; n=N/l; H=n*I
add(difficulty=1,title="Long solenoid",
 prompt="A $25\\ \\mathrm{cm}$ solenoid has $500$ turns and carries $2\\ \\mathrm{A}$. Find $H$ and $B$ inside with an air core, and $B$ with an iron core of $\\mu_r=200$.",
 hints=["$H=nI$ with $n=N/\\ell$."],
 steps=[D(f"n=\\frac{{500}}{{0.25}}={tr(n,4)}\\ \\mathrm{{turns/m}},\\qquad H=nI={teng(H,'A/m')}"),D(f"B_{{\\text{{air}}}}=\\mu_0H={teng(MU0*H,'T')}"),D(f"B_{{\\text{{iron}}}}=200\\,\\mu_0H={teng(mr*MU0*H,'T')}")],
 answers=[{"label":"H","value":teng(H,'A/m')},{"label":r"B_{\text{air}}","value":teng(MU0*H,'T')},{"label":r"B_{\text{iron}}","value":teng(mr*MU0*H,'T')}],widget="biot")

I,a,b=5,1e-3,4e-3; H1=I*0.5e-3/(2*math.pi*a*a); H2=I/(2*math.pi*3e-3)
add(difficulty=2,title="Ampère's law in a coax",
 prompt="A coax has a solid inner conductor of radius $1\\ \\mathrm{mm}$ carrying $5\\ \\mathrm{A}$ (spread uniformly) and a thin outer conductor at $4\\ \\mathrm{mm}$ carrying the $5\\ \\mathrm{A}$ return. Find $H$ at $r=0.5\\ \\mathrm{mm}$, $3\\ \\mathrm{mm}$ and $6\\ \\mathrm{mm}$.",
 hints=["Use circles of radius $r$: $H(2\\pi r)=I_{\\mathrm{enc}}$.","Inside the inner conductor $I_{\\mathrm{enc}}=I\\,r^2/a^2$. Outside everything, the currents cancel."],
 steps=[D(f"r=0.5\\ \\mathrm{{mm}}:\\ H=\\frac{{Ir}}{{2\\pi a^2}}={teng(H1,'A/m')}"),D(f"r=3\\ \\mathrm{{mm}}:\\ H=\\frac{{I}}{{2\\pi r}}={teng(H2,'A/m')}"),D(r"r=6\ \mathrm{mm}:\ I_{\mathrm{enc}}=5-5=0\ \Rightarrow\ H=0"),"A coax keeps its magnetic field inside, which is why it doesn't radiate or pick up interference."],
 answers=[{"label":r"H(0.5\ \mathrm{mm})","value":teng(H1,'A/m')},{"label":r"H(3\ \mathrm{mm})","value":teng(H2,'A/m')},{"label":r"H(6\ \mathrm{mm})","value":"0"}],widget="ampere")

N,I,r=200,1,0.05; H=N*I/(2*math.pi*r)
add(difficulty=1,title="Toroid",
 prompt="A toroid has $200$ turns carrying $1\\ \\mathrm{A}$. Find $H$ inside the core at a mean radius of $5\\ \\mathrm{cm}$, and outside it.",
 hints=["A circle inside the core links the current $NI$; one outside links zero net current."],
 steps=[D(f"H(2\\pi r)=NI\\ \\Rightarrow\\ H=\\frac{{(200)(1)}}{{2\\pi(0.05)}}={teng(H,'A/m')}"),"Outside, a loop links each turn twice (going up and coming down), so $I_{\\mathrm{enc}}=0$ and $H=0$."],
 answers=[{"label":r"H_{\text{inside}}","value":teng(H,'A/m')},{"label":r"H_{\text{outside}}","value":"0"}],widget="ampere")

I1,I2,d=10,20,0.05; Fp=MU0*I1*I2/(2*math.pi*d)
add(difficulty=1,title="Force between parallel wires",
 prompt="Two long parallel wires $5\\ \\mathrm{cm}$ apart carry $10\\ \\mathrm{A}$ and $20\\ \\mathrm{A}$ in the same direction. Find the force per meter and whether it attracts or repels.",
 hints=["Wire 1 makes $B_1=\\mu_0I_1/(2\\pi d)$ at wire 2; the force per meter is $I_2B_1$."],
 steps=[D(f"F'=\\frac{{\\mu_0I_1I_2}}{{2\\pi d}}=\\frac{{(4\\pi\\times10^{{-7}})(10)(20)}}{{2\\pi(0.05)}}={teng(Fp,'N/m')}"),"Currents in the same direction attract."],
 answers=[{"label":"F'","value":teng(Fp,'N/m')+r"\ \text{(attract)}"}],widget="ampere")

N,a,l=500,0.01,0.25; A=math.pi*a*a; L=MU0*N*N*A/l; Wm=0.5*L*2**2
add(difficulty=2,title="Inductance and energy of a solenoid",
 prompt="A $25\\ \\mathrm{cm}$ air-core solenoid has $500$ turns and a radius of $1\\ \\mathrm{cm}$. Find its inductance and the energy stored at $2\\ \\mathrm{A}$.",
 hints=["$\\Phi=BA=\\mu_0nIA$ through each turn, and $L=N\\Phi/I$."],
 steps=[D(r"L=\frac{N\Phi}{I}=\frac{\mu_0N^2A}{\ell}"),D(f"L=\\frac{{(4\\pi\\times10^{{-7}})(500)^2\\pi(0.01)^2}}{{0.25}}={teng(L,'H')}"),D(f"W_m=\\tfrac12LI^2={teng(Wm,'J')}")],
 answers=[{"label":"L","value":teng(L,'H')},{"label":"W_m","value":teng(Wm,'J')}],widget="biot")

B1=np.array([1.2,0,0.4]); mr1=1000; B2=np.array([1.2/mr1,0,0.4]); t1=math.degrees(math.atan(1.2/0.4)); t2=math.degrees(math.atan(B2[0]/0.4))
add(difficulty=2,title="Flux leaving an iron surface",
 prompt="Iron ($\\mu_r=1000$) fills $z<0$ and air fills $z>0$, with no surface current. In the iron, $\\mathbf{B}=\\hat{\\mathbf{x}}\\,1.2+\\hat{\\mathbf{z}}\\,0.4\\ \\mathrm{T}$. Find $\\mathbf{B}$ in the air just above the surface and the angles from the normal.",
 hints=["Normal $B$ is continuous: $B_z$ carries over.","Tangential $H$ is continuous: $B_x/\\mu$ carries over."],
 steps=[D(r"B_{z,\text{air}}=0.4\ \mathrm{T}"),D(f"B_{{x,\\text{{air}}}}=\\mu_0\\frac{{1.2}}{{1000\\mu_0}}={teng(B2[0],'T')}"),D(f"\\mathbf{{B}}_{{\\text{{air}}}}=\\hat{{\\mathbf{{x}}}}\\,{teng(B2[0],'T')}+\\hat{{\\mathbf{{z}}}}\\,0.4\\ \\mathrm{{T}}"),D(f"\\theta_{{\\text{{iron}}}}={deg(t1)},\\qquad\\theta_{{\\text{{air}}}}={deg(t2)}"),"The flux leaves the iron almost exactly normal to its surface."],
 answers=[{"label":r"\mathbf{B}_{\text{air}}","value":f"\\hat{{\\mathbf{{x}}}}\\,{teng(B2[0],'T')}+\\hat{{\\mathbf{{z}}}}\\,0.4\\ \\mathrm{{T}}"},{"label":r"\theta_{\text{air}}","value":deg(t2)}],widget="mboundary")

add(difficulty=1,title="Can this be a magnetic field?",
 prompt="For what value of $k$ is $\\mathbf{B}=\\hat{\\mathbf{x}}\\,2x-\\hat{\\mathbf{y}}\\,y+\\hat{\\mathbf{z}}\\,kz$ a possible magnetic field?",
 hints=["Every magnetic field has $\\nabla\\cdot\\mathbf{B}=0$."],
 steps=[D(r"\nabla\cdot\mathbf{B}=2-1+k=0"),D(r"k=-1")],
 answers=[{"label":"k","value":"-1"}],widget="divcurl")

B0,a=0.2,0.05; Phi=B0*math.pi*a*a*math.cos(math.radians(30))
add(difficulty=1,title="Flux through a tilted loop",
 prompt="A circular loop of radius $5\\ \\mathrm{cm}$ sits in a uniform $\\mathbf{B}=\\hat{\\mathbf{z}}\\,0.2\\ \\mathrm{T}$, with its normal tilted $30^\\circ$ from $\\hat{\\mathbf{z}}$. Find the flux through it.",
 hints=["For a flat loop in a uniform field, $\\Phi=BA\\cos\\theta$."],
 steps=[D(f"\\Phi=(0.2)\\,\\pi(0.05)^2\\cos30^\\circ={teng(Phi,'Wb')}")],
 answers=[{"label":r"\Phi","value":teng(Phi,'Wb')}],topics=["magnetostatics","time-varying"])

write_unit("magnetostatics","Magnetostatics",C,G,P)
