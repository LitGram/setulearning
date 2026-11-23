Quantum Mechanics I · Shiwali Sharma

## A Note to the Returning Student

You may remember orbitals, atomic energy levels and chemical spectra from B.Sc. Chemistry. This book reconnects those ideas to their physical and mathematical foundations. It does not assume that you still remember complex numbers, differential equations or matrix notation after a long break.

Quantum mechanics predicts measurement outcomes through a state and the rules for using that state. In the position description, the state is represented by a wavefunction. Its squared magnitude gives a probability density. An equation determines how it changes in time. Boundary conditions select allowed states and, in bound examples, discrete energies.

The aim is to understand those statements well enough to derive results and solve the MGSU problems. Read an explanation before memorising its formula. When you work an example, write the assumptions and interpret the answer. A number without its units or physical meaning is an unfinished answer.

Hindi meanings are aids to understanding. The main teaching language and technical vocabulary remain English. Each unit contains a glossary, a formula sheet with conditions, explained practice questions and short revision points. The questions are original model material; they are not presented as authenticated previous-year questions.

## Course Context and Contents

Coverage follows the Quantum Mechanics I course in the [MGSU programme brochure applicable to admissions in 2025–26](https://www.mgsubikaner.ac.in/PDF/68c7df9cd7f02.pdf), PDF pages 10–11. The semester table lists 20 internal and 80 external marks, while general assessment prose elsewhere in the brochure describes 100 theory marks. Follow the current examination notice and college guidance for your applicable scheme. This book does not predict particular questions or guarantee marks.

| Unit | Main learning route |
|---|---|
| 1 | Experimental motivation, Schrödinger equations, admissible states, probability and current, Ehrenfest theorem, wells, barriers and both oscillator methods |
| 2 | State vectors, completeness, delta functions, representations, matrices, unitary changes, commutators, uncertainty and minimum-product states, angular momentum, addition and tensor-operator matrix elements |
| 3 | Central potentials, spherical separation, hydrogen states and energies, non-degenerate and degenerate perturbation theory, Stark and Zeeman effects |

- [Before Unit 1: Rebuilding the Basics](#bridge)
- [Unit 1: Wavefunctions and One-Dimensional Motion](#unit-1)
- [Unit 2: States, Operators and Angular Momentum](#unit-2)
- [Unit 3: Hydrogen and Perturbation Theory](#unit-3)
- [Appendix 1: A Practical Study Route](#appendix-strategy)
- [Appendix 2: Extended Model Questions and Solution Routes](#appendix-pyq)
- [Appendix 3: References and Further Reading](#appendix-references)


## Before Unit 1: Rebuilding the Basics

### Waves and the Meaning of Frequency

A travelling sinusoidal wave can be written as cos(kx − ωt). The wave number k = 2π/λ describes spatial repetition; λ is wavelength. The angular frequency ω = 2πν describes time repetition; ν is frequency in hertz. The period is 1/ν. The phase kx − ωt is dimensionless: k has units m⁻¹ and ω has units s⁻¹.

A standing wave has a fixed spatial pattern. Its nodes are points where its amplitude is always zero. A string fixed at both ends supports only certain standing patterns because both endpoint conditions must hold. Quantum states in a box use similar mathematics, but their wavefunction is a probability amplitude, not a material string displacement.

### Complex Numbers and Conjugation

The number i satisfies i² = −1. A complex number z = a + ib has conjugate z\* = a − ib and squared magnitude |z|² = z\*z = a² + b². For z = 3 + 4i, the squared magnitude is 25 and the magnitude is 5. The conjugate of a product is the product of the conjugates.

Euler's formula is e^(iθ) = cos θ + i sin θ. Hence |e^(iθ)|² = 1. Multiplying a wavefunction by a common phase e^(iθ) leaves its probability density unchanged. Relative phases between components can change interference and measurement probabilities. Therefore the full wavefunction contains information beyond its position density alone.

In this edition, e^(q) means the exponential of q. Brackets keep its whole exponent together. A fractional power such as x^(−1/2) means 1/√x for positive x; a negative power indicates a reciprocal. A star after a symbol means complex conjugation, while a dagger after an operator means its adjoint.

**Worked refresher.** If ψ = A e^(ikx), then ψ\* = A\*e^(−ikx) and ψ\*ψ = |A|². If instead ψ = A(e^(ikx) + e^(−ikx)) = 2A cos kx, the density is 4|A|²cos²kx. The cross terms are the interference contribution.

### Probability, Density and Averages

For discrete outcomes, probabilities pᵢ obey pᵢ ≥ 0 and Σpᵢ = 1. An average is Σpᵢaᵢ. A continuous probability density ρ(x) has units of inverse length in one dimension, and probability in an interval is ∫ρ(x)dx. A density is not itself a probability; it may exceed 1 in appropriate units while its integral remains 1.

If a particle is uniformly distributed over 0 &lt; x &lt; L, its density is 1/L. Its probability in the first quarter is ∫₀^(L/4)(1/L)dx = 1/4. Its mean position is ∫₀^L x dx/L = L/2. In quantum mechanics, ρ = |ψ|², so a normalised one-dimensional ψ has units length⁻¹ᐟ².

### Derivatives and Integrals Used Here

The derivative of e^(ikx) is ik e^(ikx); a second derivative gives −k²e^(ikx). The derivative of sin kx is k cos kx. Integrals add small contributions; an integral of a density over an interval gives the amount in it. The useful identity sin²θ = (1 − cos 2θ)/2 gives ∫₀^L sin²(nπx/L)dx = L/2 for a positive integer n.

A partial derivative changes one independent variable while holding the others fixed. In ψ(x,t), ∂ψ/∂t holds x fixed and ∂ψ/∂x holds t fixed. A differential equation relates a function to its derivatives. Boundary conditions constrain the function at spatial boundaries, while an initial condition specifies its state at a starting time.

### Operators and Eigenvalues

An operator is an instruction that acts on a function or vector. Multiplication by x sends f(x) to xf(x). Differentiation sends f(x) to f′(x). Order can matter: differentiating xf gives f + xf′, while multiplying f′ by x gives only xf′.

An eigenfunction is one that an operator only multiplies by a number. For the momentum operator p̂ = −iħ d/dx, e^(ikx) is an eigenfunction because p̂e^(ikx) = ħk e^(ikx). The number ħk is the eigenvalue. This does not mean the plane wave is a normalised state over the entire infinite line; continuum normalisation is introduced in Unit 2.

### Energy Units and Useful Constants

An electronvolt is the energy gained by a particle of charge magnitude e through a potential difference of 1 volt. It is an energy unit, not a voltage. One eV = 1.602176634 × 10⁻¹⁹ J. Planck's constant is h; ħ = h/(2π), read “h-bar”.

For calculations in this book use h ≈ 6.626 × 10⁻³⁴ J·s, ħ ≈ 1.055 × 10⁻³⁴ J·s, m\_e ≈ 9.109 × 10⁻³¹ kg and hc ≈ 1240 eV·nm. Keep units consistent rather than mixing eV energies with SI masses inside the same square root without conversion.

### Readiness Check

1. Find |1 + i|². **Answer:** 2.
2. Differentiate e^(−iEt/ħ) with respect to t. **Answer:** (−iE/ħ)e^(−iEt/ħ).
3. A uniform density over a length 2 m is what? **Answer:** 0.5 m⁻¹.
4. Is an average necessarily an allowed single measurement result? **Answer:** No. Equal probabilities for outcomes 0 and 2 give mean 1 even if 1 is not an outcome.
5. What happens to |ψ|² under ψ → −ψ? **Answer:** Nothing; −1 is a common phase factor.

---

# Unit 1: Wavefunctions and One-Dimensional Motion


## भाग 1: Start Here

This unit connects experiments to a mathematical description of states. We will repeatedly use the same route: identify the potential, solve the wave equation in each region, impose physical boundary conditions, and calculate probabilities or currents.

The chemistry connection is useful: spectral lines suggest discrete energy differences, and molecular vibration motivates the oscillator. We will rebuild the needed reasoning rather than assume those old topics are still fresh.

## भाग 2: Build the Ideas

### 1.1 Why Classical Physics Needs an Extension

**In simple words:** Classical mechanics and electromagnetism work extremely well in many settings, but their original combination does not account for several microscopic observations. Quantum theory adds rules that explain those observations and recover classical behaviour in appropriate limits.

A hot body's spectrum is one example. Classical equipartition applied to electromagnetic modes gives an energy density per frequency interval u(ν,T) = 8πν²k\_BT/c³. Its integral diverges at high frequency. Planck's quantised exchange of energy gives:

> u(ν,T) = (8πhν³/c³)/[e^(hν/(k\_BT)) − 1].

Here k\_B is Boltzmann's constant and T is absolute temperature. At hν ≪ k\_BT, expand eˣ − 1 ≈ x to recover the classical low-frequency result. At high frequency, the exponential suppresses the spectrum. Statistical Physics develops this counting argument in detail.

Atomic line spectra provide another clue. The emitted photon has hν = E\_initial − E\_final. Stable discrete atomic energies are not explained by a naive radiating classical electron orbit. Bohr's model introduced stationary orbits and reproduced the simplest hydrogen energy pattern; the wave-mechanical theory later replaces those orbits by states. An orbital is not a narrow path along which an electron circles the nucleus.

The Stern–Gerlach experiment illustrates discrete magnetic-moment projections: an appropriately prepared silver-atom beam separates in a nonuniform magnetic field. In its ground state the relevant angular momentum includes electron spin. Two spots do not mean a little classical sphere has only two possible geometric orientations.

**Check your understanding.** Does quantum theory make every macroscopic Newtonian calculation useless? No. It explains when and why classical approximations work, and where they fail.

### 1.2 Photons: Photoelectric and Compton Effects

**In simple words:** Light transfers energy and momentum in events. The energy of one photon depends on frequency, while beam intensity determines how much energy arrives overall.

For one-photon photoemission from a metal with work function Φ:

> K\_max = hν − Φ; eV\_stop = K\_max; ν\_threshold = Φ/h.

Here e is the positive elementary-charge magnitude. Emission in this simple model requires hν ≥ Φ. Increasing intensity at fixed frequency raises the photon arrival rate; it does not raise each photon's energy. More complex intense-field processes lie outside this elementary model.

**Worked example.** For λ = 400 nm and Φ = 1.9 eV, photon energy is hc/λ = 1240/400 = 3.10 eV. Then K\_max = 1.20 eV and the stopping-potential magnitude is 1.20 V. A 700 nm photon has only 1.77 eV and cannot produce one-photon emission from this metal.

In Compton scattering, treat the electron as initially free and at rest. Conserve relativistic energy and momentum for the photon–electron collision. Eliminating the electron's recoil variables gives:

> λ′ − λ = (h/(m\_ec))(1 − cos θ).

θ is the photon scattering angle. The electron Compton wavelength h/(m\_ec) ≈ 0.002426 nm is distinct from a de Broglie wavelength that depends on particle momentum.

**Worked example.** An incoming wavelength 0.050 nm scattered through 90° increases by 0.002426 nm. Thus λ′ ≈ 0.05243 nm. At 180° the increase is twice the Compton wavelength; at zero angle it is zero.

**Try it.** A 3 eV photon hits a metal with Φ = 2 eV. **Answer:** K\_max = 1 eV and stopping magnitude 1 V.

### 1.3 Matter Waves and Wave Packets

**In simple words:** Particles also produce interference and diffraction. Their momentum determines a wave scale, even though a detector records individual events.

The de Broglie relation is λ = h/p. For a nonrelativistic particle p = mv and E\_kinetic = p²/(2m). An electron accelerated from rest through a voltage magnitude U has p = √(2m\_eeU), giving:

> λ ≈ 1.226/√U nm, with U in volts and nonrelativistic motion.

For U = 100 V, λ ≈ 0.1226 nm, comparable to crystal spacings. Davisson–Germer electron diffraction provided experimental support for matter waves. Use the actual scattering geometry when converting a measured angle into the Bragg angle; the two angles are not automatically identical.

A single plane wave e^(ikx) has one momentum ħk and extends over all x. A **wave packet** adds a range of wave numbers to localise the state. Different components interfere constructively in one region and less strongly elsewhere. With ω(k) = ħk²/(2m), the group velocity is dω/dk = ħk/m, matching the nonrelativistic particle velocity near the packet's central momentum. Its phase velocity ω/k = ħk/(2m) is different.

For free-particle energy differences, a momentum distribution can make the packet spread. Unit 2 constructs the Gaussian packet and relates its widths to uncertainty.

**Try it.** If momentum magnitude doubles, what happens to λ? **Answer:** It halves. If an electron accelerating voltage quadruples in the nonrelativistic regime, its wavelength also halves.

### 1.4 The Time-Dependent Schrödinger Equation

**In simple words:** Given an initial state and a Hamiltonian, the Schrödinger equation tells us how the state changes. In this course it is a foundational dynamical law, not something derived from classical Newtonian motion alone.

For a nonrelativistic spinless particle of constant mass in a real scalar potential:

> iħ ∂ψ(x,t)/∂t = [−ħ²/(2m) ∂²/∂x² + V(x,t)]ψ(x,t) = Ĥψ.

The kinetic operator follows p̂²/(2m) with p̂ = −iħ∂/∂x. The equation is linear: if ψ₁ and ψ₂ solve it for the same Ĥ, so does c₁ψ₁ + c₂ψ₂. Normalise that combination before assigning probabilities. One initial wavefunction together with the operator domain and spatial boundary conditions determines its subsequent evolution in the usual well-posed setting.

**Worked substitution.** For V = 0, take ψ = A e^(i(kx − ωt)). Then ∂ψ/∂t = −iωψ and ∂²ψ/∂x² = −k²ψ. Substitution gives ħω = ħ²k²/(2m). Momentum is p = ħk and energy is E = ħω. This is a useful eigenfunction for scattering calculations, though it is not square-normalisable over an infinite line.

The phase of ψ is essential to interference and momentum predictions. Saying that only its density “has physical meaning” would discard relative-phase information needed for those predictions.

### 1.5 Energy Eigenstates and Stationary States

**In simple words:** For a time-independent Hamiltonian, a definite-energy state changes only by a common phase. Its probability density is unchanged even though the wavefunction has time dependence.

Set V = V(x) and try ψ(x,t) = φ(x)f(t). Substitute into the TDSE and divide where the factors are nonzero:

> iħ f′/f = [−ħ²φ″/(2m) + Vφ]/φ.

The left side depends only on t and the right only on x, so both equal a constant E. The separated equations are:

> Ĥφ = Eφ; f(t) = e^(−iEt/ħ).

E is an energy eigenvalue. The density is |φ(x)|² because the time factor has unit modulus. A stationary density requires ∂j/∂x = 0 through continuity, not j = 0. A travelling plane-wave energy eigenfunction has constant nonzero current. Many normalisable nondegenerate bound states in a real one-dimensional potential can be chosen real and have zero current; that is a more specific statement.

For a superposition of different energies, ψ = c₁φ₁e^(−iE₁t/ħ) + c₂φ₂e^(−iE₂t/ħ), interference terms generally oscillate at frequency difference (E₂ − E₁)/ħ. It need not be a stationary state even when Ĥ itself is time independent.

**Try it.** Does an energy of 4 eV alone determine the current direction? **Answer:** No. The spatial wavefunction and boundary conditions are needed.

### 1.6 Probability, Normalisation and Admissibility

**In simple words:** The wavefunction is an amplitude. To obtain a probability, square its magnitude and integrate over the region of interest.

The **Born rule** gives P(a &lt; x &lt; b) = ∫ₐᵇ|ψ|²dx. A normalised bound or packet state obeys ∫all space|ψ|²dx = 1. For an observable Â, its expectation in such a state is ⟨A⟩ = ∫ψ\*Âψ dx, with a suitable operator domain. Its spread is ΔA = √(⟨A²⟩ − ⟨A⟩²).

**Admissible wavefunctions.** A physical bound-state wavefunction must have finite norm and satisfy the Hamiltonian's boundary and regularity conditions. For finite nonsingular scalar potentials and constant mass, ψ and ψ′ are continuous at an ordinary finite step. This follows by integrating the equation across a shrinking interval. At an ideal infinite wall impose ψ = 0 at the wall. A delta potential instead permits a specified derivative jump. Do not turn a useful rule for finite potentials into an unconditional rule for every singular model.

**Worked example.** Inside 0 &lt; x &lt; L, let φ = A sin(πx/L), zero outside. Normalisation gives |A|²L/2 = 1, so choose real A = √(2/L). The density is symmetric about L/2, giving ⟨x⟩ = L/2. Probability in the first half is 1/2. The wavefunction has units L⁻¹ᐟ²; its density has units L⁻¹.

![A box-state amplitude can change sign; its probability density is nonnegative and has a different shape.](images/quantum/amplitude_density.png)

**Try it.** Normalise ψ = A e^(−α|x|) on the full line, with α &gt; 0. **Answer:** 2|A|²∫₀^∞e^(−2αx)dx = |A|²/α = 1, so choose A = √α. This establishes normalisation, not that it solves every potential's Schrödinger equation.

### 1.7 Probability Current and the Continuity Equation

**In simple words:** Probability density may move between regions. Its local rate of increase equals incoming flow minus outgoing flow.

Start from the TDSE and its complex conjugate, assuming real V. Multiply the first by ψ\* and the conjugate equation by ψ, then subtract. The potential terms cancel. Combining the time derivatives and recognising a spatial derivative gives:

> ∂|ψ|²/∂t = (iħ/(2m))(ψ\*ψ″ − ψψ\*″).
> j = (ħ/(2mi))(ψ\*ψ′ − ψψ\*′) = (ħ/m) Im(ψ\*ψ′).
> ∂ρ/∂t + ∂j/∂x = 0, with ρ = |ψ|².

To check the derivative step, expand ∂(ψ\*ψ′ − ψψ\*′)/∂x: the first-derivative products cancel, leaving ψ\*ψ″ − ψψ\*″. Integrating continuity over an interval gives dP/dt = j(left) − j(right). In 3D, replace ∂j/∂x by ∇ · j. Magnetic vector potentials require the corresponding gauge-covariant current; the formula here is for the scalar-potential model stated above.

**Worked example.** For ψ = A e^(ikx), ψ′ = ikψ. Thus j = ħk|A|²/m. Positive k gives positive current; negative k reverses it. For a real standing wave, Im(ψ\*ψ′) = 0, so its current is zero.

**Try it.** A stationary density has j(left) = j(right) in an interval. Must both currents vanish? **Answer:** No. Equal nonzero flow in and out leaves the probability unchanged.

### 1.8 Ehrenfest's Theorem

**In simple words:** Quantum expectation values obey equations related to classical motion. They describe ensemble averages, not a definite microscopic path for each particle.

Differentiate ⟨A⟩ = ∫ψ\*Âψ dx. Use the TDSE for ∂ψ/∂t and its conjugate, with boundary terms or operator domains allowing Ĥ to be self-adjoint. The result is:

> d⟨A⟩/dt = ⟨[Â,Ĥ]⟩/(iħ) + ⟨∂Â/∂t⟩.

The commutator [Â,Ĥ] means ÂĤ − ĤÂ. For Ĥ = p̂²/(2m) + V(x), the canonical identity [x̂,p̂] = iħ gives [x̂,p̂²] = 2iħp̂. Therefore d⟨x⟩/dt = ⟨p⟩/m. Applying the momentum derivative to a test function shows [p̂,V] = −iħV′, hence:

> d⟨p⟩/dt = −⟨V′(x)⟩.

In general ⟨V′(x)⟩ is not V′(⟨x⟩). For a harmonic potential V′ = mω²x, they agree exactly because the force is linear. For a nonlinear force, a narrow state can sometimes justify an approximation, with errors depending on its width.

**Worked example.** In a uniform gravitational field V = mgx, d⟨p⟩/dt = −mg and d²⟨x⟩/dt² = −g. The wave packet may also spread. Its mean follows the classical acceleration without the state being a point particle.

### 1.9 The Infinite Square Well

**In simple words:** Two impenetrable boundaries select standing wavefunctions. Only wavelengths that meet both boundaries survive, giving discrete energies.

Take V = 0 for 0 &lt; x &lt; L and infinite outside. Inside, φ″ + k²φ = 0 with k² = 2mE/ħ². The general solution is A sin kx + B cos kx. The condition φ(0) = 0 sets B = 0. Then φ(L) = 0 requires sin kL = 0, so kL = nπ. n = 0 gives the zero function, not a state. Negative n duplicates states up to a sign. Thus:

> φₙ(x) = √(2/L)sin(nπx/L), n = 1,2,…
> Eₙ = n²π²ħ²/(2mL²) = n²h²/(8mL²).

The ground energy is positive because a constant nonzero wavefunction cannot meet both walls. The nth state has n − 1 interior nodes. Its probability density and average position are not the same thing: every state has ⟨x⟩ = L/2, but an even-n state has a node at that point.

**Worked example.** For an electron in a 1.00 nm well, E₁ ≈ 0.376 eV. Then E₂ ≈ 1.504 eV and the gap E₂ − E₁ ≈ 1.128 eV. Doubling L divides every energy by four.

Useful expectation values are ⟨p⟩ = 0, ⟨p²⟩ = n²π²ħ²/L² and ⟨x²⟩ = L²[1/3 − 1/(2n²π²)]. Consequently Δx = L√[1/12 − 1/(2n²π²)] and Δp = nπħ/L. For n = 1 their product is approximately 0.568ħ, greater than ħ/2. A box ground state is not a minimum-product Gaussian.

**Try it.** Find E₃/E₁ and the number of interior nodes of φ₃. **Answer:** 9 and 2.

### 1.10 The Finite Square Well

**In simple words:** A finite wall allows a bound wavefunction to extend into the classically forbidden region. It still decays far away, so the state can be normalised.

Use V = −V₀ inside |x| &lt; a and V = 0 outside, with V₀ &gt; 0. Bound states have −V₀ &lt; E &lt; 0. Define k = √[2m(E + V₀)]/ħ inside and κ = √(−2mE)/ħ outside. Inside the wave oscillates; outside it decays. Discard exponentially growing tails at infinity.

Because the potential is even, choose states of definite parity. For an even state, φ\_inside = A cos kx and φ\_right = B e^(−κx). Matching φ and φ′ at x = a and dividing the derivative condition by the value condition gives k tan(ka) = κ. For an odd state, φ\_inside = A sin kx, giving −k cot(ka) = κ.

Set z = ka, y = κa and z₀ = a√(2mV₀)/ħ. Then z² + y² = z₀². Plot y = √(z₀² − z²) against z tan z or −z cot z in their positive branches. Their intersections are the allowed energies. These transcendental equations generally require graphical or numerical solution.

For a shallow one-dimensional attractive well there is at least one even bound state; odd states need sufficient width and depth. The penetration length is 1/κ. A state near the outside threshold E = 0 has a long tail. In the deep-well limit, the internal standing patterns approach those of a box of width 2a, after accounting for the shifted potential reference.

**Try it.** Does an exponentially decaying tail itself carry outward current for a bound state chosen real? **Answer:** No. Nonzero density outside the well does not mean a steady leakage of probability out of a stationary bound state.

### 1.11 Scattering from a Potential Step

**In simple words:** Even when classical motion permits passage, a quantum wave can be partly reflected by a sudden potential change. Compare currents rather than amplitudes alone.

Let V = 0 for x &lt; 0 and V = V₀ for x &gt; 0. For incidence from the left with E &gt; V₀, write:

> φ\_left = A e^(ik₁x) + B e^(−ik₁x); φ\_right = C e^(ik₂x),
> k₁ = √(2mE)/ħ; k₂ = √[2m(E − V₀)]/ħ.

There is no incoming wave from the far right in this setup. Matching φ and φ′ at zero gives A + B = C and k₁(A − B) = k₂C. Solving:

> B/A = (k₁ − k₂)/(k₁ + k₂); C/A = 2k₁/(k₁ + k₂).
> R = |B/A|²; T = (k₂/k₁)|C/A|².

Hence R + T = 1. The k₂/k₁ factor accounts for unequal flux per unit amplitude on the two sides. For equal particle mass and real positive wave numbers, R = (k₁ − k₂)²/(k₁ + k₂)² and T = 4k₁k₂/(k₁ + k₂)².

**Worked example.** Let E = 4V₀/3. Then k₁ = 2k₂, R = 1/9 and T = 8/9. There is reflection despite E &gt; V₀.

If 0 &lt; E &lt; V₀, the right solution is a decaying exponential with κ = √[2m(V₀ − E)]/ħ. It has zero transmitted current at infinity, so R = 1. The nonzero evanescent density is not a nonzero transmission coefficient through a semi-infinite step.

### 1.12 Tunnelling Through a Finite Barrier

**In simple words:** With a barrier of finite width, a decaying wave in the forbidden region can connect to an outgoing travelling wave beyond it. This produces nonzero transmitted current.

Let V = V₀ for 0 &lt; x &lt; a and zero outside, with 0 &lt; E &lt; V₀. Write the three regional solutions:

> φ\_I = A e^(ikx) + B e^(−ikx); φ\_II = C e^(κx) + D e^(−κx); φ\_III = F e^(ikx),
> k = √(2mE)/ħ; κ = √[2m(V₀ − E)]/ħ.

Keep both exponentials inside the finite interval: neither diverges at infinity within that region. Match φ and φ′ at x = 0 and a. Eliminating C,D gives the amplitude relation, up to a phase convention:

> A/F = e^(ika)[cosh(κa) + i(κ² − k²)sinh(κa)/(2kκ)].

Taking its squared magnitude yields |A/F|² = 1 + [(k² + κ²)²/(4k²κ²)]sinh²(κa). Equal outside wave numbers mean T = |F/A|², so:

> T = [1 + V₀²sinh²(κa)/(4E(V₀ − E))]⁻¹.

For κa ≫ 1, sinh²(κa) ≈ e^(2κa)/4, giving T ≈ [16E(V₀ − E)/V₀²]e^(−2κa). State the approximation; the exponential alone omits the prefactor. The particle's energy remains E throughout this static elastic scattering problem. Tunnelling does not require “borrowing” energy.

For E &gt; V₀, replace the forbidden-region parameter by k₂ = √[2m(E − V₀)]/ħ. The corresponding formula has sin²(k₂a) and E(E − V₀) in place of sinh²(κa) and E(V₀ − E). When k₂a is a positive integer multiple of π, T = 1: a transmission resonance.

![A finite barrier has an incoming and reflected wave on the left and an outgoing transmitted wave on the right. The energy remains below the barrier top.](images/quantum/barrier.png)

**Worked example.** Take E = V₀/2 and κa = 2. Then T = 1/[1 + sinh²2] = sech²2 ≈ 0.07065. The thick-barrier estimate 4e⁻⁴ ≈ 0.07326 is close but not exact at this width. Quantum tunnelling is relevant to alpha decay and to the strong distance dependence of a scanning tunnelling microscope's current; their full physical models contain more than this rectangular barrier.

### 1.13 The Oscillator by the Differential-Equation Method

**In simple words:** Near a stable equilibrium, a smooth molecular or mechanical potential is approximately quadratic. Solving that model gives discrete vibrational energy levels.

Take V = ½mω²x². Define ξ = √(mω/ħ)x and ε = E/(ħω). The TISE becomes d²φ/dξ² + (2ε − ξ²)φ = 0. At large |ξ|, normalisable solutions decay like e^(−ξ²/2). Set φ = e^(−ξ²/2)H(ξ). Differentiating twice and substituting gives:

> H″ − 2ξH′ + (2ε − 1)H = 0.

Expand H = Σᵣaᵣξʳ. Matching the coefficient of ξʳ gives:

> a\_(r+2) = [2r + 1 − 2ε]aᵣ/[(r + 2)(r + 1)].

Even and odd coefficients form separate chains. For a physical solution normalisable at both infinities, the appropriate chain must terminate. Setting its numerator to zero at r = n gives 2ε − 1 = 2n and:

> Eₙ = (n + ½)ħω, n = 0,1,2,…

The terminating functions are the Hermite polynomials: H₀ = 1, H₁ = 2ξ and H₂ = 4ξ² − 2. The normalised states are:

> φₙ(x) = (mω/(πħ))^(1/4) Hₙ(ξ)e^(−ξ²/2)/√(2ⁿn!).

They alternate even and odd parity and have n nodes. The ground energy is ½ħω, not zero. For a diatomic molecule's harmonic stretching coordinate, use the nuclei's reduced mass rather than the mass of the whole molecule. Real molecular potentials become anharmonic away from equilibrium.

**Try it.** If ħω = 0.20 eV, find E₀ and E₂. **Answer:** 0.10 eV and 0.50 eV.

### 1.14 The Oscillator by Ladder Operators

**In simple words:** Instead of repeatedly solving differential equations, use operators that move between neighbouring energy states.

Define a = √(mω/(2ħ))x̂ + ip̂/√(2mħω) and a† with the minus sign on the momentum term. Using [x̂,p̂] = iħ, direct expansion gives [a,a†] = 1. With N = a†a:

> Ĥ = ħω(N + ½); [N,a†] = a†; [N,a] = −a.

The expectation of N is nonnegative because ⟨ψ∣a†a∣ψ⟩ is the squared norm of a∣ψ⟩. Repeated lowering therefore ends at a lowest state obeying a∣0⟩ = 0. The allowed number eigenvalues are nonnegative integers, and normalisation gives:

> a∣n⟩ = √n ∣n − 1⟩; a†∣n⟩ = √(n + 1) ∣n + 1⟩.

In position space, aφ₀ = 0 becomes dφ₀/dx = −(mω/ħ)xφ₀. Integrate to obtain the Gaussian φ₀ = (mω/(πħ))^(1/4)e^(−mωx²/(2ħ)). This agrees with the differential-equation solution.

Invert the operator definitions: x̂ = √(ħ/(2mω))(a + a†) and p̂ = −i√(mħω/2)(a − a†). In a number state, raising or lowering once gives an orthogonal state, so ⟨x⟩ = ⟨p⟩ = 0. Expanding the squares gives:

> ⟨x²⟩ₙ = (n + ½)ħ/(mω); ⟨p²⟩ₙ = (n + ½)mħω.

Thus ΔxΔp = (n + ½)ħ. The ground state saturates ħ/2. Excited number states do not. This calculation prepares the uncertainty discussion in Unit 2.

## भाग 3: Put the Ideas Together

### A Two-Energy State in a Box

Let ψ(x,0) = [φ₁(x) + φ₂(x)]/√2 in the infinite well. Orthonormality makes its norm 1. The energy measurement probabilities are 1/2 for E₁ and 1/2 for E₂, and the mean energy is (E₁ + E₂)/2. That mean need not be an energy eigenvalue.

At time t, evolve each component with its own phase. The density is ½φ₁² + ½φ₂² + φ₁φ₂ cos[(E₂ − E₁)t/ħ] for the real box eigenfunctions. It is generally time dependent. Integrating the cross term over the whole box gives zero because the states are orthogonal, so total probability stays 1 while its spatial distribution changes.

### A Boundary-Condition Checklist

Identify which regions are oscillatory or exponential. Keep both independent solutions in a finite region; discard only those excluded by boundary conditions. Match the wavefunction and the derivative where the potential is an ordinary finite step. Use currents to form R and T. Check normalisation for bound states and R + T = 1 for the real-potential scattering models.

## भाग 4: Check Your Understanding

### 1.15 Common Mistakes and Their Corrections

- A stationary density can carry steady current.
- Relative phase affects interference; a common phase does not change predictions.
- A probability density has units and is not a probability at one exact point.
- A normalisable trial function is not automatically an eigenfunction of a specified Hamiltonian.
- At a finite step with constant mass, match both φ and φ′; infinite or singular potentials need their own conditions.
- Transmission is a current ratio, so unequal outside wave numbers require a velocity factor.
- A semi-infinite step and a finite-width barrier are different physical problems.
- Keep both exponentials inside a finite barrier region.
- A finite barrier's evanescent component does not represent lost energy.
- Box quantum numbers begin at 1; oscillator number states begin at 0.
- Ehrenfest's mean force is generally not the force evaluated at the mean position.
- Molecular vibrational coordinates use the relevant reduced mass and a local potential approximation.

## भाग 5: Practice Questions with Explanations

#### Question U1-01

What failed in the classical Rayleigh–Jeans spectrum at high frequency?

- **A.** Its integrated energy diverges
- **B.** It predicts no low-frequency radiation
- **C.** It requires negative temperature
- **D.** It gives only discrete wavelengths

**Answer: A.** The mode energy combined with the density of modes produces an unbounded high-frequency integral.

#### Question U1-02

In the elementary photon model, one photon's energy is what?

- **A.** h/ν
- **B.** hν
- **C.** mc
- **D.** ν/h

**Answer: B.** Photon energy is proportional to frequency, independently of how many photons arrive.

#### Question U1-03

At fixed frequency above threshold, increasing weak-light intensity primarily changes what in elementary photoemission?

- **A.** Energy of each photon
- **B.** Metal's charge magnitude e
- **C.** Photon arrival rate
- **D.** Planck's constant

**Answer: C.** More photons can cause more emission events while the maximum one-photon kinetic energy stays fixed.

#### Question U1-04

Light of 400 nm has approximately which photon energy using hc = 1240 eV·nm?

- **A.** 0.310 eV
- **B.** 31.0 eV
- **C.** 496,000 eV
- **D.** 3.10 eV

**Answer: D.** Divide hc by wavelength with matching nanometre units.

#### Question U1-05

For that light and a 1.9 eV work function, the maximum photoelectron energy is what?

- **A.** 1.20 eV
- **B.** 5.00 eV
- **C.** 1.90 eV
- **D.** 3.10 eV

**Answer: A.** Energy conservation gives K\_max = 3.10 − 1.90 eV.

#### Question U1-06

For a free electron initially at rest, the Compton wavelength increase is largest at what photon angle?

- **A.** 0°
- **B.** 180°
- **C.** 45°
- **D.** 90°

**Answer: B.** The factor 1 − cos θ reaches two at backward scattering.

#### Question U1-07

If particle momentum doubles, what happens to de Broglie wavelength?

- **A.** It doubles
- **B.** It quadruples
- **C.** It halves
- **D.** It remains unchanged

**Answer: C.** The matter wavelength is h divided by momentum magnitude.

#### Question U1-08

A nonrelativistic electron accelerated through 100 V has approximately which wavelength?

- **A.** 1.226 nm
- **B.** 12.27 nm
- **C.** 122.7 nm
- **D.** 0.1226 nm

**Answer: D.** Use 1.226/√U nm with U = 100 volts.

#### Question U1-09

For a free nonrelativistic packet centred at wave number k, the group velocity is what?

- **A.** ħk/m
- **B.** ħk/(2m)
- **C.** 2ħk/m
- **D.** m/(ħk)

**Answer: A.** Differentiate ω = ħk²/(2m) with respect to k.

#### Question U1-10

Which statement correctly describes an infinite plane wave?

- **A.** It is a normalised finite packet
- **B.** It has definite momentum but is not square-normalisable over the whole line
- **C.** It has definite position
- **D.** It has zero momentum for every k

**Answer: B.** A constant spatial magnitude integrates to an infinite norm on the entire line.

#### Question U1-11

The Schrödinger equation used here is what kind of law?

- **A.** A consequence of Newton's law alone
- **B.** A definition of wavelength only
- **C.** A quantum dynamical postulate with a specified Hamiltonian
- **D.** An equation valid only for photons

**Answer: C.** The nonrelativistic theory specifies state evolution through its own dynamical equation.

#### Question U1-12

For ψ = A e^(i(kx − ωt)) and V = 0, which relation follows?

- **A.** ω = ck for every massive particle
- **B.** E = ħk²
- **C.** E = 0
- **D.** ħω = ħ²k²/(2m)

**Answer: D.** Substituting first time and second space derivatives yields the free-particle dispersion relation.

#### Question U1-13

For time-independent H, an energy eigenstate evolves with which factor?

- **A.** e^(−iEt/ħ)
- **B.** e^(−Et)
- **C.** e^(+Et/ħ)
- **D.** t²

**Answer: A.** The separated time equation is iħf′ = Ef.

#### Question U1-14

A stationary probability density implies which current condition in one dimension?

- **A.** Current is always zero
- **B.** Current is spatially constant
- **C.** Current must increase with x
- **D.** The wavefunction has no phase

**Answer: B.** Continuity gives ∂j/∂x = 0 when ∂ρ/∂t = 0.

#### Question U1-15

Can a stationary energy eigenfunction carry nonzero current?

- **A.** No, stationary means no flow
- **B.** Only if energy changes
- **C.** Yes, a travelling plane wave is an example
- **D.** Only if probability is not conserved

**Answer: C.** An unchanged density is compatible with equal steady incoming and outgoing flux.

#### Question U1-16

What can make a superposition of distinct energies have time-dependent density?

- **A.** A changing Planck constant
- **B.** A norm greater than one
- **C.** The absence of boundary conditions
- **D.** Their changing relative phase

**Answer: D.** Cross terms contain the phase difference evolving at the energy-gap frequency.

#### Question U1-17

The Born probability in an interval is what?

- **A.** The integral of the squared wavefunction magnitude
- **B.** The wavefunction value at its midpoint
- **C.** The wavefunction's signed integral
- **D.** The kinetic energy divided by length

**Answer: A.** Probability is obtained by integrating density, not amplitude.

#### Question U1-18

What units has a normalised one-dimensional wavefunction?

- **A.** Length
- **B.** Length⁻¹ᐟ²
- **C.** Energy
- **D.** Dimensionless for every coordinate choice

**Answer: B.** Its squared magnitude times dx must be dimensionless.

#### Question U1-19

Does a continuous probability density exceeding 1 in chosen units violate normalisation?

- **A.** Yes, every density must be below 1
- **B.** Only if it is negative
- **C.** No, its integral is the probability
- **D.** It implies a negative norm

**Answer: C.** Density has units and need not obey the dimensionless bound for an interval probability.

#### Question U1-20

For φ = A sin(πx/L) on 0 &lt; x &lt; L, choose a real positive A giving unit norm.

- **A.** √(1/L)
- **B.** 2/L
- **C.** L/2
- **D.** √(2/L)

**Answer: D.** The integral of sin² over the well is L/2.

#### Question U1-21

For that symmetric box density, what is the mean position?

- **A.** L/2
- **B.** 0
- **C.** L
- **D.** L/4

**Answer: A.** The density has equal weight about the midpoint.

#### Question U1-22

At an ordinary finite potential step with constant mass, what is matched?

- **A.** Only φ′
- **B.** Both φ and φ′
- **C.** Only energy density
- **D.** Neither function nor derivative

**Answer: B.** Integrating the nonsingular Schrödinger equation across a shrinking interval gives the derivative condition as well as continuity.

#### Question U1-23

At an ideal infinite wall of a box, which condition is imposed?

- **A.** φ′ = 0 at both walls for every state
- **B.** φ is infinite
- **C.** φ = 0 at the wall
- **D.** The current must be positive

**Answer: C.** The allowed domain enforces vanishing wavefunction at the impenetrable boundary.

#### Question U1-24

For real scalar V, which equation describes local probability balance?

- **A.** ∂ρ/∂t = ρ
- **B.** j = Eρ always
- **C.** ρ + j = 1
- **D.** ∂ρ/∂t + ∂j/∂x = 0

**Answer: D.** The continuity equation balances density change with spatial flux divergence.

#### Question U1-25

For ψ = A e^(ikx), what is its probability current?

- **A.** ħk abs(A)²/m
- **B.** Zero for every k
- **C.** ħk² abs(A)²/m
- **D.** mħk

**Answer: A.** Differentiate the plane wave and take the imaginary part of ψ\*ψ′.

#### Question U1-26

For a real bound-state spatial wavefunction, the scalar-potential current is what?

- **A.** Always positive
- **B.** Zero
- **C.** Always negative
- **D.** Equal to its energy

**Answer: B.** The product φφ′ is real, so its imaginary part vanishes.

#### Question U1-27

Which is Ehrenfest's momentum equation for a scalar potential?

- **A.** d⟨p⟩/dt = −V′(⟨x⟩) for every state
- **B.** d⟨p⟩/dt = 0 always
- **C.** d⟨p⟩/dt = −⟨V′(x)⟩
- **D.** d⟨p⟩/dt = ⟨V⟩

**Answer: C.** The theorem gives the average of the force, not generally the force at the average position.

#### Question U1-28

For which potential is the mean force exactly the force at the mean position?

- **A.** Every nonlinear potential
- **B.** An arbitrary singular potential
- **C.** Only an infinite wall
- **D.** A harmonic potential

**Answer: D.** The harmonic force is linear in x, so averaging commutes with that linear expression.

#### Question U1-29

Why is n = 0 excluded from the infinite-well eigenstates?

- **A.** It produces the zero function
- **B.** It produces an infinite energy
- **C.** It has negative probability
- **D.** It violates relativistic motion

**Answer: A.** A sine with zero wave number is zero everywhere and cannot be normalised.

#### Question U1-30

Infinite-well energy scales with width in which way?

- **A.** L²
- **B.** L⁻²
- **C.** L
- **D.** It is independent of L

**Answer: B.** The allowed wave number is nπ/L and kinetic energy is proportional to its square.

#### Question U1-31

How many interior nodes has the nth infinite-well state?

- **A.** n
- **B.** n + 1
- **C.** n − 1
- **D.** 2n

**Answer: C.** The n half-wave pattern has n − 1 zeroes strictly between the walls.

#### Question U1-32

For an electron in a 1 nm box, E₁ is approximately what?

- **A.** 13.6 eV
- **B.** 3.76 keV
- **C.** 0.00376 eV
- **D.** 0.376 eV

**Answer: D.** Substituting the electron mass and box width into h²/(8mL²) gives the stated scale.

#### Question U1-33

For the symmetric finite well with V = −V₀ inside and zero outside, bound energies lie where?

- **A.** −V₀ &lt; E &lt; 0
- **B.** E &gt; V₀ only
- **C.** E &lt; −V₀
- **D.** Only E = 0

**Answer: A.** They oscillate inside while decaying outside the well.

#### Question U1-34

Which relation selects the even bound states for finite-well half-width a?

- **A.** k cot(ka) = κ
- **B.** k tan(ka) = κ
- **C.** k = −κ always
- **D.** sin(ka) = 0 for every finite depth

**Answer: B.** Matching the cosine interior to an exponentially decaying exterior gives the tangent condition.

#### Question U1-35

For a bound state approaching the outside energy threshold from below, its decay length does what?

- **A.** Becomes zero
- **B.** Becomes negative
- **C.** Increases
- **D.** Stays fixed for every well

**Answer: C.** The decay wave number κ tends to zero and the length is 1/κ.

#### Question U1-36

For scattering above a step with k₁ = 2k₂, what is the reflection coefficient?

- **A.** 1/3
- **B.** 4/9
- **C.** 8/9
- **D.** 1/9

**Answer: D.** The reflected amplitude is (k₁ − k₂)/(k₁ + k₂) = 1/3, whose square is 1/9.

#### Question U1-37

Why does T at an unequal-potential step include k₂/k₁?

- **A.** To convert squared amplitude into a current ratio
- **B.** To renormalise Planck's constant
- **C.** To remove the reflected wave
- **D.** To make the energy change

**Answer: A.** Flux per unit squared amplitude depends on wave number for fixed mass.

#### Question U1-38

Below a semi-infinite upward step, the transmitted current at infinity is what?

- **A.** Equal to incident current
- **B.** Zero
- **C.** Always one half
- **D.** Infinite

**Answer: B.** The admissible right-hand solution decays and carries no outgoing travelling flux.

#### Question U1-39

Inside a finite barrier below its top, which solution terms are kept before matching?

- **A.** Only the decaying exponential everywhere
- **B.** Only a sine
- **C.** Both growing and decaying exponentials
- **D.** Only the zero function

**Answer: C.** The region is finite, so neither exponential is excluded by an infinite-distance divergence there.

#### Question U1-40

Does tunnelling through a static elastic barrier require a temporary increase in total energy?

- **A.** Yes, by exactly V₀
- **B.** Yes, by an uncertainty-time borrowing rule
- **C.** Only if the barrier is thin
- **D.** No

**Answer: D.** The stationary scattering solution retains the same energy across all regions.

#### Question U1-41

For E = V₀/2 and κa = 2, exact barrier transmission is approximately what?

- **A.** 0.07065
- **B.** 0.5
- **C.** 1
- **D.** 0

**Answer: A.** The formula reduces to sech²2.

#### Question U1-42

For a harmonic oscillator, which energies are allowed?

- **A.** n²ħω with n ≥ 1
- **B.** (n + ½)ħω with n ≥ 0
- **C.** Only zero energy
- **D.** Continuous energies for every bound state

**Answer: B.** Normalisability of the differential equation or the ladder algebra gives equally spaced levels.

#### Question U1-43

For ħω = 0.20 eV, the oscillator ground energy is what?

- **A.** 0 eV
- **B.** 0.20 eV
- **C.** 0.10 eV
- **D.** 0.40 eV

**Answer: C.** The lowest number state has n = 0 but retains its half-quantum energy.

#### Question U1-44

Which ladder action is correctly normalised?

- **A.** a∣n⟩ = n²∣n + 1⟩
- **B.** a†∣n⟩ = √n ∣n − 1⟩
- **C.** a∣0⟩ = ∣1⟩
- **D.** a∣n⟩ = √n ∣n − 1⟩

**Answer: D.** The coefficient follows by taking the norm with N = a†a.

#### Question U1-45

Which oscillator number state has ΔxΔp = ħ/2?

- **A.** The ground state only
- **B.** Every excited number state
- **C.** No state
- **D.** Only n = 2

**Answer: A.** The number-state product is (n + ½)ħ.


## भाग 6: Quick Revision and Terminology

### 6.1 Sixty Revision Points

1. A photon has energy hν and momentum h/λ.
2. Classical equipartition with electromagnetic modes produces the ultraviolet divergence.
3. Planck's spectrum approaches the Rayleigh–Jeans result at low frequency.
4. Atomic line frequencies correspond to energy differences divided by h.
5. An orbital is a state description, not a classical electron trajectory.
6. The one-photon photoelectric threshold is ν = Φ/h.
7. Elementary photoelectron maximum kinetic energy is hν − Φ.
8. Stopping-potential magnitude obeys eV\_stop = K\_max.
9. Increasing light intensity does not raise the energy of each fixed-frequency photon.
10. The Compton shift assumes an initially free electron at rest.
11. Compton wavelength increase is maximal for backward photon scattering.
12. The de Broglie wavelength is h/p.
13. An electron's nonrelativistic accelerating-voltage wavelength scales as U⁻¹ᐟ².
14. Wave number is k = 2π/λ and angular frequency is ω = 2πν.
15. For a free massive particle, E = ħ²k²/(2m).
16. Free-particle group velocity is dω/dk = ħk/m.
17. A packet superposes wave numbers to create spatial localisation.
18. An infinite plane wave is not a normalised finite-norm state on the full line.
19. The Schrödinger equation is linear in the wavefunction.
20. Time-independent energy eigenstates acquire a common phase e^(−iEt/ħ).
21. A stationary state has time-independent density.
22. Stationary density does not imply zero current.
23. Different-energy components generally acquire a changing relative phase.
24. A common overall phase leaves measurement probabilities unchanged.
25. Relative phase can change interference and other-basis probabilities.
26. The Born probability is an integral of squared amplitude magnitude.
27. A one-dimensional density has inverse-length units.
28. A normalised one-dimensional wavefunction has length⁻¹ᐟ² units.
29. A probability density may exceed one in chosen units without violating normalisation.
30. Expectation values are averages across identically prepared measurements.
31. The standard deviation is the square root of the variance.
32. Finite-norm trial functions must also satisfy the Hamiltonian's domain conditions.
33. At an ordinary finite step with constant mass, φ and φ′ are continuous.
34. At an infinite box wall, the allowed wavefunction vanishes.
35. A delta potential has a specified derivative jump rather than universal derivative continuity.
36. For a real scalar potential, probability obeys the continuity equation.
37. Scalar-potential current is (ħ/m) times the imaginary part of ψ\*ψ′.
38. A positive-k plane wave has positive current.
39. A real bound-state spatial function has zero scalar-potential current.
40. Integrated density change equals incoming minus outgoing probability current.
41. Ehrenfest's position relation is d⟨x⟩/dt = ⟨p⟩/m.
42. Ehrenfest's momentum relation is d⟨p⟩/dt = −⟨V′⟩.
43. The average nonlinear force need not equal force at the average position.
44. Infinite-box eigenfunctions are normalised sine functions on the interval.
45. Infinite-box quantum numbers begin at n = 1.
46. Infinite-box energies scale as n²/L².
47. The nth box state has n − 1 interior nodes.
48. The box mean position is its midpoint for every energy eigenstate.
49. The box ground uncertainty product exceeds ħ/2.
50. Finite-well bound states decay outside the well.
51. Finite-well even states satisfy k tan ka = κ for the stated convention.
52. Finite-well odd states satisfy −k cot ka = κ.
53. Step transmission is a current ratio, not generally a squared amplitude alone.
54. Below a semi-infinite step, the evanescent tail has zero transmitted current at infinity.
55. A finite barrier retains both internal exponential solutions before boundary matching.
56. Static elastic tunnelling conserves the particle's total energy.
57. Thick-barrier transmission has an exponential suppression and an energy-dependent prefactor.
58. Oscillator normalisability gives Eₙ = (n + ½)ħω with n beginning at zero.
59. The ladder operators obey [a,a†] = 1 and N = a†a.
60. The oscillator ground state is a minimum-product Gaussian with energy ½ħω.

### 6.2 Hindi-Supported Glossary

| English term | Hindi aid | Plain-English meaning |
|---|---|---|
| Wavefunction | तरंग फलन | Position-space representation of a quantum state |
| Probability | प्रायिकता | Likelihood of an outcome |
| Amplitude | आयाम | Quantity combined before squaring to obtain probabilities |
| Probability density | प्रायिकता घनत्व | Probability per unit coordinate interval or volume |
| Normalisation | प्रसामान्यीकरण | Setting total probability to one |
| Expectation value | प्रत्याशा मान | Mean of many measurements on identically prepared states |
| Stationary state | स्थिर प्रायिकता वाला अवस्था रूप | Energy eigenstate with a common time phase |
| Probability current | प्रायिकता धारा | Flow entering the local probability-balance equation |
| Boundary condition | सीमा शर्त | Requirement at a boundary or infinity |
| Node | नोड, शून्य आयाम बिंदु | Point where the wavefunction vanishes |
| Reflection | परावर्तन | Outgoing flow back towards the incident side |
| Transmission | संचरण | Outgoing flow beyond the scattering region |
| Tunnelling | सुरंगन | Transmission across a finite forbidden region |
| Harmonic oscillator | सरल आवर्ती दोलक | Model with a quadratic restoring potential |
| Zero-point energy | शून्य-बिंदु ऊर्जा | Nonzero lowest oscillator energy |
| Ladder operator | सोपान संकारक | Operator connecting neighbouring number states |

### 6.3 Formula Sheet with Conditions

| Result | Conditions or interpretation |
|---|---|
| K\_max = hν − Φ | Elementary one-photon photoemission model |
| λ = h/p | Momentum-dependent matter wavelength |
| iħ∂ψ/∂t = Ĥψ | Appropriate Hamiltonian and operator domain |
| Ĥφ = Eφ; ψ = φe^(−iEt/ħ) | Time-independent Hamiltonian and energy eigenstate |
| P(a,b) = ∫ₐᵇρ dx | ρ = squared wavefunction magnitude |
| j = (ħ/m)Im(ψ\*ψ′) | Constant mass, scalar potential, no vector potential |
| d⟨A⟩/dt = ⟨[Â,Ĥ]⟩/(iħ) + ⟨∂Â/∂t⟩ | Ehrenfest identity with valid domains |
| Eₙ = n²π²ħ²/(2mL²) | Infinite well of width L, n ≥ 1 |
| k tan ka = κ; −k cot ka = κ | Even/odd finite-well bound states for half-width a |
| T\_step = (k₂/k₁) times squared transmission amplitude | E above the step, equal masses |
| T\_barrier = [1 + V₀²sinh²κa/(4E(V₀ − E))]⁻¹ | Rectangular barrier, 0 &lt; E &lt; V₀, equal outside potentials |
| Eₙ = (n + ½)ħω | Harmonic oscillator, n ≥ 0 |

---

# Unit 2: States, Operators and Angular Momentum


## भाग 1: Start Here

The same state can be described by a wavefunction, a column of coefficients, or an abstract ket. These are different representations of one physical preparation. This unit builds that language from small examples before applying it to angular momentum and atomic transitions.

**A matrix refresher.** A column with entries (a,b) represents two coefficients in a chosen ordered basis. A matrix acts by multiplying each row by that column and adding. The matrix with rows (0,1) and (1,0) sends (a,b) to (b,a). Matrix order matters: AB need not equal BA. An eigenvector satisfies Av = λv, so the matrix only scales that vector. For a two-by-two matrix with rows (a,b) and (c,d), the determinant is ad − bc; eigenvalues solve det(A − λI) = 0. I is the identity, which leaves every column unchanged.

The adjoint A† is the complex-conjugate transpose. First interchange rows and columns, then conjugate every entry. For a column, its adjoint is a conjugated row. This is the finite-dimensional version of the conjugation used in wavefunction inner products.

## भाग 2: Build the Ideas

### 2.1 States, Inner Products and Completeness

**In simple words:** A basis supplies building blocks for a state. Completeness says those blocks are sufficient to represent every state in the space under discussion.

In the position description, the inner product is ⟨φ∣ψ⟩ = ∫φ\*(x)ψ(x)dx. We use the physics convention: it is linear in the ket ψ and conjugate-linear in φ. The norm squared ⟨ψ∣ψ⟩ is nonnegative and equals one for a normalised state.

A Hilbert space is a complete inner-product space: every Cauchy sequence converges within the space. This mathematical completeness is distinct from completeness of a chosen basis. An orthonormal discrete basis obeys ⟨n∣m⟩ = δ\_nm and:

> ∑ₙ∣n⟩⟨n∣ = I; ∣ψ⟩ = ∑ₙcₙ∣n⟩; cₙ = ⟨n∣ψ⟩.

The first equation is the closure relation. Acting with its left side on a state reconstructs that state. For a complete discrete basis, normalisation gives Σ|cₙ|² = 1. General spectra may require both sums and integrals; a finite list of bound states alone need not be complete when continuum states are also available.

**Worked example.** In an orthonormal two-state basis, let ∣ψ⟩ = (√3/2)∣1⟩ + (i/2)∣2⟩. The norm is 3/4 + 1/4 = 1. A measurement in that basis gives outcome 1 with probability 3/4 and outcome 2 with probability 1/4. The phase i disappears in these two probabilities but can affect measurements in a different basis.

**Try it.** Are (1,0) and (1,1) an orthonormal basis? **Answer:** They are linearly independent and span the two-dimensional space, but their inner product is nonzero and the second vector is not unit-normalised.

### 2.2 The Dirac Delta and Continuous Bases

**In simple words:** The delta is a device for selecting a function's value inside an integral. It is a distribution, not an ordinary function with a usable finite or infinite value at one point.

Its defining sifting property is ∫f(x)δ(x − a)dx = f(a) when a is inside the integration range and f is a suitable test function. It can be visualised as the limit of narrower normalised peaks. A Gaussian representation is δ(x) = limit as ε → 0 of e^(−x²/ε²)/(√π ε). Its total integral is one while its width shrinks.

For nonzero real c, δ(cx) = δ(x)/|c|. For a smooth f with isolated simple roots xᵢ, δ(f(x)) = Σᵢδ(x − xᵢ)/|f′(xᵢ)|. The derivative distribution satisfies ∫g(x)δ′(x − a)dx = −g′(a), from integration by parts. Products of arbitrary distributions, such as δ(x)², are not automatically defined and should not be manipulated like ordinary functions.

Position eigenkets satisfy ⟨x∣x′⟩ = δ(x − x′) and ∫∣x⟩⟨x∣dx = I. They are generalised eigenstates rather than normalised finite-norm kets. The wavefunction is ψ(x) = ⟨x∣ψ⟩. With momentum kets normalised by ⟨p∣p′⟩ = δ(p − p′), choose:

> ⟨x∣p⟩ = e^(ipx/ħ)/√(2πħ).

The Fourier identity δ(x − x′) = (1/(2πħ))∫e^(ip(x − x′)/ħ)dp expresses closure. The delta has inverse units of its argument, ensuring consistent dimensions.

**Worked example.** ∫₀^∞x²δ(x − 3)dx = 9, while ∫₀^∞x²δ(x + 3)dx = 0 because the root −3 lies outside the interval. On the whole real line, ∫g(x)δ(2x − 6)dx = g(3)/2, not g(3).

**Try it.** Evaluate ∫g(x)δ′(x − 2)dx. **Answer:** −g′(2), with boundary conditions appropriate to the distribution identity.

### 2.3 Bra-Kets, Operators and Measurements

**In simple words:** A ket describes a state; a bra pairs with a ket to give an amplitude; an operator maps a ket to another ket. Their order determines the mathematical object.

Read ∣ψ⟩ as “ket psi” and ⟨φ∣ as “bra phi”. The inner product ⟨φ∣ψ⟩ is one complex number. The outer product ∣ψ⟩⟨φ∣ is an operator: acting on ∣χ⟩ gives ∣ψ⟩ times the number ⟨φ∣χ⟩.

In an ordered orthonormal basis, A\_nm = ⟨n∣Â∣m⟩. The mth column contains the expansion coefficients of Â∣m⟩. If ∣ψ⟩ has coefficient column c, then Â∣ψ⟩ has column Ac, and ⟨A⟩ = c†Ac. Observables use self-adjoint operators with the appropriate domains. Finite-dimensional matrices then obey A† = A. Their eigenvalues are real and eigenvectors of distinct eigenvalues are orthogonal.

To see the reality statement, take Â∣a⟩ = a∣a⟩. Self-adjointness gives ⟨a∣Â∣a⟩ equal to its complex conjugate, so a = a\* for a nonzero-norm eigenvector. For two distinct eigenvalues a,b, comparing ⟨a∣Â∣b⟩ in two ways gives (b − a)⟨a∣b⟩ = 0.

An ideal projective measurement with orthogonal projectors P\_a has probability ⟨ψ∣P\_a∣ψ⟩. Conditional on outcome a with nonzero probability, the post-measurement state is P\_a∣ψ⟩ divided by its norm. For a nondegenerate outcome, P\_a = ∣a⟩⟨a∣. With degeneracy, the projector covers the whole eigenspace; do not select a unique basis vector without further information.

**Worked example.** Let A have diagonal entries (2,−1) in a two-state basis and use the state from section 2.1. Then ⟨A⟩ = (3/4)2 + (1/4)(−1) = 5/4. A single ideal measurement returns 2 or −1, not 5/4.

### 2.4 Representations and Unitary Changes of Basis

**In simple words:** Changing the basis changes the coefficient column and operator matrix together. Predictions do not change when both are transformed consistently.

Let the columns of U be the new orthonormal basis vectors expressed in the old basis. Then U†U = I, the defining finite-dimensional unitary condition. If c is the old state column, the new column is c′ = U†c. The new operator matrix is A′ = U†AU. Therefore c′†A′c′ = c†Ac and the norm is preserved.

This is a passive basis change. An active unitary acting on a state while keeping the basis fixed is a different operation, although related formulas occur. State which meaning of U is being used.

For position and momentum representations, the transform kernel is ⟨x∣p⟩. Thus:

> φ(p) = (1/√(2πħ))∫e^(−ipx/ħ)ψ(x)dx,
> ψ(x) = (1/√(2πħ))∫e^(ipx/ħ)φ(p)dp.

In position space x̂ multiplies by x and p̂ = −iħ∂/∂x. In momentum space p̂ multiplies by p and x̂ = iħ∂/∂p, with suitable boundary conditions. One physical state has both representations; they are not two independent particles.

**Worked example.** For spin one-half, ∣+x⟩ = (∣+z⟩ + ∣−z⟩)/√2 and ∣−x⟩ = (∣+z⟩ − ∣−z⟩)/√2. A particle prepared in ∣+z⟩ has equal probabilities for the two x outcomes. Preparing ∣+x⟩ instead gives the +x outcome with certainty. This difference is information about the state, not about changing its notation.

![A spin state that is definite along z has equal probabilities for the two outcomes measured along x.](images/quantum/spin_bases.png)

### 2.5 Commutators and Compatible Observables

**In simple words:** A commutator tests whether two operator actions can be interchanged. It also enters the time-evolution and uncertainty equations.

Define [A,B] = AB − BA. Acting on a differentiable test function f gives:

> [x̂,p̂]f = x(−iħf′) − (−iħ)(xf)′ = iħf.

The derivative of xf includes f + xf′. Forgetting that first term gives an incorrect zero commutator. Hence [x̂,p̂] = iħI on the appropriate common domain.

The product identities are [A,BC] = [A,B]C + B[A,C] and [AB,C] = A[B,C] + [A,C]B. They follow by inserting and cancelling a middle product. Antisymmetry gives [A,B] = −[B,A]. The nested brackets satisfy the Jacobi identity. For a differentiable multiplication potential, [p̂,V(x)] = −iħV′(x).

In a finite-dimensional setting, commuting Hermitian operators can be simultaneously diagonalised. If one has a degenerate eigenspace, diagonalise the other within it. For unbounded operators in infinite dimensions, operator domains and the corresponding spectral compatibility require care; formal symbolic commutation alone is not the entire mathematical statement.

**Worked example.** [x,p²] = [x,p]p + p[x,p] = 2iħp. Also [x²,p] = x[x,p] + [x,p]x = 2iħx. These identities produce the Ehrenfest relations in Unit 1.

**Try it.** What is [A,A]? **Answer:** Zero. This says nothing by itself about whether A commutes with a different operator.

### 2.6 The Uncertainty Relation

**In simple words:** Identically prepared quantum states can give a spread of measurement outcomes. For certain pairs of observables those spreads cannot both be made arbitrarily small. This is a property of the state, not merely instrument disturbance.

Let δA = A − ⟨A⟩ and δB = B − ⟨B⟩ in a normalised state. Define ∣f⟩ = δA∣ψ⟩ and ∣g⟩ = δB∣ψ⟩. Cauchy–Schwarz gives:

> (ΔA)²(ΔB)² ≥ |⟨f∣g⟩|² = |⟨δAδB⟩|².

Split δAδB into half its anticommutator plus half its commutator. For self-adjoint A,B, the first contribution has real expectation and the second has imaginary expectation. Keeping only the squared imaginary part yields the Robertson bound:

> ΔAΔB ≥ ½|⟨[A,B]⟩|.

The stronger Schrödinger form also retains the squared covariance C\_AB = ½⟨δAδB + δBδA⟩:

> (ΔA)²(ΔB)² ≥ C\_AB² + (¼)|⟨[A,B]⟩|².

For x,p, [x,p] = iħ gives ΔxΔp ≥ ħ/2. The Δ symbols denote standard deviations, not errors in a particular simultaneous reading. For other operator pairs the commutator expectation can vanish in some states even when the operators do not commute. The simple bound then becomes uninformative in that state; it does not establish universal compatibility.

**Worked estimate.** If Δx = 0.10 nm, then Δp ≥ ħ/(2Δx) ≈ 5.27 × 10⁻²⁵ kg·m/s. For an electron this corresponds to velocity standard deviation at least 5.79 × 10⁵ m/s in the nonrelativistic relation p = mv. The bound is not a claim that the mean velocity has that value.

### 2.7 Minimum-Product Gaussian States

**In simple words:** Some states attain ΔxΔp = ħ/2. Their unchirped position wavefunctions have a Gaussian envelope and an optional linear phase that sets mean momentum.

Equality in Cauchy–Schwarz requires δp∣ψ⟩ proportional to δx∣ψ⟩. To attain the simple x–p product bound, choose δpψ = iλδxψ with real λ &gt; 0. Put x₀ = ⟨x⟩ and p₀ = ⟨p⟩. In position space:

> (−iħ d/dx − p₀)ψ = iλ(x − x₀)ψ.
> dψ/dx = [ip₀/ħ − λ(x − x₀)/ħ]ψ.

Integrating gives ψ = A exp[−λ(x − x₀)²/(2ħ) + ip₀x/ħ]. Set σ² = ħ/(2λ). Normalisation then yields:

> ψ(x) = (2πσ²)^(−1/4) exp[−(x − x₀)²/(4σ²) + ip₀x/ħ].

Its density is a Gaussian of mean x₀ and variance σ². Differentiating ψ gives ⟨p⟩ = p₀ and (Δp)² = ħ²/(4σ²). Thus Δx = σ and ΔxΔp = ħ/2. A common phase can be included without changing the result. A general Gaussian with an additional quadratic phase has position–momentum covariance and need not attain this simple product bound.

For free evolution, an initially unchirped Gaussian spreads according to σ\_x²(t) = σ² + ħ²t²/(4m²σ²), while its momentum spread stays constant. Its later x–p product generally exceeds ħ/2 even though the stronger covariance relation remains saturated. Minimum product at one time is not a promise of minimum product at all later times.

**Connection to Unit 1.** The oscillator ground state has σ² = ħ/(2mω), so it is a minimum-product Gaussian. The box ground state and excited oscillator number states do not have that product.

### 2.8 Angular Momentum Operators and Their Spectrum

**In simple words:** Angular momentum has a definite total magnitude and one definite chosen projection in a standard simultaneous eigenstate. Other component measurements generally have a spread.

For orbital angular momentum L̂ = r̂ × p̂, use L̂\_z = −iħ∂/∂φ and the analogous Cartesian expressions. The algebra is [L̂ₓ,L̂ᵧ] = iħL̂\_z, with cyclic permutations. General angular momentum Ĵ, including spin, satisfies the same algebra. Define Ĵ² = Ĵₓ² + Ĵᵧ² + Ĵ\_z². It commutes with every component, while different components do not generally commute with each other.

Choose simultaneous eigenkets ∣jm⟩ with Ĵ² eigenvalue ħ²j(j + 1) and Ĵ\_z eigenvalue ħm. Define Ĵ\_± = Ĵₓ ± iĴᵧ. The algebra gives [Ĵ\_z,Ĵ\_±] = ±ħĴ\_± and [Ĵ²,Ĵ\_±] = 0. Hence a ladder operation changes m by one while retaining j.

The squared ladder norms follow by multiplying Ĵ\_∓Ĵ\_± = Ĵ² − Ĵ\_z² ∓ ħĴ\_z:

> Ĵ\_±∣jm⟩ = ħ√[j(j + 1) − m(m ± 1)]∣j,m ± 1⟩.

Nonnegative norms bound the ladder. A highest state has Ĵ\_+∣j,m\_max⟩ = 0, giving m\_max = j; the lowest has m\_min = −j. Since steps have size one, 2j is a nonnegative integer. Thus j = 0,½,1,3/2,… and m = −j,…,+j. Orbital angular momentum has integer l due to single-valued spatial angular functions; spin may be half-integer.

**Worked example.** For j = 1, the magnitude is √2ħ and possible z results are −ħ,0,+ħ. A zero z result does not mean zero total angular momentum. In ∣1,0⟩, the transverse components supply the nonzero squared magnitude.

### 2.9 Spin One-Half and Angular-Momentum Examples

**In simple words:** Spin is intrinsic angular momentum. Its algebra can be represented by small matrices without imagining a tiny charged sphere rotating about an axis.

In the ordered z basis (∣+z⟩,∣−z⟩), write Ŝᵢ = (ħ/2)σᵢ. The Pauli matrices have rows:

| Matrix | First row | Second row |
|---|---|---|
| σₓ | (0,1) | (1,0) |
| σᵧ | (0,−i) | (i,0) |
| σ\_z | (1,0) | (0,−1) |

They obey σᵢ² = I and [σₓ,σᵧ] = 2iσ\_z. Therefore Ŝ² = 3ħ²I/4, corresponding to s = ½. The z eigenvalues are ±ħ/2. The total magnitude is √3ħ/2, not ħ/2.

For an orbital state with l = 2, L² = 6ħ², magnitude √6ħ, and m = −2,−1,0,1,2. A ladder step from m = 1 to 2 has coefficient ħ√[6 − 1×2] = 2ħ. A raising step from m = 2 vanishes.

**Worked measurement.** For ∣ψ⟩ = (√3/2)∣+z⟩ + (1/2)∣−z⟩, ⟨S\_z⟩ = ħ/4. Since every S\_z outcome squares to ħ²/4, (ΔS\_z)² = ħ²/4 − ħ²/16 = 3ħ²/16. Thus ΔS\_z = √3ħ/4. This average is not itself an allowed single S\_z outcome.

**Try it.** What are ⟨S\_x⟩ and ΔS\_x in ∣+z⟩? **Answer:** 0 and ħ/2.

### 2.10 Adding Angular Momenta

**In simple words:** For two angular momenta, we may label each separately or label their total. These are two bases in the same combined state space.

Let J = J₁ + J₂, with operators on different subsystems commuting. The uncoupled basis is ∣j₁m₁⟩∣j₂m₂⟩. The coupled basis is ∣j₁j₂;jm⟩, diagonalising J₁²,J₂²,J²,J\_z. The allowed totals are j = |j₁ − j₂|, |j₁ − j₂| + 1,…,j₁ + j₂. Their projections satisfy m = m₁ + m₂.

The total state count is preserved: Σⱼ(2j + 1) = (2j₁ + 1)(2j₂ + 1). For j₁ = 1 and j₂ = ½, j = 3/2 or 1/2, giving 4 + 2 = 6 states.

Use J² = J₁² + J₂² + 2J₁ · J₂. Therefore in a coupled state:

> ⟨J₁ · J₂⟩ = (ħ²/2)[j(j + 1) − j₁(j₁ + 1) − j₂(j₂ + 1)].

This is particularly useful for spin-coupling energies. For two spins one-half, the triplet j = 1 has S₁ · S₂ = ħ²/4, while the singlet j = 0 has −3ħ²/4. Adding quantum angular momenta does not mean adding only their classical magnitudes as ordinary numbers.

### 2.11 Clebsch–Gordan Coefficients by Lowering

**In simple words:** Clebsch–Gordan coefficients are the amplitudes that express a coupled state in the uncoupled basis. Their squared magnitudes give the corresponding basis-measurement probabilities.

For two spin-one-half particles, abbreviate ∣+z⟩ by ↑ and ∣−z⟩ by ↓. The highest state is ∣1,1⟩ = ∣↑↑⟩. Apply S\_- = S₁- + S₂-. The coupled ladder gives ħ√2∣1,0⟩, while the uncoupled action gives ħ(∣↓↑⟩ + ∣↑↓⟩). Equating them and normalising yields:

> ∣1,1⟩ = ∣↑↑⟩.
> ∣1,0⟩ = (∣↑↓⟩ + ∣↓↑⟩)/√2.
> ∣1,−1⟩ = ∣↓↓⟩.
> ∣0,0⟩ = (∣↑↓⟩ − ∣↓↑⟩)/√2.

The last state is normalised and orthogonal to the m = 0 triplet. Applying total S\_+ or S\_- annihilates it, consistent with j = 0. An overall sign of any whole ket is a phase convention; the relative sign within that singlet is physically significant.

For j₁ = 1 and j₂ = ½, start with ∣3/2,3/2⟩ = ∣1,1⟩∣½,½⟩. One lowering step gives:

> ∣3/2,1/2⟩ = √(2/3)∣1,0⟩∣½,½⟩ + √(1/3)∣1,1⟩∣½,−½⟩.

An orthogonal normalised state with j = ½,m = ½ can be chosen as √(1/3)∣1,0⟩∣½,½⟩ − √(2/3)∣1,1⟩∣½,−½⟩. Tables may choose its opposite overall sign. State counts, normalisation, orthogonality and ladder relations are checks on any CG table.

**Try it.** If ∣1,0⟩ for two spins is measured separately along z, what are the outcomes? **Answer:** ↑↓ and ↓↑ each with probability 1/2; ↑↑ and ↓↓ have zero probability.

### 2.12 Wigner–Eckart Theorem and Selection Rules

**In simple words:** Rotational symmetry separates angular geometry from the remaining physical information in a matrix element. Clebsch–Gordan coefficients supply the angular part.

A spherical tensor operator T\_q^(k) of rank k has components q = −k,…,k that transform like angular momentum k. In particular, [J\_z,T\_q^(k)] = ħqT\_q^(k), and its ladder commutators have the corresponding angular-momentum coefficients. A scalar has rank zero; position and electric dipole are rank-one vectors. For position, one convention is r₀ = z and r\_±1 = ∓(x ± iy)/√2.

Choose a reduced-matrix-element convention such that:

> ⟨α′j′m′∣T\_q^(k)∣αjm⟩ = C(jm,kq;j′m′) ⟨α′j′∥T^(k)∥αj⟩/√(2j′ + 1).

α labels additional quantum numbers. Other books may absorb the square-root factor or phases into their reduced element. Use one convention consistently. The reduced element is independent of m,m′,q.

**Why the theorem has this form.** Apply the J\_z and J\_± commutators to the matrix elements. They impose the same projection and ladder recursion relations as coupling j with k. The solution for the angular dependence is therefore proportional to the corresponding CG coefficients; the remaining proportionality is the reduced element.

The CG factor requires m′ = m + q and |j − k| ≤ j′ ≤ j + k. For electric dipole radiation, k = 1, so Δj = 0,±1 with 0 → 0 excluded. Orbital dipole transitions also require opposite parity because r is odd under inversion. For one-electron orbital states, this gives Δl = ±1 and Δm = 0,±1. These rules are necessary conditions; a remaining radial matrix element can still vanish. At the basic spin-independent dipole level, spin is unchanged.

**Worked example.** A hydrogen 2p → 1s electric-dipole transition satisfies Δl = −1. A 2s → 1s single-photon electric-dipole transition has Δl = 0 and is forbidden in this approximation, though other processes such as two-photon decay can occur. “Forbidden” is always relative to the interaction and approximation being discussed.

## भाग 3: Put the Ideas Together

### Same Probabilities, Different Relative Phases

Compare ∣ψ₊⟩ = (∣+z⟩ + ∣−z⟩)/√2 with ∣ψ₋⟩ = (∣+z⟩ − ∣−z⟩)/√2. Both give equal probabilities for S\_z. But they are +x and −x eigenstates, respectively, so their S\_x outcomes are opposite and certain. Position or basis probabilities in one representation do not specify every relative phase of a state.

### A Method for an Unfamiliar Operator Question

Identify the state space and ordered basis, write the operator action or matrix, and check its adjoint when it represents an observable. Find eigenvalues and normalised eigenvectors. Expand the given state in that basis to calculate probabilities. For uncertainty, calculate both first and second moments. For angular transitions, separate projection, triangle and parity restrictions from any radial calculation.

## भाग 4: Check Your Understanding

### 2.13 Common Mistakes and Their Corrections

- Completeness of a Hilbert space and completeness of an eigenbasis are different statements.
- A delta-normalised ket is not a unit-norm ordinary bound state.
- Use conjugation in a bra and the complex adjoint of a matrix.
- Specify whether a unitary is a basis change or an active change of state.
- An average need not be a single measurement outcome.
- Commutators act on functions or vectors; the order of differentiation matters.
- Uncertainty refers to standard deviations of prepared-state measurement distributions.
- A Gaussian with arbitrary quadratic phase need not minimise the simple x–p product.
- Angular-momentum magnitude is ħ√[j(j + 1)], while its z projection is ħm.
- CG coefficients are amplitudes, not probabilities.
- An overall ket phase is conventional; a relative sign can affect predictions.
- State the reduced-element convention and the interaction behind selection rules.

## भाग 5: Practice Questions with Explanations

#### Question U2-01

In the physics inner-product convention, which argument is linear?

- **A.** The bra argument
- **B.** The ket argument
- **C.** Neither argument
- **D.** Both without conjugation

**Answer: B.** The bra is conjugate-linear while the ket carries ordinary linear coefficients.

#### Question U2-02

For a complete discrete orthonormal basis, closure is which equation?

- **A.** Σ∣n⟩ = 0
- **B.** ⟨n∣n⟩ = 0
- **C.** Σ∣n⟩⟨n∣ = I
- **D.** ΣEₙ = 1

**Answer: C.** The sum of basis projectors reconstructs every state in that space.

#### Question U2-03

For coefficients √3/2 and i/2 in an orthonormal basis, the first-basis-outcome probability is what?

- **A.** √3/2
- **B.** 1/4
- **C.** 1/2
- **D.** 3/4

**Answer: D.** Probabilities are squared coefficient magnitudes, not the coefficients themselves.

#### Question U2-04

What is the Dirac delta mathematically?

- **A.** A distribution defined through integrals
- **B.** An ordinary bounded function
- **C.** A dimensionless probability at one point
- **D.** A matrix with every entry one

**Answer: A.** Its sifting action on test functions is the defining property.

#### Question U2-05

What is ∫g(x)δ(2x − 6)dx over the full line?

- **A.** g(3)
- **B.** g(3)/2
- **C.** 2g(3)
- **D.** g(6)

**Answer: B.** The root is at x = 3 and the derivative scale contributes 1/2.

#### Question U2-06

What is ∫g(x)δ′(x − a)dx with suitable boundaries?

- **A.** g′(a)
- **B.** g(a)
- **C.** −g′(a)
- **D.** Zero for every g

**Answer: C.** The derivative distribution transfers a derivative with a minus sign.

#### Question U2-07

Is a position eigenket a finite-norm normalised packet?

- **A.** Yes, it has a Gaussian norm
- **B.** Yes, it is a box ground state
- **C.** Only at x = 0
- **D.** No, it is a generalised eigenstate

**Answer: D.** Its inner products use delta normalisation rather than ordinary unit norm.

#### Question U2-08

Which object is an operator rather than one complex number?

- **A.** ∣ψ⟩⟨φ∣
- **B.** ⟨φ∣ψ⟩
- **C.** The norm squared
- **D.** One expansion coefficient

**Answer: A.** The outer product maps an input ket to a multiple of ∣ψ⟩.

#### Question U2-09

The matrix entry A\_nm equals what?

- **A.** ⟨m∣n⟩ for every A
- **B.** ⟨n∣Â∣m⟩
- **C.** Eₙ + E\_m
- **D.** The nth state probability

**Answer: B.** It is the nth coefficient in the expansion of Â acting on basis ket m.

#### Question U2-10

For diagonal observable eigenvalues 2 and −1 with probabilities 3/4 and 1/4, the mean is what?

- **A.** 1/2
- **B.** 2
- **C.** 5/4
- **D.** −1

**Answer: C.** The probability-weighted average is 2(3/4) − 1/4.

#### Question U2-11

Must that mean be an allowed individual measurement outcome?

- **A.** Yes for every observable
- **B.** Only if the state is complex
- **C.** Only if the basis changes
- **D.** No

**Answer: D.** An expectation is an ensemble average and need not equal an eigenvalue.

#### Question U2-12

What condition defines a finite-dimensional unitary matrix?

- **A.** U†U = I
- **B.** U† = 0
- **C.** U² = 0
- **D.** Every entry is real

**Answer: A.** Its adjoint is its inverse, preserving inner products.

#### Question U2-13

If columns of U are the new basis in old coordinates, what is the new state column?

- **A.** Uc for this stated convention
- **B.** U†c
- **C.** U + c
- **D.** c†U

**Answer: B.** Projecting onto the new basis gives the adjoint transformation.

#### Question U2-14

Under that passive basis change, what is the new operator matrix?

- **A.** UAU† for the same stated convention
- **B.** A + U
- **C.** U†AU
- **D.** A/U

**Answer: C.** The state and operator transformations together preserve expectation values.

#### Question U2-15

Which momentum-space position operator matches the stated Fourier convention?

- **A.** −iħ∂/∂p
- **B.** p
- **C.** ħp²
- **D.** iħ∂/∂p

**Answer: D.** Differentiating the momentum-space phase gives the position representation with the positive sign.

#### Question U2-16

What is [x̂,p̂] on the suitable common domain?

- **A.** iħI
- **B.** 0
- **C.** −iħI
- **D.** ħ²I

**Answer: A.** The derivative of xf contains the extra f term.

#### Question U2-17

Which commutator product identity is correct?

- **A.** [A,BC] = [A,B][A,C]
- **B.** [A,BC] = [A,B]C + B[A,C]
- **C.** [A,BC] = 0 always
- **D.** [A,BC] = C[A,B] only

**Answer: B.** Expand both products and cancel the inserted middle term.

#### Question U2-18

What is [x̂,p̂²]?

- **A.** iħp̂²
- **B.** 0
- **C.** 2iħp̂
- **D.** −2iħx̂

**Answer: C.** Use the product identity twice with the fundamental commutator.

#### Question U2-19

The Robertson uncertainty bound is what?

- **A.** ΔAΔB = 0 for every state
- **B.** ΔA + ΔB ≥ ħ always
- **C.** ΔAΔB ≥ ⟨A⟩⟨B⟩
- **D.** ΔAΔB ≥ ½abs(⟨[A,B]⟩)

**Answer: D.** Cauchy–Schwarz and the imaginary part of the centred-operator product give the bound.

#### Question U2-20

For position and momentum, the lower product bound is what?

- **A.** ħ/2
- **B.** ħ²
- **C.** 1/2 metre
- **D.** Zero for every packet

**Answer: A.** The commutator expectation is iħ in a normalised state.

#### Question U2-21

What do Δx and Δp denote here?

- **A.** Instrument dial spacing only
- **B.** Prepared-state standard deviations
- **C.** Mean position and mean momentum
- **D.** A mandatory simultaneous measurement error

**Answer: B.** They describe distributions across identically prepared state measurements.

#### Question U2-22

If the commutator expectation vanishes for one state, what follows from the simple Robertson bound?

- **A.** The operators commute universally
- **B.** Both variances must vanish
- **C.** It may give no nonzero lower bound in that state
- **D.** The state cannot exist

**Answer: C.** A zero bound is not proof of universal observable compatibility.

#### Question U2-23

Which extra term enters the stronger Schrödinger uncertainty inequality?

- **A.** The mass alone
- **B.** Total angular momentum alone
- **C.** A negative norm
- **D.** Squared covariance

**Answer: D.** The real part of the centred-operator product supplies the covariance contribution.

#### Question U2-24

For the unchirped Gaussian with density variance σ², Δp is what?

- **A.** ħ/(2σ)
- **B.** ħσ
- **C.** 2ħ/σ
- **D.** σ/ħ

**Answer: A.** Differentiating the normalised Gaussian gives momentum variance ħ²/(4σ²).

#### Question U2-25

Does every Gaussian with arbitrary quadratic phase attain ΔxΔp = ħ/2?

- **A.** Yes without conditions
- **B.** No
- **C.** Only if its norm is zero
- **D.** Only at infinite mass

**Answer: B.** A quadratic phase can create nonzero position–momentum covariance and increase the simple product.

#### Question U2-26

During free evolution of an initially unchirped Gaussian, what stays constant?

- **A.** Position variance
- **B.** Both variances for every packet
- **C.** Momentum variance
- **D.** The packet centre position

**Answer: C.** The free Hamiltonian preserves the momentum distribution while the position packet spreads.

#### Question U2-27

Which pair of angular observables commutes?

- **A.** Jₓ and Jᵧ universally
- **B.** Jᵧ and J\_z universally
- **C.** J\_z and Jₓ universally
- **D.** J² and J\_z

**Answer: D.** Total squared angular momentum commutes with each component.

#### Question U2-28

In ∣jm⟩, the angular-momentum magnitude is what?

- **A.** ħ√[j(j + 1)]
- **B.** ħm
- **C.** ħj for every j
- **D.** j²ħ²

**Answer: A.** The magnitude is the square root of the J² eigenvalue.

#### Question U2-29

Which m values belong to j = 1?

- **A.** Only +1
- **B.** −1,0,+1
- **C.** −½,+½
- **D.** Every integer

**Answer: B.** The projection ladder runs from −j to +j in unit steps.

#### Question U2-30

What does J\_+ do within a fixed-j multiplet?

- **A.** Raises j by one
- **B.** Changes ħ
- **C.** Raises m by one
- **D.** Always annihilates every state

**Answer: C.** Its commutator with J\_z is +ħJ\_+ and with J² is zero.

#### Question U2-31

For l = 2 and m = 1, the orbital raising coefficient is what?

- **A.** √2ħ
- **B.** 6ħ
- **C.** Zero
- **D.** 2ħ

**Answer: D.** Evaluate ħ√[6 − 1(2)] = 2ħ.

#### Question U2-32

Why is orbital l integer rather than half-integer in the scalar spatial problem?

- **A.** Single-valued regular angular wavefunctions impose integer angular labels
- **B.** All angular momentum must be integer
- **C.** Spin is absent from nature
- **D.** The radius is quantised to integers

**Answer: A.** The azimuthal factor and polar regularity restrict the spatial angular functions.

#### Question U2-33

For spin one-half, S² has which eigenvalue?

- **A.** ħ²/4
- **B.** 3ħ²/4
- **C.** ħ/2
- **D.** Zero

**Answer: B.** Use s(s + 1)ħ² with s = 1/2.

#### Question U2-34

In a +z spin-one-half state, an x-spin measurement gives what?

- **A.** Only +ħ/2
- **B.** Only zero
- **C.** ±ħ/2 with equal probabilities
- **D.** Only −ħ/2

**Answer: C.** The +z state has equal overlap magnitudes with the two x eigenstates.

#### Question U2-35

For state (√3/2)∣+z⟩ + (1/2)∣−z⟩, what is ⟨S\_z⟩?

- **A.** ħ/2
- **B.** 0
- **C.** 3ħ/4
- **D.** ħ/4

**Answer: D.** Weight +ħ/2 by 3/4 and −ħ/2 by 1/4.

#### Question U2-36

Adding j₁ = 1 and j₂ = 1/2 allows which total j values?

- **A.** 3/2 and 1/2
- **B.** Only 3/2
- **C.** Only 1
- **D.** 2 and 0

**Answer: A.** Total j runs from the absolute difference to the sum in unit steps.

#### Question U2-37

How many states are in that combined space?

- **A.** Three
- **B.** Six
- **C.** Four
- **D.** Two

**Answer: B.** The dimension is (2j₁ + 1)(2j₂ + 1) = 3 × 2.

#### Question U2-38

For two spins one-half, which state is the singlet?

- **A.** (∣↑↓⟩ + ∣↓↑⟩)/√2
- **B.** ∣↑↑⟩
- **C.** (∣↑↓⟩ − ∣↓↑⟩)/√2
- **D.** ∣↓↓⟩

**Answer: C.** The antisymmetric m = 0 combination has total spin zero.

#### Question U2-39

For the spin singlet, S₁ · S₂ equals what?

- **A.** +ħ²/4
- **B.** 0
- **C.** ħ²
- **D.** −3ħ²/4

**Answer: D.** Use half the difference between total and individual squared-spin eigenvalues.

#### Question U2-40

What are Clebsch–Gordan coefficients?

- **A.** Basis-change amplitudes
- **B.** Classical angles only
- **C.** Probabilities before squaring
- **D.** Energy shifts for every atom

**Answer: A.** They expand coupled angular states in the uncoupled product basis.

#### Question U2-41

If one entire ket is multiplied by −1, what changes physically?

- **A.** All probabilities reverse sign
- **B.** No predictions
- **C.** Its energy changes sign
- **D.** Its norm doubles

**Answer: B.** An overall phase is conventional, unlike a changed relative sign between components.

#### Question U2-42

For rank-k tensor component q, which projection condition can permit a matrix element?

- **A.** m′ = m − k always
- **B.** m′ = −m always
- **C.** m′ = m + q
- **D.** q = j + j′ always

**Answer: C.** The J\_z commutator imposes the stated projection change.

#### Question U2-43

Which additional angular condition enters Wigner–Eckart matrix elements?

- **A.** j′ &gt; j + k always
- **B.** j′ = 0 always
- **C.** k = m²
- **D.** abs(j − k) ≤ j′ ≤ j + k

**Answer: D.** The Clebsch–Gordan triangle rule restricts the coupled angular labels.

#### Question U2-44

For one-electron orbital electric-dipole transitions, which rule applies?

- **A.** Δl = ±1
- **B.** Δl = 0 only
- **C.** Δl = ±2 only
- **D.** No parity change

**Answer: A.** A rank-one odd-parity position operator requires opposite parity and the angular triangle rule.

#### Question U2-45

Why can a transition satisfying angular selection rules still have zero amplitude?

- **A.** Selection rules guarantee every rate is nonzero
- **B.** Its remaining radial matrix element may vanish
- **C.** Planck's constant must vanish
- **D.** Its norm must be negative

**Answer: B.** The angular rules are necessary conditions and do not determine the whole physical matrix element.


## भाग 6: Quick Revision and Terminology

### 6.1 Sixty Revision Points

1. A quantum state has many possible representations in chosen bases.
2. The physics inner product is linear in its ket argument.
3. The bra argument carries complex conjugation.
4. A normalised state has inner product with itself equal to one.
5. Hilbert-space completeness concerns convergence within the space.
6. Basis completeness concerns reconstruction from the selected basis vectors.
7. Orthonormal basis inner products equal the Kronecker delta.
8. The sum of a complete discrete basis's projectors is the identity.
9. Expansion coefficient cₙ is the inner product of basis bra n with the state.
10. Discrete-basis probabilities are squared coefficient magnitudes.
11. A continuum spectrum requires integrals and generalised eigenstates.
12. The Dirac delta is a distribution defined by sifting integrals.
13. The delta has inverse units of its argument.
14. For nonzero real c, δ(cx) = δ(x)/abs(c).
15. The delta derivative transfers a derivative with a minus sign under integration.
16. Products such as δ² are not automatically meaningful ordinary functions.
17. Position kets are delta-normalised, not ordinary unit-norm packets.
18. The stated position-momentum kernel is e^(ipx/ħ)/√(2πħ).
19. An inner product is a complex number; an outer product is an operator.
20. An operator's matrix columns record its action on basis kets.
21. Finite-dimensional observable matrices are Hermitian.
22. The adjoint is the conjugate transpose in an orthonormal finite basis.
23. Self-adjoint observable eigenvalues are real.
24. Eigenvectors of distinct Hermitian eigenvalues are orthogonal.
25. A degenerate measurement outcome projects into an entire eigenspace.
26. An expectation value need not be an allowed individual outcome.
27. Unitary matrices obey U†U = I.
28. A passive basis change transforms both states and operators consistently.
29. With new basis columns U, the state column is c′ = U†c.
30. With that convention, A′ = U†AU.
31. An active unitary operation on a state is distinct from relabelling its basis.
32. Position and momentum wavefunctions are Fourier-related representations.
33. In position space, momentum is −iħ∂/∂x.
34. In momentum space, position is iħ∂/∂p for the stated Fourier convention.
35. The commutator is [A,B] = AB − BA.
36. The canonical position-momentum commutator is iħ times the identity.
37. Commutators obey the product rule and Jacobi identity.
38. Finite-dimensional commuting Hermitian observables admit a common eigenbasis.
39. Uncertainty uses standard deviations of the prepared-state distributions.
40. Cauchy–Schwarz applied to centred-operator states yields uncertainty bounds.
41. The Robertson bound retains the commutator contribution.
42. The stronger Schrödinger bound also retains squared covariance.
43. A zero commutator expectation in one state does not prove universal commutation.
44. The position-momentum product is at least ħ/2.
45. An unchirped Gaussian of position variance σ² has momentum variance ħ²/(4σ²).
46. A Gaussian with arbitrary quadratic phase need not minimise the simple product.
47. A freely evolving packet may spread while its momentum variance stays constant.
48. Total squared angular momentum commutes with every angular component.
49. Different angular components do not generally commute.
50. Angular-momentum magnitude is ħ√[j(j + 1)].
51. Its chosen projection is ħm with m from −j to +j.
52. Angular ladder operators change m by one within a fixed j.
53. The nonnegative ladder norms allow integer or half-integer j.
54. Scalar spatial orbital angular momentum uses integer l.
55. Spin one-half has squared magnitude 3ħ²/4 and two projection outcomes.
56. Adding j₁ and j₂ allows totals from their absolute difference to their sum.
57. Clebsch–Gordan coefficients are coupled-to-uncoupled basis amplitudes.
58. Two spins one-half form a triplet and a singlet.
59. The Wigner–Eckart theorem factors angular CG geometry from a reduced matrix element.
60. Electric-dipole selection rules require rank-one angular conditions and opposite parity.

### 6.2 Hindi-Supported Glossary

| English term | Hindi aid | Plain-English meaning |
|---|---|---|
| State vector | अवस्था सदिश | Abstract description of a pure quantum preparation |
| Inner product | आंतरिक गुणनफल | Amplitude formed by pairing two vectors |
| Basis | आधार | Independent building blocks for state expansion |
| Completeness | पूर्णता | Ability of the stated basis to reconstruct states |
| Operator | संकारक | Linear action on state vectors |
| Adjoint | सहसंयुग्मी | Conjugate-transpose or its operator generalisation |
| Eigenvalue | अभिलाक्षणिक मान | Scalar obtained when an operator preserves a vector's direction |
| Unitary | यूनिटरी | Norm-preserving linear transformation with a unitary inverse |
| Commutator | क्रमविनिमेयक | Difference AB − BA |
| Standard deviation | मानक विचलन | Square root of the outcome variance |
| Uncertainty | अनिश्चितता | Spread of measurement outcomes in a state |
| Gaussian | गाउसियन | Exponential of a negative quadratic envelope |
| Angular momentum | कोणीय संवेग | Generator and observable associated with rotations |
| Spin | प्रचक्रण, स्पिन | Intrinsic angular momentum |
| Coupled basis | युग्मित आधार | Basis labelled by total angular momentum |
| Selection rule | चयन नियम | Symmetry condition for a matrix element to be nonzero |

### 6.3 Formula Sheet with Conditions

| Result | Conditions or interpretation |
|---|---|
| Σ∣n⟩⟨n∣ = I | Complete discrete orthonormal basis |
| δ(cx) = δ(x)/abs(c) | Nonzero real c |
| A\_nm = ⟨n∣Â∣m⟩ | Ordered orthonormal basis |
| c′ = U†c; A′ = U†AU | Columns of U are the new basis in old coordinates |
| [x̂,p̂] = iħI | Suitable common domain |
| ΔAΔB ≥ ½abs(⟨[A,B]⟩) | Finite required moments and valid operator products |
| Δx = σ; Δp = ħ/(2σ) | Unchirped normalised minimum-product Gaussian |
| J² = ħ²j(j + 1); J\_z = ħm | Simultaneous angular-momentum eigenstate |
| J\_± coefficient = ħ√[j(j + 1) − m(m ± 1)] | Ladder action within fixed j |
| j = abs(j₁ − j₂),…,j₁ + j₂ | Angular-momentum addition |
| Δl = ±1; Δm = 0,±1 | One-electron orbital electric-dipole selection rules |

---

# Unit 3: Hydrogen and Perturbation Theory


## भाग 1: Start Here

The orbital names s,p,d,f are familiar from chemistry. We now derive their angular-momentum meaning and the hydrogen energy pattern. Then we add small changes to a solved Hamiltonian and calculate how its energies and states respond.

Keep three distinctions in view: a three-dimensional probability density is different from a radial probability distribution; a degenerate energy needs a subspace treatment; and an individual level shift is different from the separation of two shifted levels.

## भाग 2: Build the Ideas

### 3.1 Spherical Coordinates and Central Potentials

**In simple words:** When the potential depends only on distance from a centre, use coordinates adapted to that symmetry. They separate distance from direction.

The spherical coordinates are radius r ≥ 0, polar angle θ measured from +z, and azimuth φ around z. Their Cartesian relations are x = r sin θ cos φ, y = r sin θ sin φ and z = r cos θ. The volume element is d³r = r²sin θ dr dθ dφ. The factor r² is essential for normalisation.

For two interacting particles, remove centre-of-mass translation and use the relative coordinate with reduced mass μ = m₁m₂/(m₁ + m₂). The relative Schrödinger equation is:

> [−ħ²∇²/(2μ) + V(r)]ψ = Eψ.

The spherical Laplacian separates into radial and angular pieces:

> ∇² = (1/r²)∂ᵣ(r²∂ᵣ) − L̂²/(ħ²r²),
> L̂² = −ħ²[(1/sin θ)∂θ(sin θ ∂θ) + (1/sin²θ)∂φ²].

The subscripts indicate the differentiated coordinate. This form connects the differential equation to the angular-momentum operator already studied in Unit 2.

For a central scalar potential, [Ĥ,L̂²] = [Ĥ,L̂\_z] = 0. Therefore choose simultaneous energy, total orbital-angular-momentum and z-projection eigenfunctions. Spin is an additional degree of freedom when included; the scalar spatial equation alone does not generate spin.

**Try it.** For two equal masses m, what mass enters the relative Schrödinger equation? **Answer:** μ = m/2, while centre-of-mass translation uses total mass 2m.

### 3.2 Angular Separation and Spherical Harmonics

**In simple words:** The angular functions tell us how the state depends on direction. The radial function determines how it depends on distance.

Try ψ(r,θ,φ) = R(r)Y(θ,φ), and choose L̂²Y = ħ²l(l + 1)Y. Substitution gives:

> (1/r²)d/dr(r²dR/dr) + [2μ(E − V)/ħ² − l(l + 1)/r²]R = 0.

Separating Y = Θ(θ)Φ(φ), the L\_z equation gives −iħdΦ/dφ = ħmΦ, so Φ is proportional to e^(imφ). Requiring the spatial wavefunction to be single-valued under φ → φ + 2π gives integer m. The regular polar equation is the associated Legendre equation. Its regular solutions require l = 0,1,2,… and |m| ≤ l. The normalised combined functions are the spherical harmonics Y\_l^m.

Their angular normalisation is ∫|Y\_l^m|²dΩ = 1, with dΩ = sin θ dθ dφ. In a standard phase convention:

| Angular function | Expression |
|---|---|
| Y₀⁰ | 1/√(4π) |
| Y₁⁰ | √(3/(4π))cos θ |
| Y₁^±1 | ∓√(3/(8π))sin θ e^(±iφ) |
| Y₂⁰ | √(5/(16π))(3cos²θ − 1) |

The letters s,p,d,f correspond to l = 0,1,2,3. Real chemical orbitals such as p\_x and p\_y are linear combinations of the complex m = ±1 angular functions. Choosing such combinations changes the basis within the degenerate p subspace, not the number of states.

Set u(r) = rR(r). Direct differentiation removes the first radial derivative and yields:

> −ħ²u″/(2μ) + [V(r) + ħ²l(l + 1)/(2μr²)]u = Eu.

For the regular Coulomb bound-state problem, u(0) = 0 and u decays at infinity. Radial normalisation is ∫₀^∞|u|²dr = ∫₀^∞r²|R|²dr = 1. The positive l(l + 1) term is a centrifugal barrier. It vanishes for l = 0, but that fact alone does not determine where an arbitrary potential's wavefunction is largest.

### 3.3 Deriving the Hydrogen Energy Levels

**In simple words:** The Coulomb radial equation admits a decaying solution at infinity and a regular solution at the origin. Requiring one solution to satisfy both conditions restricts the energy.

Let κ\_C = e²/(4πε₀) &gt; 0 and V = −κ\_C/r. We use κ\_C for the Coulomb strength to distinguish it from a decay wave number. For a bound state E &lt; 0 define k\_E = √(−2μE)/ħ, ρ = 2k\_Er and λ = μκ\_C/(ħ²k\_E). The radial equation becomes:

> d²u/dρ² + [−¼ + λ/ρ − l(l + 1)/ρ²]u = 0.

At large ρ, select the decaying exponential e^(−ρ/2). Near zero, the regular branch behaves as ρ^(l + 1). Write u = ρ^(l + 1)e^(−ρ/2)F(ρ). Substituting and collecting derivatives gives:

> ρF″ + (2l + 2 − ρ)F′ + (λ − l − 1)F = 0.

Expand F = Σ\_sa\_sρˢ. Matching powers gives:

> a\_(s+1) = [s + l + 1 − λ]a\_s/[(s + 1)(s + 2l + 2)].

The regular solution must terminate in a polynomial for the required decaying bound state. If the highest power is n\_r ≥ 0, termination requires λ = n\_r + l + 1. Define the principal quantum number n = n\_r + l + 1. Then k\_E = μκ\_C/(ħ²n), and:

> Eₙ = −μκ\_C²/(2ħ²n²), n = 1,2,3,…

The polynomial is an associated Laguerre polynomial. This derivation explains why ρ can later be written 2r/(na), where a = ħ²/(μκ\_C): n is obtained from termination, rather than assumed before quantising the energy.

With μ approximated by m\_e, a is the Bohr radius a₀ ≈ 0.529 Å and Eₙ ≈ −13.6 eV/n². Using finite proton mass changes a and the energy scale slightly. For a hydrogen-like nucleus of charge +Ze, use Zκ\_C; the energy magnitude scales as μZ² and the length scale as 1/(μZ).

The quantum numbers satisfy l = 0,…,n − 1 and m = −l,…,l. The radial-node count is n − l − 1. These restrictions arise from the differential equation and boundary conditions, not from assigning a classical electron orbit.

### 3.4 Wavefunctions, Radial Probability and Degeneracy

**In simple words:** The density at one spatial point and the probability of finding a particle within a thin spherical shell are different quantities. The shell includes more volume as r increases.

The spatial hydrogen functions are ψ\_nlm = R\_nlY\_l^m. With a = ħ²/(μκ\_C), the first radial functions are:

| State | R\_nl(r) |
|---|---|
| 1s | 2a^(−3/2)e^(−r/a) |
| 2s | [1/(2√2)]a^(−3/2)(2 − r/a)e^(−r/(2a)) |
| 2p | [1/(2√6)]a^(−3/2)(r/a)e^(−r/(2a)) |

For normalised Y, radial probability in dr is P(r)dr = r²|R(r)|²dr. The 1s density per unit volume is |ψ\_100|² = e^(−2r/a)/(πa³), maximal at the origin. Its radial distribution is P\_1s(r) = 4r²e^(−2r/a)/a³, zero at r = 0 and maximal at r = a. There is no contradiction: the volume of a thin shell tends to zero with r² near the origin.

To find its mean radius, use ∫₀^∞rⁿe^(−βr)dr = n!/β^(n+1). Then ⟨r⟩ = (4/a³)∫r³e^(−2r/a)dr = 3a/2. Similarly ⟨1/r⟩ = 1/a for 1s. More generally ⟨r⟩\_nl = (a/2)[3n² − l(l + 1)] and ⟨1/r⟩\_nl = 1/(n²a).

![The hydrogen 1s radial distribution peaks at a finite radius even though the density per unit volume is greatest at the centre.](images/quantum/hydrogen_radial.png)

For a fixed n, count states by summing 2l + 1 over l = 0,…,n − 1. The result is n² spatial states. Including a free spin-one-half label gives 2n² in the nonrelativistic spin-independent Coulomb model. For n = 3, there are 1 + 3 + 5 = 9 spatial states. Rotational symmetry accounts for m degeneracy; the additional equality across different l is special to the Coulomb model. Perturbations may split some or all of these degeneracies depending on their symmetry.

**Try it.** How many radial nodes does 3p have? **Answer:** n − l − 1 = 3 − 1 − 1 = 1.

### 3.5 Hydrogen Numericals and Reduced-Mass Checks

**In simple words:** Energy differences determine emitted or absorbed photon energies. Length and energy scales change when the reduced mass changes.

**Ionisation from n = 2.** In the −13.6/n² eV approximation, E₂ = −3.4 eV. The continuum threshold is zero, so the minimum energy required is 3.4 eV, not −3.4 eV.

**The n = 3 to 2 photon.** The emitted energy is E₃ − E₂ = 13.6(1/4 − 1/9) eV ≈ 1.889 eV. Thus λ = hc/ΔE ≈ 1240/1.889 = 656.5 nm. The rounded nonrelativistic inputs give an approximate Balmer Hα wavelength, not a precision spectroscopic prediction.

**Muonic hydrogen.** Replace the electron by a particle of mass 207m\_e while retaining a proton of mass 1836m\_e. The reduced mass is μ = (207 × 1836)/(207 + 1836)m\_e ≈ 186.0m\_e. The length scale relative to the m\_e-based a₀ is a\_muonic ≈ a₀/186.0 ≈ 0.002844 Å = 0.2844 pm. Approximating μ by 207m\_e is less accurate here because the proton is only about nine times heavier than the muon. Reduced mass, not simply the replacement particle's mass, controls the scale.

**Try it.** A hydrogen-like ion has Z = 2 and the same reduced mass approximation. What is its n = 1 energy? **Answer:** Approximately −4 × 13.6 = −54.4 eV.

### 3.6 Non-Degenerate Perturbation Theory

**In simple words:** If a small extra interaction is added to a solved problem, expand the energy and state in powers of its strength. Keep enough terms for the required accuracy.

Write H = H₀ + λW, where λ is a dimensionless bookkeeping parameter. Let H₀∣n₀⟩ = E\_n⁽⁰⁾∣n₀⟩ with a non-degenerate level. Expand E\_n = E\_n⁽⁰⁾ + λE\_n⁽¹⁾ + λ²E\_n⁽²⁾ + … and ∣n⟩ = ∣n₀⟩ + λ∣n₁⟩ + λ²∣n₂⟩ + …. These superscripts denote coefficients; the powers of λ are outside them.

At first order, substitute into H∣n⟩ = E\_n∣n⟩ and collect λ terms:

> (H₀ − E\_n⁽⁰⁾)∣n₁⟩ = (E\_n⁽¹⁾ − W)∣n₀⟩.

Project with ⟨n₀∣. The left side is zero, giving E\_n⁽¹⁾ = ⟨n₀∣W∣n₀⟩. Project instead with another unperturbed eigenbra ⟨m₀∣, m ≠ n. Then:

> ⟨m₀∣n₁⟩ = W\_mn/(E\_n⁽⁰⁾ − E\_m⁽⁰⁾),
> ∣n₁⟩ = Σ\_(m≠n)∣m₀⟩W\_mn/(E\_n⁽⁰⁾ − E\_m⁽⁰⁾).

We chose intermediate normalisation ⟨n₀∣n₁⟩ = 0. A separately unit-normalised approximate state needs the corresponding higher-order norm correction. The actual first-order state change is λ∣n₁⟩.

The mixing estimate is |λW\_mn| ≪ |E\_n⁽⁰⁾ − E\_m⁽⁰⁾| for relevant states. A small absolute energy scale is not sufficient if two levels are nearly degenerate. Matrix elements and gaps together determine applicability. Spectral sums may also contain continuum contributions.

### 3.7 First-Order Examples and Symmetry

**In simple words:** The first-order shift samples the perturbation through the unperturbed state's probability distribution. A symmetry can make that average zero.

**Constant shift.** In an infinite box, W = V\_c throughout the accessible region gives E\_n⁽¹⁾ = V\_c∫|φₙ|²dx = V\_c. This is actually exact: all energies shift equally and eigenfunctions are unchanged. An overall reference shift does not change energy differences.

**A central delta.** In 0 &lt; x &lt; L, let W = gδ(x − L/2). Since δ has inverse-length units, g has units energy times length. The shift is E\_n⁽¹⁾ = g|φₙ(L/2)|² = (2g/L)sin²(nπ/2). Odd n have shift 2g/L; even n have zero shift. An even-n box state has a node at the centre. It is odd about the box centre, even though the integer n itself is even; do not confuse these uses of the word “odd”.

**A quadratic oscillator change.** With W = αx² and λ = 1, use ⟨x²⟩\_n = (n + ½)ħ/(mω). Thus ΔE\_n at first order is α(n + ½)ħ/(mω). The exact frequency becomes Ω = √(ω² + 2α/m), provided the modified potential remains confining. Expanding Ω ≈ ω + α/(mω) reproduces the perturbative result and supplies a useful check.

**Try it.** Let W = Fx in a centred oscillator eigenstate. **Answer:** Its first-order energy shift vanishes because x is odd and the probability density is even. The state may still acquire mixing and a second-order energy shift.

### 3.8 Second-Order Energy and an Exactly Unchanged State

**In simple words:** Off-diagonal couplings change a state's energy through mixing with other levels. If every such coupling vanishes, there is no second-order shift either.

Collect the λ² terms and project with ⟨n₀∣, retaining the intermediate-normalisation choice. The result is E\_n⁽²⁾ = ⟨n₀∣W∣n₁⟩. Insert the first-order state correction:

> E\_n⁽²⁾ = Σ\_(m≠n)|W\_mn|²/(E\_n⁽⁰⁾ − E\_m⁽⁰⁾).

The actual second-order contribution is λ²E\_n⁽²⁾. For a non-degenerate ground state all denominators are negative, so this coefficient is nonpositive; it is strictly negative only if a coupling is nonzero. An excited state can have either sign. A small gap does not dominate if the corresponding matrix element vanishes.

**Worked oscillator example.** For W = Fx, x = √(ħ/(2mω))(a + a†) couples n only to n ± 1. The upper-state contribution is −F²(n + 1)/(2mω²), and the lower-state contribution is +F²n/(2mω²). Their sum is −F²/(2mω²), independent of n. Completing the square gives V = ½mω²[x + F/(mω²)]² − F²/(2mω²), confirming the exact energy shift.

**Correcting the delta example.** For a state that vanishes at the delta's location, W\_mn = gφ\_m\*(x₀)φ\_n(x₀) = 0 for every m. The entire second-order sum is zero. Indeed, that unperturbed eigenfunction still obeys the delta jump condition φ′(x₀+) − φ′(x₀−) = (2μg/ħ²)φ(x₀) = 0, so it is unchanged exactly in this ideal model. There is no mixing with a “nearest even state” when the matrix element is identically zero.

### 3.9 Degenerate Perturbation Theory

**In simple words:** Within a degenerate energy subspace, the original basis is not unique. First choose the combinations selected by the perturbation; then calculate their shifts.

Let ∣i⟩, i = 1,…,g span an unperturbed eigenspace with energy E₀. A candidate zeroth-order combination is ∣χ⟩ = Σᵢcᵢ∣i⟩. Project the first-order equation into that subspace:

> ΣⱼW\_ij cⱼ = w cᵢ; W\_ij = ⟨i∣W∣j⟩.

The eigenvalues w are first-order energy coefficients and the normalised eigenvectors give the appropriate zeroth-order combinations. This avoids division by zero inside the degenerate space. Mixing with states outside the space uses their nonzero unperturbed gaps; residual degeneracy requires additional analysis, not an automatic return to a formula with zero denominators.

**Worked two-state example.** Suppose the perturbation matrix has rows (0,v) and (v,0), with real v. Its characteristic equation is w² − v² = 0. The shifts are ±v and the states are (∣1⟩ ± ∣2⟩)/√2. Each original diagonal average was zero, but the levels split at first order. Off-diagonal information is essential.

The same method applies to larger subspaces. Symmetry can divide a large matrix into smaller blocks. Before calculating every integral, use parity and angular selection rules to locate its zero entries.

### 3.10 The Orbital and Spin Zeeman Effects

**In simple words:** A magnetic field distinguishes states with different magnetic-moment projections. State the coupling regime before choosing angular-momentum labels.

For an electron with charge −e, orbital magnetic moment is μ\_L = −eL/(2m\_e). In a uniform field B along z, the linear interaction −μ\_L · B is:

> W\_orbital = μ\_B B L\_z/ħ; μ\_B = eħ/(2m\_e).

In the spinless orbital model, the basis ∣nlm⟩ already diagonalises this perturbation, and ΔE = μ\_BBm. Adjacent m sublevels are separated by μ\_BB. The model neglects the quadratic diamagnetic term and any spin-related structure. The normal Zeeman effect is physically realised for suitable zero-total-spin atomic terms; applying this orbital calculation to hydrogen while ignoring spin is an instructional approximation.

When both upper and lower terms have the same orbital g = 1, electric-dipole transitions with Δm = 0,±1 produce frequency changes 0,±μ\_BB/h, yielding the normal triplet if the relevant transitions and viewing geometry are available. Energy spacing is μ\_BB; frequency spacing is μ\_BB/h. They are not the same units. Viewed along the field, the π component is absent and the σ components have opposite circular polarisations. Viewed transverse to it, the π component is linearly polarised parallel to the field and the σ components perpendicular.

Including spin gives W = μ\_BB(L\_z + g\_sS\_z)/ħ with g\_s ≈ 2 in the leading model. In the weak-field LS-coupling regime, spin–orbit coupling first forms J = L + S, and:

> ΔE = μ\_BBg\_Jm\_J,
> g\_J = 1 + [J(J + 1) + S(S + 1) − L(L + 1)]/[2J(J + 1)], for J ≠ 0.

For J = 0, the linear shift vanishes rather than using this expression's zero denominator. If the magnetic field dominates spin–orbit coupling, the uncoupled m\_l,m\_s description is appropriate instead; the weak-field Landé formula should not be carried over without checking the regime.

**Worked example.** μ\_B ≈ 5.788 × 10⁻⁵ eV/T. At B = 1 T, an orbital adjacent-level energy spacing is 5.788 × 10⁻⁵ eV. Using h ≈ 4.136 × 10⁻¹⁵ eV·s gives frequency spacing 1.399 × 10¹⁰ Hz. For L = 1,S = ½,J = 3/2, the Landé factor is 4/3.

### 3.11 The Stark Effect: Why Degeneracy Matters

**In simple words:** An electric field couples to position. A definite-parity state's diagonal position average vanishes, but degenerate opposite-parity states can mix and split at first order.

Let the external field be F along +z. With e &gt; 0 and the electron coordinate relative to the nucleus, W = eFz. The sign follows the electron charge and external electrostatic potential. The 1s state has even parity and z is odd, so ⟨1s∣z∣1s⟩ = 0. Its first-order shift vanishes. Second-order coupling to opposite-parity states gives a negative leading shift. In the nonrelativistic Coulomb approximation:

> ΔE\_1s = −½α\_EF²; α\_E = (9/2)4πε₀a³.

α\_E is electric polarisability; its SI definition includes the displayed 4πε₀. Distinguish it from a polarisability “volume” that omits that factor.

In the ideal n = 2 Coulomb subspace, use ∣2s⟩,∣2p,m = 0⟩,∣2p,+1⟩,∣2p,−1⟩. The diagonal elements vanish by parity. Since z has q = 0, only the 2s–2p,m = 0 pair couples within this subspace. With the radial and spherical-harmonic phases used above, the matrix element is ⟨2s∣z∣2p,0⟩ = −3a. Its sign can reverse under a phase change of one basis ket, but the resulting eigenvalues do not.

Let d = 3eaF &gt; 0. The coupled block has rows (0,−d) and (−d,0); the other two entries are zero. Its eigenvalues are −d and +d. Thus the first-order pattern is:

> −3eaF, 0, 0, +3eaF.

The equal-sign combination (∣2s⟩ + ∣2p,0⟩)/√2 has the lower shift with this convention; the opposite-sign combination has the upper shift. Each contains opposite parity and can have a nonzero dipole expectation. This calculation neglects fine structure, Lamb shift and spin effects; the ideal degeneracy must be appropriate relative to the field coupling before using it to model measured hydrogen levels.

### 3.12 Stark Matrix Element and Splitting Numerical

**In simple words:** A matrix element separates into a radial integral and an angular integral. Carrying both through explains the factor 3 in the Stark result.

Since z = r cos θ, the off-diagonal element is:

> ⟨2s∣z∣2p,0⟩ = [∫₀^∞r³R₂₀R₂₁dr][∫Y₀⁰\* cos θ Y₁⁰dΩ].

The angular factor is 1/√3. With s = r/a and the radial functions above, the radial factor is a/(8√3) times ∫₀^∞(2s⁴ − s⁵)e^(−s)ds. Using the factorial integral gives (a/(8√3))(2×4! − 5!) = −3√3a. Their product is −3a.

**Numerical example.** Take a ≈ 5.29 × 10⁻¹¹ m and F = 10⁷ V/m. The magnitude of each outer level's shift is d = 3eaF. In eV, the factor e converts the voltage product directly, so d = 3 × 5.29 × 10⁻¹¹ × 10⁷ eV = 1.587 × 10⁻³ eV. The outermost separation is 2d = 3.174 × 10⁻³ eV. Calling d the full outer separation would miss a factor of two.

**Try it.** If the field is halved in this ideal linear regime, how do the outer separation and the ground-state quadratic shift change? **Answer:** The outer separation halves; the magnitude of the leading ground-state quadratic shift becomes one quarter.

## भाग 3: Put the Ideas Together

### Choosing the Correct Perturbation Method

Start with H₀ and identify its actual unperturbed degeneracies at the accuracy being used. If the target level is isolated, calculate the diagonal average and the allowed off-diagonal couplings. If the first-order average vanishes, inspect the second-order sum rather than assuming it must be nonzero. If a degenerate subspace exists, construct and diagonalise the perturbation in that subspace first.

A useful comparison is the central delta versus the n = 2 Stark effect. In the delta example, a node makes every coupling out of the chosen odd-about-centre state zero. In the Stark example, diagonal parity averages are zero but an off-diagonal opposite-parity coupling is nonzero. Both have a zero original diagonal expectation, yet their behaviour is different because the full operator action is different.

### A Two-Level Exact Check

Let H have rows (E₁,v) and (v,E₂), with real v and E₂ &gt; E₁. Its exact energies are (E₁ + E₂)/2 ± √[((E₂ − E₁)/2)² + v²]. For |v| ≪ E₂ − E₁, the lower level shifts by −v²/(E₂ − E₁) and the upper by +v²/(E₂ − E₁), agreeing with second-order perturbation theory. When E₁ = E₂, the exact shifts are ±|v| and the non-degenerate expansion fails. This small matrix captures why the choice of method matters.

## भाग 4: Check Your Understanding

### 3.13 Common Mistakes and Their Corrections

- Include r² in radial probability integrals.
- The 1s radial distribution is zero at the origin even though the volume density is largest there.
- Use reduced mass when both interacting bodies move.
- State whether a hydrogen degeneracy count includes spin and ignores fine structure.
- Do not claim every perturbation removes every degeneracy.
- In perturbation expansions, keep bookkeeping powers outside the consistently defined coefficients.
- A zero first-order shift does not imply either zero or nonzero second order without inspecting couplings.
- Delta-coupling strength has energy-length units in one dimension.
- Diagonalise within an unperturbed degenerate subspace before using gap denominators.
- Distinguish an energy spacing from its frequency equivalent.
- State the magnetic-field coupling regime before using a Landé factor.
- The magnitude of one Stark shift is half the full separation of the two outer levels.

## भाग 5: Practice Questions with Explanations

#### Question U3-01

The spherical volume element is what?

- **A.** dr dθ dφ
- **B.** r dr dθ dφ
- **C.** r²sin θ dr dθ dφ
- **D.** sin φ dr dθ dφ

**Answer: C.** The geometric Jacobian accounts for shell area and polar-angle spacing.

#### Question U3-02

For a central scalar potential, which spatial observables can be chosen together with energy?

- **A.** All three L components with sharp values universally
- **B.** Only radius and momentum simultaneously sharp
- **C.** Position in every direction exactly
- **D.** L² and L\_z

**Answer: D.** The central Hamiltonian commutes with total orbital angular momentum and a chosen component.

#### Question U3-03

What does u = rR accomplish in the radial equation?

- **A.** It removes the first radial derivative
- **B.** It eliminates the angular barrier for every l
- **C.** It sets energy to zero
- **D.** It removes the boundary at the origin

**Answer: A.** Substitution converts the radial equation to a second-derivative Schrödinger-like form.

#### Question U3-04

With angular functions normalised to one, radial probability density is what?

- **A.** abs(R)² alone
- **B.** r² abs(R)²
- **C.** R alone
- **D.** 4πR for every state

**Answer: B.** Integrating angular variables leaves the radial volume factor r².

#### Question U3-05

Which l corresponds to a p orbital?

- **A.** 0
- **B.** 2
- **C.** 1
- **D.** 3

**Answer: C.** The orbital sequence s,p,d,f corresponds to l = 0,1,2,3.

#### Question U3-06

For l = 1, how many m states exist?

- **A.** One
- **B.** Two
- **C.** Four
- **D.** Three

**Answer: D.** There are 2l + 1 projection states.

#### Question U3-07

Real p\_x and p\_y orbitals are what relative to complex m states?

- **A.** Linear combinations within the p subspace
- **B.** Additional independent states beyond the three p states
- **C.** Classical electron paths
- **D.** States with l = 0

**Answer: A.** A different basis can be chosen within the same degenerate angular subspace.

#### Question U3-08

The quantum centrifugal-barrier term is what?

- **A.** −ħ²l/(2μr)
- **B.** ħ²l(l + 1)/(2μr²)
- **C.** μr²
- **D.** ħl/r

**Answer: B.** It enters the effective radial potential after angular separation.

#### Question U3-09

For l = 0, what can be concluded from the barrier term alone?

- **A.** That every wavefunction peaks at zero radius
- **B.** That the energy is zero
- **C.** That this angular barrier vanishes
- **D.** That no bound state exists

**Answer: C.** The remaining potential and boundary conditions still determine the radial solution.

#### Question U3-10

Hydrogen polynomial termination gives which relation?

- **A.** n = l − n\_r
- **B.** n = m only
- **C.** n = 0 for the ground state
- **D.** n = n\_r + l + 1

**Answer: D.** The terminating associated-Laguerre series fixes the principal quantum number.

#### Question U3-11

Which l values are allowed for n = 3?

- **A.** 0,1,2
- **B.** 0,1,2,3
- **C.** Only 3
- **D.** Only 0

**Answer: A.** The radial termination condition requires l ≤ n − 1.

#### Question U3-12

How many radial nodes has 3p?

- **A.** Zero
- **B.** One
- **C.** Two
- **D.** Three

**Answer: B.** The radial-node count is n − l − 1.

#### Question U3-13

For the ideal hydrogen Coulomb model, energy depends on which spatial principal label?

- **A.** m alone
- **B.** l alone
- **C.** n
- **D.** The orientation angle alone

**Answer: C.** Its additional Coulomb degeneracy makes the energy independent of l and m.

#### Question U3-14

The approximate n = 2 hydrogen energy is what?

- **A.** −13.6 eV
- **B.** +3.4 eV
- **C.** −6.8 eV
- **D.** −3.4 eV

**Answer: D.** Divide the ground-scale energy −13.6 eV by n² = 4.

#### Question U3-15

The ionisation energy from that level is what?

- **A.** +3.4 eV
- **B.** −3.4 eV
- **C.** +13.6 eV
- **D.** Zero

**Answer: A.** The supplied energy must raise the state from −3.4 eV to the zero-energy continuum threshold.

#### Question U3-16

For hydrogen-like Z = 2 with the same mass approximation, ground energy is approximately what?

- **A.** −27.2 eV
- **B.** −54.4 eV
- **C.** −6.8 eV
- **D.** +54.4 eV

**Answer: B.** The Coulomb energy magnitude scales as Z².

#### Question U3-17

Where does the hydrogen 1s density per unit volume peak?

- **A.** At r = a only
- **B.** At r = 2a only
- **C.** At r = 0
- **D.** At infinity

**Answer: C.** The spatial density is proportional to e^(−2r/a).

#### Question U3-18

Where does its radial shell distribution peak?

- **A.** At r = 0
- **B.** At r = 3a/2
- **C.** At infinity
- **D.** At r = a

**Answer: D.** The extra r² factor shifts the maximum of 4r²e^(−2r/a)/a³.

#### Question U3-19

The 1s mean radius is what?

- **A.** 3a/2
- **B.** a/2
- **C.** a
- **D.** 2a

**Answer: A.** The radial integral with an additional factor r gives 3a/2.

#### Question U3-20

How many n = 3 spatial hydrogen states exist without spin in the ideal model?

- **A.** Three
- **B.** Nine
- **C.** Six
- **D.** Eighteen

**Answer: B.** Sum the 1 s, 3 p and 5 d projection states.

#### Question U3-21

Including a free electron spin label, that ideal count is what?

- **A.** Nine
- **B.** Six
- **C.** Eighteen
- **D.** Thirty-six

**Answer: C.** Each spatial state has two independent spin labels in the spin-independent model.

#### Question U3-22

For muon mass 207m\_e and proton mass 1836m\_e, the reduced mass is approximately what?

- **A.** 207m\_e exactly
- **B.** 1836m\_e
- **C.** 2043m\_e
- **D.** 186m\_e

**Answer: D.** Use the product of the two masses divided by their sum.

#### Question U3-23

The muonic length scale compared with the m\_e-based Bohr radius is approximately what?

- **A.** a₀/186
- **B.** 186a₀
- **C.** a₀/1836
- **D.** a₀ unchanged

**Answer: A.** The Coulomb length is inversely proportional to reduced mass.

#### Question U3-24

For H = H₀ + λW, the coefficient E\_n⁽¹⁾ is what?

- **A.** λ²⟨n₀∣W∣n₀⟩
- **B.** ⟨n₀∣W∣n₀⟩
- **C.** The energy gap alone
- **D.** Always zero

**Answer: B.** Project the first-order equation with the unperturbed eigenbra.

#### Question U3-25

What controls non-degenerate perturbative mixing between two levels?

- **A.** The absolute energy origin
- **B.** The number of printed states only
- **C.** The perturbation matrix element relative to their gap
- **D.** The sign of the wavefunction only

**Answer: C.** The dimensionless mixing estimate is abs(λW\_mn)/abs(E\_n⁽⁰⁾ − E\_m⁽⁰⁾).

#### Question U3-26

Adding a constant V\_c over the whole accessible box does what?

- **A.** Splits every degeneracy necessarily
- **B.** Changes all wavefunctions to zero
- **C.** Changes only the ground state
- **D.** Shifts every energy by V\_c without changing eigenfunctions

**Answer: D.** A constant times identity changes the reference energy exactly.

#### Question U3-27

For W = gδ(x − L/2) in a box, what units must g have?

- **A.** Energy times length
- **B.** Energy only
- **C.** Inverse length only
- **D.** Momentum only

**Answer: A.** The delta has inverse-length units, so its coefficient supplies the missing length.

#### Question U3-28

Which infinite-box integer-n states have zero central-delta first-order shift?

- **A.** Odd n
- **B.** Even n
- **C.** Every n
- **D.** No n

**Answer: B.** Even-n sine functions vanish at the centre of the box.

#### Question U3-29

For such a nodal state, the central delta's off-diagonal matrix elements are what?

- **A.** Nonzero only to the nearest state
- **B.** Infinite
- **C.** All zero
- **D.** Equal to g for every state

**Answer: C.** Each matrix element contains the original state's zero value at the delta location.

#### Question U3-30

What is the second-order shift of that exactly nodal state in this ideal delta model?

- **A.** Necessarily positive
- **B.** Necessarily negative
- **C.** Infinite
- **D.** Zero

**Answer: D.** Every numerator in the perturbative sum vanishes, and the exact boundary jump is unchanged.

#### Question U3-31

For W = αx² in an oscillator, the first-order shift is what?

- **A.** α(n + ½)ħ/(mω)
- **B.** αmω/ħ
- **C.** α(n + 1)²
- **D.** Zero for every n

**Answer: A.** The correction is α times the known x² expectation value.

#### Question U3-32

For W = Fx in a centred oscillator number state, the first-order shift is what?

- **A.** F²/(2mω²)
- **B.** Zero
- **C.** Fn
- **D.** Fħω

**Answer: B.** The diagonal average of the odd position operator vanishes by parity.

#### Question U3-33

For that linear oscillator perturbation, the exact energy shift is what?

- **A.** +F²/(2mω²)
- **B.** Zero to every order
- **C.** −F²/(2mω²)
- **D.** −F

**Answer: C.** Completing the potential square shifts the equilibrium and subtracts the stated constant energy.

#### Question U3-34

For a non-degenerate ground state, the second-order energy coefficient has which sign?

- **A.** Strictly positive always
- **B.** Either sign without conditions
- **C.** Always exactly zero
- **D.** Nonpositive

**Answer: D.** All denominators are negative, but the result can be zero if every coupling vanishes.

#### Question U3-35

If two unperturbed levels are degenerate, the first step is what?

- **A.** Diagonalise W within that subspace
- **B.** Divide by their zero gap
- **C.** Choose only the original diagonal averages
- **D.** Discard one state

**Answer: A.** The perturbation selects the proper zeroth-order linear combinations.

#### Question U3-36

A degenerate two-state W with rows (0,v) and (v,0) has which shifts?

- **A.** Both zero
- **B.** +v and −v
- **C.** Both +v
- **D.** v² only

**Answer: B.** Its characteristic equation is w² − v² = 0.

#### Question U3-37

What is the electron orbital magnetic moment's relation to L?

- **A.** +eL/(2m\_e)
- **B.** −eL/m\_e²
- **C.** −eL/(2m\_e)
- **D.** It is always zero

**Answer: C.** The electron's negative charge sets the magnetic-moment sign.

#### Question U3-38

In the spinless orbital Zeeman model, the level shift is what?

- **A.** −μ\_BB for every m
- **B.** μ\_BB²m
- **C.** μ\_BB/m
- **D.** μ\_BBm

**Answer: D.** The interaction is −μ\_L · B = μ\_BB L\_z/ħ.

#### Question U3-39

At B = 1 T, the adjacent orbital Zeeman energy spacing is approximately what?

- **A.** 5.788 × 10⁻⁵ eV
- **B.** 1 eV
- **C.** 13.6 eV
- **D.** 5.788 × 10⁵ eV

**Answer: A.** It equals μ\_BB with the Bohr magneton in eV/T.

#### Question U3-40

To convert that energy spacing into frequency spacing, divide by what?

- **A.** ħ²
- **B.** h
- **C.** m\_e
- **D.** c²

**Answer: B.** Photon energy differences obey ΔE = hΔν.

#### Question U3-41

The usual Landé formula applies in which stated regime?

- **A.** Every field strength without qualification
- **B.** Only when spin is absent
- **C.** Weak magnetic field relative to the relevant LS coupling
- **D.** Only when J = 0 in its denominator

**Answer: C.** The good coupled labels must remain appropriate before using g\_Jm\_J.

#### Question U3-42

Why does the 1s linear Stark shift vanish?

- **A.** The electron has no charge
- **B.** Every electric field is zero
- **C.** The state has no probability density
- **D.** The diagonal average of odd z in an even-parity state is zero

**Answer: D.** Parity makes the first-order integral vanish.

#### Question U3-43

In the ideal n = 2 Coulomb Stark problem, which pair mixes within the subspace for a z field?

- **A.** 2s and 2p with m = 0
- **B.** 2p,+1 and 2p,−1 only
- **C.** 1s and 3d only within n = 2
- **D.** All four states with equal matrix elements

**Answer: A.** Parity and the q = 0 projection rule isolate the 2s–2p,0 block.

#### Question U3-44

If d = 3eaF, the two outer Stark levels have what full separation?

- **A.** d
- **B.** 2d
- **C.** d/2
- **D.** Zero

**Answer: B.** Their shifts are +d and −d relative to the unperturbed energy.

#### Question U3-45

At F = 10⁷ V/m and a = 5.29 × 10⁻¹¹ m, that full outer separation is approximately what?

- **A.** 1.587 × 10⁻³ eV
- **B.** 3.174 eV
- **C.** 3.174 × 10⁻³ eV
- **D.** 1.587 × 10⁻⁶ eV

**Answer: C.** Each outer shift has magnitude 3aF eV, so the separation is twice that value.


## भाग 6: Quick Revision and Terminology

### 6.1 Sixty Revision Points

1. Spherical coordinates separate radial distance from direction.
2. The three-dimensional spherical volume element contains r²sin θ.
3. Two-body relative quantum motion uses reduced mass.
4. A central scalar Hamiltonian commutes with L² and a chosen L component.
5. Spherical harmonics are simultaneous orbital-angular-momentum eigenfunctions.
6. Their azimuthal dependence is proportional to e^(imφ).
7. Single-valued spatial angular functions have integer m.
8. Regular polar solutions require integer l ≥ 0 and abs(m) ≤ l.
9. The orbital letters s,p,d,f correspond to l = 0,1,2,3.
10. Real chemical orbitals may be linear combinations of complex m eigenfunctions.
11. The substitution u = rR removes the first radial derivative.
12. The radial effective potential contains ħ²l(l + 1)/(2μr²).
13. The regular Coulomb radial function u vanishes at the origin.
14. Radial bound-state normalisation is ∫abs(u)²dr = 1.
15. For a normalised angular function, shell density is r²abs(R)².
16. Hydrogen bound-state energy is negative relative to the continuum threshold.
17. The Coulomb radial solution combines regular power, decaying exponential and a polynomial.
18. Series termination gives n = n\_r + l + 1.
19. Hydrogen radial functions involve associated Laguerre polynomials.
20. The allowed orbital label satisfies l ≤ n − 1.
21. The radial-node count is n − l − 1.
22. The ideal Coulomb energy is proportional to −μ/n².
23. For hydrogen-like charge Z, the energy magnitude scales as Z².
24. The Coulomb length scale is inversely proportional to μZ.
25. The approximate hydrogen energy is −13.6 eV/n² using the electron-mass scale.
26. The ionisation threshold is E = 0 in the chosen reference.
27. Emission photon energy is the initial level energy minus the final energy.
28. The 1s volume density is largest at the origin.
29. The 1s radial shell distribution instead peaks at r = a.
30. The 1s mean radius is 3a/2.
31. The ideal n shell has n² spatial states.
32. Including a free spin-one-half label doubles that ideal count.
33. Rotational symmetry explains m degeneracy, while Coulomb symmetry also permits l degeneracy.
34. Different perturbations may preserve different parts of a degeneracy.
35. Muonic hydrogen requires the finite-proton reduced mass rather than simply the muon mass.
36. Write perturbation coefficients consistently with their bookkeeping powers outside them.
37. The first-order energy coefficient is the diagonal perturbation expectation.
38. The first-order state correction sums off-diagonal couplings divided by unperturbed gaps.
39. Intermediate normalisation makes the first-order correction orthogonal to the starting ket.
40. Small matrix elements relative to gaps control non-degenerate perturbative mixing.
41. A constant added over the whole accessible region shifts all energies equally.
42. A one-dimensional delta strength has energy-length units.
43. A node at a central delta makes every coupling out of that state vanish.
44. The exactly nodal state has no first- or second-order central-delta energy shift.
45. Second-order energy uses the sum of squared coupling magnitudes over signed gaps.
46. A non-degenerate ground state's second-order coefficient is nonpositive.
47. An excited state's second-order coefficient can have either sign.
48. A vanishing diagonal average does not by itself determine higher-order corrections.
49. Adding Fx to a centred harmonic oscillator shifts all energies by −F²/(2mω²).
50. Degenerate perturbation theory begins by diagonalising the perturbation within the subspace.
51. Off-diagonal coupling can split degenerate levels even when all original diagonal averages vanish.
52. The electron orbital magnetic moment is opposite to orbital angular momentum.
53. The linear orbital Zeeman shift is μ\_BBm in the spinless model.
54. Convert a Zeeman energy spacing to ordinary frequency by dividing by h.
55. The weak-field LS-coupling Landé formula requires the corresponding angular-momentum regime.
56. For a non-degenerate parity eigenstate, the diagonal electric-dipole average vanishes.
57. The ideal 1s Stark shift begins quadratically and is negative at leading order.
58. In the ideal n = 2 Stark subspace, 2s mixes with 2p,m = 0.
59. Its first-order shifts are −3eaF,0,0,+3eaF.
60. The full separation between the two outer Stark levels is 6eaF.

### 6.2 Hindi-Supported Glossary

| English term | Hindi aid | Plain-English meaning |
|---|---|---|
| Central potential | केंद्रीय विभव | Potential depending only on radial distance |
| Spherical harmonic | गोलीय हार्मोनिक | Angular-momentum eigenfunction on the sphere |
| Radial function | त्रिज्यीय फलन | Distance-dependent part of the separated wavefunction |
| Reduced mass | अपचयित द्रव्यमान | Mass governing relative two-body motion |
| Degeneracy | समऊर्जता | More than one independent state with the same energy |
| Parity | समता | Behaviour under spatial inversion |
| Radial node | त्रिज्यीय नोड | Nonzero radius at which the radial function vanishes |
| Perturbation | विक्षोभ | Additional interaction treated as a controlled small change |
| Matrix element | आव्यूह अवयव | Amplitude obtained between a bra, operator and ket |
| Energy correction | ऊर्जा संशोधन | Term added to the solved model's energy |
| Mixing | अवस्थाओं का मिश्रण | Addition of components from other unperturbed states |
| Polarisability | ध्रुवणीयता | Response coefficient relating induced dipole to field |
| Stark effect | स्टार्क प्रभाव | Electric-field-induced level shifts or splitting |
| Zeeman effect | ज़ीमान प्रभाव | Magnetic-field-induced level shifts or splitting |
| Ionisation | आयनीकरण | Removal from a bound state to the continuum |

### 6.3 Formula Sheet with Conditions

| Result | Conditions or interpretation |
|---|---|
| d³r = r²sin θ dr dθ dφ | Spherical coordinates |
| ψ = R\_nlY\_l^m; u = rR | Separated central-potential states |
| P(r) = r²abs(R)² | Angular factor normalised to one |
| Eₙ = −μκ\_C²/(2ħ²n²) | Nonrelativistic hydrogen relative Coulomb model |
| n\_r = n − l − 1 | Hydrogen radial-node count |
| Spatial degeneracy n²; with spin 2n² | Ideal Coulomb model without fine-structure splitting |
| E\_n⁽¹⁾ = W\_nn | Coefficient of λ in H₀ + λW |
| E\_n⁽²⁾ = Σ\_(m≠n)abs(W\_mn)²/(E\_n⁽⁰⁾ − E\_m⁽⁰⁾) | Non-degenerate level and valid perturbative gaps |
| W\_ij cⱼ summed over j = w cᵢ | First-order diagonalisation inside a degenerate subspace |
| ΔE\_orbital = μ\_BBm | Linear spinless orbital Zeeman model |
| ΔE = μ\_BBg\_Jm\_J | Weak-field LS-coupling Zeeman regime |
| n = 2 Stark shifts: −3eaF,0,0,+3eaF | Ideal degenerate Coulomb subspace |

---


# Appendix 1: A Practical Study Route

## Learning the Course After a Long Gap

Begin with the complex-number and probability refreshers. Work on paper: square a complex amplitude, normalise a simple function and differentiate a plane wave. These small operations recur throughout the book. If a later derivation becomes difficult, identify the missing operation rather than trying to memorise the entire page.

For Unit 1, solve a box completely and use its states to practise probabilities, expectation values and time evolution. Then compare a bound-state tail, a semi-infinite step and a finite barrier. Their similar exponentials have different boundary conditions and currents. Solve the oscillator by both methods and check that their energies and ground-state functions agree.

For Unit 2, use two-component columns before abstract notation. Compute a bra, inner product, outer product and expectation value explicitly. Transform a spin state between z and x bases. Derive the Gaussian uncertainty widths once. For angular momentum, check a ladder coefficient and reconstruct the two-spin singlet and triplet by normalisation and lowering.

For Unit 3, draw a sphere and distinguish the radial distribution from volume density. Follow the hydrogen series until the termination condition appears. In perturbation problems, identify degeneracy before choosing a formula. Use parity to eliminate integrals, but examine off-diagonal couplings before concluding that an effect vanishes.

## Three Revision Days

This is a revision route for material already studied, not a substitute for first-time learning.

| Day | Main work | Independent check |
|---|---|---|
| 1 | Schrödinger equations, probabilities, current, wells, barrier and oscillator | Solve one box and step problem; reconstruct the continuity equation; compare oscillator methods |
| 2 | Representations, commutators, uncertainty, spin, addition and selection rules | Transform a two-state column; compute two commutators; derive Gaussian widths; write singlet/triplet states |
| 3 | Central separation, hydrogen and perturbations | Derive radial quantisation; check one radial probability; solve a two-state degenerate matrix and distinguish Stark shift from splitting |

Use the practice explanations to correct mistakes, not just to record a score. Consult current university notices and authenticated papers for the examination format. No selection of topics here guarantees a particular paper or result.


# Appendix 2: Extended Model Questions and Solution Routes

These original questions guide written practice. The indicated sections contain the complete teaching steps. They are not labelled as verified previous-year questions.

## Unit 1

**1. Derive the time-independent equation and explain stationarity.** Assume a time-independent scalar potential, substitute a product state, separate the constant E and solve the time factor. Explain why density is unchanged and why current need not vanish. See sections 1.4–1.5.

**2. Derive probability continuity.** Use the TDSE and its conjugate for real V, multiply by the opposite factors and subtract. Expand the derivative in the current expression to show cancellation. Integrate over an interval to interpret the boundary currents. See section 1.7.

**3. Establish Ehrenfest's equations.** Differentiate the expectation value with its explicit operator dependence, use the TDSE and valid boundary/domain conditions, then evaluate the x and p commutators. Discuss why the average nonlinear force differs from the force at the average position. See section 1.8.

**4. Solve the infinite and finite wells.** For the infinite well impose both zero boundaries and normalise the surviving sine. For a symmetric finite well use parity, discard growing exterior tails and match derivatives to obtain the two transcendental equations. Explain the outside density and its current. See sections 1.9–1.10.

**5. Derive step and barrier transmission.** Write the correct regional solutions and matching equations. Use current ratios for the step and eliminate the barrier's internal coefficients to obtain the amplitude denominator. Distinguish exact and thick-barrier expressions. See sections 1.11–1.12.

**6. Solve the oscillator by both methods.** In the differential method remove the Gaussian asymptotic factor, derive the recursion and impose termination. In the operator method derive the commutator, nonnegative number spectrum and ground-state Gaussian. Check the first two moments. See sections 1.13–1.14.

## Unit 2

**7. Explain completeness in discrete and continuous bases.** Distinguish the Hilbert-space definition from a basis closure relation. Expand a state and derive its coefficients. Introduce position kets, the delta kernel and the momentum Fourier transform. See sections 2.1–2.2 and 2.4.

**8. Calculate a two-state measurement in two bases.** Prepare (√3/2)∣+z⟩ + (1/2)∣−z⟩. For S\_z, obtain probabilities 3/4 and 1/4 and mean ħ/4. For S\_x, use overlaps with (∣+z⟩ ± ∣−z⟩)/√2; probabilities are (2 + √3)/4 and (2 − √3)/4 and the mean is √3ħ/4. Confirm both probability sums are one. See sections 2.3–2.4 and 2.9.

**9. Derive uncertainty and the minimum-product state.** Apply Cauchy–Schwarz to centred-operator states. Separate commutator and covariance contributions. Solve δpψ = iλδxψ, normalise the Gaussian and calculate Δx and Δp explicitly. See sections 2.6–2.7.

**10. Derive the angular-momentum spectrum.** Use the component algebra, J² commutation and J\_±. Calculate ladder norms, identify upper/lower endpoints and derive the integer or half-integer ladder labels. Distinguish orbital and spin restrictions. See sections 2.8–2.9.

**11. Construct CG coefficients without a table.** Start at the highest two-spin state, lower once, normalise, and construct its orthogonal singlet. Repeat one lowering for j₁ = 1,j₂ = ½. Check state counts, amplitudes and orthogonality. See sections 2.10–2.11.

**12. State Wigner–Eckart and derive necessary dipole selection rules.** Specify the tensor rank and reduced-element convention, explain the CG dependence, apply projection and triangle rules, and include parity. Explain why permitted angular labels do not alone establish a nonzero transition rate. See section 2.12.

## Unit 3

**13. Separate a central-potential Schrödinger equation.** Write the spherical volume element and angular operator, substitute RY and identify spherical harmonics. Use u = rR to derive the radial effective potential and normalisation. See sections 3.1–3.2.

**14. Obtain hydrogen quantisation from the radial series.** Define the energy-dependent decay scale before introducing n, remove both asymptotic factors, obtain the recursion and impose polynomial termination. Derive E\_n, the quantum-number ranges and node count. See section 3.3.

**15. Distinguish three hydrogen length measures.** For 1s, show that the volume density peaks at zero, shell probability peaks at a, and the mean radius is 3a/2. Explain why they answer different questions. See section 3.4.

**16. Derive non-degenerate perturbation formulas.** Expand energy and state with consistent λ powers. Project the first-order equation on the original and other eigenbras, then project the second-order equation. State the gap criterion and examine the central-delta nodal state as a zero-coupling example. See sections 3.6–3.8.

**17. Calculate the n = 2 linear Stark pattern.** Choose the ideal Coulomb subspace, use parity and m selection to identify its matrix blocks, evaluate the radial and angular factors for the off-diagonal element and diagonalise. State neglected structure and distinguish each shift from the full outer separation. See sections 3.9 and 3.11–3.12.

**18. Explain normal and spin-dependent Zeeman shifts.** Derive the orbital interaction sign from the electron magnetic moment. Distinguish energy and frequency separations, state transition and viewing conditions, and introduce the weak-field Landé expression with its regime and J = 0 exception. See section 3.10.


# Appendix 3: References and Further Reading

## Course References

The MGSU brochure lists L. I. Schiff, \*Quantum Mechanics\*; S. Gasiorowicz, \*Quantum Physics\*; B. Crasemann and J. D. Powell, \*Quantum Mechanics\*; A. Messiah, \*Quantum Mechanics\*; J. J. Sakurai, \*Modern Quantum Mechanics\*; P. M. Mathews and K. Venkatesan, \*A Textbook of Quantum Mechanics\*; and A. Ghatak and S. Lokanathan, \*Quantum Mechanics: Theory and Applications\*. Use your lecturer's chosen edition and notation. The explanations, diagrams and model questions here are independently written.

## Online Learning and Checks

- [MGSU programme brochure](https://www.mgsubikaner.ac.in/PDF/68c7df9cd7f02.pdf): official course scope and published assessment context.
- [MIT Quantum Physics I lecture notes](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2013/pages/lecture-notes/): supplementary study of wavefunctions, current, wells and uncertainty.
- [MIT Quantum Mechanics I, Chemistry](https://ocw.mit.edu/courses/5-73-quantum-mechanics-i-fall-2018/pages/lecture-notes/): a useful connection between quantum formalism and chemical applications.
- [Michael Fowler, University of Virginia: Tensor Operators](https://galileo.phys.virginia.edu/classes/752.mf1i.spring03/TensorOperators.htm): further discussion of tensor matrix elements and angular dependence.
- [MIT Quantum Physics III lecture notes](https://ocw.mit.edu/courses/8-06-quantum-physics-iii-spring-2018/pages/lecture-notes/): further study of time-independent perturbation theory.
- [Richard Fitzpatrick, University of Texas: Linear Stark Effect](https://farside.ph.utexas.edu/teaching/qm/Quantum/node70.html): the ideal hydrogen n = 2 subspace calculation.

## A Final Learning Check

For a new problem, identify the state, Hamiltonian, boundary conditions and measurement being asked about. Decide whether the exact equation, an operator relation or a controlled approximation is appropriate. A result becomes useful when you can explain both its calculation and its conditions of validity in ordinary English.

**End of Quantum Mechanics I guide. Author: Shiwali Sharma.**
