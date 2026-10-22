# Fields and phasors: flashcards, glossary and practice problems.
# Every number in the steps and answers is computed here. Run: python3 tools/make_phasors.py
import math, cmath, os, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lib import *
D=lambda s:"$$"+s+"$$"
deg=lambda x:f"{tr(x)}^\\circ"
EPS0=8.854187817e-12; MU0=4e-7*math.pi
T=["phasors"]

C=[
("What is the difference between a scalar field and a vector field?","A scalar field gives a number at each point (temperature, potential $V$). A vector field gives a magnitude and a direction at each point ($\\mathbf{E}$, $\\mathbf{H}$).","concept",T),
("What are the four field quantities, and their units?","$\\mathbf{E}$ (V/m), $\\mathbf{D}$ (C/m²), $\\mathbf{H}$ (A/m), $\\mathbf{B}$ (T = Wb/m²).","concept",T),
("Force on a charge $q$ in an electric field?",D(r"\mathbf{F}=q\mathbf{E}"),"equation",T),
("How are $\\mathbf{D}$ and $\\mathbf{E}$ related in a simple medium?",D(r"\mathbf{D}=\varepsilon\mathbf{E}=\varepsilon_r\varepsilon_0\mathbf{E}"),"equation",T),
("How are $\\mathbf{B}$ and $\\mathbf{H}$ related in a simple medium?",D(r"\mathbf{B}=\mu\mathbf{H}=\mu_r\mu_0\mathbf{H}"),"equation",T),
("Values of $\\varepsilon_0$ and $\\mu_0$?",D(r"\varepsilon_0\approx 8.854\times10^{-12}\ \mathrm{F/m},\qquad \mu_0=4\pi\times10^{-7}\ \mathrm{H/m}"),"equation",T),
("Speed of light from $\\mu_0$ and $\\varepsilon_0$?",D(r"c=\frac{1}{\sqrt{\mu_0\varepsilon_0}}\approx 3\times10^{8}\ \mathrm{m/s}"),"equation",T),
("What does conductivity $\\sigma$ describe, and in what units?","How easily charge flows through a material, in S/m. A perfect conductor has $\\sigma\\to\\infty$; a perfect insulator has $\\sigma=0$.","concept",T),
("Relations among $f$, $\\omega$ and the period $T$?",D(r"\omega=2\pi f,\qquad T=\frac{1}{f}"),"equation",T),
("Relations among $\\lambda$, $\\beta$, $f$ and $u_p$?",D(r"\lambda=\frac{u_p}{f},\qquad \beta=\frac{2\pi}{\lambda},\qquad u_p=\frac{\omega}{\beta}"),"equation",T),
("Which way does $\\cos(\\omega t-\\beta z)$ travel? And $\\cos(\\omega t+\\beta z)$?","$\\omega t-\\beta z$: toward $+z$. $\\omega t+\\beta z$: toward $-z$. Follow a crest: $\\omega t\\mp\\beta z=$ const.","concept",T),
("Phase velocity in a medium with $\\varepsilon_r$ and $\\mu_r$?",D(r"u_p=\frac{1}{\sqrt{\mu\varepsilon}}=\frac{c}{\sqrt{\mu_r\varepsilon_r}}"),"equation",T),
("Wavelength in a non-magnetic dielectric compared with free space?",D(r"\lambda=\frac{\lambda_0}{\sqrt{\varepsilon_r}}")+"The wave slows down, so it gets shorter.","equation",T),
("Euler's identity?",D(r"e^{j\theta}=\cos\theta+j\sin\theta"),"equation",T),
("What is a phasor?","A complex number that holds a sinusoid's amplitude and phase. The time function comes back with"+D(r"v(t)=\mathrm{Re}\left\{\tilde V e^{j\omega t}\right\}"),"concept",T),
("Phasor of $A\\cos(\\omega t+\\phi)$?",D(r"\tilde V=Ae^{j\phi}=A\angle\phi"),"equation",T),
("Phasor of $A\\sin(\\omega t+\\phi)$?","Write it as a cosine first: $\\sin x=\\cos(x-90^\\circ)$."+D(r"\tilde V=A\angle(\phi-90^\circ)=-jAe^{j\phi}"),"equation",T),
("What do $\\dfrac{d}{dt}$ and $\\displaystyle\\int dt$ become for phasors?",D(r"\frac{d}{dt}\to j\omega,\qquad \int dt\to\frac{1}{j\omega}"),"equation",T),
("Why use phasors, and when do they work?","They turn differential equations in time into algebra. They work for linear systems driven at a single frequency, in sinusoidal steady state.","concept",T),
("Convert $a+jb$ to polar form.",D(r"|z|=\sqrt{a^2+b^2},\qquad \theta=\operatorname{atan2}(b,a)")+"Check the quadrant: $-3-j4$ is at $-126.9^\\circ$, not $53.1^\\circ$.","equation",T),
("How do you multiply and divide complex numbers in polar form?","Multiply: magnitudes multiply, angles add. Divide: magnitudes divide, angles subtract.","concept",T),
("Can you add the phasors of a 1 kHz and a 2 kHz signal?","No. A phasor assumes one frequency $\\omega$. Signals at different frequencies must be added in the time domain.","concept",T),
("What is $j$ as a phasor, and what does multiplying by $j$ do?","$j=e^{j90^\\circ}$. Multiplying by $j$ advances the phase by $90^\\circ$; multiplying by $-j$ delays it by $90^\\circ$.","concept",T),
("Guided versus unguided waves?","Guided waves follow a structure such as a transmission line or waveguide. Unguided waves spread through space from an antenna, like radio and light.","concept",T),
]

G=[
("Scalar field","","","A quantity with only a magnitude at each point in space, such as temperature or electric potential $V(x,y,z)$.",None,T),
("Vector field","","","A quantity with a magnitude and a direction at each point in space, such as $\\mathbf{E}(x,y,z)$. Drawn as arrows or field lines.",None,T),
("Electric field intensity","\\mathbf{E}","\\mathrm{V/m}","Force per unit charge on a small test charge: $\\mathbf{F}=q\\mathbf{E}$.",None,T),
("Electric flux density","\\mathbf{D}","\\mathrm{C/m^2}","Also called electric displacement. In a simple medium $\\mathbf{D}=\\varepsilon\\mathbf{E}$. Its flux through a closed surface equals the enclosed free charge.",None,T),
("Magnetic flux density","\\mathbf{B}","\\mathrm{T}","Sets the force on a moving charge: $\\mathbf{F}=q\\mathbf{u}\\times\\mathbf{B}$. One tesla is one Wb/m².",None,T),
("Magnetic field intensity","\\mathbf{H}","\\mathrm{A/m}","The magnetic field set up by currents. In a simple medium $\\mathbf{B}=\\mu\\mathbf{H}$.",None,T),
("Permittivity","\\varepsilon=\\varepsilon_r\\varepsilon_0","\\mathrm{F/m}","How a material responds to an electric field. $\\varepsilon_0\\approx8.854\\times10^{-12}$ F/m; $\\varepsilon_r$ is the dielectric constant.","travel",T),
("Permeability","\\mu=\\mu_r\\mu_0","\\mathrm{H/m}","How a material responds to a magnetic field. $\\mu_0=4\\pi\\times10^{-7}$ H/m. Most materials have $\\mu_r\\approx1$; iron and ferrites are much larger.","travel",T),
("Conductivity","\\sigma","\\mathrm{S/m}","How easily current flows in a material: $\\mathbf{J}=\\sigma\\mathbf{E}$. Copper is about $5.8\\times10^7$ S/m.",None,T),
("Constitutive relations","","","The material equations that tie the fields together: $\\mathbf{D}=\\varepsilon\\mathbf{E}$, $\\mathbf{B}=\\mu\\mathbf{H}$, $\\mathbf{J}=\\sigma\\mathbf{E}$.",None,T),
("Angular frequency","\\omega","\\mathrm{rad/s}","$\\omega=2\\pi f$. The rate at which a sinusoid's phase advances in time.","phasor",T),
("Wavelength","\\lambda","\\mathrm{m}","Distance between crests of a wave at one instant: $\\lambda=\\dfrac{u_p}{f}=\\dfrac{2\\pi}{\\beta}$.","travel",T),
("Traveling wave","","","A disturbance that moves without changing shape, like $A\\cos(\\omega t-\\beta z)$ moving toward $+z$ at $u_p=\\omega/\\beta$.","travel",T),
("Euler's identity","","","$e^{j\\theta}=\\cos\\theta+j\\sin\\theta$. It links a rotating complex number to a sinusoid, which is the basis of phasors.","phasor",T),
("Polar form","A\\angle\\theta","","A complex number written as a magnitude and an angle: $A\\angle\\theta=Ae^{j\\theta}=A\\cos\\theta+jA\\sin\\theta$.","phasor",T),
("Sinusoidal steady state","","","The state of a linear system long after a sinusoidal source turns on, when every voltage and current is a sinusoid at the source frequency. Phasors describe it.","phasor",T),
("Electromagnetic spectrum","","","The range of EM wave frequencies: radio, microwave (about 300 MHz to 300 GHz), infrared, visible light, ultraviolet, X-rays and gamma rays. All travel at $c$ in vacuum.",None,T),
]

P=[]
def add(**k): k.setdefault("source","original"); k.setdefault("topics",T); P.append(k)

z=12*cmath.exp(1j*math.radians(-60))
add(difficulty=1,title="Phasor of a sine",
 prompt="Find the phasor of $v(t)=12\\sin(\\omega t+30^\\circ)\\ \\mathrm{V}$ in polar and rectangular form.",
 hints=["Phasors are defined from cosines. Use $\\sin x=\\cos(x-90^\\circ)$."],
 steps=[D(r"v(t)=12\cos(\omega t+30^\circ-90^\circ)=12\cos(\omega t-60^\circ)\ \mathrm{V}"),D(f"\\tilde V=12\\angle {deg(-60)}\\ \\mathrm{{V}}=12\\cos(-60^\\circ)+j12\\sin(-60^\\circ)={tc(z)}\\ \\mathrm{{V}}")],
 answers=[{"label":r"\tilde V","value":f"12\\angle {deg(-60)}\\ \\mathrm{{V}}={tc(z)}\\ \\mathrm{{V}}"}],widget="phasor")

I=3-4j
add(difficulty=1,title="Back to the time domain",
 prompt="A 60 Hz current has phasor $\\tilde I=3-j4\\ \\mathrm{A}$. Write $i(t)$.",
 hints=["Convert to polar form first.","$i(t)=\\mathrm{Re}\\{\\tilde Ie^{j\\omega t}\\}=|\\tilde I|\\cos(\\omega t+\\theta)$ with $\\omega=2\\pi(60)$."],
 steps=[D(f"|\\tilde I|=\\sqrt{{3^2+4^2}}={tr(abs(I))}\\ \\mathrm{{A}},\\qquad \\theta=\\tan^{{-1}}\\frac{{-4}}{{3}}={deg(math.degrees(cmath.phase(I)))}"),D(f"\\omega=2\\pi(60)={tr(2*math.pi*60)}\\ \\mathrm{{rad/s}}"),D(f"i(t)=5\\cos(120\\pi t{deg(math.degrees(cmath.phase(I)))})\\ \\mathrm{{A}}")],
 answers=[{"label":"i(t)","value":f"5\\cos(120\\pi t{deg(math.degrees(cmath.phase(I)))})\\ \\mathrm{{A}}"}],widget="phasor")

a=5*cmath.exp(1j*math.radians(30)); b=8*cmath.exp(1j*math.radians(-45)); s=a+b
add(difficulty=2,title="Add two sinusoids with phasors",
 prompt="Write $v(t)=5\\cos(\\omega t+30^\\circ)+8\\cos(\\omega t-45^\\circ)$ as a single cosine.",
 hints=["Both terms have the same $\\omega$, so add their phasors.","Add in rectangular form, then convert back to polar."],
 steps=[D(f"5\\angle 30^\\circ={tc(a)},\\qquad 8\\angle {deg(-45)}={tc(b)}"),D(f"\\tilde V={tc(s)}={tp(s)}"),D(f"v(t)={tr(abs(s))}\\cos(\\omega t{'+' if cmath.phase(s)>=0 else ''}{deg(math.degrees(cmath.phase(s)))})")],
 answers=[{"label":"v(t)","value":f"{tr(abs(s))}\\cos(\\omega t{'+' if cmath.phase(s)>=0 else ''}{deg(math.degrees(cmath.phase(s)))})"}],widget="phasor")

z1=(3+4j)*(2-1j)/(1+1j)
add(difficulty=1,title="Complex arithmetic in polar form",
 prompt="Evaluate $\\dfrac{(3+j4)(2-j)}{1+j}$ in polar and rectangular form.",
 hints=["Convert each factor to polar. Magnitudes multiply and divide; angles add and subtract."],
 steps=["Each factor in polar form:"+D(f"3+j4={tp(3+4j)}")+D(f"2-j={tp(2-1j)}")+D(f"1+j={tp(1+1j)}"),
        D(f"\\text{{magnitude}}=\\frac{{5\\cdot{tr(abs(2-1j))}}}{{{tr(abs(1+1j))}}}={tr(abs(z1))}"),
        D(f"\\text{{angle}}={deg(math.degrees(cmath.phase(3+4j)))}{deg(math.degrees(cmath.phase(2-1j)))}-45^\\circ={deg(math.degrees(cmath.phase(z1)))}"),
        D(f"{tp(z1)}={tc(z1)}")],
 answers=[{"label":"\\text{Result}","value":f"{tp(z1)}={tc(z1)}"}],widget="phasor")

Zr=3+4j; Ip=10/Zr
add(difficulty=2,title="RL circuit with phasors",
 prompt="A source $v(t)=10\\cos(1000t)\\ \\mathrm{V}$ drives a $3\\ \\Omega$ resistor in series with a $4\\ \\mathrm{mH}$ inductor. Find $i(t)$ by writing the circuit equation in phasor form.",
 hints=["KVL in time: $v=Ri+L\\dfrac{di}{dt}$.","Replace $\\dfrac{d}{dt}$ with $j\\omega$."],
 steps=["KVL in phasor form:"+D(r"\tilde V=(R+j\omega L)\tilde I"),D(r"R+j\omega L=3+j(1000)(0.004)=3+j4\ \Omega=5\angle 53.13^\circ\ \Omega"),D(f"\\tilde I=\\frac{{10\\angle 0^\\circ}}{{5\\angle 53.13^\\circ}}={tp(Ip)}\\ \\mathrm{{A}}"),D(f"i(t)={tr(abs(Ip))}\\cos(1000t{deg(math.degrees(cmath.phase(Ip)))})\\ \\mathrm{{A}}")],
 answers=[{"label":"i(t)","value":f"{tr(abs(Ip))}\\cos(1000t{deg(math.degrees(cmath.phase(Ip)))})\\ \\mathrm{{A}}"}],widget="phasor")

Vp=10/(500+500j)
add(difficulty=2,title="Solve a differential equation with phasors",
 prompt="Find the steady-state solution of"+D(r"\frac{dv}{dt}+500\,v=10\cos(500t)"),
 hints=["Let $v(t)=\\mathrm{Re}\\{\\tilde Ve^{j500t}\\}$, so $\\dfrac{dv}{dt}\\to j500\\,\\tilde V$."],
 steps=[D(r"j500\,\tilde V+500\,\tilde V=10"),D(f"\\tilde V=\\frac{{10}}{{500+j500}}=\\frac{{10}}{{{tp(500+500j)}}}={tp(Vp)}"),D(f"v(t)={teng(abs(Vp),'V')}\\,\\cos(500t{deg(math.degrees(cmath.phase(Vp)))})")],
 answers=[{"label":"v(t)","value":f"{teng(abs(Vp),'V')}\\,\\cos(500t{deg(math.degrees(cmath.phase(Vp)))})"}],widget="phasor")

w=2*math.pi*1e8; be=2.5; lam=2*math.pi/be; up=w/be; er=(c/up)**2
add(difficulty=2,title="Read a traveling wave",
 prompt="In a non-magnetic material,"+D(r"E(z,t)=10\cos\left(2\pi\times10^{8}\,t-2.5z\right)\ \mathrm{V/m}")+"Find $f$, $\\lambda$, $u_p$, the direction of travel, and $\\varepsilon_r$.",
 hints=["Match the form $A\\cos(\\omega t-\\beta z)$.","$u_p=\\omega/\\beta$ and $u_p=c/\\sqrt{\\varepsilon_r}$."],
 steps=[D(r"\omega=2\pi\times10^8\ \mathrm{rad/s}\ \Rightarrow\ f=100\ \mathrm{MHz}"),D(f"\\lambda=\\frac{{2\\pi}}{{\\beta}}=\\frac{{2\\pi}}{{2.5}}={teng(lam,'m')}"),D(f"u_p=\\frac{{\\omega}}{{\\beta}}={tsci(up,'m/s')}"),"The sign of $\\beta z$ is negative, so the wave travels toward $+z$.",D(f"\\varepsilon_r=\\left(\\frac{{c}}{{u_p}}\\right)^2={tr(er)}")],
 answers=[{"label":"f","value":r"100\ \mathrm{MHz}"},{"label":r"\lambda","value":teng(lam,'m')},{"label":"u_p","value":tsci(up,'m/s')},{"label":r"\text{Direction}","value":"+z"},{"label":r"\varepsilon_r","value":tr(er)}],widget="travel")

w=4*math.pi*1e6; be=0.05; lam=2*math.pi/be; up=w/be
add(difficulty=1,title="Which way is it going?",
 prompt="A wave is $y(z,t)=3\\cos(4\\pi\\times10^{6}\\,t+0.05z)$. Find its frequency, wavelength, speed and direction.",
 hints=["A plus sign between $\\omega t$ and $\\beta z$ means travel toward $-z$."],
 steps=[D(r"f=\frac{\omega}{2\pi}=\frac{4\pi\times10^6}{2\pi}=2\ \mathrm{MHz}"),D(f"\\lambda=\\frac{{2\\pi}}{{0.05}}={teng(lam,'m')}"),D(f"u_p=\\frac{{\\omega}}{{\\beta}}={tsci(up,'m/s')}"),"Follow a crest: $\\omega t+0.05z=$ const, so $z$ decreases as $t$ grows. It travels toward $-z$."],
 answers=[{"label":"f","value":r"2\ \mathrm{MHz}"},{"label":r"\lambda","value":teng(lam,'m')},{"label":"u_p","value":tsci(up,'m/s')},{"label":r"\text{Direction}","value":"-z"}],widget="travel")

f=2.4e9; l0=c/f; l1=l0/2
add(difficulty=1,title="Wi-Fi wavelength in a dielectric",
 prompt="Find the wavelength of a $2.4\\ \\mathrm{GHz}$ signal in free space and in a non-magnetic dielectric with $\\varepsilon_r=4$. How fast does it travel in the dielectric?",
 hints=["$\\lambda_0=c/f$ and $\\lambda=\\lambda_0/\\sqrt{\\varepsilon_r}$."],
 steps=[D(f"\\lambda_0=\\frac{{3\\times10^8}}{{2.4\\times10^9}}={teng(l0,'m')}"),D(f"u_p=\\frac{{c}}{{\\sqrt{{4}}}}={tsci(c/2,'m/s')}"),D(f"\\lambda=\\frac{{\\lambda_0}}{{2}}={teng(l1,'m')}")],
 answers=[{"label":r"\lambda_0","value":teng(l0,'m')},{"label":r"\lambda","value":teng(l1,'m')},{"label":"u_p","value":tsci(c/2,'m/s')}],widget="travel")

Dv=2.5*EPS0*5000
add(difficulty=1,title="Flux density in a dielectric",
 prompt="A uniform field $\\mathbf{E}=\\hat{\\mathbf{x}}\\,5\\ \\mathrm{kV/m}$ exists in a material with $\\varepsilon_r=2.5$. Find $\\mathbf{D}$.",
 hints=["$\\mathbf{D}=\\varepsilon_r\\varepsilon_0\\mathbf{E}$."],
 steps=[D(f"\\mathbf{{D}}=\\hat{{\\mathbf{{x}}}}\\,(2.5)(8.854\\times10^{{-12}})(5000)=\\hat{{\\mathbf{{x}}}}\\,{teng(Dv,'C/m^2')}")],
 answers=[{"label":r"\mathbf{D}","value":f"\\hat{{\\mathbf{{x}}}}\\,{teng(Dv,'C/m^2')}"}])

H1=50e-3/(1000*MU0); H0=50e-3/MU0
add(difficulty=1,title="H from B in iron and in air",
 prompt="A magnetic flux density of $50\\ \\mathrm{mT}$ exists in a soft-iron core with $\\mu_r=1000$. Find $H$ in the core, and the $H$ that would give the same $B$ in air.",
 hints=["$H=\\dfrac{B}{\\mu_r\\mu_0}$."],
 steps=[D(f"H_{{\\text{{iron}}}}=\\frac{{0.05}}{{1000\\cdot4\\pi\\times10^{{-7}}}}={teng(H1,'A/m')}"),D(f"H_{{\\text{{air}}}}=\\frac{{0.05}}{{4\\pi\\times10^{{-7}}}}={teng(H0,'A/m')}"),"The iron needs 1000 times less $H$ (so 1000 times less current) for the same $B$."],
 answers=[{"label":r"H_{\text{iron}}","value":teng(H1,'A/m')},{"label":r"H_{\text{air}}","value":teng(H0,'A/m')}])

E=(4,-1,3); m=math.sqrt(sum(x*x for x in E))
add(difficulty=1,title="A vector field at a point",
 prompt="Evaluate $\\mathbf{E}=\\hat{\\mathbf{x}}\\,2xy-\\hat{\\mathbf{y}}\\,z^2+\\hat{\\mathbf{z}}\\,3\\ \\mathrm{V/m}$ at $(1,2,-1)$. Give its magnitude and unit vector there.",
 hints=["Substitute the coordinates into each component.","$\\hat{\\mathbf{a}}=\\mathbf{E}/|\\mathbf{E}|$."],
 steps=[D(r"\mathbf{E}(1,2,-1)=\hat{\mathbf{x}}\,4-\hat{\mathbf{y}}\,1+\hat{\mathbf{z}}\,3\ \mathrm{V/m}"),D(f"|\\mathbf{{E}}|=\\sqrt{{16+1+9}}=\\sqrt{{26}}={tr(m)}\\ \\mathrm{{V/m}}"),D(f"\\hat{{\\mathbf{{a}}}}=\\hat{{\\mathbf{{x}}}}\\,{tr(4/m)}-\\hat{{\\mathbf{{y}}}}\\,{tr(1/m)}+\\hat{{\\mathbf{{z}}}}\\,{tr(3/m)}")],
 answers=[{"label":r"|\mathbf{E}|","value":f"{tr(m)}\\ \\mathrm{{V/m}}"},{"label":r"\hat{\mathbf{a}}","value":f"\\hat{{\\mathbf{{x}}}}\\,{tr(4/m)}-\\hat{{\\mathbf{{y}}}}\\,{tr(1/m)}+\\hat{{\\mathbf{{z}}}}\\,{tr(3/m)}"}],topics=["phasors","vectors"])

Ep=6-8j; w=2*3e8; f=w/(2*math.pi)
add(difficulty=2,title="A phasor field in the time domain",
 prompt="In free space, $\\tilde{\\mathbf{E}}(z)=\\hat{\\mathbf{x}}\\,(6-j8)\\,e^{-j2z}\\ \\mathrm{V/m}$. Find the frequency, the direction of travel, and $\\mathbf{E}(z,t)$.",
 hints=["In free space $\\beta=\\omega/c$.","Put $6-j8$ in polar form, then use $\\mathbf{E}(z,t)=\\mathrm{Re}\\{\\tilde{\\mathbf{E}}e^{j\\omega t}\\}$."],
 steps=[D(f"\\omega=\\beta c={tsci(w,'rad/s')}")+D(f"f=\\frac{{\\omega}}{{2\\pi}}={teng(f,'Hz')}"),D(f"6-j8={tp(Ep)}"),D(f"\\mathbf{{E}}=\\hat{{\\mathbf{{x}}}}\\,10\\cos\\left(\\omega t-2z{deg(math.degrees(cmath.phase(Ep)))}\\right)\\ \\mathrm{{V/m}}"),"The phase is $\\omega t-2z$, so it travels toward $+z$."],
 answers=[{"label":"f","value":teng(f,'Hz')},{"label":r"\text{Direction}","value":"+z"},{"label":r"\mathbf{E}(z,t)","value":f"\\hat{{\\mathbf{{x}}}}\\,10\\cos(\\omega t-2z{deg(math.degrees(cmath.phase(Ep)))})\\ \\mathrm{{V/m}}"}],widget="travel")

write_unit("fields-and-phasors","Fields and phasors",C,G,P)
