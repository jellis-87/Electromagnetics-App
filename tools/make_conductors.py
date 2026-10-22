# Current and conductors: flashcards, glossary and practice problems.
# Every number in the steps and answers is computed here. Run: python3 tools/make_conductors.py
import math, os, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lib import *
D=lambda s:"$$"+s+"$$"
EPS0=8.854187817e-12; QE=1.602176634e-19
T=["conductors"]

C=[
("Current through a surface from the current density?",D(r"I=\int_S\mathbf{J}\cdot d\mathbf{s}")+"$\\mathbf{J}$ is in A/m².","equation",T),
("Point form of Ohm's law?",D(r"\mathbf{J}=\sigma\mathbf{E}"),"equation",T),
("Current density from moving charge?",D(r"\mathbf{J}=\rho_v\mathbf{u}")+"$\\rho_v$ is the moving charge density and $\\mathbf{u}$ its velocity.","equation",T),
("Conduction versus convection current?","Conduction current flows in a conductor and obeys $\\mathbf{J}=\\sigma\\mathbf{E}$. Convection current is charge carried through space, such as an electron beam, and does not.","concept",T),
("Conductivity from carrier densities and mobilities?",D(r"\sigma=-\rho_{ve}\mu_e+\rho_{vh}\mu_h=q(N_e\mu_e+N_h\mu_h)")+"In a metal only electrons matter.","equation",T),
("Drift velocity of electrons in a field $\\mathbf{E}$?",D(r"\mathbf{u}_e=-\mu_e\mathbf{E}")+"Opposite to $\\mathbf{E}$, and very slow: millimeters per second or less in a metal wire.","equation",T),
("Resistance of a uniform conductor?",D(r"R=\frac{\ell}{\sigma A}"),"equation",T),
("Resistance of any shape from fields?",D(r"R=\frac{V}{I}=\frac{-\int_l\mathbf{E}\cdot d\mathbf{l}}{\int_S\sigma\mathbf{E}\cdot d\mathbf{s}}"),"equation",T),
("Power dissipated in a conductor (Joule's law)?",D(r"P=\int_V\mathbf{E}\cdot\mathbf{J}\,dV=I^2R"),"equation",T),
("Charge continuity equation?",D(r"\nabla\cdot\mathbf{J}=-\frac{\partial\rho_v}{\partial t}")+"Current leaving a point drains its charge. In steady state $\\nabla\\cdot\\mathbf{J}=0$, which is Kirchhoff's current law.","equation",T),
("Conductivity of copper, and how it compares to seawater and glass?","Copper: about $5.8\\times10^7$ S/m. Seawater: about 4 S/m. Glass: about $10^{-12}$ S/m.","concept",T),
("What is a perfect conductor?","$\\sigma\\to\\infty$. The field inside is zero, so it is an equipotential, and current flows only on its surface.","concept",T),
("Boundary condition on $\\mathbf{J}$ between two conductors?","Normal $\\mathbf{J}$ is continuous (steady state): $J_{1n}=J_{2n}$. Tangential $\\mathbf{E}$ is continuous, so $\\dfrac{J_{1t}}{\\sigma_1}=\\dfrac{J_{2t}}{\\sigma_2}$.","concept",T),
("Why doesn't a static field exist inside a conductor?","Free charges move until their own field cancels the applied field. In a good conductor this takes far less than a nanosecond.","concept",T),
]

G=[
("Current density","\\mathbf{J}","\\mathrm{A/m^2}","Current per unit area, pointing in the direction positive charge flows. $I=\\int\\mathbf{J}\\cdot d\\mathbf{s}$.","wire",T),
("Conductivity","\\sigma","\\mathrm{S/m}","How readily a material conducts: $\\mathbf{J}=\\sigma\\mathbf{E}$. Its reciprocal is resistivity.","wire",T),
("Resistivity","\\rho=1/\\sigma","\\Omega\\,\\mathrm{m}","Resistance of a 1 m cube of the material. Copper: $1.72\\times10^{-8}\\ \\Omega\\,\\mathrm{m}$.","wire",T),
("Mobility","\\mu_e,\\ \\mu_h","\\mathrm{m^2/(V\\,s)}","Drift speed per unit field for electrons or holes.","wire",T),
("Drift velocity","\\mathbf{u}","\\mathrm{m/s}","The average velocity of charge carriers in a field, on top of their fast random thermal motion.","wire",T),
("Conduction current","","","Current due to charges drifting through a conductor under an applied field, $\\mathbf{J}=\\sigma\\mathbf{E}$.","wire",T),
("Convection current","","","Current due to charge moving through a region without a conductor, such as an electron beam: $\\mathbf{J}=\\rho_v\\mathbf{u}$.",None,T),
("Resistance","R","\\Omega","Voltage across a conductor divided by current through it. For a uniform bar, $R=\\ell/(\\sigma A)$.","wire",T),
("Joule's law","","","Power turned into heat in a conductor: $P=\\int\\mathbf{E}\\cdot\\mathbf{J}\\,dV$, which is $I^2R$ for a resistor.","wire",T),
("Continuity equation","","","Conservation of charge in point form: $\\nabla\\cdot\\mathbf{J}=-\\partial\\rho_v/\\partial t$.",None,T),
("Semiconductor","","","A material with conductivity between conductors and insulators, set by electron and hole densities that doping and temperature control.","wire",T),
]

P=[]
def add(**k): k.setdefault("source","original"); k.setdefault("topics",T); P.append(k)

s=5.8e7; d=1e-3; L=100; A=math.pi*(d/2)**2; R=L/(s*A)
add(difficulty=1,title="Resistance of a copper wire",
 prompt="Find the resistance of $100\\ \\mathrm{m}$ of copper wire ($\\sigma=5.8\\times10^7\\ \\mathrm{S/m}$) with a diameter of $1\\ \\mathrm{mm}$.",
 hints=["$R=\\dfrac{\\ell}{\\sigma A}$ with $A=\\pi r^2$."],
 steps=[D(f"A=\\pi(0.5\\times10^{{-3}})^2={tsci(A,'m^2')}"),D(f"R=\\frac{{100}}{{(5.8\\times10^7)({tsci(A)})}}={teng(R,'Ω')}")],
 answers=[{"label":"R","value":teng(R,'Ω')}],widget="wire")

I=2; s=3.5e7; d=2e-3; A=math.pi*(d/2)**2; J=I/A; E=J/s; V=E*1000
add(difficulty=1,title="Current density and field in a wire",
 prompt="An aluminum wire ($\\sigma=3.5\\times10^7\\ \\mathrm{S/m}$, diameter $2\\ \\mathrm{mm}$) carries $2\\ \\mathrm{A}$. Find $J$, the field $E$ inside it, and the voltage drop along $1\\ \\mathrm{km}$.",
 hints=["$J=I/A$, then $E=J/\\sigma$, then $V=E\\ell$."],
 steps=[D(f"J=\\frac{{2}}{{\\pi(10^{{-3}})^2}}={teng(J,'A/m^2')}"),D(f"E=\\frac{{J}}{{\\sigma}}={teng(E,'V/m')}"),D(f"V=E\\ell=({tsci(E)})(1000)={teng(V,'V')}")],
 answers=[{"label":"J","value":teng(J,'A/m^2')},{"label":"E","value":teng(E,'V/m')},{"label":"V","value":teng(V,'V')}],widget="wire")

N=8.5e28; A=1e-6; u=1/(N*QE*A)
add(difficulty=2,title="How fast do the electrons move?",
 prompt="A copper wire with a $1\\ \\mathrm{mm^2}$ cross-section carries $1\\ \\mathrm{A}$. Copper has about $8.5\\times10^{28}$ free electrons per cubic meter. Find the drift speed.",
 hints=["$J=\\rho_vu=Nqu$."],
 steps=[D(r"J=\frac{I}{A}=\frac{1}{10^{-6}}=10^6\ \mathrm{A/m^2}"),D(f"u=\\frac{{J}}{{Nq}}=\\frac{{10^6}}{{(8.5\\times10^{{28}})(1.602\\times10^{{-19}})}}={teng(u,'m/s')}"),f"That is about ${tr(u*3600*1000)}\\ \\mathrm{{mm}}$ per hour. The signal travels near the speed of light, but the electrons themselves crawl."],
 answers=[{"label":"u","value":teng(u,'m/s')}],widget="wire")

J0=2e6; a=1e-3; I=2*math.pi*J0*a*a/6
add(difficulty=2,title="Current from a nonuniform current density",
 prompt="In a wire of radius $a=1\\ \\mathrm{mm}$, $\\mathbf{J}=\\hat{\\mathbf{z}}\\,J_0\\left(1-\\dfrac{r}{a}\\right)$ with $J_0=2\\times10^6\\ \\mathrm{A/m^2}$. Find the total current.",
 hints=["$d\\mathbf{s}=\\hat{\\mathbf{z}}\\,r\\,dr\\,d\\phi$ on the cross-section."],
 steps=[D(r"I=\int_0^{2\pi}\!\!\int_0^aJ_0\left(1-\frac{r}{a}\right)r\,dr\,d\phi=2\pi J_0\left(\frac{a^2}{2}-\frac{a^2}{3}\right)=\frac{\pi J_0a^2}{3}"),D(f"I=\\frac{{\\pi(2\\times10^6)(10^{{-3}})^2}}{{3}}={teng(I,'A')}")],
 answers=[{"label":"I","value":teng(I,'A')}],widget="wire")

ni=1.5e16; me,mh=0.135,0.048; sig=ni*QE*(me+mh)
add(difficulty=2,title="Conductivity of intrinsic silicon",
 prompt="Pure silicon at room temperature has $N_e=N_h=1.5\\times10^{16}\\ \\mathrm{m^{-3}}$, $\\mu_e=0.135$ and $\\mu_h=0.048\\ \\mathrm{m^2/(V\\,s)}$. Find its conductivity and the resistance of a $1\\ \\mathrm{cm}$ cube.",
 hints=["$\\sigma=q(N_e\\mu_e+N_h\\mu_h)$.","For a cube of side $\\ell$, $R=\\dfrac{\\ell}{\\sigma\\ell^2}=\\dfrac{1}{\\sigma\\ell}$."],
 steps=[D(f"\\sigma=(1.602\\times10^{{-19}})(1.5\\times10^{{16}})(0.135+0.048)={tsci(sig,'S/m')}"),D(f"R=\\frac{{1}}{{\\sigma(0.01)}}={teng(1/(sig*0.01),'Ω')}")],
 answers=[{"label":r"\sigma","value":tsci(sig,'S/m')},{"label":"R","value":teng(1/(sig*0.01),'Ω')}],widget="wire")

s=1e-4; a,b=1e-3,4e-3; Gp=2*math.pi*s/math.log(b/a)
add(difficulty=3,title="Leakage through a coax dielectric",
 prompt="A coax has $a=1\\ \\mathrm{mm}$, $b=4\\ \\mathrm{mm}$, and a slightly lossy filling with $\\sigma=10^{-4}\\ \\mathrm{S/m}$. Find the leakage conductance per meter and the leakage resistance of a $1\\ \\mathrm{m}$ length.",
 hints=["A leakage current $I$ per meter spreads out radially: $J_r=\\dfrac{I}{2\\pi r}$.","Find $E_r=J_r/\\sigma$, integrate from $a$ to $b$ for $V$, then $G'=I/V$."],
 steps=[D(r"V=\int_a^b\frac{I}{2\pi\sigma r}\,dr=\frac{I}{2\pi\sigma}\ln\frac{b}{a}"),D(r"G'=\frac{I}{V}=\frac{2\pi\sigma}{\ln(b/a)}"),D(f"G'=\\frac{{2\\pi(10^{{-4}})}}{{\\ln4}}={teng(Gp,'S/m')}"),D(f"R=\\frac{{1}}{{G'\\ell}}={teng(1/Gp,'Ω')}")],
 answers=[{"label":"G'","value":teng(Gp,'S/m')},{"label":"R","value":teng(1/Gp,'Ω')}],topics=["conductors","tline"],widget="params")

add(difficulty=1,title="Charge build-up from the continuity equation",
 prompt="In a region, $\\mathbf{J}=\\hat{\\mathbf{x}}\\,3x^2\\ \\mathrm{A/m^2}$. How fast is the charge density changing at $x=2\\ \\mathrm{m}$?",
 hints=["$\\dfrac{\\partial\\rho_v}{\\partial t}=-\\nabla\\cdot\\mathbf{J}$."],
 steps=[D(r"\nabla\cdot\mathbf{J}=\frac{\partial(3x^2)}{\partial x}=6x"),D(r"\frac{\partial\rho_v}{\partial t}=-6x=-12\ \mathrm{C/(m^3\,s)}"),"More current leaves than arrives, so the charge density there is falling."],
 answers=[{"label":r"\partial\rho_v/\partial t","value":r"-12\ \mathrm{C/(m^3\,s)}"}])

Rs=1/(4*1e-4); Rc=1/(5.8e7*1e-4); I=10
add(difficulty=1,title="Copper versus seawater",
 prompt="Compare the resistance of a $1\\ \\mathrm{m}$ long, $1\\ \\mathrm{cm^2}$ column of copper ($5.8\\times10^7\\ \\mathrm{S/m}$) and of seawater ($4\\ \\mathrm{S/m}$).",
 hints=["$R=\\dfrac{\\ell}{\\sigma A}$ with $A=10^{-4}\\ \\mathrm{m^2}$."],
 steps=[D(f"R_{{\\text{{Cu}}}}=\\frac{{1}}{{(5.8\\times10^7)(10^{{-4}})}}={teng(Rc,'Ω')}"),D(f"R_{{\\text{{sea}}}}=\\frac{{1}}{{(4)(10^{{-4}})}}={teng(Rs,'Ω')}"),f"Seawater is about ${tsci(Rs/Rc)}$ times more resistive. It still conducts well enough to block most radio waves."],
 answers=[{"label":r"R_{\text{Cu}}","value":teng(Rc,'Ω')},{"label":r"R_{\text{sea}}","value":teng(Rs,'Ω')}],widget="wire")

R=0.5; Pw=I*I*R
add(difficulty=1,title="Heat in a resistor from fields",
 prompt="A $0.5\\ \\Omega$ bar carries $10\\ \\mathrm{A}$. Use Joule's law to find the power it dissipates, and say where the energy comes from.",
 hints=["For a uniform bar $\\int\\mathbf{E}\\cdot\\mathbf{J}\\,dV=(E\\ell)(JA)=VI$."],
 steps=[D(r"P=\int_V\mathbf{E}\cdot\mathbf{J}\,dV=(E\ell)(JA)=VI=I^2R"),D(f"P=(10)^2(0.5)={teng(Pw,'W')}"),"The field does work on the drifting charges, and collisions turn that work into heat."],
 answers=[{"label":"P","value":teng(Pw,'W')}],widget="wire")

write_unit("current-and-conductors","Current and conductors",C,G,P)
