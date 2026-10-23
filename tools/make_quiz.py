# Multiple-choice quiz questions for every topic.
# Numeric answers and distractors are computed here. Run: python3 tools/make_quiz.py
# Each question lists the correct choice first; the app shuffles the choices.
import math, cmath, json, os, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lib import *
EPS0=8.854187817e-12; MU0=4e-7*math.pi; ETA0=math.sqrt(MU0/EPS0); K=1/(4*math.pi*EPS0)
deg=math.degrees; rad=math.radians

Q={}   # folder -> list of questions
def q(folder,topics,question,right,wrong,explain):
    assert len(wrong)==3 and right not in wrong and len(set(wrong))==3,(question,right,wrong)
    Q.setdefault(folder,[]).append({"question":question,"choices":[right]+wrong,"answer":0,"explain":explain,"topics":topics})
def num(v,u="",n=3):
    """A number with units as inline TeX."""
    return "$"+(teng(v,u,n) if u else tr(v,n))+"$"

# ---------------- Fields and phasors ----------------
F,T="fields-and-phasors",["phasors"]
q(F,T,"What is the phasor of $v(t)=10\\cos(\\omega t-30^\\circ)$?","$10\\angle-30^\\circ$",["$10\\angle30^\\circ$","$10\\angle60^\\circ$","$-10j$"],"A phasor keeps the amplitude and the phase of the cosine: $10e^{-j30^\\circ}$.")
q(F,T,"What is the phasor of $5\\sin\\omega t$, using the cosine reference?","$-5j$",["$5$","$5j$","$-5$"],"$\\sin\\omega t=\\cos(\\omega t-90^\\circ)$, so the phasor is $5e^{-j90^\\circ}=-5j$.")
z=3+4j
q(F,T,"What is $3+j4$ in polar form?",f"${tp(z)}$",[f"$5\\angle{tr(deg(math.atan2(3,4)))}^\\circ$","$7\\angle53.1^\\circ$","$5\\angle-53.1^\\circ$"],"$|z|=\\sqrt{3^2+4^2}=5$ and $\\angle z=\\tan^{-1}(4/3)=53.1^\\circ$.")
q(F,T,"In the phasor domain, taking $d/dt$ of a signal does what?","Multiplies its phasor by $j\\omega$",["Divides its phasor by $j\\omega$","Multiplies its phasor by $\\omega$","Leaves the phasor unchanged"],"$\\frac{d}{dt}\\mathrm{Re}\\{\\tilde Ve^{j\\omega t}\\}=\\mathrm{Re}\\{j\\omega\\tilde Ve^{j\\omega t}\\}$.")
q(F,T,"Which way does $\\cos(\\omega t+\\beta z)$ travel?","Toward $-z$",["Toward $+z$","It does not travel","Toward $+t$"],"The phase stays constant when $\\omega t+\\beta z$ is constant, so $z$ must fall as $t$ grows.")
f=100e6
q(F,T,"What is the free-space wavelength at $100\\ \\mathrm{MHz}$?",num(c/f,'m'),[num(c/f/10,'m'),num(c/f*10,'m'),num(c/f/2,'m')],"$\\lambda=c/f=3\\times10^8/10^8\\approx3\\ \\mathrm{m}$.")
q(F,T,"A wave in a medium with $\\varepsilon_r=4$, $\\mu_r=1$ has phase velocity",num(c/2,'m/s'),[num(c/4,'m/s'),num(c,'m/s'),num(c*2,'m/s')],"$u_p=c/\\sqrt{\\mu_r\\varepsilon_r}=c/2$.")
q(F,T,"What does Euler's identity say?","$e^{j\\theta}=\\cos\\theta+j\\sin\\theta$",["$e^{j\\theta}=\\cos\\theta-j\\sin\\theta$","$e^{j\\theta}=\\sin\\theta+j\\cos\\theta$","$e^{j\\theta}=1+j\\theta$"],"It is the link between phasors and sinusoids.")

# ---------------- Transmission lines and their sub-topics ----------------
F="transmission-lines"
T=["tline"]
q(F,T,"When does a circuit need transmission-line analysis?","When its length is a sizeable fraction of a wavelength (say more than $\\lambda/100$)",["Only when the frequency is above 1 GHz","Only when the wires are coaxial","Whenever the current is AC"],"Below that, the phase change along the wire is negligible and lumped circuit theory works.")
q(F,T,"Characteristic impedance of a lossless line?","$Z_0=\\sqrt{L'/C'}$",["$Z_0=\\sqrt{C'/L'}$","$Z_0=L'C'$","$Z_0=1/\\sqrt{L'C'}$"],"Lossless means $R'=G'=0$ in $Z_0=\\sqrt{(R'+j\\omega L')/(G'+j\\omega C')}$.")
q(F,T,"Phase velocity on a lossless line?","$u_p=1/\\sqrt{L'C'}$",["$u_p=\\sqrt{L'C'}$","$u_p=\\sqrt{L'/C'}$","$u_p=L'/C'$"],"$\\beta=\\omega\\sqrt{L'C'}$ and $u_p=\\omega/\\beta$.")
Z0,ZL=50,50
q(F,T,"Input impedance of a $50\\ \\Omega$ line of any length ending in $50\\ \\Omega$?","$50\\ \\Omega$",["$0$","$100\\ \\Omega$","It depends on the length"],"A matched line has no reflection, so $Z_{in}=Z_0$ at every point.")
q(F,T,"Input impedance of a quarter-wave line ending in $Z_L$?","$Z_0^2/Z_L$",["$Z_L$","$Z_0$","$Z_L^2/Z_0$"],"$\\tan\\beta\\ell\\to\\infty$ at $\\ell=\\lambda/4$, which leaves $Z_{in}=Z_0^2/Z_L$.")
q(F,T,"Input impedance of a half-wave lossless line ending in $Z_L$?","$Z_L$",["$Z_0^2/Z_L$","$Z_0$","$-Z_L$"],"$\\tan\\beta\\ell=0$ at $\\ell=\\lambda/2$, so the line repeats its load.")
q(F,T,"A short-circuited lossless stub shorter than $\\lambda/4$ looks like","An inductor",["A capacitor","An open circuit","A resistor"],"$Z_{in}=jZ_0\\tan\\beta\\ell$ is positive imaginary for $0<\\beta\\ell<\\pi/2$.")
T=["reflection"]
G_=(100-50)/(100+50)
q(F,T,"Reflection coefficient for a $100\\ \\Omega$ load on a $50\\ \\Omega$ line?",num(G_),[num(-G_),num(0.5),num(2)],"$\\Gamma=(Z_L-Z_0)/(Z_L+Z_0)=50/150$.")
S=(1+abs(G_))/(1-abs(G_))
q(F,T,"VSWR when $|\\Gamma|=1/3$?",num(S),[num(1.5),num(3),num(4/3)],"$S=(1+|\\Gamma|)/(1-|\\Gamma|)=(4/3)/(2/3)=2$.")
q(F,T,"$\\Gamma$ for a short circuit?","$-1$",["$+1$","$0$","$j$"],"$Z_L=0$ gives $\\Gamma=(0-Z_0)/(0+Z_0)=-1$.")
q(F,T,"How far apart are adjacent voltage maxima on a standing wave?","$\\lambda/2$",["$\\lambda/4$","$\\lambda$","$\\lambda/8$"],"The pattern $|V(z)|$ repeats every half wavelength. A maximum and the next minimum are $\\lambda/4$ apart.")
q(F,T,"What fraction of incident power reaches a load with $|\\Gamma|=0.5$?",num(0.75),[num(0.5),num(0.25),num(0.875)],"$P_L/P^i=1-|\\Gamma|^2=0.75$.")
q(F,T,"On a line with a purely resistive load $R_L>Z_0$, where is the first voltage maximum?","At the load",["$\\lambda/4$ from the load","$\\lambda/2$ from the load","There is no maximum"],"$\\Gamma$ is real and positive, so $\\theta_r=0$ and $d_{\\max}=0$.")
T=["smith"]
q(F,T,"Where is a matched load on the Smith chart?","At the centre",["On the far right","On the far left","On the outer circle"],"$z_L=1$ gives $\\Gamma=0$, the centre of the chart.")
q(F,T,"Moving from the load toward the generator rotates you on the Smith chart","Clockwise",["Counterclockwise","Straight toward the centre","Along a constant-reactance arc"],"$\\Gamma(d)=\\Gamma e^{-j2\\beta d}$: the angle decreases, which is clockwise.")
q(F,T,"How much line length is one full trip around the Smith chart?","$\\lambda/2$",["$\\lambda$","$\\lambda/4$","$2\\lambda$"],"$2\\beta d=2\\pi$ when $d=\\lambda/2$.")
q(F,T,"How do you turn an impedance into an admittance on the Smith chart?","Go to the point diametrically opposite",["Reflect it about the horizontal axis","Move to the centre","Rotate it by $90^\\circ$"],"Opposite points are a quarter wave apart, and a quarter-wave line inverts normalized impedance.")
q(F,T,"The outer circle of the Smith chart holds loads that are","Purely reactive",["Purely resistive","Matched","Open circuits only"],"$|\\Gamma|=1$ there: no power is absorbed.")
T=["matching"]
Zq=math.sqrt(50*200)
q(F,T,"A quarter-wave transformer matches a $200\\ \\Omega$ load to a $50\\ \\Omega$ line. Its impedance?",num(Zq,'Ω'),[num(125,'Ω'),num(150,'Ω'),num(250,'Ω')],"$Z_{0,\\lambda/4}=\\sqrt{Z_0Z_L}=\\sqrt{50\\cdot200}$.")
q(F,T,"A single shunt stub matches by","Cancelling the susceptance at a point where $y=1+jb$",["Adding resistance in series","Changing $Z_0$ of the main line","Absorbing the reflected power"],"Move along the line until $\\mathrm{Re}\\{y\\}=1$, then add a stub with susceptance $-b$.")
q(F,T,"A quarter-wave transformer on its own can directly match","A purely resistive load",["Any complex load","Only a short circuit","Only loads below $Z_0$"],"$\\sqrt{Z_0Z_L}$ must be real. A complex load first needs a length of line to make it real.")
q(F,T,"Why are shunt stubs often preferred to series stubs?","They are easier to build: just tee a stub onto the line",["They never need a short circuit","They work at every frequency","They have no loss"],"A series stub needs the main line to be cut, which is awkward in coax or microstrip.")
T=["transients"]
q(F,T,"A step travels down a line. Its first value at the input is","$V_s\\,Z_0/(R_s+Z_0)$",["$V_s$","$V_s\\,R_L/(R_s+R_L)$","$0$"],"Before any reflection returns, the line looks like a resistor $Z_0$.")
q(F,T,"Final steady-state voltage on a lossless line after a step?","$V_s\\,R_L/(R_s+R_L)$",["$V_s\\,Z_0/(R_s+Z_0)$","$V_s$","$0$"],"At DC the line is just a wire: a voltage divider of $R_s$ and $R_L$.")
q(F,T,"What does a bounce diagram plot?","Each wave's voltage against position and time, zig-zagging between the ends",["The Smith chart over time","Current against frequency","The reflection coefficient against length"],"Each leg adds a reflected wave, and summing them gives $V(z,t)$.")
q(F,T,"With $R_s=R_L=Z_0$, how many reflections occur?","None",["One at the load","One at each end","Infinitely many"],"Both ends are matched, so $\\Gamma_L=\\Gamma_g=0$.")

# ---------------- Vector calculus ----------------
F,T="vector-calculus",["vectors"]
A,B=(1,2,3),(4,-5,6)
dot=sum(a*b for a,b in zip(A,B))
q(F,T,"What is $\\mathbf{A}\\cdot\\mathbf{B}$ for $\\mathbf{A}=(1,2,3)$ and $\\mathbf{B}=(4,-5,6)$?",f"${dot}$",["$32$","$-12$","$(4,-10,18)$"],"$4-10+18=12$.")
q(F,T,"What does $\\nabla\\cdot\\mathbf{F}>0$ at a point mean?","The point is a source: net flux flows out",["The field circulates around the point","The field is zero there","The field is uniform"],"Divergence is outward flux per unit volume.")
q(F,T,"The curl of any gradient is","Zero",["The Laplacian","The divergence","A unit vector"],"$\\nabla\\times\\nabla V=0$ always, which is why static $\\mathbf{E}$ can be written as $-\\nabla V$.")
q(F,T,"The divergence of any curl is","Zero",["The gradient","The curl","One"],"$\\nabla\\cdot(\\nabla\\times\\mathbf{A})=0$, which is why $\\mathbf{B}=\\nabla\\times\\mathbf{A}$ automatically has no divergence.")
q(F,T,"The divergence theorem relates","A volume integral of $\\nabla\\cdot\\mathbf{F}$ to the flux through the closed surface",["A line integral to a surface integral of the curl","A gradient to a line integral","Two volume integrals"],"$\\int_V\\nabla\\cdot\\mathbf{F}\\,dv=\\oint_S\\mathbf{F}\\cdot d\\mathbf{s}$.")
q(F,T,"Stokes's theorem relates","The circulation around a loop to the flux of the curl through it",["Flux to divergence","Gradient to potential","Two surface integrals"],"$\\oint_C\\mathbf{F}\\cdot d\\mathbf{l}=\\int_S(\\nabla\\times\\mathbf{F})\\cdot d\\mathbf{s}$.")
x,y=3,4
q(F,T,"The point $(x,y)=(3,4)$ has cylindrical coordinates",f"$r=5,\\ \\phi={tr(deg(math.atan2(y,x)))}^\\circ$",["$r=7,\\ \\phi=53.1^\\circ$",f"$r=5,\\ \\phi={tr(deg(math.atan2(x,y)))}^\\circ$","$r=25,\\ \\phi=53.1^\\circ$"],"$r=\\sqrt{x^2+y^2}$, $\\phi=\\tan^{-1}(y/x)$.")
q(F,T,"Differential volume in spherical coordinates?","$R^2\\sin\\theta\\,dR\\,d\\theta\\,d\\phi$",["$R\\,dR\\,d\\theta\\,d\\phi$","$dR\\,d\\theta\\,d\\phi$","$R^2\\,dR\\,d\\theta\\,d\\phi$"],"The sides are $dR$, $R\\,d\\theta$ and $R\\sin\\theta\\,d\\phi$.")
q(F,T,"Which unit vector changes direction from point to point?","$\\hat{\\mathbf{r}}$ (cylindrical)",["$\\hat{\\mathbf{x}}$","$\\hat{\\mathbf{z}}$","$\\hat{\\mathbf{y}}$"],"$\\hat{\\mathbf{r}}$ points away from the $z$ axis, so it depends on $\\phi$.")

# ---------------- Electrostatics ----------------
F,T="electrostatics",["electrostatics"]
Qc,R=1e-9,0.1; E=K*Qc/R**2
q(F,T,"Field $10\\ \\mathrm{cm}$ from a $1\\ \\mathrm{nC}$ point charge in air?",num(E,'V/m'),[num(E/10,"V/m"),num(E*10,"V/m"),num(E/2,"V/m")],"$E=Q/(4\\pi\\varepsilon_0R^2)=(8.99\\times10^9)(10^{-9})/0.01$.")
q(F,T,"Gauss's law says the electric flux out of a closed surface equals","The free charge enclosed",["Zero, always","The charge on the surface only","The potential on the surface"],"$\\oint\\mathbf{D}\\cdot d\\mathbf{s}=Q_{\\mathrm{enc}}$.")
q(F,T,"How does the field of an infinite line charge fall off with distance $r$?","$1/r$",["$1/r^2$","$1/r^3$","It is constant"],"A cylinder of radius $r$ gives $E\\cdot2\\pi r\\ell=\\rho_\\ell\\ell/\\varepsilon_0$.")
q(F,T,"The field of an infinite sheet of charge","Does not depend on distance",["Falls as $1/r$","Falls as $1/r^2$","Is zero"],"$E=\\rho_s/(2\\varepsilon_0)$ on each side.")
q(F,T,"Inside a conductor in electrostatic equilibrium, $\\mathbf{E}$ is","Zero",["Equal to the surface field","Normal to the surface","Infinite"],"Any field would move the free charges until it vanished.")
q(F,T,"At a charge-free dielectric boundary, which field components are continuous?","Tangential $\\mathbf{E}$ and normal $\\mathbf{D}$",["Normal $\\mathbf{E}$ and tangential $\\mathbf{D}$","All of $\\mathbf{E}$","Nothing"],"$E_{1t}=E_{2t}$ and $D_{1n}-D_{2n}=\\rho_s=0$.")
A_,d,er=1e-2,1e-3,4; Cc=er*EPS0*A_/d
q(F,T,"Capacitance of parallel plates, $A=100\\ \\mathrm{cm^2}$, $d=1\\ \\mathrm{mm}$, $\\varepsilon_r=4$?",num(Cc,'F'),[num(Cc/4,'F'),num(Cc*10,'F'),num(Cc/10,'F')],"$C=\\varepsilon A/d=4(8.854\\times10^{-12})(10^{-2})/10^{-3}$.")
q(F,T,"Energy stored in a capacitor $C$ at voltage $V$?","$\\tfrac12CV^2$",["$CV^2$","$\\tfrac12CV$","$CV$"],"Also $\\tfrac12\\int\\varepsilon E^2\\,dv$ over the field.")
q(F,T,"The relation between $\\mathbf{E}$ and the potential $V$ is","$\\mathbf{E}=-\\nabla V$",["$\\mathbf{E}=\\nabla V$","$\\mathbf{E}=\\nabla\\times V$","$V=-\\nabla\\cdot\\mathbf{E}$"],"$\\mathbf{E}$ points downhill in potential.")
q(F,T,"Poisson's equation?","$\\nabla^2V=-\\rho_v/\\varepsilon$",["$\\nabla^2V=0$ everywhere","$\\nabla V=\\rho_v$","$\\nabla\\times V=\\rho_v$"],"It reduces to Laplace's equation where $\\rho_v=0$.")

# ---------------- Current and conductors ----------------
F,T="current-and-conductors",["conductors"]
L,Ar,s=100,1e-6,5.8e7; Rw=L/(s*Ar)
q(F,T,"Resistance of $100\\ \\mathrm{m}$ of copper wire with a $1\\ \\mathrm{mm^2}$ cross-section ($\\sigma=5.8\\times10^7$)?",num(Rw,'Ω'),[num(Rw*10,'Ω'),num(Rw/10,'Ω'),num(Rw*1000,'Ω')],"$R=\\ell/(\\sigma A)=100/(5.8\\times10^7\\cdot10^{-6})$.")
q(F,T,"Point form of Ohm's law?","$\\mathbf{J}=\\sigma\\mathbf{E}$",["$\\mathbf{E}=\\sigma\\mathbf{J}$","$V=IR$ only","$\\mathbf{J}=\\varepsilon\\mathbf{E}$"],"It holds at every point in a conductor.")
q(F,T,"Joule's law gives the power dissipated per unit volume as","$\\mathbf{J}\\cdot\\mathbf{E}=\\sigma E^2$",["$\\varepsilon E^2$","$\\mathbf{J}\\times\\mathbf{E}$","$\\sigma/E^2$"],"Total power is $\\int\\sigma E^2\\,dv=I^2R$.")
q(F,T,"Drift velocity of electrons is related to $\\mathbf{E}$ by","$\\mathbf{u}_e=-\\mu_e\\mathbf{E}$",["$\\mathbf{u}_e=\\mu_e\\mathbf{E}$","$\\mathbf{u}_e=\\sigma\\mathbf{E}$","$\\mathbf{u}_e=c$"],"Electrons drift against the field; $\\mu_e$ is the mobility.")
q(F,T,"Charge continuity says","$\\nabla\\cdot\\mathbf{J}=-\\partial\\rho_v/\\partial t$",["$\\nabla\\cdot\\mathbf{J}=0$ always","$\\nabla\\times\\mathbf{J}=\\rho_v$","$\\mathbf{J}=\\rho_v$"],"Current leaving a volume must drain the charge inside it.")
q(F,T,"Where does excess charge on a conductor sit?","On its outer surface",["Spread through its volume","At its centre","Nowhere: it leaves"],"Charge inside would make a field inside, which a conductor cannot hold in equilibrium.")

# ---------------- Magnetostatics ----------------
F,T="magnetostatics",["magnetostatics"]
I,r=10,0.05; B=MU0*I/(2*math.pi*r)
q(F,T,"$B$ at $5\\ \\mathrm{cm}$ from a long wire carrying $10\\ \\mathrm{A}$?",num(B,'T'),[num(B*2,'T'),num(B/2,'T'),num(MU0*I/(2*r),'T')],"$B=\\mu_0I/(2\\pi r)$.")
q(F,T,"Which way does $\\mathbf{B}$ circle a current flowing along $+z$?","$+\\hat{\\boldsymbol{\\phi}}$ (counterclockwise seen from above)",["$-\\hat{\\boldsymbol{\\phi}}$","Along $+\\hat{\\mathbf{z}}$","Radially outward"],"Right-hand rule: thumb along the current, fingers along $\\mathbf{B}$.")
q(F,T,"The magnetic force on a moving charge is","$q\\mathbf{u}\\times\\mathbf{B}$",["$q\\mathbf{B}$","$q\\mathbf{u}\\cdot\\mathbf{B}$","$q\\mathbf{E}\\times\\mathbf{B}$"],"It is perpendicular to the velocity, so it does no work.")
q(F,T,"Why is $\\nabla\\cdot\\mathbf{B}=0$?","There are no magnetic charges",["$\\mathbf{B}$ is always zero","Currents are always steady","$\\mu$ is constant"],"Field lines of $\\mathbf{B}$ always close on themselves.")
N,L_,I=1000,0.5,2; Bs=MU0*N*I/L_
q(F,T,"$B$ inside a long solenoid, $1000$ turns over $50\\ \\mathrm{cm}$, at $2\\ \\mathrm{A}$?",num(Bs,'T'),[num(Bs/2,'T'),num(Bs*2,'T'),num(Bs*10,"T")],"$B=\\mu_0nI$ with $n=N/\\ell=2000$ turns per metre.")
q(F,T,"Force per unit length between two parallel wires with currents in the same direction is","Attractive",["Repulsive","Zero","Along the wires"],"Like currents attract; opposite currents repel.")
q(F,T,"At a boundary with no surface current, which components are continuous?","Normal $\\mathbf{B}$ and tangential $\\mathbf{H}$",["Tangential $\\mathbf{B}$ and normal $\\mathbf{H}$","Only $\\mathbf{B}$","Nothing"],"$B_{1n}=B_{2n}$ always; $\\mathbf{H}_t$ jumps only by a surface current.")
q(F,T,"Energy density stored in a magnetic field?","$\\tfrac12\\mu H^2$",["$\\mu H^2$","$\\tfrac12\\varepsilon E^2$","$\\tfrac12LI$"],"Integrated over space it gives $\\tfrac12LI^2$.")

# ---------------- Time-varying fields ----------------
F,T="time-varying-fields",["time-varying"]
q(F,T,"Faraday's law in differential form?","$\\nabla\\times\\mathbf{E}=-\\partial\\mathbf{B}/\\partial t$",["$\\nabla\\cdot\\mathbf{E}=-\\partial\\mathbf{B}/\\partial t$","$\\nabla\\times\\mathbf{H}=-\\partial\\mathbf{B}/\\partial t$","$\\nabla\\times\\mathbf{E}=0$"],"A changing $\\mathbf{B}$ makes a curling $\\mathbf{E}$.")
u,B_,l=4,0.3,0.5
q(F,T,"A $0.5\\ \\mathrm{m}$ bar slides at $4\\ \\mathrm{m/s}$ across a $0.3\\ \\mathrm{T}$ field. The EMF?",num(u*B_*l,'V'),[num(u*B_,'V'),num(u*l,'V'),num(u*B_*l/2,'V')],"$V=uB\\ell$.")
q(F,T,"Lenz's law says the induced current","Opposes the change in flux that caused it",["Adds to the change in flux","Always flows clockwise","Is zero in a closed loop"],"That is the minus sign in Faraday's law.")
q(F,T,"What did Maxwell add to Ampère's law?","Displacement current $\\partial\\mathbf{D}/\\partial t$",["Conduction current $\\sigma\\mathbf{E}$","Magnetic charge","The Lorentz force"],"It makes Ampère's law consistent with charge continuity and predicts waves.")
q(F,T,"A material with $\\sigma/(\\omega\\varepsilon)\\gg1$ is","A good conductor",["A low-loss dielectric","A perfect insulator","Magnetic"],"Conduction current dominates displacement current.")
q(F,T,"An ideal transformer with $N_1/N_2=10$ and $V_1=120\\ \\mathrm{V}$ gives $V_2=$","$12\\ \\mathrm{V}$",["$1200\\ \\mathrm{V}$","$120\\ \\mathrm{V}$","$1.2\\ \\mathrm{V}$"],"$V_1/V_2=N_1/N_2$.")
q(F,T,"Peak EMF of an $N$-turn loop of area $A$ spinning at $\\omega$ in a field $B$?","$NBA\\omega$",["$NBA$","$BA\\omega$","$NBA/\\omega$"],"$\\Phi=BA\\cos\\omega t$, so $V=NBA\\omega\\sin\\omega t$.")

# ---------------- Plane waves ----------------
F,T="plane-waves",["plane-waves"]
q(F,T,"Intrinsic impedance of free space?",num(ETA0,'Ω'),[num(50,'Ω'),num(ETA0/2,'Ω'),num(ETA0*2,'Ω')],"$\\eta_0=\\sqrt{\\mu_0/\\varepsilon_0}\\approx120\\pi$.")
q(F,T,"In a plane wave, $\\mathbf{E}$, $\\mathbf{H}$ and the direction of travel are","Mutually perpendicular",["All parallel","$\\mathbf{E}\\parallel\\mathbf{H}$, both perpendicular to travel","$\\mathbf{E}$ along the direction of travel"],"A uniform plane wave is TEM, with $\\mathbf{E}\\times\\mathbf{H}$ along $\\hat{\\mathbf{k}}$.")
q(F,T,"For $\\mathbf{E}=\\hat{\\mathbf{x}}E_0\\cos(\\omega t-kz)$ in air, $\\mathbf{H}$ points along","$+\\hat{\\mathbf{y}}$",["$-\\hat{\\mathbf{y}}$","$+\\hat{\\mathbf{x}}$","$+\\hat{\\mathbf{z}}$"],"$\\tilde{\\mathbf{H}}=\\frac1\\eta\\hat{\\mathbf{z}}\\times\\hat{\\mathbf{x}}E_0=\\hat{\\mathbf{y}}E_0/\\eta$.")
d=1/math.sqrt(math.pi*1e6*MU0*5.8e7)
q(F,T,"Skin depth of copper at $1\\ \\mathrm{MHz}$?",num(d,'m'),[num(d*10,'m'),num(d/10,'m'),num(d*1000,'m')],"$\\delta_s=1/\\sqrt{\\pi f\\mu\\sigma}$.")
q(F,T,"In a good conductor, $\\alpha$ and $\\beta$ are","Equal",["$\\alpha=0$","$\\beta=0$","$\\alpha=2\\beta$"],"Both are $\\sqrt{\\pi f\\mu\\sigma}$.")
q(F,T,"How many dB is a loss of $1\\ \\mathrm{Np}$?","$8.686\\ \\mathrm{dB}$",["$1\\ \\mathrm{dB}$","$4.343\\ \\mathrm{dB}$","$20\\ \\mathrm{dB}$"],"$20\\log_{10}e=8.686$.")
E0=10
q(F,T,"Average power density of a $10\\ \\mathrm{V/m}$ plane wave in air?",num(E0**2/(2*ETA0),'W/m^2'),[num(E0**2/ETA0,'W/m^2'),num(E0/(2*ETA0),'W/m^2'),num(E0**2*ETA0/2,'W/m^2')],"$S_{\\mathrm{av}}=|E_0|^2/(2\\eta_0)$.")
q(F,T,"Phase angle of $\\eta_c$ in a good conductor?","$45^\\circ$",["$0^\\circ$","$90^\\circ$","$-45^\\circ$"],"$\\eta_c\\approx(1+j)\\alpha/\\sigma$: $\\mathbf{H}$ lags $\\mathbf{E}$ by $45^\\circ$.")

# ---------------- Polarization ----------------
F,T="polarization",["polarization"]
q(F,T,"$\\tilde{\\mathbf{E}}=(\\hat{\\mathbf{x}}+j\\hat{\\mathbf{y}})e^{-jkz}$ is","Left-hand circular",["Right-hand circular","Linear","Elliptical with axial ratio 2"],"$a_x=a_y$ and $\\delta=+90^\\circ$ for a wave toward $+z$.")
q(F,T,"$\\mathbf{E}=\\hat{\\mathbf{x}}\\cos(\\omega t-kz)-\\hat{\\mathbf{y}}\\,2\\cos(\\omega t-kz)$ is","Linear",["Left-hand elliptical","Right-hand circular","Right-hand elliptical"],"$\\delta=180^\\circ$: the two components stay in step (or exactly opposite), so $\\mathbf{E}$ stays on one line.")
q(F,T,"Axial ratio of a circularly polarized wave?","$1$",["$0$","$\\infty$","$\\sqrt2$"],"Major and minor axes are equal.")
q(F,T,"Axial ratio of a linearly polarized wave?","$\\infty$",["$1$","$0$","$2$"],"The minor axis is zero.")
q(F,T,"Adding equal LHC and RHC waves gives","A linearly polarized wave",["A circular wave of twice the amplitude","An elliptical wave","Nothing: they cancel"],"$(\\hat{\\mathbf{x}}+j\\hat{\\mathbf{y}})+(\\hat{\\mathbf{x}}-j\\hat{\\mathbf{y}})=2\\hat{\\mathbf{x}}$.")
q(F,T,"For a wave toward $+z$, the sign of the ellipticity angle $\\chi$ tells you","The handedness",["The amplitude","The frequency","The direction of travel"],"$\\chi>0$ is left-handed, $\\chi<0$ right-handed.")
q(F,T,"With $a_x=a_y$ and $\\delta=-60^\\circ$, the wave is","Right-hand elliptical",["Right-hand circular","Left-hand elliptical","Linear"],"Circular needs $\\delta=\\pm90^\\circ$; negative $\\delta$ is right-handed.")

# ---------------- Reflection at boundaries ----------------
F,T="reflection-at-boundaries",["boundaries"]
q(F,T,"$\\Gamma$ for air onto glass ($\\varepsilon_r=4$) at normal incidence?","$-1/3$",["$1/3$","$-1/2$","$2/3$"],"$\\eta_2=\\eta_0/2$, so $\\Gamma=(1/2-1)/(1/2+1)$.")
q(F,T,"At normal incidence on a perfect conductor, $\\Gamma=$","$-1$",["$0$","$+1$","$j$"],"$\\eta_2=0$.")
q(F,T,"Snell's law?","$n_1\\sin\\theta_i=n_2\\sin\\theta_t$",["$n_1\\cos\\theta_i=n_2\\cos\\theta_t$","$n_1\\theta_i=n_2\\theta_t$","$\\sin\\theta_i=\\sin\\theta_t$"],"The tangential phase must match along the boundary.")
tc_=deg(math.asin(1/1.5))
q(F,T,"Critical angle going from glass ($n=1.5$) into air?",f"${tr(tc_)}^\\circ$",[f"${tr(deg(math.atan(1/1.5)))}^\\circ$",f"${tr(deg(math.atan(1.5)))}^\\circ$","$90^\\circ$"],"$\\theta_c=\\sin^{-1}(n_2/n_1)$.")
tB=deg(math.atan(1.5))
q(F,T,"Brewster angle from air into glass ($n=1.5$)?",f"${tr(tB)}^\\circ$",[f"${tr(tc_)}^\\circ$",f"${tr(90-tB)}^\\circ$","$45^\\circ$"],"$\\theta_B=\\tan^{-1}(n_2/n_1)$.")
q(F,T,"At the Brewster angle, which polarization reflects?","Only perpendicular (TE)",["Only parallel (TM)","Both equally","Neither"],"$\\Gamma_\\parallel=0$ at $\\theta_B$.")
q(F,T,"A critical angle exists only when","The wave goes into a less dense medium ($n_2<n_1$)",["$n_2>n_1$","The media are magnetic","The wave is circularly polarized"],"$\\sin\\theta_c=n_2/n_1$ must be less than 1.")
q(F,T,"A quarter-wave antireflection coating between air and glass ($n=1.5$) needs index","$\\sqrt{1.5}\\approx1.22$",["$1.5$","$1.25$","$2.25$"],"$n_2=\\sqrt{n_1n_3}$, like a quarter-wave transformer.")
q(F,T,"Optical fibres guide light by","Total internal reflection at the core–cladding boundary",["Reflection off a metal coating","The Brewster effect","Absorption in the cladding"],"The core has a slightly higher index than the cladding.")

for folder,items in Q.items():
    n={}
    for x in items:
        t=x["topics"][0]; n[t]=n.get(t,0)+1; x["id"]=f"quiz-{t}-{n[t]:02d}"
    out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","content",folder,"quiz.json")
    json.dump({"unit":folder,"format":"Text with inline TeX in $...$. The correct choice is at index answer; the app shuffles the choices.","questions":[{"id":x.pop("id"),**x} for x in items]},open(out,"w"),ensure_ascii=False,indent=1)
print("quiz",{f:len(v) for f,v in Q.items()},"total",sum(len(v) for v in Q.values()))
