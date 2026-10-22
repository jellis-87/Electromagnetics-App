# Reflection at boundaries: flashcards, glossary and practice problems.
# Every number in the steps and answers is computed here. Run: python3 tools/make_boundaries.py
import math, cmath, os, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lib import *
D=lambda s:"$$"+s+"$$"
EPS0=8.854187817e-12; MU0=4e-7*math.pi; ETA0=math.sqrt(MU0/EPS0)
T=["boundaries"]
deg=math.degrees; rad=math.radians

def oblique(n1,n2,ti):
    """theta_t, Gamma_perp, Gamma_par, R and T for nonmagnetic media (no total internal reflection)."""
    t=math.asin(n1/n2*math.sin(ti)); e1,e2=ETA0/n1,ETA0/n2
    gs=(e2*math.cos(ti)-e1*math.cos(t))/(e2*math.cos(ti)+e1*math.cos(t))
    gp=(e2*math.cos(t)-e1*math.cos(ti))/(e2*math.cos(t)+e1*math.cos(ti))
    return t,gs,gp

C=[
("Reflection coefficient at normal incidence?",D(r"\Gamma=\frac{E^r_0}{E^i_0}=\frac{\eta_2-\eta_1}{\eta_2+\eta_1}"),"equation",T),
("Transmission coefficient at normal incidence?",D(r"\tau=\frac{E^t_0}{E^i_0}=\frac{2\eta_2}{\eta_2+\eta_1}=1+\Gamma"),"equation",T),
("$\\Gamma$ for nonmagnetic media in terms of refractive index?",D(r"\Gamma=\frac{n_1-n_2}{n_1+n_2},\qquad n=\sqrt{\varepsilon_r}"),"equation",T),
("How does the normal-incidence problem map onto a transmission line?","Medium 1 is a line with $Z_0=\\eta_1$; medium 2 is its load $Z_L=\\eta_2$. $\\Gamma$, the standing-wave ratio and the positions of maxima and minima all follow the same formulas.","concept",T),
("Reflected and transmitted power fractions at normal incidence?",D(r"R=|\Gamma|^2,\qquad T=|\tau|^2\frac{\eta_1}{\eta_2}=1-R")+"For lossless media.","equation",T),
("Field in medium 1 in front of a perfect conductor?",D(r"\tilde E_1=E^i_0\left(e^{-jk_1z}-e^{jk_1z}\right)=-2jE^i_0\sin k_1z")+"A pure standing wave with nulls every $\\lambda_1/2$, starting at the conductor.","equation",T),
("Standing-wave ratio in medium 1?",D(r"S=\frac{|\tilde E_1|_{\max}}{|\tilde E_1|_{\min}}=\frac{1+|\Gamma|}{1-|\Gamma|}"),"equation",T),
("How does a quarter-wave antireflection coating work?","A layer $\\lambda/4$ thick with $\\eta_2=\\sqrt{\\eta_1\\eta_3}$ makes the two reflections cancel, exactly like a quarter-wave transformer on a line. For nonmagnetic media, $n_2=\\sqrt{n_1n_3}$.","concept",T),
("Snell's law of reflection and refraction?",D(r"\theta_r=\theta_i,\qquad n_1\sin\theta_i=n_2\sin\theta_t"),"equation",T),
("Critical angle?",D(r"\theta_c=\sin^{-1}\frac{n_2}{n_1}")+"Exists only going from a denser to a less dense medium ($n_1>n_2$). Beyond it, all power reflects.","equation",T),
("What happens beyond the critical angle?","Total internal reflection: $|\\Gamma|=1$ for both polarizations. A field still exists in medium 2, but it decays away from the boundary and carries no average power across it.","concept",T),
("Numerical aperture and acceptance angle of an optical fibre?",D(r"\sin\theta_a=\frac{1}{n_0}\sqrt{n_f^2-n_c^2}")+"$n_f$: core, $n_c$: cladding.","equation",T),
("Plane of incidence?","The plane containing the normal to the boundary and the direction of the incident wave.","concept",T),
("Perpendicular (TE) and parallel (TM) polarization?","Perpendicular, or TE: $\\mathbf{E}$ is normal to the plane of incidence. Parallel, or TM: $\\mathbf{E}$ lies in the plane of incidence. Any wave is a sum of the two.","concept",T),
("Reflection coefficient, perpendicular polarization?",D(r"\Gamma_\perp=\frac{\eta_2\cos\theta_i-\eta_1\cos\theta_t}{\eta_2\cos\theta_i+\eta_1\cos\theta_t},\qquad\tau_\perp=1+\Gamma_\perp"),"equation",T),
("Reflection coefficient, parallel polarization?",D(r"\Gamma_\parallel=\frac{\eta_2\cos\theta_t-\eta_1\cos\theta_i}{\eta_2\cos\theta_t+\eta_1\cos\theta_i}")+D(r"\tau_\parallel=(1+\Gamma_\parallel)\frac{\cos\theta_i}{\cos\theta_t}"),"equation",T),
("Brewster angle for nonmagnetic media?",D(r"\theta_B=\tan^{-1}\frac{n_2}{n_1}=\tan^{-1}\sqrt{\frac{\varepsilon_2}{\varepsilon_1}}")+"$\\Gamma_\\parallel=0$ there. Nonmagnetic media have no Brewster angle for perpendicular polarization.","equation",T),
("What is special about $\\theta_B+\\theta_t$?","At the Brewster angle, $\\theta_B+\\theta_t=90^\\circ$: the reflected and transmitted rays are perpendicular.","concept",T),
("Why is light reflected at the Brewster angle polarized?","Only the perpendicular component reflects, since $\\Gamma_\\parallel=0$. That is why polarized sunglasses cut glare off water and roads.","concept",T),
("Reflectivity and transmissivity at oblique incidence?",D(r"R=|\Gamma|^2,\qquad T=|\tau|^2\frac{\eta_1\cos\theta_t}{\eta_2\cos\theta_i},\qquad R+T=1")+"The cosines account for the change in beam cross-section.","equation",T),
]

G=[
("Reflection coefficient","\\Gamma","","Ratio of reflected to incident electric field at a boundary.","normalinc",T),
("Transmission coefficient","\\tau","","Ratio of transmitted to incident electric field at a boundary.","normalinc",T),
("Reflectivity","R=|\\Gamma|^2","","Fraction of incident power that reflects.","normalinc",T),
("Transmissivity","T","","Fraction of incident power that crosses the boundary. $R+T=1$ for lossless media.","normalinc",T),
("Refractive index","n=\\sqrt{\\mu_r\\varepsilon_r}","","Ratio of the speed of light in vacuum to the phase velocity in the medium.","oblique",T),
("Antireflection coating","","","A quarter-wave layer whose impedance is the geometric mean of the media on either side, so reflections cancel.","normalinc",T),
("Snell's law","","","$n_1\\sin\\theta_i=n_2\\sin\\theta_t$, with $\\theta_r=\\theta_i$.","oblique",T),
("Plane of incidence","","","The plane containing the incident direction and the normal to the boundary.","oblique",T),
("Perpendicular polarization","\\perp","","$\\mathbf{E}$ normal to the plane of incidence. Also called TE or s-polarization.","oblique",T),
("Parallel polarization","\\parallel","","$\\mathbf{E}$ in the plane of incidence. Also called TM or p-polarization.","oblique",T),
("Critical angle","\\theta_c","^\\circ","Incidence angle beyond which a wave going into a less dense medium is totally reflected.","oblique",T),
("Total internal reflection","","","Complete reflection beyond the critical angle. It guides light along optical fibres.","oblique",T),
("Brewster angle","\\theta_B","^\\circ","Incidence angle at which the parallel component is fully transmitted.","oblique",T),
("Optical fibre","","","A glass core inside a cladding of slightly lower index, which guides light by total internal reflection.","oblique",T),
]

P=[]
def add(**k): k.setdefault("source","original"); k.setdefault("topics",T); P.append(k)

er=4; e2=ETA0/2; G_=(e2-ETA0)/(e2+ETA0); tau=1+G_; S=(1+abs(G_))/(1-abs(G_))
add(difficulty=1,title="Air onto glass at normal incidence",
 prompt="A plane wave in air hits a glass surface ($\\varepsilon_r=4$, $\\mu_r=1$) at normal incidence. Find $\\Gamma$, $\\tau$, the standing-wave ratio in air, and the fractions of power reflected and transmitted.",
 hints=["$\\eta_2=\\eta_0/\\sqrt{\\varepsilon_r}$.","$R=|\\Gamma|^2$, $T=1-R$."],
 steps=[D(f"\\eta_2=\\frac{{\\eta_0}}{{2}}={tr(e2)}\\ \\Omega"),D(f"\\Gamma=\\frac{{\\eta_2-\\eta_0}}{{\\eta_2+\\eta_0}}={tr(G_)},\\qquad\\tau=1+\\Gamma={tr(tau)}"),D(f"S=\\frac{{1+|\\Gamma|}}{{1-|\\Gamma|}}={tr(S)}"),D(f"R=|\\Gamma|^2={tr(G_**2)},\\qquad T=1-R={tr(1-G_**2)}")],
 answers=[{"label":r"\Gamma","value":tr(G_)},{"label":r"\tau","value":tr(tau)},{"label":"S","value":tr(S)},{"label":"R","value":tr(G_**2)},{"label":"T","value":tr(1-G_**2)}],widget="normalinc")

er,E0=9,10; e2=ETA0/3; G_=(e2-ETA0)/(e2+ETA0); tau=1+G_; Si=E0**2/(2*ETA0); Sr=(G_*E0)**2/(2*ETA0); St=(tau*E0)**2/(2*e2)
add(difficulty=2,title="Checking power balance",
 prompt="A $10\\ \\mathrm{V/m}$ plane wave in air hits a dielectric with $\\varepsilon_r=9$ at normal incidence. Find the reflected and transmitted field amplitudes and the three average power densities, and check that power balances.",
 hints=["$S_{\\mathrm{av}}=|E|^2/(2\\eta)$ in each medium, using that medium's $\\eta$."],
 steps=[D(f"\\Gamma=\\frac{{1-3}}{{1+3}}={tr(G_)},\\qquad\\tau={tr(tau)}"),D(f"E^r_0={tr(G_*E0)}\\ \\mathrm{{V/m}},\\qquad E^t_0={tr(tau*E0)}\\ \\mathrm{{V/m}}"),
        D(f"S^i=\\frac{{10^2}}{{2\\eta_0}}={teng(Si,'W/m^2')},\\quad S^r=\\frac{{{tr(abs(G_*E0))}^2}}{{2\\eta_0}}={teng(Sr,'W/m^2')}"),D(f"S^t=\\frac{{{tr(tau*E0)}^2}}{{2(\\eta_0/3)}}={teng(St,'W/m^2')}"),D(f"S^r+S^t={teng(Sr+St,'W/m^2')}=S^i")],
 answers=[{"label":"E^r_0","value":f"{tr(G_*E0)}\\ \\mathrm{{V/m}}"},{"label":"E^t_0","value":f"{tr(tau*E0)}\\ \\mathrm{{V/m}}"},{"label":"S^i","value":teng(Si,'W/m^2')},{"label":"S^r","value":teng(Sr,'W/m^2')},{"label":"S^t","value":teng(St,'W/m^2')}],widget="normalinc")

f,E0=1e9,5; lam=3e8/f
add(difficulty=2,title="Standing wave in front of a metal plate",
 prompt="A $1\\ \\mathrm{GHz}$ plane wave with $E^i_0=5\\ \\mathrm{V/m}$ in air hits a perfectly conducting plate at $z=0$ at normal incidence. Write the total field in air, and find where it is zero and where it is largest.",
 hints=["$\\Gamma=-1$ at a perfect conductor ($\\eta_2=0$).","$e^{-jx}-e^{jx}=-2j\\sin x$."],
 steps=[D(r"\tilde E_1(z)=5\left(e^{-jk_1z}-e^{jk_1z}\right)=-10j\sin k_1z"),D(r"E_1(z,t)=\mathrm{Re}\{\tilde E_1e^{j\omega t}\}=10\sin k_1z\,\sin\omega t\ \mathrm{V/m}"),D(f"\\lambda=\\frac{{3\\times10^8}}{{10^9}}={teng(lam,'m')}"),f"Zeros at $z=-n\\lambda/2$: $0,\\ -{teng(lam/2,'m')},\\ -{teng(lam,'m')},\\dots$",f"Maxima of $10\\ \\mathrm{{V/m}}$ at $z=-\\lambda/4-n\\lambda/2$: $-{teng(lam/4,'m')},\\ -{teng(3*lam/4,'m')},\\dots$"],
 answers=[{"label":r"E_1(z,t)","value":r"10\sin k_1z\,\sin\omega t\ \mathrm{V/m}"},{"label":"\\text{first null}","value":f"z=-{teng(lam/2,'m')}"},{"label":"\\text{first maximum}","value":f"z=-{teng(lam/4,'m')}"}],widget="normalinc")

f,s,er=1e6,4,81; w=2*math.pi*f; e2=cmath.sqrt(1j*w*MU0/(s+1j*w*er*EPS0)); G_=(e2-ETA0)/(e2+ETA0); R=abs(G_)**2
add(difficulty=3,title="Radio waves into the sea",
 prompt="A $1\\ \\mathrm{MHz}$ plane wave in air hits the sea ($\\sigma=4\\ \\mathrm{S/m}$, $\\varepsilon_r=81$) at normal incidence. Find $\\eta_2$, $\\Gamma$ and the fraction of power that enters the water.",
 hints=["Seawater is a good conductor at 1 MHz: $\\eta_c\\approx(1+j)\\sqrt{\\pi f\\mu/\\sigma}$.","The power fraction that enters is $1-|\\Gamma|^2$."],
 steps=[D(f"\\eta_2=\\sqrt{{\\frac{{j\\omega\\mu_0}}{{\\sigma+j\\omega\\varepsilon}}}}={tc(e2)}\\ \\Omega"),D(f"\\Gamma=\\frac{{\\eta_2-\\eta_0}}{{\\eta_2+\\eta_0}}={tc(G_,4)}={tp(G_,4)}"),D(f"1-|\\Gamma|^2={tr(1-R)}"),f"Only about {r(100*(1-R),2)}% of the power enters the sea, and that part dies within a few skin depths."],
 answers=[{"label":r"\eta_2","value":f"{tc(e2)}\\ \\Omega"},{"label":r"\Gamma","value":tp(G_,4)},{"label":"T","value":tr(1-R)}],widget="normalinc")

n3,l0=1.5,600e-9; n2=math.sqrt(n3); d=l0/(4*n2); G0=(1-n3)/(1+n3)
add(difficulty=2,title="Antireflection coating for a lens",
 prompt="Glass has $n=1.5$. How much light (at normal incidence) reflects from bare glass in air? Design a single-layer antireflection coating for $\\lambda_0=600\\ \\mathrm{nm}$: find its refractive index and thickness.",
 hints=["$\\Gamma=(n_1-n_2)/(n_1+n_2)$.","The coating needs $n_2=\\sqrt{n_1n_3}$ and a thickness of a quarter of the wavelength inside it."],
 steps=[D(f"\\Gamma=\\frac{{1-1.5}}{{1+1.5}}={tr(G0)},\\qquad R={tr(G0**2)}"),"About 4% of the light reflects from each bare surface.",D(f"n_2=\\sqrt{{(1)(1.5)}}={tr(n2)}"),D(f"d=\\frac{{\\lambda_0}}{{4n_2}}=\\frac{{600}}{{4({tr(n2)})}}={teng(d,'m')}")],
 answers=[{"label":"R\\ (\\text{bare})","value":tr(G0**2)},{"label":"n_2","value":tr(n2)},{"label":"d","value":teng(d,'m')}],widget="normalinc")

n1,n2,ti=1,1.33,30; tt=deg(math.asin(n1/n2*math.sin(rad(ti))))
add(difficulty=1,title="Light entering water",
 prompt="Light in air hits a still water surface ($n=1.33$) at $30^\\circ$ from the normal. Find the angles of reflection and transmission.",
 hints=["$\\theta_r=\\theta_i$ and $n_1\\sin\\theta_i=n_2\\sin\\theta_t$."],
 steps=[D(r"\theta_r=\theta_i=30^\circ"),D(f"\\sin\\theta_t=\\frac{{\\sin30^\\circ}}{{1.33}}={tr(math.sin(rad(tt)))}\\ \\Rightarrow\\ \\theta_t={tr(tt)}^\\circ"),"The wave bends toward the normal going into the denser medium."],
 answers=[{"label":r"\theta_r","value":"30^\\circ"},{"label":r"\theta_t","value":f"{tr(tt)}^\\circ"}],widget="oblique")

n1,n2=1.5,1; tc_=deg(math.asin(n2/n1))
add(difficulty=1,title="Critical angle of glass",
 prompt="Light travels inside glass ($n=1.5$) toward a glass–air surface. Find the critical angle. What happens to a ray that arrives at $50^\\circ$?",
 hints=["$\\theta_c=\\sin^{-1}(n_2/n_1)$."],
 steps=[D(f"\\theta_c=\\sin^{{-1}}\\frac{{1}}{{1.5}}={tr(tc_)}^\\circ"),f"$50^\\circ>{tr(tc_)}^\\circ$, so the ray is totally internally reflected. That is how a prism with $45^\\circ$ faces works as a mirror."],
 answers=[{"label":r"\theta_c","value":f"{tr(tc_)}^\\circ"},{"label":"50^\\circ","value":"\\text{total internal reflection}"}],widget="oblique")

nf,nc=1.52,1.49; tcf=deg(math.asin(nc/nf)); NA=math.sqrt(nf**2-nc**2); ta=deg(math.asin(NA))
add(difficulty=2,title="Acceptance angle of an optical fibre",
 prompt="An optical fibre has a core with $n_f=1.52$ and cladding with $n_c=1.49$. Find the critical angle at the core–cladding boundary, the numerical aperture and the acceptance angle in air.",
 hints=["$\\sin\\theta_a=\\sqrt{n_f^2-n_c^2}/n_0$ with $n_0=1$."],
 steps=[D(f"\\theta_c=\\sin^{{-1}}\\frac{{1.49}}{{1.52}}={tr(tcf)}^\\circ"),D(f"\\mathrm{{NA}}=\\sqrt{{1.52^2-1.49^2}}={tr(NA)}"),D(f"\\theta_a=\\sin^{{-1}}({tr(NA)})={tr(ta)}^\\circ"),"Light entering the end face within this angle of the axis stays trapped in the core."],
 answers=[{"label":r"\theta_c","value":f"{tr(tcf)}^\\circ"},{"label":r"\mathrm{NA}","value":tr(NA)},{"label":r"\theta_a","value":f"{tr(ta)}^\\circ"}],widget="oblique")

n1,n2=1,1.5; tB=deg(math.atan(n2/n1)); t,gs,gp=oblique(n1,n2,rad(tB))
add(difficulty=2,title="Brewster angle of glass",
 prompt="Find the Brewster angle for light going from air into glass ($n=1.5$), the transmission angle there, and the fraction of perpendicularly polarized power that reflects.",
 hints=["$\\theta_B=\\tan^{-1}(n_2/n_1)$.","Use $\\Gamma_\\perp$ with $\\eta=\\eta_0/n$."],
 steps=[D(f"\\theta_B=\\tan^{{-1}}1.5={tr(tB)}^\\circ"),D(f"\\theta_t=\\sin^{{-1}}\\frac{{\\sin\\theta_B}}{{1.5}}={tr(deg(t))}^\\circ"),f"Check: $\\theta_B+\\theta_t={tr(tB+deg(t))}^\\circ$.",D(f"\\Gamma_\\perp=\\frac{{\\cos\\theta_i-1.5\\cos\\theta_t}}{{\\cos\\theta_i+1.5\\cos\\theta_t}}={tr(gs)},\\qquad R_\\perp={tr(gs**2)}"),"Only about 15% of the perpendicular part reflects, and none of the parallel part, so the reflected light is fully polarized."],
 answers=[{"label":r"\theta_B","value":f"{tr(tB)}^\\circ"},{"label":r"\theta_t","value":f"{tr(deg(t))}^\\circ"},{"label":r"R_\perp","value":tr(gs**2)}],widget="oblique")

n1,n2,ti=1,2,30; t,gs,gp=oblique(n1,n2,rad(ti)); ts=1+gs; tp_=(1+gp)*math.cos(rad(ti))/math.cos(t)
Ts=ts**2*n2*math.cos(t)/(n1*math.cos(rad(ti))); Tp=tp_**2*n2*math.cos(t)/(n1*math.cos(rad(ti)))
assert abs(Ts+gs**2-1)<1e-12 and abs(Tp+gp**2-1)<1e-12
add(difficulty=3,title="Both polarizations at 30 degrees",
 prompt="A plane wave in air hits a dielectric with $\\varepsilon_r=4$ at $\\theta_i=30^\\circ$. Find $\\theta_t$, then $\\Gamma$, $\\tau$, $R$ and $T$ for both perpendicular and parallel polarization.",
 hints=["$n_2=2$, so $\\eta_2=\\eta_0/2$.","$T=|\\tau|^2\\frac{\\eta_1\\cos\\theta_t}{\\eta_2\\cos\\theta_i}$; check $R+T=1$."],
 steps=[D(f"\\theta_t=\\sin^{{-1}}\\frac{{\\sin30^\\circ}}{{2}}={tr(deg(t))}^\\circ"),D(f"\\Gamma_\\perp=\\frac{{\\tfrac12\\cos30^\\circ-\\cos\\theta_t}}{{\\tfrac12\\cos30^\\circ+\\cos\\theta_t}}={tr(gs)},\\qquad\\tau_\\perp={tr(ts)}"),
        D(f"\\Gamma_\\parallel=\\frac{{\\tfrac12\\cos\\theta_t-\\cos30^\\circ}}{{\\tfrac12\\cos\\theta_t+\\cos30^\\circ}}={tr(gp)},\\qquad\\tau_\\parallel={tr(tp_)}"),D(f"R_\\perp={tr(gs**2)},\\quad T_\\perp={tr(Ts)},\\quad R_\\parallel={tr(gp**2)},\\quad T_\\parallel={tr(Tp)}"),"The parallel component reflects less: it is heading toward its Brewster angle of 63.4°."],
 answers=[{"label":r"\theta_t","value":f"{tr(deg(t))}^\\circ"},{"label":r"\Gamma_\perp","value":tr(gs)},{"label":r"\Gamma_\parallel","value":tr(gp)},{"label":r"R_\perp,\ T_\perp","value":f"{tr(gs**2)},\\ {tr(Ts)}"},{"label":r"R_\parallel,\ T_\parallel","value":f"{tr(gp**2)},\\ {tr(Tp)}"}],widget="oblique")

n1,n2=1,1.33; tB=deg(math.atan(n2)); t,gs,gp=oblique(n1,n2,rad(tB)); Rtot=(gs**2+gp**2)/2
add(difficulty=2,title="Glare off a lake",
 prompt="Unpolarized sunlight (equal perpendicular and parallel power) hits a lake ($n=1.33$) at the Brewster angle. Find the angle, and the fraction of the total incident power that reflects. Which polarization is it?",
 hints=["At $\\theta_B$, $\\Gamma_\\parallel=0$.","Each polarization carries half the incident power."],
 steps=[D(f"\\theta_B=\\tan^{{-1}}1.33={tr(tB)}^\\circ,\\qquad\\theta_t=90^\\circ-\\theta_B={tr(deg(t))}^\\circ"),D(f"\\Gamma_\\perp={tr(gs)},\\qquad R_\\perp={tr(gs**2)}"),D(f"R=\\tfrac12R_\\perp+\\tfrac12(0)={tr(Rtot)}"),"The reflected glare is all perpendicular, which is horizontal for a flat lake, so vertically polarized sunglasses block it."],
 answers=[{"label":r"\theta_B","value":f"{tr(tB)}^\\circ"},{"label":"R","value":tr(Rtot)},{"label":"\\text{polarization}","value":"\\perp\\ (\\text{horizontal})"}],widget="oblique")

write_unit("reflection-at-boundaries","Reflection at boundaries",C,G,P)
