# Polarization: flashcards, glossary and practice problems.
# Every number in the steps and answers is computed here. Run: python3 tools/make_polarization.py
# Handedness follows the course text: a wave toward +z with 0 < delta < 180 deg is left-handed.
import math, cmath, os, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lib import *
D=lambda s:"$$"+s+"$$"
T=["polarization"]
deg=math.degrees; rad=math.radians

def ellipse(ax,ay,dl):
    """psi0, gamma, chi (degrees), axial ratio and a name for E = x ax + y ay e^{j dl} (dl in degrees)."""
    p0=math.atan2(ay,ax); d=rad(dl)
    g=0.5*math.atan2(math.sin(2*p0)*math.cos(d),math.cos(2*p0))
    ch=0.5*math.asin(max(-1,min(1,math.sin(2*p0)*math.sin(d))))
    AR=math.inf if abs(math.tan(ch))<1e-12 else 1/abs(math.tan(ch))
    if abs(math.sin(d))<1e-12 or ax==0 or ay==0: name="linear"
    elif abs(AR-1)<1e-9: name="left-hand circular" if ch>0 else "right-hand circular"
    else: name="left-hand elliptical" if ch>0 else "right-hand elliptical"
    return deg(p0),deg(g),deg(ch),AR,name

C=[
("What does the polarization of a wave describe?","The path traced by the tip of $\\mathbf{E}$ over time at a fixed point in space, seen with the wave travelling away from or toward you.","concept",T),
("General phasor for a wave toward $+z$ with both transverse components?",D(r"\tilde{\mathbf{E}}=(\hat{\mathbf{x}}a_x+\hat{\mathbf{y}}a_ye^{j\delta})e^{-jkz}")+"$a_x,a_y\\ge0$; $\\delta$ is the phase of the $y$ component relative to $x$.","equation",T),
("When is a wave linearly polarized?","When $\\delta=0$ or $\\delta=\\pm180^\\circ$, or when one component is zero. $\\mathbf{E}$ then swings back and forth along a fixed line.","concept",T),
("Angle of a linearly polarized field from the $x$ axis?",D(r"\psi_0=\tan^{-1}\frac{a_y}{a_x}")+"For $\\delta=180^\\circ$ the line has angle $-\\psi_0$.","equation",T),
("When is a wave circularly polarized?","When $a_x=a_y$ and $\\delta=\\pm90^\\circ$. The magnitude of $\\mathbf{E}$ stays constant while its direction turns once per period.","concept",T),
("Left- or right-handed: how to tell (wave toward $+z$)?","$0<\\delta<180^\\circ$: left-handed. $-180^\\circ<\\delta<0$: right-handed. Point the thumb along the direction of travel; the fingers of that hand curl the way $\\mathbf{E}$ turns.","concept",T),
("What is the auxiliary angle $\\psi_0$?",D(r"\tan\psi_0=\frac{a_y}{a_x},\qquad0\le\psi_0\le90^\circ"),"equation",T),
("Rotation angle $\\gamma$ of the polarization ellipse?",D(r"\tan2\gamma=\tan2\psi_0\cos\delta")+"$\\gamma>0$ when $\\cos\\delta>0$, $\\gamma<0$ when $\\cos\\delta<0$.","equation",T),
("Ellipticity angle $\\chi$?",D(r"\sin2\chi=\sin2\psi_0\sin\delta,\qquad-45^\circ\le\chi\le45^\circ")+"$\\chi>0$ is left-handed, $\\chi<0$ right-handed.","equation",T),
("Axial ratio of the polarization ellipse?",D(r"R=\frac{a_\xi}{a_\eta}=\frac{1}{|\tan\chi|}")+"$R=1$ for circular, $R=\\infty$ for linear.","equation",T),
("Time-domain fields for LHC and RHC waves toward $+z$ with amplitude $a$?",D(r"\text{LHC: }\hat{\mathbf{x}}a\cos(\omega t-kz)-\hat{\mathbf{y}}a\sin(\omega t-kz)")+D(r"\text{RHC: }\hat{\mathbf{x}}a\cos(\omega t-kz)+\hat{\mathbf{y}}a\sin(\omega t-kz)"),"equation",T),
("Phasor forms of LHC and RHC waves toward $+z$?",D(r"\text{LHC: }a(\hat{\mathbf{x}}+j\hat{\mathbf{y}})e^{-jkz},\qquad\text{RHC: }a(\hat{\mathbf{x}}-j\hat{\mathbf{y}})e^{-jkz}"),"equation",T),
("What do you get by adding equal LHC and RHC waves?","A linearly polarized wave. The rotating parts cancel along one axis and add along the other.","concept",T),
("Does the handedness change if the wave travels toward $-z$?","The time behaviour at a point is the same, but the direction of travel is reversed, so the same $\\delta$ gives the opposite handedness. Always check against the direction of travel.","concept",T),
("Why does polarization matter for antennas?","A receiving antenna only picks up the component of the wave that matches its own polarization. A vertical dipole receives nothing from a horizontally polarized wave, and half the power from a circular one.","concept",T),
]

G=[
("Polarization","","","The shape traced by the tip of $\\mathbf{E}$ in time at a fixed point: a line, a circle or an ellipse.","polarization",T),
("Linear polarization","","","$\\mathbf{E}$ oscillates along one fixed line. $\\delta=0$ or $180^\\circ$.","polarization",T),
("Circular polarization","","","$\\mathbf{E}$ keeps a constant magnitude and turns at $\\omega$. $a_x=a_y$, $\\delta=\\pm90^\\circ$.","polarization",T),
("Elliptical polarization","","","The general case: the tip of $\\mathbf{E}$ traces an ellipse.","polarization",T),
("Left-hand circular (LHC)","","","Circular polarization that turns the way the fingers of the left hand curl when its thumb points along the direction of travel. $\\delta=+90^\\circ$ for a wave toward $+z$.","polarization",T),
("Right-hand circular (RHC)","","","Circular polarization that turns with the right-hand rule about the direction of travel. $\\delta=-90^\\circ$ for a wave toward $+z$.","polarization",T),
("Phase difference","\\delta","^\\circ","Phase of the $y$ component of $\\tilde{\\mathbf{E}}$ relative to the $x$ component.","polarization",T),
("Auxiliary angle","\\psi_0","^\\circ","$\\tan^{-1}(a_y/a_x)$: sets the relative size of the two components.","polarization",T),
("Rotation angle","\\gamma","^\\circ","Angle between the major axis of the polarization ellipse and the $x$ axis.","polarization",T),
("Ellipticity angle","\\chi","^\\circ","Sets the shape and handedness of the ellipse: $0$ for linear, $\\pm45^\\circ$ for circular.","polarization",T),
("Axial ratio","R","","Major axis over minor axis of the polarization ellipse. 1 for circular, infinite for linear.","polarization",T),
]

P=[]
def add(**k): k.setdefault("source","original"); k.setdefault("topics",T); P.append(k)

ax,ay=3,4; p0=deg(math.atan2(ay,ax))
add(difficulty=1,title="A linearly polarized wave",
 prompt="Describe the polarization of $\\mathbf{E}=\\hat{\\mathbf{x}}\\,3\\cos(\\omega t-kz)+\\hat{\\mathbf{y}}\\,4\\cos(\\omega t-kz)\\ \\mathrm{V/m}$, and find its amplitude and the angle of $\\mathbf{E}$ from the $x$ axis.",
 hints=["Both components have the same phase, so $\\delta=0$."],
 steps=["$\\delta=0$, so the wave is linearly polarized.",D(f"|\\mathbf{{E}}|_{{\\max}}=\\sqrt{{3^2+4^2}}={tr(math.hypot(ax,ay))}\\ \\mathrm{{V/m}}"),D(f"\\psi_0=\\tan^{{-1}}\\frac{{4}}{{3}}={tr(p0)}^\\circ")],
 answers=[{"label":"\\text{type}","value":"\\text{linear}"},{"label":"|\\mathbf{E}|_{\\max}","value":f"{tr(math.hypot(ax,ay))}\\ \\mathrm{{V/m}}"},{"label":"\\psi_0","value":f"{tr(p0)}^\\circ"}],widget="polarization")

add(difficulty=1,title="Which way does it turn?",
 prompt="Find the polarization state of $\\mathbf{E}=\\hat{\\mathbf{x}}\\,5\\cos(\\omega t-kz)-\\hat{\\mathbf{y}}\\,5\\sin(\\omega t-kz)\\ \\mathrm{V/m}$.",
 hints=["Write $-\\sin\\theta$ as a cosine with a phase shift.","Then read off $\\delta$ and use the sign rule."],
 steps=[D(r"-\sin\theta=\cos(\theta+90^\circ)\ \Rightarrow\ \delta=+90^\circ"),"$a_x=a_y=5$ and $\\delta=+90^\\circ$, so the wave is left-hand circularly polarized.","Check at $z=0$: $\\omega t=0$ gives $\\mathbf{E}=5\\hat{\\mathbf{x}}$; $\\omega t=90^\\circ$ gives $\\mathbf{E}=-5\\hat{\\mathbf{y}}$. Looking at the wave coming toward you, $\\mathbf{E}$ turns clockwise, which is the left-hand rule about $+\\hat{\\mathbf{z}}$."],
 answers=[{"label":"\\delta","value":"+90^\\circ"},{"label":"\\text{type}","value":"\\text{left-hand circular}"}],widget="polarization")

add(difficulty=1,title="From a phasor to the time domain",
 prompt="A wave in air has $\\tilde{\\mathbf{E}}=10(\\hat{\\mathbf{x}}-j\\hat{\\mathbf{y}})e^{-jkz}\\ \\mathrm{V/m}$. Write $\\mathbf{E}(z,t)$ and name its polarization.",
 hints=["$-j=e^{-j90^\\circ}$."],
 steps=[D(r"\tilde{\mathbf{E}}=10\left(\hat{\mathbf{x}}+\hat{\mathbf{y}}e^{-j90^\circ}\right)e^{-jkz}"),D(r"\mathbf{E}(z,t)=\hat{\mathbf{x}}\,10\cos(\omega t-kz)+\hat{\mathbf{y}}\,10\cos(\omega t-kz-90^\circ)"),D(r"=\hat{\mathbf{x}}\,10\cos(\omega t-kz)+\hat{\mathbf{y}}\,10\sin(\omega t-kz)"),"$a_x=a_y$ and $\\delta=-90^\\circ$: right-hand circular."],
 answers=[{"label":"\\mathbf{E}(z,t)","value":r"\hat{\mathbf{x}}\,10\cos(\omega t-kz)+\hat{\mathbf{y}}\,10\sin(\omega t-kz)\ \mathrm{V/m}"},{"label":"\\text{type}","value":"\\text{right-hand circular}"}],widget="polarization")

ax,ay,dl=3,4,45; p0,g,ch,AR,name=ellipse(ax,ay,dl)
add(difficulty=2,title="Characterizing an ellipse",
 prompt="Find $\\psi_0$, the rotation angle $\\gamma$, the ellipticity angle $\\chi$, the axial ratio and the handedness of $\\tilde{\\mathbf{E}}=(\\hat{\\mathbf{x}}\\,3+\\hat{\\mathbf{y}}\\,4e^{j45^\\circ})e^{-jkz}$.",
 hints=["$\\tan\\psi_0=a_y/a_x$.","$\\tan2\\gamma=\\tan2\\psi_0\\cos\\delta$, $\\sin2\\chi=\\sin2\\psi_0\\sin\\delta$.","$\\tan2\\psi_0$ is negative here, but $\\cos\\delta>0$ means $\\gamma>0$: take the angle in the right quadrant."],
 steps=[D(f"\\psi_0=\\tan^{{-1}}\\frac{{4}}{{3}}={tr(p0)}^\\circ"),D(f"\\tan2\\gamma=\\tan({tr(2*p0)}^\\circ)\\cos45^\\circ={tr(math.tan(rad(2*p0))*math.cos(rad(dl)))}"),f"Since $\\cos\\delta>0$, $\\gamma>0$, so $2\\gamma={tr(2*g)}^\\circ$ and $\\gamma={tr(g)}^\\circ$.",
        D(f"\\sin2\\chi=\\sin({tr(2*p0)}^\\circ)\\sin45^\\circ={tr(math.sin(rad(2*p0))*math.sin(rad(dl)))}\\ \\Rightarrow\\ \\chi={tr(ch)}^\\circ"),D(f"R=\\frac{{1}}{{\\tan{tr(ch)}^\\circ}}={tr(AR)}"),"$\\chi>0$, so the wave is left-hand elliptically polarized."],
 answers=[{"label":"\\psi_0","value":f"{tr(p0)}^\\circ"},{"label":"\\gamma","value":f"{tr(g)}^\\circ"},{"label":"\\chi","value":f"{tr(ch)}^\\circ"},{"label":"R","value":tr(AR)},{"label":"\\text{type}","value":"\\text{left-hand elliptical}"}],widget="polarization")

ax,ay,dl=2,2,-60; p0,g,ch,AR,name=ellipse(ax,ay,dl)
add(difficulty=2,title="Equal amplitudes, not circular",
 prompt="Characterize $\\tilde{\\mathbf{E}}=2(\\hat{\\mathbf{x}}+\\hat{\\mathbf{y}}e^{-j60^\\circ})e^{-jkz}$: find $\\gamma$, $\\chi$, the axial ratio and the handedness.",
 hints=["$\\psi_0=45^\\circ$, so $\\tan2\\psi_0$ is infinite and $\\sin2\\psi_0=1$."],
 steps=["$\\psi_0=45^\\circ$ and $\\cos\\delta>0$, so the major axis lies at $\\gamma=45^\\circ$.",D(f"\\sin2\\chi=\\sin(-60^\\circ)\\ \\Rightarrow\\ \\chi={tr(ch)}^\\circ"),D(f"R=\\frac{{1}}{{|\\tan{tr(ch)}^\\circ|}}={tr(AR)}"),"$\\chi<0$: right-hand elliptical. Equal amplitudes give a circle only when $\\delta=\\pm90^\\circ$."],
 answers=[{"label":"\\gamma","value":f"{tr(g)}^\\circ"},{"label":"\\chi","value":f"{tr(ch)}^\\circ"},{"label":"R","value":tr(AR)},{"label":"\\text{type}","value":"\\text{right-hand elliptical}"}],widget="polarization")

add(difficulty=2,title="Two circular waves make a line",
 prompt="An LHC wave $\\tilde{\\mathbf{E}}_1=a(\\hat{\\mathbf{x}}+j\\hat{\\mathbf{y}})e^{-jkz}$ and an RHC wave $\\tilde{\\mathbf{E}}_2=a(\\hat{\\mathbf{x}}-j\\hat{\\mathbf{y}})e^{-jkz}$ travel together. Find the polarization of their sum. What if the RHC wave is $a(\\hat{\\mathbf{x}}-j\\hat{\\mathbf{y}})e^{j60^\\circ}e^{-jkz}$ instead?",
 hints=["Add the phasors component by component.","With the extra phase, factor out $e^{j30^\\circ}$ and look at what is left."],
 steps=[D(r"\tilde{\mathbf{E}}_1+\tilde{\mathbf{E}}_2=2a\,\hat{\mathbf{x}}\,e^{-jkz}"),"Linear along $x$.",D(r"\hat{\mathbf{x}}a(1+e^{j60^\circ})+\hat{\mathbf{y}}ja(1-e^{j60^\circ})=2ae^{j30^\circ}\left(\hat{\mathbf{x}}\cos30^\circ+\hat{\mathbf{y}}\sin30^\circ\right)"),"Still linear, but tilted to $30^\\circ$: shifting the phase of one circular wave by $\\phi$ rotates the line by $\\phi/2$."],
 answers=[{"label":"\\text{sum}","value":r"2a\,\hat{\mathbf{x}}\,e^{-jkz}\ (\text{linear})"},{"label":"\\text{shifted}","value":r"\text{linear at }30^\circ"}],widget="polarization")

AR,g,hand=3,30,-1; ch=hand*deg(math.atan(1/AR)); p0=0.5*deg(math.acos(math.cos(rad(2*g))*math.cos(rad(2*ch)))); dl=deg(math.atan2(math.tan(rad(2*ch)),math.sin(rad(2*g))))
pc,gc,cc,ARc,_=ellipse(math.cos(rad(p0)),math.sin(rad(p0)),dl)
assert abs(gc-g)<1e-9 and abs(cc-ch)<1e-9 and abs(ARc-AR)<1e-9
add(difficulty=3,title="Working backward from the ellipse",
 prompt="A right-hand elliptically polarized wave toward $+z$ has axial ratio 3 and its major axis at $\\gamma=30^\\circ$ from the $x$ axis. Find $\\psi_0$ and $\\delta$.",
 hints=["$\\tan\\chi=-1/R$ for right-handed.","$\\cos2\\psi_0=\\cos2\\gamma\\cos2\\chi$ and $\\tan\\delta=\\tan2\\chi/\\sin2\\gamma$."],
 steps=[D(f"\\chi=-\\tan^{{-1}}\\frac{{1}}{{3}}={tr(ch)}^\\circ"),D(f"\\cos2\\psi_0=\\cos60^\\circ\\cos({tr(2*ch)}^\\circ)={tr(math.cos(rad(2*p0)))}\\ \\Rightarrow\\ \\psi_0={tr(p0)}^\\circ"),D(f"\\tan\\delta=\\frac{{\\tan({tr(2*ch)}^\\circ)}}{{\\sin60^\\circ}}={tr(math.tan(rad(dl)))}\\ \\Rightarrow\\ \\delta={tr(dl)}^\\circ"),
        "Check: $\\delta$ is negative (right-handed) and $\\cos\\delta>0$ (so $\\gamma>0$), as required."],
 answers=[{"label":"\\psi_0","value":f"{tr(p0)}^\\circ"},{"label":"\\delta","value":f"{tr(dl)}^\\circ"}],widget="polarization")

ax,ay,dl=1,2,135; p0,g,ch,AR,name=ellipse(ax,ay,dl)
add(difficulty=2,title="A phase over 90 degrees",
 prompt="Characterize $\\mathbf{E}=\\hat{\\mathbf{x}}\\cos(\\omega t-kz)+\\hat{\\mathbf{y}}\\,2\\cos(\\omega t-kz+135^\\circ)$: find $\\gamma$, $\\chi$, the axial ratio and the handedness.",
 hints=["Here $\\cos\\delta<0$, so $\\gamma$ is negative."],
 steps=[D(f"\\psi_0=\\tan^{{-1}}2={tr(p0)}^\\circ"),D(f"\\tan2\\gamma=\\tan({tr(2*p0)}^\\circ)\\cos135^\\circ={tr(math.tan(rad(2*p0))*math.cos(rad(dl)))}"),f"With $\\cos\\delta<0$, $\\gamma<0$: $2\\gamma={tr(2*g)}^\\circ$, so $\\gamma={tr(g)}^\\circ$.",D(f"\\sin2\\chi=\\sin({tr(2*p0)}^\\circ)\\sin135^\\circ={tr(math.sin(rad(2*p0))*math.sin(rad(dl)))}\\ \\Rightarrow\\ \\chi={tr(ch)}^\\circ"),D(f"R={tr(AR)}"),"$\\chi>0$: left-hand elliptical."],
 answers=[{"label":"\\gamma","value":f"{tr(g)}^\\circ"},{"label":"\\chi","value":f"{tr(ch)}^\\circ"},{"label":"R","value":tr(AR)},{"label":"\\text{type}","value":"\\text{left-hand elliptical}"}],widget="polarization")

write_unit("polarization","Polarization",C,G,P)
