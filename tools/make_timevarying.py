# Time-varying fields: flashcards, glossary and practice problems.
# Every number in the steps and answers is computed here. Run: python3 tools/make_timevarying.py
import math, os, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lib import *
D=lambda s:"$$"+s+"$$"
EPS0=8.854187817e-12; MU0=4e-7*math.pi; ETA0=math.sqrt(MU0/EPS0)
T=["time-varying"]

C=[
("Faraday's law, integral form?",D(r"V_{\mathrm{emf}}=\oint_C\mathbf{E}\cdot d\mathbf{l}=-\frac{d\Phi}{dt}=-\frac{d}{dt}\int_S\mathbf{B}\cdot d\mathbf{s}"),"equation",T),
("Faraday's law, differential form?",D(r"\nabla\times\mathbf{E}=-\frac{\partial\mathbf{B}}{\partial t}"),"equation",T),
("EMF of a coil with $N$ turns?",D(r"V_{\mathrm{emf}}=-N\frac{d\Phi}{dt}"),"equation",T),
("What does Lenz's law say?","The induced current flows so that its own magnetic field opposes the change in flux. That is the minus sign in Faraday's law.","concept",T),
("Three ways to change the flux through a loop?","Change $\\mathbf{B}$ in time (transformer EMF), move or deform the loop in a static $\\mathbf{B}$ (motional EMF), or both.","concept",T),
("Motional EMF of a conductor moving through $\\mathbf{B}$?",D(r"V_{\mathrm{emf}}=\oint(\mathbf{u}\times\mathbf{B})\cdot d\mathbf{l}")+"For a bar of length $\\ell$ moving at $u$ across $B$: $V=uB\\ell$.","equation",T),
("Peak EMF of a loop spinning at $\\omega$ in a uniform field?",D(r"V_{\mathrm{peak}}=NBA\omega"),"equation",T),
("Ideal transformer voltage and current ratios?",D(r"\frac{V_1}{V_2}=\frac{N_1}{N_2},\qquad\frac{I_1}{I_2}=\frac{N_2}{N_1}"),"equation",T),
("Displacement current density?",D(r"\mathbf{J}_d=\frac{\partial\mathbf{D}}{\partial t}\ \xrightarrow{\text{phasor}}\ j\omega\varepsilon\mathbf{E}"),"equation",T),
("Ampère's law with Maxwell's correction?",D(r"\nabla\times\mathbf{H}=\mathbf{J}+\frac{\partial\mathbf{D}}{\partial t}"),"equation",T),
("Why did Maxwell add displacement current?","Without it, Ampère's law gives different answers for surfaces that pass between a capacitor's plates. It also makes Ampère's law agree with charge continuity, and it predicts EM waves.","concept",T),
("Ratio of conduction to displacement current in a material?",D(r"\frac{|J_c|}{|J_d|}=\frac{\sigma}{\omega\varepsilon}")+"Much greater than 1: good conductor. Much less than 1: good dielectric.","equation",T),
("Charge relaxation time?",D(r"\tau_r=\frac{\varepsilon}{\sigma}")+"Excess charge inside a conductor decays as $e^{-t/\\tau_r}$. Copper: about $10^{-19}$ s.","equation",T),
("Maxwell's equations in differential form?",D(r"\nabla\cdot\mathbf{D}=\rho_v,\quad\nabla\times\mathbf{E}=-\frac{\partial\mathbf{B}}{\partial t},\quad\nabla\cdot\mathbf{B}=0,\quad\nabla\times\mathbf{H}=\mathbf{J}+\frac{\partial\mathbf{D}}{\partial t}"),"equation",T),
("Maxwell's curl equations in phasor form?",D(r"\nabla\times\tilde{\mathbf{E}}=-j\omega\mu\tilde{\mathbf{H}},\qquad\nabla\times\tilde{\mathbf{H}}=(\sigma+j\omega\varepsilon)\tilde{\mathbf{E}}"),"equation",T),
("What do the static equations lose, compared with the dynamic ones?","The coupling terms $\\partial\\mathbf{B}/\\partial t$ and $\\partial\\mathbf{D}/\\partial t$. With them, a changing $\\mathbf{E}$ makes $\\mathbf{H}$ and a changing $\\mathbf{H}$ makes $\\mathbf{E}$, which is what lets waves travel.","concept",T),
("Complex permittivity of a lossy material?",D(r"\varepsilon_c=\varepsilon-j\frac{\sigma}{\omega}")+"It folds conduction into the displacement term.","equation",T),
]

G=[
("Faraday's law","","","A changing magnetic flux through a loop induces an EMF around it: $V_{\\mathrm{emf}}=-d\\Phi/dt$.","faraday",T),
("Electromotive force","V_{\\mathrm{emf}}","\\mathrm{V}","The work per unit charge done around a closed loop, $\\oint\\mathbf{E}\\cdot d\\mathbf{l}$. Not conservative when fields change in time.","faraday",T),
("Lenz's law","","","The induced current opposes the change in flux that caused it.","faraday",T),
("Transformer EMF","","","EMF in a stationary loop from a time-varying $\\mathbf{B}$: $-\\int\\partial\\mathbf{B}/\\partial t\\cdot d\\mathbf{s}$.","faraday",T),
("Motional EMF","","","EMF from a conductor moving through a magnetic field: $\\oint(\\mathbf{u}\\times\\mathbf{B})\\cdot d\\mathbf{l}$. The basis of generators.","faraday",T),
("Displacement current","\\mathbf{J}_d=\\partial\\mathbf{D}/\\partial t","\\mathrm{A/m^2}","The term Maxwell added to Ampère's law. It carries current across a capacitor gap and lets a changing $\\mathbf{E}$ create $\\mathbf{H}$.","dispcur",T),
("Relaxation time","\\tau_r=\\varepsilon/\\sigma","\\mathrm{s}","Time for excess charge inside a material to fall to $1/e$ of its starting value.","dispcur",T),
("Good conductor","","","A material with $\\sigma/(\\omega\\varepsilon)\\gg1$ at the frequency of interest. Whether a material counts as one depends on frequency.","dispcur",T),
("Low-loss dielectric","","","A material with $\\sigma/(\\omega\\varepsilon)\\ll1$, where displacement current dominates.","dispcur",T),
("Loss tangent","\\tan\\delta=\\sigma/(\\omega\\varepsilon)","","The ratio of conduction to displacement current, used to grade dielectrics.","dispcur",T),
("Maxwell's equations","","","Four equations for $\\mathbf{E}$, $\\mathbf{D}$, $\\mathbf{B}$, $\\mathbf{H}$ and their sources: Gauss's law, Faraday's law, no magnetic charge, and Ampère's law with displacement current.",None,T),
("Quasi-static","","","When a structure is much smaller than a wavelength, the displacement-current and induction effects are small, so circuit theory works.",None,T),
]

P=[]
def add(**k): k.setdefault("source","original"); k.setdefault("topics",T); P.append(k)

N,B0,A,w=10,0.1,0.05,120*math.pi; Vp=N*B0*A*w
add(difficulty=1,title="EMF in a stationary coil",
 prompt="A 10-turn coil of area $0.05\\ \\mathrm{m^2}$ sits in $\\mathbf{B}=\\hat{\\mathbf{z}}\\,0.1\\cos(120\\pi t)\\ \\mathrm{T}$, with its normal along $\\hat{\\mathbf{z}}$. Find the induced EMF.",
 hints=["$\\Phi=BA$ through each turn, and $V_{\\mathrm{emf}}=-N\\,d\\Phi/dt$."],
 steps=[D(r"\Phi=(0.1)(0.05)\cos(120\pi t)=0.005\cos(120\pi t)\ \mathrm{Wb}"),D(f"V_{{\\mathrm{{emf}}}}=-10\\frac{{d\\Phi}}{{dt}}=(10)(0.005)(120\\pi)\\sin(120\\pi t)={tr(Vp)}\\sin(120\\pi t)\\ \\mathrm{{V}}")],
 answers=[{"label":r"V_{\mathrm{emf}}","value":f"{tr(Vp)}\\sin(120\\pi t)\\ \\mathrm{{V}}"}],widget="faraday")

L,u,B,R=0.5,4,0.3,2; V=u*B*L; I=V/R; F=I*L*B
add(difficulty=2,title="Sliding bar on rails",
 prompt="A metal bar $0.5\\ \\mathrm{m}$ long slides at $4\\ \\mathrm{m/s}$ along rails in a uniform $0.3\\ \\mathrm{T}$ field normal to the rails. The circuit resistance is $2\\ \\Omega$. Find the EMF, the current, the force needed to keep the bar moving, and the power.",
 hints=["$V=uB\\ell$.","The current in the bar feels $F=I\\ell B$, opposing the motion (Lenz)."],
 steps=[D(f"V=uB\\ell=(4)(0.3)(0.5)={tr(V)}\\ \\mathrm{{V}}"),D(f"I=\\frac{{V}}{{R}}={tr(I)}\\ \\mathrm{{A}}"),D(f"F=I\\ell B={teng(F,'N')}"),D(f"P=Fu=I^2R={teng(F*u,'W')}"),"The mechanical power you supply equals the electrical power dissipated in the resistor."],
 answers=[{"label":"V","value":f"{tr(V)}\\ \\mathrm{{V}}"},{"label":"I","value":f"{tr(I)}\\ \\mathrm{{A}}"},{"label":"F","value":teng(F,'N')},{"label":"P","value":teng(F*u,'W')}],widget="faraday")

N,A,B,f=100,0.01,0.5,60; Vp=N*B*A*2*math.pi*f
add(difficulty=1,title="A simple generator",
 prompt="A 100-turn coil of area $100\\ \\mathrm{cm^2}$ spins at $60$ revolutions per second in a uniform $0.5\\ \\mathrm{T}$ field. Find the peak and RMS EMF.",
 hints=["$\\Phi=NBA\\cos\\omega t$, so $V=NBA\\omega\\sin\\omega t$."],
 steps=[D(r"\omega=2\pi(60)=377\ \mathrm{rad/s}"),D(f"V_{{\\mathrm{{peak}}}}=NBA\\omega=(100)(0.5)(0.01)(377)={tr(Vp)}\\ \\mathrm{{V}}"),D(f"V_{{\\mathrm{{rms}}}}=\\frac{{V_{{\\mathrm{{peak}}}}}}{{\\sqrt2}}={tr(Vp/math.sqrt(2))}\\ \\mathrm{{V}}")],
 answers=[{"label":r"V_{\mathrm{peak}}","value":f"{tr(Vp)}\\ \\mathrm{{V}}"},{"label":r"V_{\mathrm{rms}}","value":f"{tr(Vp/math.sqrt(2))}\\ \\mathrm{{V}}"}],widget="faraday")

add(difficulty=1,title="Which way does the current flow?",
 prompt="A horizontal wire loop sits in a vertical magnetic field pointing up, and the field is getting stronger. Looking down from above, which way does the induced current flow? What if the field is getting weaker?",
 hints=["The induced current makes a field that opposes the change.","Use the right-hand rule: counterclockwise current (seen from above) makes a field pointing up."],
 steps=["The upward flux is increasing, so the induced field must point down inside the loop.","A downward field inside the loop needs clockwise current, seen from above.","If the field is weakening, the induced field points up to prop up the flux: counterclockwise."],
 answers=[{"label":r"\text{Increasing}","value":r"\text{clockwise}"},{"label":r"\text{Decreasing}","value":r"\text{counterclockwise}"}],widget="faraday")

N1,N2,V1=100,500,10
add(difficulty=1,title="Ideal transformer",
 prompt="An ideal transformer has $100$ primary turns and $500$ secondary turns. With $10\\ \\mathrm{V}$ RMS on the primary and a $250\\ \\Omega$ load, find the secondary voltage and both currents.",
 hints=["The same flux links both coils, so the voltage per turn is the same."],
 steps=[D(r"V_2=V_1\frac{N_2}{N_1}=10\cdot5=50\ \mathrm{V}"),D(r"I_2=\frac{50}{250}=0.2\ \mathrm{A},\qquad I_1=I_2\frac{N_2}{N_1}=1\ \mathrm{A}"),"Power in, $10\\times1=10$ W, equals power out, $50\\times0.2=10$ W."],
 answers=[{"label":"V_2","value":r"50\ \mathrm{V}"},{"label":"I_2","value":r"0.2\ \mathrm{A}"},{"label":"I_1","value":r"1\ \mathrm{A}"}])

er,E0,w=4,100,1e9; Jd=er*EPS0*E0*w
add(difficulty=1,title="Displacement current density",
 prompt="In a lossless dielectric with $\\varepsilon_r=4$, $\\mathbf{E}=\\hat{\\mathbf{x}}\\,100\\cos(10^9t)\\ \\mathrm{V/m}$. Find $\\mathbf{J}_d$.",
 hints=["$\\mathbf{J}_d=\\varepsilon\\,\\partial\\mathbf{E}/\\partial t$."],
 steps=[D(r"\mathbf{J}_d=\varepsilon_r\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}=-\hat{\mathbf{x}}\,(4)(8.854\times10^{-12})(100)(10^9)\sin(10^9t)"),D(f"\\mathbf{{J}}_d=-\\hat{{\\mathbf{{x}}}}\\,{tr(Jd)}\\sin(10^9t)\\ \\mathrm{{A/m^2}}")],
 answers=[{"label":r"\mathbf{J}_d","value":f"-\\hat{{\\mathbf{{x}}}}\\,{tr(Jd)}\\sin(10^9t)\\ \\mathrm{{A/m^2}}"}],widget="dispcur")

s,er=4,81; r1=s/(2*math.pi*1e6*er*EPS0); r2=s/(2*math.pi*10e9*er*EPS0); fc=s/(2*math.pi*er*EPS0)
add(difficulty=2,title="Is seawater a conductor?",
 prompt="Seawater has $\\sigma=4\\ \\mathrm{S/m}$ and $\\varepsilon_r=81$. Find $\\sigma/(\\omega\\varepsilon)$ at $1\\ \\mathrm{MHz}$ and at $10\\ \\mathrm{GHz}$, and the frequency where conduction and displacement currents are equal.",
 hints=["Compare $\\sigma$ with $\\omega\\varepsilon=2\\pi f\\varepsilon_r\\varepsilon_0$."],
 steps=[D(f"1\\ \\mathrm{{MHz}}:\\ \\frac{{\\sigma}}{{\\omega\\varepsilon}}=\\frac{{4}}{{2\\pi(10^6)(81)\\varepsilon_0}}={tr(r1)}"),D(f"10\\ \\mathrm{{GHz}}:\\ \\frac{{\\sigma}}{{\\omega\\varepsilon}}={tr(r2)}"),D(f"f_c=\\frac{{\\sigma}}{{2\\pi\\varepsilon}}={teng(fc,'Hz')}"),"Seawater is a good conductor at 1 MHz but behaves like a lossy dielectric at 10 GHz."],
 answers=[{"label":r"\sigma/\omega\varepsilon\ (1\ \mathrm{MHz})","value":tr(r1)},{"label":r"\sigma/\omega\varepsilon\ (10\ \mathrm{GHz})","value":tr(r2)},{"label":"f_c","value":teng(fc,'Hz')}],widget="dispcur")

A,d,V0,f=1e-4,1e-3,10,1e6; Cc=EPS0*A/d; Id=Cc*V0*2*math.pi*f
add(difficulty=2,title="Displacement current in a capacitor",
 prompt="An air-filled parallel-plate capacitor ($A=1\\ \\mathrm{cm^2}$, $d=1\\ \\mathrm{mm}$) has $v(t)=10\\sin(2\\pi\\times10^6t)\\ \\mathrm{V}$ across it. Find the displacement current between the plates and compare it with the current in the leads.",
 hints=["$E=v/d$ and $J_d=\\varepsilon_0\\,\\partial E/\\partial t$; multiply by $A$.","The lead current is $C\\,dv/dt$."],
 steps=[D(r"I_d=AJ_d=A\varepsilon_0\frac{1}{d}\frac{dv}{dt}=C\frac{dv}{dt}"),D(f"C=\\frac{{\\varepsilon_0A}}{{d}}={teng(Cc,'F')}"),D(f"I_d=CV_0\\omega\\cos\\omega t={teng(Id,'A')}\\,\\cos(2\\pi\\times10^6t)"),"It equals the conduction current in the leads exactly, so current is continuous around the circuit."],
 answers=[{"label":"I_d","value":f"{teng(Id,'A')}\\,\\cos(2\\pi\\times10^6t)"}],widget="dispcur")

tc=EPS0/5.8e7; tg=6*EPS0/1e-15
add(difficulty=1,title="Relaxation times",
 prompt="Find the charge relaxation time of copper ($\\sigma=5.8\\times10^7\\ \\mathrm{S/m}$, $\\varepsilon_r=1$) and of mica ($\\sigma=10^{-15}\\ \\mathrm{S/m}$, $\\varepsilon_r=6$).",
 hints=["$\\tau_r=\\varepsilon/\\sigma$."],
 steps=[D(f"\\tau_{{\\text{{Cu}}}}=\\frac{{8.854\\times10^{{-12}}}}{{5.8\\times10^7}}={tsci(tc,'s')}"),D(f"\\tau_{{\\text{{mica}}}}=\\frac{{6(8.854\\times10^{{-12}})}}{{10^{{-15}}}}={tsci(tg,'s')}={tr(tg/3600)}\\ \\mathrm{{h}}"),"Charge put inside copper vanishes to the surface essentially instantly; charge on mica stays for hours."],
 answers=[{"label":r"\tau_{\text{Cu}}","value":tsci(tc,'s')},{"label":r"\tau_{\text{mica}}","value":f"{tsci(tg,'s')}={tr(tg/3600)}\\ \\mathrm{{h}}"}],widget="dispcur")

E0,f=10,100e6; be=2*math.pi*f/c; H0=E0/ETA0
add(difficulty=3,title="H from E with Faraday's law",
 prompt="In free space, $\\mathbf{E}=\\hat{\\mathbf{x}}\\,10\\cos(\\omega t-\\beta z)\\ \\mathrm{V/m}$ at $f=100\\ \\mathrm{MHz}$. Use Faraday's law to find $\\mathbf{H}$, then check that it satisfies Ampère's law with $\\mathbf{J}=0$.",
 hints=["In phasor form, $\\nabla\\times\\tilde{\\mathbf{E}}=-j\\omega\\mu_0\\tilde{\\mathbf{H}}$.","Only $\\partial\\tilde E_x/\\partial z$ survives in the curl: it points along $\\hat{\\mathbf{y}}$."],
 steps=[D(r"\tilde{\mathbf{E}}=\hat{\mathbf{x}}\,10e^{-j\beta z},\qquad\nabla\times\tilde{\mathbf{E}}=\hat{\mathbf{y}}\,\frac{\partial\tilde E_x}{\partial z}=-\hat{\mathbf{y}}\,j\beta\,10e^{-j\beta z}"),
        D(r"\tilde{\mathbf{H}}=\frac{\nabla\times\tilde{\mathbf{E}}}{-j\omega\mu_0}=\hat{\mathbf{y}}\,\frac{10\beta}{\omega\mu_0}e^{-j\beta z}=\hat{\mathbf{y}}\,\frac{10}{\eta_0}e^{-j\beta z}"),
        D(f"\\beta=\\frac{{\\omega}}{{c}}={tr(be)}\\ \\mathrm{{rad/m}},\\qquad\\eta_0={tr(ETA0)}\\ \\Omega"),D(f"\\mathbf{{H}}=\\hat{{\\mathbf{{y}}}}\\,{teng(H0,'A/m')}\\cos(\\omega t-{tr(be)}z)"),
        "Check: $\\nabla\\times\\tilde{\\mathbf{H}}=-\\hat{\\mathbf{x}}\\,\\dfrac{\\partial\\tilde H_y}{\\partial z}=\\hat{\\mathbf{x}}\\,\\dfrac{j\\beta\\,10}{\\eta_0}e^{-j\\beta z}$, and $j\\omega\\varepsilon_0\\tilde{\\mathbf{E}}=\\hat{\\mathbf{x}}\\,j\\omega\\varepsilon_0\\,10e^{-j\\beta z}$. They match because $\\beta/\\eta_0=\\omega\\varepsilon_0$."],
 answers=[{"label":r"\mathbf{H}","value":f"\\hat{{\\mathbf{{y}}}}\\,{teng(H0,'A/m')}\\cos(\\omega t-{tr(be)}z)"}],topics=["time-varying","plane-waves"],widget="travel")

write_unit("time-varying-fields","Time-varying fields",C,G,P)
