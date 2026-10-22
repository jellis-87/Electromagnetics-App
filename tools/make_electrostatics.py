# Electrostatics: flashcards, glossary and practice problems.
# Every number in the steps and answers is computed here. Run: python3 tools/make_electrostatics.py
import math, os, sys
import numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lib import *
D=lambda s:"$$"+s+"$$"
deg=lambda x:f"{tr(x)}^\\circ"
EPS0=8.854187817e-12; K=1/(4*math.pi*EPS0)
T=["electrostatics"]
def vec(v,u=("\\mathbf{x}","\\mathbf{y}","\\mathbf{z}"),n=3):
    s=""
    for k,a in zip(u,v):
        if abs(a)<1e-15: continue
        s+=("-" if a<0 else ("+" if s else ""))+f"\\hat{{{k}}}\\,{int(round(abs(a))) if abs(a-round(a))<1e-9 else tr(abs(a),n)}"
    return s or "0"
def vecu(v,unit,n=3):
    """vector with a common SI prefix: (x̂ 1.2 − ŷ 3.4) nN"""
    m=max(abs(x) for x in v)
    for k,p in [(1e3,'k'),(1,''),(1e-3,'m'),(1e-6,'\\mu '),(1e-9,'n'),(1e-12,'p')]:
        if m>=k*0.9995: break
    return f"\\left({vec([x/k for x in v],n=n)}\\right)\\ \\mathrm{{{p}{unit}}}"

C=[
("Coulomb's law: force on $Q_2$ due to $Q_1$?",D(r"\mathbf{F}_{12}=\frac{Q_1Q_2}{4\pi\varepsilon R_{12}^2}\,\hat{\mathbf{R}}_{12}")+"$\\hat{\\mathbf{R}}_{12}$ points from $Q_1$ to $Q_2$. Like charges repel.","equation",T),
("Electric field of a point charge $Q$ at the origin?",D(r"\mathbf{E}=\hat{\mathbf{R}}\,\frac{Q}{4\pi\varepsilon R^2}"),"equation",T),
("Field of several point charges?","Superposition: add the vector fields of each charge."+D(r"\mathbf{E}(\mathbf{R})=\frac{1}{4\pi\varepsilon}\sum_i\frac{Q_i(\mathbf{R}-\mathbf{R}_i)}{|\mathbf{R}-\mathbf{R}_i|^3}"),"equation",T),
("Line, surface and volume charge densities, and their units?","$\\rho_l$ (C/m), $\\rho_s$ (C/m²), $\\rho_v$ (C/m³). Total charge: $Q=\\int\\rho_l\\,dl$, $\\int\\rho_s\\,ds$ or $\\int\\rho_v\\,dV$.","concept",T),
("Field of an infinite line charge $\\rho_l$?",D(r"\mathbf{E}=\hat{\mathbf{r}}\,\frac{\rho_l}{2\pi\varepsilon r}")+"It falls off as $1/r$, not $1/r^2$.","equation",T),
("Field of an infinite sheet of charge $\\rho_s$?",D(r"\mathbf{E}=\hat{\mathbf{n}}\,\frac{\rho_s}{2\varepsilon}")+"Uniform, pointing away from the sheet on both sides.","equation",T),
("Field on the axis of a ring of charge (radius $a$, height $z$)?",D(r"\mathbf{E}=\hat{\mathbf{z}}\,\frac{\rho_l\,a\,z}{2\varepsilon\,(a^2+z^2)^{3/2}}")+"The radial parts cancel by symmetry.","equation",T),
("Gauss's law, integral form?",D(r"\oint_S\mathbf{D}\cdot d\mathbf{s}=Q_{\mathrm{enc}}"),"equation",T),
("Gauss's law, differential form?",D(r"\nabla\cdot\mathbf{D}=\rho_v"),"equation",T),
("When is Gauss's law useful for finding $\\mathbf{E}$?","When symmetry makes $|\\mathbf{D}|$ constant and normal on a closed surface: spheres for point and spherical charges, cylinders for line charges, pillboxes for sheets.","concept",T),
("Field inside a charged conducting shell or sphere?","Zero. Charge on a conductor sits on its surface, and the static field inside the conductor is zero.","concept",T),
("Electric potential difference from $A$ to $B$?",D(r"V_{BA}=V_B-V_A=-\int_A^B\mathbf{E}\cdot d\mathbf{l}")+"It does not depend on the path.","equation",T),
("How do you get $\\mathbf{E}$ from $V$?",D(r"\mathbf{E}=-\nabla V")+"$\\mathbf{E}$ points downhill in potential.","equation",T),
("Potential of a point charge (zero at infinity)?",D(r"V=\frac{Q}{4\pi\varepsilon R}"),"equation",T),
("Why is the static electric field conservative?",D(r"\oint_C\mathbf{E}\cdot d\mathbf{l}=0,\qquad\nabla\times\mathbf{E}=0")+"The work around any closed loop is zero.","equation",T),
("Poisson's and Laplace's equations?",D(r"\nabla^2V=-\frac{\rho_v}{\varepsilon}\qquad\nabla^2V=0\ \text{(no charge)}"),"equation",T),
("How are equipotential surfaces related to field lines?","They are perpendicular everywhere. Moving along an equipotential takes no work.","concept",T),
("Work to move charge $q$ from $A$ to $B$?",D(r"W=q\,(V_B-V_A)"),"equation",T),
("Boundary condition on tangential $\\mathbf{E}$?",D(r"E_{1t}=E_{2t}")+"Tangential $\\mathbf{E}$ is continuous across any boundary.","equation",T),
("Boundary condition on normal $\\mathbf{D}$?",D(r"\hat{\mathbf{n}}_2\cdot(\mathbf{D}_1-\mathbf{D}_2)=\rho_s")+"$\\hat{\\mathbf{n}}_2$ points from medium 2 into medium 1. With no surface charge, $\\varepsilon_1E_{1n}=\\varepsilon_2E_{2n}$.","equation",T),
("Fields at the surface of a conductor?","Tangential $\\mathbf{E}$ is zero, and $\\mathbf{E}$ just outside is normal:"+D(r"D_n=\varepsilon E_n=\rho_s"),"concept",T),
("Refraction of $\\mathbf{E}$ at a charge-free dielectric boundary?",D(r"\frac{\tan\theta_1}{\tan\theta_2}=\frac{\varepsilon_1}{\varepsilon_2}")+"Angles are measured from the normal.","equation",T),
("Definition of capacitance?",D(r"C=\frac{Q}{V}")+"It depends only on geometry and material, not on $Q$ or $V$.","equation",T),
("Parallel-plate capacitor?",D(r"C=\frac{\varepsilon A}{d}"),"equation",T),
("Coaxial capacitance per unit length?",D(r"C'=\frac{2\pi\varepsilon}{\ln(b/a)}"),"equation",T),
("Energy stored in a capacitor, and the energy density of the field?",D(r"W_e=\tfrac12CV^2,\qquad w_e=\tfrac12\varepsilon E^2"),"equation",T),
("What happens when $E$ exceeds the dielectric strength?","The material breaks down and conducts (an arc or spark). For air it is about $3\\ \\mathrm{MV/m}$.","concept",T),
("Recipe for capacitance from fields?","Assume $\\pm Q$ on the conductors, find $\\mathbf{E}$ (Gauss's law), integrate to get $V$, then $C=Q/V$.","concept",T),
]

G=[
("Coulomb's law","","","The force between two point charges: proportional to the product of the charges and inversely proportional to the square of their separation.","charges",T),
("Point charge","Q","\\mathrm{C}","A charge whose size is negligible compared with the distances of interest.","charges",T),
("Line charge density","\\rho_l","\\mathrm{C/m}","Charge per unit length along a wire or edge.","gauss",T),
("Surface charge density","\\rho_s","\\mathrm{C/m^2}","Charge per unit area on a sheet or conductor surface.","gauss",T),
("Volume charge density","\\rho_v","\\mathrm{C/m^3}","Charge per unit volume in a region.","gauss",T),
("Superposition","","","In linear media the total field is the vector sum of the fields of each charge acting alone.","charges",T),
("Gauss's law","","","The outward flux of $\\mathbf{D}$ through any closed surface equals the free charge enclosed: $\\oint\\mathbf{D}\\cdot d\\mathbf{s}=Q_{\\mathrm{enc}}$.","gauss",T),
("Gaussian surface","","","An imaginary closed surface chosen so that $\\mathbf{D}$ is constant and normal on it, which turns Gauss's law into simple algebra.","gauss",T),
("Electric potential","V","\\mathrm{V}","Work per unit charge to bring a test charge from the reference point (usually infinity) to a point: $V=-\\int_\\infty^P\\mathbf{E}\\cdot d\\mathbf{l}$.","charges",T),
("Equipotential surface","","","A surface on which $V$ is constant. Field lines cross it at right angles.","charges",T),
("Electric field line","","","A curve that follows the direction of $\\mathbf{E}$. Lines start on positive charge and end on negative charge.","charges",T),
("Electric dipole","\\mathbf{p}=Q\\mathbf{d}","\\mathrm{C\\,m}","Equal and opposite charges a small distance apart. Far away its potential falls as $1/R^2$ and its field as $1/R^3$.","charges",T),
("Poisson's equation","","","$\\nabla^2V=-\\rho_v/\\varepsilon$. Reduces to Laplace's equation, $\\nabla^2V=0$, where there is no charge.",None,T),
("Conductor","","","A material with free charges. In electrostatics its interior field is zero, its surface is an equipotential, and any net charge sits on the surface.",None,T),
("Dielectric","","","An insulator whose molecules polarize in an applied field, which reduces the field for a given free charge. Described by $\\varepsilon_r>1$.","boundary",T),
("Polarization","\\mathbf{P}","\\mathrm{C/m^2}","Dipole moment per unit volume in a dielectric: $\\mathbf{D}=\\varepsilon_0\\mathbf{E}+\\mathbf{P}$.","boundary",T),
("Dielectric strength","E_{ds}","\\mathrm{V/m}","The largest field a material can take before it breaks down. Air: about $3\\ \\mathrm{MV/m}$.","capacitor",T),
("Electrostatic boundary conditions","","","Tangential $\\mathbf{E}$ is continuous; normal $\\mathbf{D}$ jumps by the surface charge $\\rho_s$. At a conductor, $E_t=0$ and $D_n=\\rho_s$.","boundary",T),
("Capacitance","C","\\mathrm{F}","Charge stored per volt between two conductors: $C=Q/V$.","capacitor",T),
("Electrostatic energy","W_e","\\mathrm{J}","Energy stored in the field: $W_e=\\tfrac12\\int_V\\varepsilon E^2\\,dV=\\tfrac12CV^2$.","capacitor",T),
("Image method","","","Replaces a grounded conducting plane with a mirror-image charge of opposite sign, which gives the same field above the plane.","charges",T),
]

P=[]
def add(**k): k.setdefault("source","original"); k.setdefault("topics",T); P.append(k)

Q1,Q2=2e-9,-5e-9; R1=np.array([1,2,0]); R2=np.array([-1,0,2]); R12=R2-R1; d=np.linalg.norm(R12); F=K*Q1*Q2*R12/d**3
add(difficulty=2,title="Force between two point charges",
 prompt="A $2\\ \\mathrm{nC}$ charge sits at $(1,2,0)$ and a $-5\\ \\mathrm{nC}$ charge at $(-1,0,2)$, in meters, in free space. Find the force on the $-5\\ \\mathrm{nC}$ charge.",
 hints=["$\\mathbf{R}_{12}$ points from $Q_1$ to $Q_2$.","$\\mathbf{F}_{12}=\\dfrac{Q_1Q_2}{4\\pi\\varepsilon_0}\\dfrac{\\mathbf{R}_{12}}{|\\mathbf{R}_{12}|^3}$."],
 steps=[D(f"\\mathbf{{R}}_{{12}}=\\mathbf{{R}}_2-\\mathbf{{R}}_1={vec(R12)},\\quad |\\mathbf{{R}}_{{12}}|=\\sqrt{{12}}={tr(d)}\\ \\mathrm{{m}}"),
        D(f"\\frac{{Q_1Q_2}}{{4\\pi\\varepsilon_0|\\mathbf{{R}}_{{12}}|^3}}=\\frac{{(8.99\\times10^9)(2\\times10^{{-9}})(-5\\times10^{{-9}})}}{{{tr(d**3)}}}={tsci(K*Q1*Q2/d**3,'N/m')}"),
        D(f"\\mathbf{{F}}_{{12}}={vecu(F,'N')}"),"The charges have opposite signs, so the force on $Q_2$ points back toward $Q_1$."],
 answers=[{"label":r"\mathbf{F}_{12}","value":vecu(F,'N')},{"label":r"|\mathbf{F}_{12}|","value":teng(np.linalg.norm(F),'N')}],widget="charges")

Qa,Qb=4e-9,-4e-9; Pa=np.array([-0.1,0,0]); Pb=np.array([0.1,0,0]); Pp=np.array([0,0.1,0])
Ea=K*Qa*(Pp-Pa)/np.linalg.norm(Pp-Pa)**3; Eb=K*Qb*(Pp-Pb)/np.linalg.norm(Pp-Pb)**3; E=Ea+Eb
Va=K*Qa/np.linalg.norm(Pp-Pa); Vb=K*Qb/np.linalg.norm(Pp-Pb)
add(difficulty=2,title="Field and potential of a dipole pair",
 prompt="Charges $+4\\ \\mathrm{nC}$ at $(-10,0,0)\\ \\mathrm{cm}$ and $-4\\ \\mathrm{nC}$ at $(10,0,0)\\ \\mathrm{cm}$ sit in free space. Find $\\mathbf{E}$ and $V$ at $(0,10,0)\\ \\mathrm{cm}$.",
 hints=["Add the two fields as vectors.","Potential is a scalar: just add the two potentials."],
 steps=[D(f"\\mathbf{{R}}-\\mathbf{{R}}_+={vec((Pp-Pa)*100)}\\ \\mathrm{{cm}},\\quad\\mathbf{{R}}-\\mathbf{{R}}_-={vec((Pp-Pb)*100)}\\ \\mathrm{{cm}}"),
        D(f"\\mathbf{{E}}_+={vecu(Ea,'V/m')}"),D(f"\\mathbf{{E}}_-={vecu(Eb,'V/m')}"),D(f"\\mathbf{{E}}={vecu(E,'V/m')}"),
        D(f"V=\\frac{{1}}{{4\\pi\\varepsilon_0}}\\left(\\frac{{4\\ \\mathrm{{nC}}}}{{{tr(np.linalg.norm(Pp-Pa))}}}-\\frac{{4\\ \\mathrm{{nC}}}}{{{tr(np.linalg.norm(Pp-Pb))}}}\\right)=0"),"The point is the same distance from both charges, so $V=0$ there even though $\\mathbf{E}\\ne0$."],
 answers=[{"label":r"\mathbf{E}","value":vecu(E,'V/m')},{"label":"V","value":"0"}],widget="charges")
assert abs(Va+Vb)<1e-9

rl,a,z=5e-9,0.1,0.2; Ez=rl*a*z/(2*EPS0*(a*a+z*z)**1.5)
add(difficulty=2,title="Ring of charge, on the axis",
 prompt="A ring of radius $10\\ \\mathrm{cm}$ in the $xy$-plane carries $\\rho_l=5\\ \\mathrm{nC/m}$. Find $\\mathbf{E}$ on the axis at $z=20\\ \\mathrm{cm}$.",
 hints=["By symmetry only $E_z$ survives.",D(r"dE_z=\frac{\rho_l\,a\,d\phi}{4\pi\varepsilon_0(a^2+z^2)}\cdot\frac{z}{\sqrt{a^2+z^2}}")],
 steps=[D(r"E_z=\int_0^{2\pi}\frac{\rho_l\,a\,z\,d\phi}{4\pi\varepsilon_0(a^2+z^2)^{3/2}}=\frac{\rho_l\,a\,z}{2\varepsilon_0(a^2+z^2)^{3/2}}"),
        D(f"E_z=\\frac{{(5\\times10^{{-9}})(0.1)(0.2)}}{{2\\varepsilon_0(0.05)^{{3/2}}}}={teng(Ez,'V/m')}")],
 answers=[{"label":r"\mathbf{E}","value":f"\\hat{{\\mathbf{{z}}}}\\,{teng(Ez,'V/m')}"}])

rs,a,z=1e-6,0.2,0.1; Ed=rs/(2*EPS0)*(1-z/math.sqrt(z*z+a*a))
add(difficulty=3,title="Charged disk, on the axis",
 prompt="A disk of radius $20\\ \\mathrm{cm}$ carries $\\rho_s=1\\ \\mu\\mathrm{C/m^2}$. Find $E$ on its axis $10\\ \\mathrm{cm}$ above the center, and compare with an infinite sheet.",
 hints=["Build the disk from rings of radius $r$ and width $dr$, each with $\\rho_l=\\rho_s\\,dr$.","Use the ring result and integrate from $0$ to $a$."],
 steps=[D(r"E_z=\int_0^a\frac{\rho_s\,r\,z\,dr}{2\varepsilon_0(r^2+z^2)^{3/2}}=\frac{\rho_s}{2\varepsilon_0}\left(1-\frac{z}{\sqrt{z^2+a^2}}\right)"),
        D(f"E_z=\\frac{{10^{{-6}}}}{{2\\varepsilon_0}}\\left(1-\\frac{{0.1}}{{{tr(math.sqrt(z*z+a*a))}}}\\right)={teng(Ed,'V/m')}"),
        D(f"\\text{{Infinite sheet: }}\\frac{{\\rho_s}}{{2\\varepsilon_0}}={teng(rs/(2*EPS0),'V/m')}"),f"The disk gives {tr(100*Ed/(rs/(2*EPS0)))}% of the sheet value at this height. Close in, $z\\ll a$, they agree."],
 answers=[{"label":"E_z","value":teng(Ed,'V/m')},{"label":r"E_{\text{sheet}}","value":teng(rs/(2*EPS0),'V/m')}])

rl,r=10e-9,0.5; El=rl/(2*math.pi*EPS0*r)
add(difficulty=1,title="Gauss's law for a line charge",
 prompt="Use Gauss's law to find $\\mathbf{E}$ a distance $r$ from an infinite line charge $\\rho_l$, then evaluate it for $\\rho_l=10\\ \\mathrm{nC/m}$ and $r=50\\ \\mathrm{cm}$ in air.",
 hints=["Use a cylinder of radius $r$ and length $\\ell$ around the line. No flux leaves the flat ends."],
 steps=[D(r"\oint\mathbf{D}\cdot d\mathbf{s}=D_r(2\pi r\ell)=\rho_l\ell"),D(r"\mathbf{E}=\hat{\mathbf{r}}\,\frac{\rho_l}{2\pi\varepsilon_0r}"),D(f"E=\\frac{{10\\times10^{{-9}}}}{{2\\pi\\varepsilon_0(0.5)}}={teng(El,'V/m')}")],
 answers=[{"label":r"\mathbf{E}","value":r"\hat{\mathbf{r}}\,\frac{\rho_l}{2\pi\varepsilon_0r}"},{"label":"E","value":teng(El,'V/m')}],widget="gauss")

rv,a=2e-6,0.05; Ein=lambda r:rv*r/(3*EPS0); Eout=lambda r:rv*a**3/(3*EPS0*r*r); Q=rv*4/3*math.pi*a**3
add(difficulty=2,title="Gauss's law for a charged sphere",
 prompt="A sphere of radius $5\\ \\mathrm{cm}$ holds a uniform $\\rho_v=2\\ \\mu\\mathrm{C/m^3}$ in free space. Find $E$ at $R=2\\ \\mathrm{cm}$ and at $R=10\\ \\mathrm{cm}$.",
 hints=["Use a spherical Gaussian surface of radius $R$.","Inside, only the charge within radius $R$ counts."],
 steps=[D(r"\text{Inside: }D_R(4\pi R^2)=\rho_v\tfrac43\pi R^3\ \Rightarrow\ E=\frac{\rho_vR}{3\varepsilon_0}"),D(f"E(2\\ \\mathrm{{cm}})={teng(Ein(0.02),'V/m')}"),
        D(r"\text{Outside: }D_R(4\pi R^2)=\rho_v\tfrac43\pi a^3\ \Rightarrow\ E=\frac{\rho_va^3}{3\varepsilon_0R^2}"),D(f"E(10\\ \\mathrm{{cm}})={teng(Eout(0.1),'V/m')}"),
        f"Total charge ${teng(Q,'C')}$. Outside, the sphere looks like a point charge."],
 answers=[{"label":r"E(2\ \mathrm{cm})","value":teng(Ein(0.02),'V/m')},{"label":r"E(10\ \mathrm{cm})","value":teng(Eout(0.1),'V/m')}],widget="gauss")

add(difficulty=1,title="Charge density from D",
 prompt="In a region, $\\mathbf{D}=\\hat{\\mathbf{x}}\\,2xy+\\hat{\\mathbf{y}}\\,x^2+\\hat{\\mathbf{z}}\\,3z^2\\ \\mathrm{C/m^2}$. Find $\\rho_v$ at $(1,2,3)$.",
 hints=["$\\rho_v=\\nabla\\cdot\\mathbf{D}$."],
 steps=[D(r"\rho_v=\frac{\partial(2xy)}{\partial x}+\frac{\partial(x^2)}{\partial y}+\frac{\partial(3z^2)}{\partial z}=2y+6z"),D(r"\rho_v(1,2,3)=4+18=22\ \mathrm{C/m^3}")],
 answers=[{"label":r"\rho_v","value":r"22\ \mathrm{C/m^3}"}])

gV=np.array([20*1*2,10*1,-5])
add(difficulty=1,title="Electric field from potential",
 prompt="Given $V=10x^2y-5z\\ \\mathrm{V}$, find $\\mathbf{E}$ at $(1,2,3)\\ \\mathrm{m}$.",
 hints=["$\\mathbf{E}=-\\nabla V$."],
 steps=[D(r"\nabla V=\hat{\mathbf{x}}\,20xy+\hat{\mathbf{y}}\,10x^2-\hat{\mathbf{z}}\,5"),D(f"\\mathbf{{E}}=-\\nabla V={vec(-gV)}\\ \\mathrm{{V/m}}")],
 answers=[{"label":r"\mathbf{E}","value":vec(-gV)+r"\ \mathrm{V/m}"}],widget="charges")

Q=3e-9; VA=K*Q/0.2; VB=K*Q/0.05; q=-2e-9; W=q*(VB-VA)
add(difficulty=2,title="Work to move a charge",
 prompt="How much work does it take to move a $-2\\ \\mathrm{nC}$ charge from $20\\ \\mathrm{cm}$ to $5\\ \\mathrm{cm}$ away from a fixed $3\\ \\mathrm{nC}$ charge in air?",
 hints=["$W=q(V_B-V_A)$, with $V=\\dfrac{Q}{4\\pi\\varepsilon_0R}$."],
 steps=[D(f"V_A=\\frac{{Q}}{{4\\pi\\varepsilon_0(0.2)}}={teng(VA,'V')},\\qquad V_B=\\frac{{Q}}{{4\\pi\\varepsilon_0(0.05)}}={teng(VB,'V')}"),D(f"W=q(V_B-V_A)=(-2\\times10^{{-9}})({tr(VB-VA)})={teng(W,'J')}"),"The work is negative: the charges attract, so the field does the work as the charge moves in."],
 answers=[{"label":"W","value":teng(W,'J')}],widget="charges")

E1=np.array([2,-3,5]); e1,e2=2,8; E2=np.array([2,-3,e1*5/e2]); t1=math.degrees(math.atan(math.hypot(2,3)/5)); t2=math.degrees(math.atan(math.hypot(2,3)/E2[2]))
add(difficulty=2,title="Field across a dielectric boundary",
 prompt=f"The plane $z=0$ separates medium 1 ($z>0$, $\\varepsilon_{{r1}}=2$) from medium 2 ($z<0$, $\\varepsilon_{{r2}}=8$). There is no surface charge. If $\\mathbf{{E}}_1={vec(E1)}\\ \\mathrm{{V/m}}$, find $\\mathbf{{E}}_2$ and the angles both make with the normal.",
 hints=["Tangential components ($x$ and $y$) carry over unchanged.","Normal $\\mathbf{D}$ is continuous: $\\varepsilon_{r1}E_{1z}=\\varepsilon_{r2}E_{2z}$."],
 steps=[D(r"E_{2x}=2,\qquad E_{2y}=-3"),D(f"E_{{2z}}=\\frac{{\\varepsilon_{{r1}}}}{{\\varepsilon_{{r2}}}}E_{{1z}}=\\frac{{2}}{{8}}(5)={tr(E2[2])}"),D(f"\\mathbf{{E}}_2={vec(E2)}\\ \\mathrm{{V/m}}"),
        D(f"\\theta_1=\\tan^{{-1}}\\frac{{\\sqrt{{13}}}}{{5}}={deg(t1)},\\qquad\\theta_2=\\tan^{{-1}}\\frac{{\\sqrt{{13}}}}{{{tr(E2[2])}}}={deg(t2)}"),"The field bends away from the normal going into the higher-permittivity medium."],
 answers=[{"label":r"\mathbf{E}_2","value":vec(E2)+r"\ \mathrm{V/m}"},{"label":r"\theta_1","value":deg(t1)},{"label":r"\theta_2","value":deg(t2)}],widget="boundary")

En=500; rs=EPS0*En
add(difficulty=1,title="Surface charge on a conductor",
 prompt="Just outside a charged conductor in air the field is $500\\ \\mathrm{V/m}$, pointing away from the surface. Find the surface charge density, and the field inside the conductor.",
 hints=["At a conductor surface $D_n=\\rho_s$, and $\\mathbf{E}=0$ inside."],
 steps=[D(f"\\rho_s=\\varepsilon_0E_n=(8.854\\times10^{{-12}})(500)={teng(rs,'C/m^2')}"),"Inside the conductor $\\mathbf{E}=0$."],
 answers=[{"label":r"\rho_s","value":teng(rs,'C/m^2')},{"label":r"E_{\text{inside}}","value":"0"}],widget="boundary")

A,d,er,V0=4e-4,0.5e-3,4,10; Cp=er*EPS0*A/d; Qp=Cp*V0; We=0.5*Cp*V0**2; Ep=V0/d
add(difficulty=1,title="Parallel-plate capacitor",
 prompt="A capacitor has plates of area $4\\ \\mathrm{cm^2}$ spaced $0.5\\ \\mathrm{mm}$ apart, filled with a dielectric of $\\varepsilon_r=4$. With $10\\ \\mathrm{V}$ across it, find $C$, $Q$, $E$ and the stored energy.",
 hints=["$C=\\varepsilon A/d$, $Q=CV$, $E=V/d$, $W_e=\\tfrac12CV^2$."],
 steps=[D(f"C=\\frac{{(4)(8.854\\times10^{{-12}})(4\\times10^{{-4}})}}{{5\\times10^{{-4}}}}={teng(Cp,'F')}"),D(f"Q=CV={teng(Qp,'C')}"),D(f"E=\\frac{{V}}{{d}}={teng(Ep,'V/m')}"),D(f"W_e=\\tfrac12CV^2={teng(We,'J')}")],
 answers=[{"label":"C","value":teng(Cp,'F')},{"label":"Q","value":teng(Qp,'C')},{"label":"E","value":teng(Ep,'V/m')},{"label":"W_e","value":teng(We,'J')}],widget="capacitor")

a,b,er=0.5e-3,2e-3,2.25; Cc=2*math.pi*er*EPS0/math.log(b/a)
add(difficulty=2,title="Capacitance of a coax",
 prompt="Find the capacitance per meter of a coax with inner radius $0.5\\ \\mathrm{mm}$, outer radius $2\\ \\mathrm{mm}$ and polyethylene ($\\varepsilon_r=2.25$) between.",
 hints=["Put $\\rho_l$ on the inner conductor and use Gauss's law: $E_r=\\dfrac{\\rho_l}{2\\pi\\varepsilon r}$.","Integrate $E_r$ from $a$ to $b$ for $V$, then $C'=\\rho_l/V$."],
 steps=[D(r"V=\int_a^b\frac{\rho_l}{2\pi\varepsilon r}\,dr=\frac{\rho_l}{2\pi\varepsilon}\ln\frac{b}{a}"),D(r"C'=\frac{\rho_l}{V}=\frac{2\pi\varepsilon}{\ln(b/a)}"),D(f"C'=\\frac{{2\\pi(2.25)\\varepsilon_0}}{{\\ln4}}={teng(Cc,'F/m')}")],
 answers=[{"label":"C'","value":teng(Cc,'F/m')}],widget="capacitor",topics=["electrostatics","tline"])

a,b=0.05,0.1; Cs=4*math.pi*EPS0*a*b/(b-a)
add(difficulty=2,title="Spherical capacitor",
 prompt="Find the capacitance of two concentric conducting spheres of radii $5\\ \\mathrm{cm}$ and $10\\ \\mathrm{cm}$ with air between.",
 hints=["Put $+Q$ on the inner sphere; between the spheres $E_R=\\dfrac{Q}{4\\pi\\varepsilon_0R^2}$."],
 steps=[D(r"V=\int_a^b\frac{Q}{4\pi\varepsilon_0R^2}\,dR=\frac{Q}{4\pi\varepsilon_0}\left(\frac1a-\frac1b\right)"),D(r"C=\frac{Q}{V}=\frac{4\pi\varepsilon_0ab}{b-a}"),D(f"C=\\frac{{4\\pi\\varepsilon_0(0.05)(0.1)}}{{0.05}}={teng(Cs,'F')}")],
 answers=[{"label":"C","value":teng(Cs,'F')}],widget="capacitor")

d,V0=2e-3,12; Ef=V0/d
add(difficulty=2,title="Laplace's equation between plates",
 prompt="Two large plates sit at $z=0$ ($V=0$) and $z=2\\ \\mathrm{mm}$ ($V=12\\ \\mathrm{V}$), with no charge between. Solve Laplace's equation for $V(z)$ and find $\\mathbf{E}$.",
 hints=["With no $x$ or $y$ variation, $\\dfrac{d^2V}{dz^2}=0$, so $V=Az+B$."],
 steps=[D(r"\frac{d^2V}{dz^2}=0\ \Rightarrow\ V=Az+B"),D(r"V(0)=0\Rightarrow B=0,\qquad V(d)=12\Rightarrow A=\frac{12}{0.002}=6000"),D(f"V(z)=6000\\,z\\ \\mathrm{{V}},\\qquad \\mathbf{{E}}=-\\nabla V=-\\hat{{\\mathbf{{z}}}}\\,{teng(Ef,'V/m')}")],
 answers=[{"label":"V(z)","value":r"6000\,z\ \mathrm{V}"},{"label":r"\mathbf{E}","value":f"-\\hat{{\\mathbf{{z}}}}\\,{teng(Ef,'V/m')}"}],widget="capacitor")

Ebd=3e6; dmin=1000/Ebd
add(difficulty=1,title="Breakdown in an air gap",
 prompt="Air breaks down at about $3\\ \\mathrm{MV/m}$. What is the smallest gap between two parallel plates that can hold off $1\\ \\mathrm{kV}$?",
 hints=["$E=V/d$ between parallel plates."],
 steps=[D(f"d=\\frac{{V}}{{E_{{ds}}}}=\\frac{{1000}}{{3\\times10^6}}={teng(dmin,'m')}")],
 answers=[{"label":r"d_{\min}","value":teng(dmin,'m')}],widget="capacitor")

write_unit("electrostatics","Electrostatics",C,G,P)
