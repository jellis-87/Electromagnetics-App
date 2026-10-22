# Plane waves: flashcards, glossary and practice problems.
# Every number in the steps and answers is computed here. Run: python3 tools/make_planewaves.py
import math, cmath, os, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lib import *
D=lambda s:"$$"+s+"$$"
EPS0=8.854187817e-12; MU0=4e-7*math.pi; ETA0=math.sqrt(MU0/EPS0)
T=["plane-waves"]

def medium(f,er,mr,s):
    """alpha, beta, complex eta for a general medium (exact formulas)."""
    w=2*math.pi*f; eps=er*EPS0; mu=mr*MU0
    g=cmath.sqrt(1j*w*mu*(s+1j*w*eps)); eta=cmath.sqrt(1j*w*mu/(s+1j*w*eps))
    return g.real,g.imag,eta

C=[
("Helmholtz equation for $\\tilde{\\mathbf{E}}$ in a source-free lossless medium?",D(r"\nabla^2\tilde{\mathbf{E}}+k^2\tilde{\mathbf{E}}=0,\qquad k=\omega\sqrt{\mu\varepsilon}"),"equation",T),
("What is a uniform plane wave?","A wave whose $\\mathbf{E}$ and $\\mathbf{H}$ have the same magnitude and phase over every plane normal to the direction of travel. A good model of any wave far from its source.","concept",T),
("How are $\\mathbf{E}$, $\\mathbf{H}$ and the direction of travel $\\hat{\\mathbf{k}}$ arranged?","All three are mutually perpendicular, with $\\mathbf{E}\\times\\mathbf{H}$ pointing along $\\hat{\\mathbf{k}}$. The wave is TEM: no field component along the direction of travel.","concept",T),
("$\\tilde{\\mathbf{H}}$ from $\\tilde{\\mathbf{E}}$ for a plane wave?",D(r"\tilde{\mathbf{H}}=\frac{1}{\eta}\,\hat{\mathbf{k}}\times\tilde{\mathbf{E}},\qquad\tilde{\mathbf{E}}=-\eta\,\hat{\mathbf{k}}\times\tilde{\mathbf{H}}"),"equation",T),
("Phase constant, phase velocity and wavelength in a lossless medium?",D(r"\beta=\omega\sqrt{\mu\varepsilon},\quad u_p=\frac{1}{\sqrt{\mu\varepsilon}}=\frac{c}{\sqrt{\mu_r\varepsilon_r}},\quad\lambda=\frac{2\pi}{\beta}"),"equation",T),
("Intrinsic impedance of a lossless medium?",D(r"\eta=\sqrt{\frac{\mu}{\varepsilon}}=\eta_0\sqrt{\frac{\mu_r}{\varepsilon_r}}"),"equation",T),
("Intrinsic impedance of free space?",D(r"\eta_0=\sqrt{\frac{\mu_0}{\varepsilon_0}}\approx120\pi\approx377\ \Omega"),"equation",T),
("Propagation constant of a lossy medium?",D(r"\gamma=\alpha+j\beta=j\omega\sqrt{\mu\varepsilon_c},\qquad\varepsilon_c=\varepsilon-j\frac{\sigma}{\omega}"),"equation",T),
("Exact $\\alpha$ and $\\beta$ in a lossy medium?",D(r"\alpha=\omega\sqrt{\frac{\mu\varepsilon}{2}\left[\sqrt{1+\left(\frac{\sigma}{\omega\varepsilon}\right)^2}-1\right]}")+D(r"\beta=\omega\sqrt{\frac{\mu\varepsilon}{2}\left[\sqrt{1+\left(\frac{\sigma}{\omega\varepsilon}\right)^2}+1\right]}"),"equation",T),
("Intrinsic impedance of a lossy medium?",D(r"\eta_c=\sqrt{\frac{j\omega\mu}{\sigma+j\omega\varepsilon}}=|\eta_c|e^{j\theta_\eta}")+"$\\mathbf{H}$ lags $\\mathbf{E}$ by $\\theta_\\eta$.","equation",T),
("Low-loss dielectric approximations ($\\sigma/\\omega\\varepsilon\\ll1$)?",D(r"\alpha\approx\frac{\sigma}{2}\sqrt{\frac{\mu}{\varepsilon}},\quad\beta\approx\omega\sqrt{\mu\varepsilon},\quad\eta_c\approx\sqrt{\frac{\mu}{\varepsilon}}"),"equation",T),
("Good-conductor approximations ($\\sigma/\\omega\\varepsilon\\gg1$)?",D(r"\alpha=\beta\approx\sqrt{\pi f\mu\sigma},\qquad\eta_c\approx(1+j)\frac{\alpha}{\sigma}"),"equation",T),
("Skin depth?",D(r"\delta_s=\frac{1}{\alpha}\ \xrightarrow{\text{good conductor}}\ \frac{1}{\sqrt{\pi f\mu\sigma}}")+"The depth where the field falls to $1/e$ (about 37%) of its surface value.","equation",T),
("Skin depth of copper at 60 Hz, 1 MHz and 10 GHz?",f"About {r(1/math.sqrt(math.pi*60*MU0*5.8e7)*1e3)} mm, {r(1/math.sqrt(math.pi*1e6*MU0*5.8e7)*1e6)} µm and {r(1/math.sqrt(math.pi*1e10*MU0*5.8e7)*1e6)} µm. It scales as $1/\\sqrt{{f}}$.","concept",T),
("Phase angle of $\\eta_c$ in a good conductor?","$45^\\circ$: $\\mathbf{H}$ lags $\\mathbf{E}$ by an eighth of a cycle. In a lossless medium the angle is $0$.","concept",T),
("Poynting vector?",D(r"\mathbf{S}=\mathbf{E}\times\mathbf{H}\ \ (\mathrm{W/m^2}),\qquad\mathbf{S}_{\mathrm{av}}=\tfrac12\mathrm{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\}"),"equation",T),
("Average power density of a plane wave in a lossless medium?",D(r"S_{\mathrm{av}}=\frac{|E_0|^2}{2\eta}"),"equation",T),
("Average power density in a lossy medium?",D(r"S_{\mathrm{av}}(z)=\frac{|E_0|^2}{2|\eta_c|}e^{-2\alpha z}\cos\theta_\eta")+"Power decays twice as fast (in nepers) as the field.","equation",T),
("Attenuation in decibels?",D(r"A=20\log_{10}e^{\alpha z}=8.686\,\alpha z\ \ \mathrm{dB}")+"So 1 Np = 8.686 dB.","equation",T),
("Why does a good conductor make a poor medium for waves?","$\\alpha=\\beta$, so the field falls by $e^{-2\\pi}$, about 0.2%, in one wavelength. The wave dies within a few skin depths.","concept",T),
("Surface resistance of a good conductor?",D(r"R_s=\frac{1}{\sigma\delta_s}=\sqrt{\frac{\pi f\mu}{\sigma}}\ \ \Omega")+"It equals the real part of $\\eta_c$, and it is the AC resistance of a skin-depth-thick sheet.","equation",T),
("What is dispersion?","When the phase velocity depends on frequency, so a pulse made of many frequencies spreads out. Lossy media are dispersive: in a good conductor $u_p=\\sqrt{4\\pi f/\\mu\\sigma}$.","concept",T),
]

G=[
("Uniform plane wave","","","A wave with uniform magnitude and phase over every plane normal to its direction of travel.","planewave",T),
("TEM wave","","","Transverse electromagnetic: $\\mathbf{E}$ and $\\mathbf{H}$ both perpendicular to the direction of travel.","planewave",T),
("Wavenumber","k=\\omega\\sqrt{\\mu\\varepsilon}","\\mathrm{rad/m}","Phase change per unit length in a lossless medium. Equal to $\\beta$ there.","planewave",T),
("Intrinsic impedance","\\eta","\\Omega","Ratio of $E$ to $H$ in a plane wave. $\\sqrt{\\mu/\\varepsilon}$ for a lossless medium, complex for a lossy one.","planewave",T),
("Propagation constant","\\gamma=\\alpha+j\\beta","\\mathrm{m^{-1}}","Sets how a wave decays and shifts phase with distance: $e^{-\\gamma z}$.","planewave",T),
("Attenuation constant","\\alpha","\\mathrm{Np/m}","Rate at which the field amplitude decays, $e^{-\\alpha z}$.","planewave",T),
("Phase constant","\\beta","\\mathrm{rad/m}","Phase change per unit length. $\\lambda=2\\pi/\\beta$, $u_p=\\omega/\\beta$.","planewave",T),
("Skin depth","\\delta_s","\\mathrm{m}","Depth at which a wave in a conductor falls to $1/e$ of its surface value: $1/\\alpha$.","skindepth",T),
("Surface resistance","R_s=1/(\\sigma\\delta_s)","\\Omega","Resistance of a square of conductor surface at high frequency, where current flows within about a skin depth.","skindepth",T),
("Poynting vector","\\mathbf{S}=\\mathbf{E}\\times\\mathbf{H}","\\mathrm{W/m^2}","Power flow per unit area. Its direction is the direction energy travels.","planewave",T),
("Neper","\\mathrm{Np}","","Natural-log unit for field ratios: a field that falls by $e^{-1}$ has lost 1 Np, or 8.686 dB.","planewave",T),
("Dispersion","","","Phase velocity that changes with frequency, which spreads pulses out.",None,T),
("Good conductor (waves)","","","A medium with $\\sigma/(\\omega\\varepsilon)>100$ or so, where $\\alpha\\approx\\beta\\approx\\sqrt{\\pi f\\mu\\sigma}$.","skindepth",T),
("Low-loss dielectric (waves)","","","A medium with $\\sigma/(\\omega\\varepsilon)<0.01$ or so, where $\\beta$ and $\\eta$ are nearly the lossless values.","planewave",T),
]

P=[]
def add(**k): k.setdefault("source","original"); k.setdefault("topics",T); P.append(k)

w=6*math.pi*1e8; be=4*math.pi; f=w/(2*math.pi); lam=2*math.pi/be; up=w/be; er=(3e8/up)**2; eta=ETA0/math.sqrt(er); H0=20/eta
add(difficulty=1,title="Reading a plane wave",
 prompt="In a nonmagnetic lossless medium, $\\mathbf{E}=\\hat{\\mathbf{y}}\\,20\\cos(6\\pi\\times10^8t-4\\pi z)\\ \\mathrm{V/m}$. Find $f$, $\\lambda$, $u_p$, $\\varepsilon_r$, $\\eta$ and $\\mathbf{H}$.",
 hints=["Read $\\omega$ and $\\beta$ off the argument of the cosine.","$\\tilde{\\mathbf{H}}=\\frac{1}{\\eta}\\hat{\\mathbf{k}}\\times\\tilde{\\mathbf{E}}$ with $\\hat{\\mathbf{k}}=\\hat{\\mathbf{z}}$."],
 steps=[D(f"f=\\frac{{\\omega}}{{2\\pi}}={teng(f,'Hz')},\\qquad\\lambda=\\frac{{2\\pi}}{{\\beta}}={teng(lam,'m')}"),D(f"u_p=\\frac{{\\omega}}{{\\beta}}={tsci(up,'m/s')}"),D(f"\\varepsilon_r=\\left(\\frac{{3\\times10^8}}{{u_p}}\\right)^2={tr(er)},\\qquad\\eta=\\frac{{\\eta_0}}{{\\sqrt{{\\varepsilon_r}}}}={tr(eta)}\\ \\Omega"),
        D(r"\hat{\mathbf{z}}\times\hat{\mathbf{y}}=-\hat{\mathbf{x}}"),D(f"\\mathbf{{H}}=-\\hat{{\\mathbf{{x}}}}\\,{teng(H0,'A/m')}\\cos(6\\pi\\times10^8t-4\\pi z)")],
 answers=[{"label":"f","value":teng(f,'Hz')},{"label":r"\lambda","value":teng(lam,'m')},{"label":"u_p","value":tsci(up,'m/s')},{"label":r"\varepsilon_r","value":tr(er)},{"label":r"\eta","value":f"{tr(eta)}\\ \\Omega"},{"label":r"\mathbf{H}","value":f"-\\hat{{\\mathbf{{x}}}}\\,{teng(H0,'A/m')}\\cos(6\\pi\\times10^8t-4\\pi z)"}],widget="planewave")

f,er=1e9,2.25; be=2*math.pi*f*math.sqrt(er)/c; up=c/math.sqrt(er); lam=up/f; eta=ETA0/math.sqrt(er)
add(difficulty=1,title="Wave in polyethylene",
 prompt="A 1 GHz plane wave travels in polyethylene ($\\varepsilon_r=2.25$, $\\mu_r=1$, lossless). Find $\\beta$, $u_p$, $\\lambda$ and $\\eta$, and compare $\\lambda$ with its free-space value.",
 hints=["$u_p=c/\\sqrt{\\varepsilon_r}$ and $\\eta=\\eta_0/\\sqrt{\\varepsilon_r}$."],
 steps=[D(f"u_p=\\frac{{c}}{{\\sqrt{{2.25}}}}={tsci(up,'m/s')}"),D(f"\\beta=\\frac{{\\omega}}{{u_p}}={tr(be)}\\ \\mathrm{{rad/m}},\\qquad\\lambda=\\frac{{u_p}}{{f}}={teng(lam,'m')}"),D(f"\\eta=\\frac{{{tr(ETA0)}}}{{1.5}}={tr(eta)}\\ \\Omega"),f"In free space $\\lambda_0={teng(c/f,'m')}$, so the wave is $1.5$ times shorter in polyethylene."],
 answers=[{"label":r"\beta","value":f"{tr(be)}\\ \\mathrm{{rad/m}}"},{"label":"u_p","value":tsci(up,'m/s')},{"label":r"\lambda","value":teng(lam,'m')},{"label":r"\eta","value":f"{tr(eta)}\\ \\Omega"}],widget="planewave")

H0=0.1; E0=ETA0*H0
add(difficulty=2,title="E from H for a wave going the other way",
 prompt="In free space, $\\mathbf{H}=\\hat{\\mathbf{z}}\\,0.1\\cos(\\omega t+\\beta y)\\ \\mathrm{A/m}$. Which way does the wave travel? Find $\\mathbf{E}$.",
 hints=["$\\omega t+\\beta y$ means the wave moves toward $-y$.","$\\tilde{\\mathbf{E}}=-\\eta_0\\,\\hat{\\mathbf{k}}\\times\\tilde{\\mathbf{H}}$."],
 steps=["The phase is constant when $\\omega t+\\beta y$ is constant, so $y$ decreases as $t$ grows: $\\hat{\\mathbf{k}}=-\\hat{\\mathbf{y}}$.",D(r"\tilde{\mathbf{E}}=-\eta_0(-\hat{\mathbf{y}})\times\hat{\mathbf{z}}\,0.1e^{j\beta y}=\eta_0\,(0.1)\,\hat{\mathbf{x}}\,e^{j\beta y}"),D(f"\\mathbf{{E}}=\\hat{{\\mathbf{{x}}}}\\,{tr(E0)}\\cos(\\omega t+\\beta y)\\ \\mathrm{{V/m}}"),"Check: $\\hat{\\mathbf{x}}\\times\\hat{\\mathbf{z}}=-\\hat{\\mathbf{y}}$, the direction of travel."],
 answers=[{"label":r"\hat{\mathbf{k}}","value":r"-\hat{\mathbf{y}}"},{"label":r"\mathbf{E}","value":f"\\hat{{\\mathbf{{x}}}}\\,{tr(E0)}\\cos(\\omega t+\\beta y)\\ \\mathrm{{V/m}}"}],widget="planewave")

E0=50; Sav=E0**2/(2*ETA0); A=0.5
add(difficulty=1,title="Power density in free space",
 prompt="A plane wave in air has a peak electric field of $50\\ \\mathrm{V/m}$. Find the average power density and the power collected by a $0.5\\ \\mathrm{m^2}$ aperture facing the wave.",
 hints=["$S_{\\mathrm{av}}=|E_0|^2/(2\\eta_0)$."],
 steps=[D(f"S_{{\\mathrm{{av}}}}=\\frac{{50^2}}{{2({tr(ETA0)})}}={teng(Sav,'W/m^2')}"),D(f"P=S_{{\\mathrm{{av}}}}A={teng(Sav*A,'W')}")],
 answers=[{"label":r"S_{\mathrm{av}}","value":teng(Sav,'W/m^2')},{"label":"P","value":teng(Sav*A,'W')}],widget="planewave")

f,er,s=1e7,3,1e-4; al,be,eta=medium(f,er,1,s); ratio=s/(2*math.pi*f*er*EPS0)
ala=s/2*ETA0/math.sqrt(er); bea=2*math.pi*f*math.sqrt(er)/c
add(difficulty=2,title="Dry soil as a low-loss dielectric",
 prompt="Dry soil has $\\varepsilon_r=3$, $\\mu_r=1$ and $\\sigma=10^{-4}\\ \\mathrm{S/m}$. At $10\\ \\mathrm{MHz}$, check that it is a low-loss dielectric, then find $\\alpha$, $\\beta$, $\\eta_c$ and the distance over which the field falls by half.",
 hints=["Compute $\\sigma/(\\omega\\varepsilon)$ first.","Low-loss: $\\alpha\\approx\\frac{\\sigma}{2}\\eta$, $\\beta\\approx\\omega\\sqrt{\\mu\\varepsilon}$.","The field halves when $e^{-\\alpha z}=0.5$."],
 steps=[D(f"\\frac{{\\sigma}}{{\\omega\\varepsilon}}=\\frac{{10^{{-4}}}}{{2\\pi(10^7)(3)\\varepsilon_0}}={tr(ratio)}"),"That is well below 1, so the low-loss formulas apply.",D(f"\\alpha\\approx\\frac{{\\sigma}}{{2}}\\frac{{\\eta_0}}{{\\sqrt{{3}}}}={tsci(ala,'Np/m')}"),D(f"\\beta\\approx\\frac{{\\omega\\sqrt{{3}}}}{{c}}={tr(bea)}\\ \\mathrm{{rad/m}},\\qquad\\eta_c\\approx\\frac{{\\eta_0}}{{\\sqrt3}}={tr(abs(eta))}\\ \\Omega"),
        D(f"z_{{1/2}}=\\frac{{\\ln2}}{{\\alpha}}={teng(math.log(2)/ala,'m')}"),f"The exact formulas give $\\alpha={tsci(al,'Np/m')}$ and $\\eta_c={tp(eta)}\\ \\Omega$: the approximations are good to well under 1%."],
 answers=[{"label":r"\sigma/\omega\varepsilon","value":tr(ratio)},{"label":r"\alpha","value":tsci(ala,'Np/m')},{"label":r"\beta","value":f"{tr(bea)}\\ \\mathrm{{rad/m}}"},{"label":r"\eta_c","value":f"{tr(abs(eta))}\\ \\Omega"},{"label":"z_{1/2}","value":teng(math.log(2)/ala,'m')}],widget="planewave")

f,er,s=1e8,10,0.05; al,be,eta=medium(f,er,1,s); ratio=s/(2*math.pi*f*er*EPS0)
add(difficulty=3,title="A medium that is neither",
 prompt="Wet clay has $\\varepsilon_r=10$, $\\mu_r=1$ and $\\sigma=0.05\\ \\mathrm{S/m}$. At $100\\ \\mathrm{MHz}$ find $\\sigma/(\\omega\\varepsilon)$, then use the exact formulas for $\\alpha$, $\\beta$ and $\\eta_c$. Find the skin depth and the wavelength.",
 hints=["When $\\sigma/(\\omega\\varepsilon)$ is near 1, neither approximation works.","$\\eta_c=\\sqrt{j\\omega\\mu/(\\sigma+j\\omega\\varepsilon)}$."],
 steps=[D(f"\\frac{{\\sigma}}{{\\omega\\varepsilon}}={tr(ratio)}"),D(r"\alpha=\omega\sqrt{\frac{\mu\varepsilon}{2}\left[\sqrt{1+(%s)^2}-1\right]}=%s\ \mathrm{Np/m}"%(tr(ratio),tr(al))),D(r"\beta=\omega\sqrt{\frac{\mu\varepsilon}{2}\left[\sqrt{1+(%s)^2}+1\right]}=%s\ \mathrm{rad/m}"%(tr(ratio),tr(be))),
        D(f"\\eta_c=\\sqrt{{\\frac{{j\\omega\\mu_0}}{{\\sigma+j\\omega\\varepsilon}}}}={tp(eta)}\\ \\Omega"),D(f"\\delta_s=\\frac{{1}}{{\\alpha}}={teng(1/al,'m')},\\qquad\\lambda=\\frac{{2\\pi}}{{\\beta}}={teng(2*math.pi/be,'m')}")],
 answers=[{"label":r"\sigma/\omega\varepsilon","value":tr(ratio)},{"label":r"\alpha","value":f"{tr(al)}\\ \\mathrm{{Np/m}}"},{"label":r"\beta","value":f"{tr(be)}\\ \\mathrm{{rad/m}}"},{"label":r"\eta_c","value":f"{tp(eta)}\\ \\Omega"},{"label":r"\delta_s","value":teng(1/al,'m')},{"label":r"\lambda","value":teng(2*math.pi/be,'m')}],widget="planewave")

E0,z=10,1; S0=E0**2/(2*abs(eta))*math.cos(cmath.phase(eta)); Sz=S0*math.exp(-2*al*z); dB=10*math.log10(S0/Sz)
add(difficulty=2,title="Power lost in wet clay",
 prompt="In the wet clay of the previous problem ($100\\ \\mathrm{MHz}$), the field just inside the surface is $E_0=10\\ \\mathrm{V/m}$. Find the average power density there and $1\\ \\mathrm{m}$ deeper, and the loss in dB.",
 hints=[f"Use $\\alpha={tr(al)}\\ \\mathrm{{Np/m}}$ and $\\eta_c={tp(eta)}\\ \\Omega$.","$S_{\\mathrm{av}}=\\frac{|E_0|^2}{2|\\eta_c|}e^{-2\\alpha z}\\cos\\theta_\\eta$."],
 steps=[D(f"S_{{\\mathrm{{av}}}}(0)=\\frac{{10^2}}{{2({tr(abs(eta))})}}\\cos({tr(math.degrees(cmath.phase(eta)))}^\\circ)={teng(S0,'W/m^2')}"),D(f"S_{{\\mathrm{{av}}}}(1)=S_{{\\mathrm{{av}}}}(0)\\,e^{{-2({tr(al)})}}={teng(Sz,'W/m^2')}"),D(f"A=8.686\\,\\alpha z={tr(8.686*al*z)}\\ \\mathrm{{dB}}")],
 answers=[{"label":r"S_{\mathrm{av}}(0)","value":teng(S0,'W/m^2')},{"label":r"S_{\mathrm{av}}(1\ \mathrm{m})","value":teng(Sz,'W/m^2')},{"label":"A","value":f"{tr(dB)}\\ \\mathrm{{dB}}"}],widget="planewave")

s=5.8e7; d1=1/math.sqrt(math.pi*1e6*MU0*s); d2=1/math.sqrt(math.pi*1e9*MU0*s); Rs=1/(s*d2); up=2*math.pi*1e9*d2
add(difficulty=2,title="Copper at radio frequencies",
 prompt="For copper ($\\sigma=5.8\\times10^7\\ \\mathrm{S/m}$, $\\mu_r=1$), find the skin depth at $1\\ \\mathrm{MHz}$ and $1\\ \\mathrm{GHz}$. At $1\\ \\mathrm{GHz}$ also find the surface resistance, $\\eta_c$ and the phase velocity.",
 hints=["$\\delta_s=1/\\sqrt{\\pi f\\mu\\sigma}$.","$R_s=1/(\\sigma\\delta_s)$ and $\\eta_c=(1+j)R_s$.","$u_p=\\omega/\\beta=\\omega\\delta_s$."],
 steps=[D(f"\\delta_s(1\\ \\mathrm{{MHz}})=\\frac{{1}}{{\\sqrt{{\\pi(10^6)(4\\pi\\times10^{{-7}})(5.8\\times10^7)}}}}={teng(d1,'m')}"),D(f"\\delta_s(1\\ \\mathrm{{GHz}})={teng(d2,'m')}"),D(f"R_s=\\frac{{1}}{{\\sigma\\delta_s}}={teng(Rs,'Ω')},\\qquad\\eta_c=(1+j)R_s=(1+j)\\,{teng(Rs,'Ω')}"),D(f"u_p=\\omega\\delta_s={teng(up,'m/s')}"),"Barely a millionth of the speed of light, and the field is gone within a few micrometres."],
 answers=[{"label":r"\delta_s(1\ \mathrm{MHz})","value":teng(d1,'m')},{"label":r"\delta_s(1\ \mathrm{GHz})","value":teng(d2,'m')},{"label":"R_s","value":teng(Rs,'Ω')},{"label":r"\eta_c","value":f"(1+j)\\,{teng(Rs,'Ω')}"},{"label":"u_p","value":teng(up,'m/s')}],widget="skindepth")

f,s,er=1e3,4,81; ratio=s/(2*math.pi*f*er*EPS0); al=math.sqrt(math.pi*f*MU0*s); zd=60/(8.686*al)
add(difficulty=2,title="Talking to a submarine",
 prompt="A $1\\ \\mathrm{kHz}$ signal enters seawater ($\\sigma=4\\ \\mathrm{S/m}$, $\\varepsilon_r=81$). Show that seawater is a good conductor here, then find the skin depth and the depth at which the field is $60\\ \\mathrm{dB}$ below its value at the surface.",
 hints=["Good conductor: $\\alpha\\approx\\sqrt{\\pi f\\mu\\sigma}$.","$60\\ \\mathrm{dB}=8.686\\,\\alpha z$."],
 steps=[D(f"\\frac{{\\sigma}}{{\\omega\\varepsilon}}={tsci(ratio)}\\gg1"),D(f"\\alpha=\\sqrt{{\\pi(10^3)(4\\pi\\times10^{{-7}})(4)}}={tr(al)}\\ \\mathrm{{Np/m}},\\qquad\\delta_s={teng(1/al,'m')}"),D(f"z=\\frac{{60}}{{8.686\\,\\alpha}}={teng(zd,'m')}"),"That is why submarines use very low frequencies, and still have to stay near the surface."],
 answers=[{"label":r"\delta_s","value":teng(1/al,'m')},{"label":"z","value":teng(zd,'m')}],widget="skindepth")

A,z=30,5; al=A/(8.686*z)
add(difficulty=1,title="From decibels to nepers",
 prompt="A wave loses $30\\ \\mathrm{dB}$ over $5\\ \\mathrm{m}$ in a lossy medium. Find $\\alpha$, and the fractions of the field amplitude and of the power that remain.",
 hints=["$A(\\mathrm{dB})=8.686\\,\\alpha z$.","Field ratio is $10^{-A/20}$; power ratio is $10^{-A/10}$."],
 steps=[D(f"\\alpha=\\frac{{30}}{{8.686(5)}}={tr(al)}\\ \\mathrm{{Np/m}}"),D(f"\\frac{{E}}{{E_0}}=10^{{-30/20}}={tr(10**(-1.5))},\\qquad\\frac{{S}}{{S_0}}=10^{{-30/10}}=10^{{-3}}")],
 answers=[{"label":r"\alpha","value":f"{tr(al)}\\ \\mathrm{{Np/m}}"},{"label":"E/E_0","value":tr(10**(-1.5))},{"label":"S/S_0","value":"10^{-3}"}],widget="planewave")

s,f=3.5e7,1e6; d=1/math.sqrt(math.pi*f*MU0*s); t=100/8.686*d
add(difficulty=2,title="Aluminium shield thickness",
 prompt="An aluminium shield ($\\sigma=3.5\\times10^7\\ \\mathrm{S/m}$) must attenuate a $1\\ \\mathrm{MHz}$ field by $100\\ \\mathrm{dB}$ as it passes through the metal. Ignoring reflection at the surfaces, how thick must it be?",
 hints=["Find $\\delta_s$, then $100\\ \\mathrm{dB}=8.686\\,t/\\delta_s$."],
 steps=[D(f"\\delta_s=\\frac{{1}}{{\\sqrt{{\\pi f\\mu_0\\sigma}}}}={teng(d,'m')}"),D(f"t=\\frac{{100}}{{8.686}}\\delta_s={tr(100/8.686)}\\,\\delta_s={teng(t,'m')}"),"In practice, reflection at the front surface adds a lot more shielding on top of this."],
 answers=[{"label":r"\delta_s","value":teng(d,'m')},{"label":"t","value":teng(t,'m')}],widget="skindepth")

f=60; dfe=1/math.sqrt(math.pi*f*1000*MU0*1e7); dcu=1/math.sqrt(math.pi*f*MU0*5.8e7)
add(difficulty=2,title="Why transformer cores are laminated",
 prompt="Compare the skin depth at $60\\ \\mathrm{Hz}$ in iron ($\\sigma=10^7\\ \\mathrm{S/m}$, $\\mu_r=1000$) and in copper ($\\sigma=5.8\\times10^7\\ \\mathrm{S/m}$, $\\mu_r=1$).",
 hints=["$\\delta_s=1/\\sqrt{\\pi f\\mu\\sigma}$: a large $\\mu_r$ shrinks it."],
 steps=[D(f"\\delta_{{\\text{{Fe}}}}=\\frac{{1}}{{\\sqrt{{\\pi(60)(1000)(4\\pi\\times10^{{-7}})(10^7)}}}}={teng(dfe,'m')}"),D(f"\\delta_{{\\text{{Cu}}}}={teng(dcu,'m')}"),"A solid iron core thicker than a millimetre would carry flux only near its surface and waste power in eddy currents, so cores are built from thin insulated sheets."],
 answers=[{"label":r"\delta_{\text{Fe}}","value":teng(dfe,'m')},{"label":r"\delta_{\text{Cu}}","value":teng(dcu,'m')}],widget="skindepth")

write_unit("plane-waves","Plane waves",C,G,P)
