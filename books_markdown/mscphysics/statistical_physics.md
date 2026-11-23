Statistical Physics · Shiwali Sharma

## A Note to the Returning Student

You may remember the ideal gas law, entropy and molecular energy levels from chemistry. Statistical physics explains how those large-scale ideas arise from many microscopic possibilities. It asks how to assign probabilities to those possibilities and how to calculate the averages we measure.

This book is written for a learner returning after a long study gap. It rebuilds probability, counting, logarithms and thermodynamic notation before using partition functions. The advanced topics remain: quantum distributions, interacting gases, phase transitions, correlations and random motion. Each is approached through a small model and then developed into the M.Sc. calculation.

Read the physical situation before the formula. Decide what the system can exchange with its surroundings. Identify what is fixed when taking a derivative. After calculating an average, ask how much a single observation might fluctuate around it. These habits connect the units and prevent many notation errors.

The main language is English. Hindi terminology supplies selected memory aids and a glossary in each unit. Practice questions are original model material. They are not labelled as authenticated previous-year questions or guaranteed examination predictions.

## Course Context and Contents

Coverage follows PHY6.0-CC-104 in the [MGSU programme brochure applicable to admissions in 2025–26](https://www.mgsubikaner.ac.in/PDF/68c7df9cd7f02.pdf), PDF pages 11–12. The brochure calls the course Statistical Mechanics; the existing series title Statistical Physics is retained here. Its semester table lists 20 internal and 80 external marks, while general prose elsewhere describes 100 theory marks. Use the current university notice and college guidance to establish your applicable examination scheme.

| Unit | Learning route |
|---|---|
| 1 | Microstates, phase space, density of states, Liouville theorem, ensembles, ideal gas, mixing, thermodynamic quantities and ensemble fluctuations |
| 2 | Density matrices, indistinguishable particles, classical and quantum distributions, Bose condensation, radiation, Fermi gases and electrons, cluster/virial expansions and Ising models |
| 3 | Landau transitions, critical exponents, scaling, spatial/time correlations, transport, Brownian motion, Langevin, fluctuation–dissipation and Fokker–Planck descriptions |

- [Before Unit 1: Rebuilding the Basics](#bridge)
- [Unit 1: States, Ensembles and Thermodynamics](#unit-1)
- [Unit 2: Quantum Statistics and Interacting Systems](#unit-2)
- [Unit 3: Phase Transitions and Fluctuating Motion](#unit-3)
- [Appendix 1: A Practical Study Route](#appendix-strategy)
- [Appendix 2: Extended Model Questions and Solution Routes](#appendix-pyq)
- [Appendix 3: References and Further Reading](#appendix-references)


## Before Unit 1: Rebuilding the Basics

### Averages and Fluctuations

For outcomes aᵢ with probabilities pᵢ, the average is ⟨A⟩ = Σᵢpᵢaᵢ. Probabilities are nonnegative and sum to one. The variance is Var(A) = ⟨A²⟩ − ⟨A⟩²; its square root is the standard deviation ΔA. A single outcome need not equal the average.

For outcomes 0 and ε with probabilities 3/4 and 1/4, ⟨E⟩ = ε/4 and ⟨E²⟩ = ε²/4. Therefore Var(E) = 3ε²/16. The spread is not an uncertainty about the arithmetic. It describes different microscopic observations of a system with the stated probability distribution.

For a continuous variable, replace sums by integrals over a density. A probability density has inverse units of its integration variable. The probability of an interval is its integral over that interval.

### Counting Possibilities

The factorial N! means N(N − 1)…2×1, with 0! = 1. The number of ways to choose r sites out of N is N!/[r!(N − r)!]. Three sites with two possible states each have 2³ = 8 configurations. Exactly one excited site can be chosen in three ways: 100,010,001. These are separate configurations even though their total energy is the same.

For large N, Stirling's approximation is ln N! ≈ N ln N − N. We will state when this thermodynamic approximation is used. It is unnecessary for counting three sites exactly.

### Logarithms and Boltzmann Factors

The exponential eˣ grows when x is positive and decays when x is negative. Its inverse is the natural logarithm ln. Useful rules are ln(ab) = ln a + ln b, ln(a/b) = ln a − ln b and d(ln x)/dx = 1/x for x &gt; 0. A logarithm or exponential takes a dimensionless argument.

Define β = 1/(k\_BT). It has inverse-energy units. The factor e^(−βE) suppresses higher energy relative to lower energy at positive temperature. If E = k\_BT ln 3, then e^(−βE) = 1/3. You will use this simple arithmetic repeatedly in two-level examples.

We write e^(q) for the exponential with the entire q in its exponent. A power x^(−1/2) means 1/√x for positive x. Greek symbols are labels, not additional operations; read their definitions before manipulating them.

### Heat, Temperature and Thermodynamic State

Temperature is an equilibrium property determining thermal balance. Heat is energy transferred because of a temperature difference; it is not energy stored as a separate state variable. Internal energy U includes the microscopic energy represented by the model.

For a simple compressible one-component system in reversible equilibrium changes:

> dU = T dS − P dV + μ dN.

S is entropy, P pressure, V volume, N particle number and μ chemical potential, the energy-like coefficient for changing N under the specified thermodynamic conditions. The displayed relation concerns a state differential. Along a reversible path, T dS is the exchanged heat; it is not a formula replacing heat transfer in every irreversible process.

Use kelvin for absolute T. Boltzmann's constant is k\_B ≈ 1.380649 × 10⁻²³ J/K. For a mole of particles, N\_Ak\_B = R ≈ 8.314 J/(mol·K). Keep molecular and molar conventions distinct.

### Partial Derivatives and Fixed Variables

In (∂U/∂T)\_V,N, vary T while holding V and N fixed. It is not the same experiment as holding pressure fixed. In a partition function Z(β,V,N), a β derivative holds V,N fixed unless stated otherwise. In a grand partition function Ξ(β,z,V), changing β at fixed fugacity z differs from changing it at fixed chemical potential because z = e^(βμ).

For f(x,y) = x²y, ∂f/∂x at fixed y is 2xy. A total change can involve both terms: df = 2xy dx + x² dy. Writing the fixed quantities is a compact way of stating which change is being considered.

### Readiness Check

1. How many two-state configurations do four labelled sites have? **Answer:** 16.
2. What is ln(e³)? **Answer:** 3.
3. If E = 2k\_BT, what is βE? **Answer:** 2, dimensionless.
4. Can a gas have fixed temperature and fluctuating microscopic energy? **Answer:** Yes, when it exchanges energy with a reservoir.
5. Is R the same numerical constant as k\_B? **Answer:** No. R is molar; k\_B is per particle, related by N\_A.

---

# Unit 1: States, Ensembles and Thermodynamics


## भाग 1: Start Here

The same macroscopic description can hide many microscopic configurations. We begin with three sites that can be counted exactly. Then we generalise to gases with an enormous number of particles.

The central choice is what the system exchanges with its surroundings. An isolated system has fixed energy. A system in thermal contact has fluctuating energy. A system that also exchanges particles has fluctuating particle number. Each situation has a corresponding ensemble.

## भाग 2: Build the Ideas

### 1.1 Microstates, Macrostates and Counting

**In simple words:** A microstate specifies the microscopic arrangement. A macrostate specifies a few large-scale quantities and can correspond to many microstates.

Take three labelled sites, each with energy 0 or ε. The microstates 100,010,001 all have total energy ε. The macrostate “total energy ε” therefore has multiplicity Ω = 3. The possible total energies 0,ε,2ε,3ε have multiplicities 1,3,3,1. Their sum is eight, the total number of configurations.

If the system is isolated at energy ε and the accessible microstates are assigned equal probabilities, each of those three configurations has probability 1/3. The probability that the first site is excited is 1/3. This is an example of a microscopic average conditioned on a specified macrostate.

For N two-state labelled sites with r excitations, Ω(r) = N!/[r!(N − r)!]. Counting sites is appropriate to this fixed-site model. It does not justify treating exchanged identical gas particles as permanently labelled distinguishable objects; that issue enters the ideal-gas state count later.

Entropy in a microcanonical description is S = k\_B ln Ω for the stated state-counting convention. Multiplicities multiply for independent systems, while their entropies add, because ln(Ω\_AΩ\_B) = ln Ω\_A + ln Ω\_B.

**Try it.** Four sites have exactly two excitations. **Answer:** Ω = 4!/(2!2!) = 6 and S = k\_B ln 6.

### 1.2 Phase Space and Density of States

**In simple words:** In classical mechanics, positions and momenta describe a state. Phase space puts them into one mathematical coordinate space; its dimension is a count of required numbers, not a count of physical spatial directions.

For N unconstrained particles moving in 3D, there are 3N position components and 3N momentum components. The full phase space has dimension 6N. One point specifies one instantaneous classical state, and its path in time is a phase trajectory. Constraints can reduce the number of independent coordinates.

A phase-volume element is dΓ = ∏ⱼdqⱼdpⱼ. In a dilute classical approximation to quantum state counting for identical particles, divide a phase-space integral by N!h^(3N). The h factors give dimensionless state counts; N! removes permutation overcounting in this regime.

Let G(E) count states with energy at most E. The **density of states** is g(E) = dG/dE. A narrow shell has approximately Ω(E,δE) = g(E)δE states, provided the shell is narrow on the scale of variation but contains many quantum levels. Do not confuse G, g and Ω; they have different meanings and units.

For a free particle in a large box, momentum states occupy cells of volume h³/V. The momentum sphere of radius p has volume 4πp³/3. Thus G₁(E) = V(4π/3)(2mE)^(3/2)/h³ per internal state, and:

> g₁(E) = (2πV/h³)(2m)^(3/2)√E, for E &gt; 0.

An internal degeneracy g\_s multiplies this result when each spatial state has g\_s independent internal states. This √E dependence will be used for both Bose and Fermi gases.

**Try it.** A one-particle 3D phase point needs how many components? **Answer:** Six: three positions and three momenta.

### 1.3 Liouville's Theorem

**In simple words:** Hamiltonian motion preserves phase volume. A probability density carried along its flow is unchanged along a trajectory, even though its value at a fixed phase point can vary with time.

For a smooth canonical Hamiltonian H(q,p), Hamilton's equations are q̇ⱼ = ∂H/∂pⱼ and ṗⱼ = −∂H/∂qⱼ. The phase-flow divergence is:

> Σⱼ(∂q̇ⱼ/∂qⱼ + ∂ṗⱼ/∂pⱼ) = Σⱼ(H\_pⱼqⱼ − H\_qⱼpⱼ) = 0.

The mixed partial derivatives cancel. Conservation of probability in phase space gives ∂ρ/∂t + Σⱼ[∂(ρq̇ⱼ)/∂qⱼ + ∂(ρṗⱼ)/∂pⱼ] = 0. Expanding the derivatives and using zero divergence yields:

> dρ/dt = ∂ρ/∂t + Σⱼ(q̇ⱼρ\_qⱼ + ṗⱼρ\_pⱼ) = 0.

Equivalently ∂ρ/∂t + {ρ,H} = 0, using the Classical Mechanics bracket convention. The total derivative follows a moving phase point. It is different from the partial time derivative at a fixed point.

Liouville's theorem alone does not prove equal probabilities for all accessible microstates, thermalisation, or equality of time and ensemble averages. Equal a priori probabilities are an equilibrium postulate for the microcanonical description; ergodic assumptions concern sampling by trajectories. For an autonomous H, a density depending only on H is stationary, but a general evolving density need not already have that equilibrium form.

**Try it.** For H = p²/(2m) + kq²/2, calculate the phase-flow divergence. **Answer:** ∂(p/m)/∂q + ∂(−kq)/∂p = 0.

### 1.4 Microcanonical Ensemble and Thermal Equilibrium

**In simple words:** Describe an isolated equilibrium system by assigning equal weight to the microstates compatible with its fixed energy, volume and particle number.

The microcanonical variables are E,V,N. In a large system the accessible energies are often represented by a thin shell E to E + δE. Each of Ω accessible states has probability 1/Ω. The entropy is S(E,V,N) = k\_B ln Ω, with a consistent shell-count convention.

To derive thermal equilibrium, place two weakly interacting systems A,B in energy contact while keeping their combined energy E\_total fixed. Their joint multiplicity at one energy split is Ω\_A(E\_A)Ω\_B(E\_total − E\_A). Maximise its logarithm. Differentiating with respect to E\_A gives:

> (∂S\_A/∂E\_A)\_V,N = (∂S\_B/∂E\_B)\_V,N.

Define 1/T = (∂S/∂E)\_V,N. Equality of these derivatives means equal temperatures. Similarly P/T = (∂S/∂V)\_E,N and −μ/T = (∂S/∂N)\_E,V. These connect microscopic counting to thermodynamic response.

The overwhelming multiplicity of an equilibrium macrostate explains why its averages are typical for a macroscopic system. This does not mean every allowed microstate has the same instantaneous observable value.

**Worked example.** For the three sites fixed at total energy ε, Ω = 3 and S = k\_B ln 3. Doubling an independent copy at the same separately fixed energy multiplies its multiplicity to 9 and doubles its entropy.

### 1.5 Canonical Ensemble and the Partition Function

**In simple words:** A small system can exchange energy with a much larger reservoir. The reservoir's state count determines the relative weight of each system energy.

Keep the combined system isolated. When the subsystem is in state i with energy Eᵢ, the reservoir has energy E\_total − Eᵢ. Expand the reservoir entropy to first order: S\_R(E\_total − Eᵢ) ≈ S\_R(E\_total) − Eᵢ/T. Exponentiating its multiplicity gives a relative factor e^(−βEᵢ). Normalise by summing over all subsystem microstates:

> pᵢ = e^(−βEᵢ)/Z; Z(β,V,N) = Σᵢe^(−βEᵢ).

Z is the canonical **partition function (विभाजन फलन)**. It is a sum of weights, not a probability itself. If grouping states by an energy label r, include degeneracy d\_r: Z = Σ\_rd\_re^(−βE\_r).

**A complete two-level example.** One site has energies 0,ε with no extra degeneracy. Let x = e^(−βε). Then Z₁ = 1 + x, p\_excited = x/(1 + x), and U₁ = εx/(1 + x). If βε = ln 3, x = 1/3, Z₁ = 4/3 and p\_excited = 1/4. At high T the two probabilities approach 1/2; at low positive T the ground state dominates.

For three independent labelled sites, Z₃ = (1 + x)³. Expanding it gives 1 + 3x + 3x² + x³, exactly the multiplicities counted in section 1.1. At x = 1/3, Z₃ = 64/27 and U₃ = 3ε/4.

![Three fixed two-level sites have energy multiplicities 1, 3, 3, 1. The partition function weights each group by its Boltzmann factor.](images/statistical/two_level_states.png)

**Try it.** An excited energy ε has degeneracy 2 and the ground energy 0 has degeneracy 1. **Answer:** Z = 1 + 2e^(−βε); total excited probability is 2e^(−βε)/Z.

### 1.6 Thermodynamic Quantities from Z

**In simple words:** Derivatives of ln Z turn the weighted sum into observable averages. State the fixed variables before differentiating.

At fixed V,N with no extra temperature dependence in the energy spectrum:

> U = −(∂ln Z/∂β)\_V,N; F = −k\_BT ln Z.

To derive U, differentiate Z: ∂Z/∂β = −ΣᵢEᵢe^(−βEᵢ). Divide by Z to obtain −ΣᵢpᵢEᵢ. The Helmholtz free energy F has differential dF = −S dT − P dV + μ dN. Therefore:

> S = −(∂F/∂T)\_V,N = k\_B(ln Z + βU),
> P = −(∂F/∂V)\_T,N = k\_BT(∂ln Z/∂V)\_T,N.

The heat capacity is C\_V = (∂U/∂T)\_V,N. For the single two-level site, differentiate x = e^(−ε/(k\_BT)) to get:

> C\_V = k\_B(βε)²x/(1 + x)².

It tends to zero at both very low and very high T, with an intermediate peak: at low T excitations are rare; at high T the populations approach saturation at 1/2 and change slowly. This is a simple Schottky-type heat-capacity maximum.

**Worked example.** At βε = ln 3, C\_V/k\_B = 3(ln 3)²/16 ≈ 0.2263. For three independent sites the heat capacity is three times as large.

### 1.7 Canonical Energy Fluctuations

**In simple words:** Fixed temperature does not mean fixed energy. A reservoir allows the subsystem to gain and lose energy, producing a measurable variance.

Differentiate ln Z a second time at fixed V,N. The result is ⟨E²⟩ − ⟨E⟩². Since ∂U/∂β = −Var(E) and dβ/dT = −1/(k\_BT²):

> Var(E) = k\_BT²C\_V.

For a stable ordinary canonical system, the variance is nonnegative, giving C\_V ≥ 0 under these assumptions. For many weakly correlated independent contributions, U grows as N and Var(E) as N, so ΔE/U usually scales as 1/√N away from special regimes.

For N independent two-level sites, Var(E) = Nε²x/(1 + x)². At x = 1/3, Var(E) = 3Nε²/16. For N = 3 this is 9ε²/16 and ΔE = 3ε/4. A small three-site system can fluctuate strongly; the same relative fluctuations become small for enormous N.

**Try it.** If the number of independent comparable particles increases by a factor of 100, how does the usual relative fluctuation change? **Answer:** It becomes one tenth as large, subject to the independence/finite-correlation assumptions.

### 1.8 Grand Canonical Ensemble

**In simple words:** A reservoir can exchange particles as well as energy. Sum over both particle number and the states available for each number.

For a state i in the N-particle sector, the grand weight is e^(−β(E\_i,N − μN)). Define fugacity z = e^(βμ) and:

> Ξ(β,z,V) = Σ\_N zᴺ Z\_N(β,V),
> p\_i,N = zᴺe^(−βE\_i,N)/Ξ.

The reservoir fixes T,V,μ for the subsystem, while E and N fluctuate. The grand potential is Φ\_G = −k\_BT ln Ξ, avoiding confusion with multiplicity Ω. Its differential is dΦ\_G = −S dT − P dV − N dμ. For a homogeneous extensive system, Φ\_G = −PV.

Differentiate the defining sum at fixed β,V to obtain ⟨N⟩ = z∂ln Ξ/∂z. For energy, U = −(∂ln Ξ/∂β)\_z,V. If instead μ is held fixed, −∂ln Ξ/∂β gives U − μ⟨N⟩. The difference follows because z changes with β when μ is fixed.

**Worked single-state example.** A fermionic one-particle level of energy ε can be empty or occupied once. Its grand factor is 1 + ze^(−βε). Its mean occupation is ze^(−βε)/[1 + ze^(−βε)]. Unit 2 generalises this reasoning to full gases.

### 1.9 Particle, Density and Energy Fluctuations

**In simple words:** A second grand derivative calculates how broadly particle number fluctuates. Correlations between energy and particle number matter when particles carry energy in and out.

At fixed T,V:

> Var(N) = z∂⟨N⟩/∂z = k\_BT(∂⟨N⟩/∂μ)\_T,V.

For number density n = N/V in a fixed volume, Var(n) = Var(N)/V². Define isothermal compressibility κ\_T = −(1/V)(∂V/∂P)\_T,N. Using dP = n dμ at fixed T for a homogeneous one-component phase gives:

> Var(N)/⟨N⟩² = k\_BT κ\_T/V.

A more compressible equilibrium fluid has larger number fluctuations in the corresponding ensemble. Do not apply the formula to a strictly fixed-N total system as if its global N fluctuated; a subvolume or grand description is required.

At fixed fugacity, ∂²ln Ξ/∂β² = Var(E). A mixed derivative gives Cov(E,N) = −∂⟨N⟩/∂β at fixed z,V. Canonical and grand energy variances need not coincide because the second allows number fluctuations.

For a dilute monatomic ideal gas, grand N is Poisson: Var(N) = ⟨N⟩. It has U = (3/2)⟨N⟩k\_BT, Cov(E,N) = (3/2)⟨N⟩k\_BT and Var(E) = (15/4)⟨N⟩(k\_BT)². At fixed N, the canonical result is only (3/2)N(k\_BT)². The additional grand term comes from fluctuations in how many particles contribute energy.

### 1.10 The Classical Ideal Gas

**In simple words:** Independent translational motion makes the gas partition function factorise. Correct counting of identical particles is essential for its entropy.

For one structureless particle in a large 3D box, integrate over position and momentum:

> Z₁ = (V/h³)∫e^(−βp²/(2m))d³p = V/λ\_T³,
> λ\_T = h/√(2πmk\_BT).

The momentum integral is a product of three Gaussian integrals. For N identical particles in the dilute classical regime, Z\_N = (V/λ\_T³)ᴺ/N!. This is not a Bose or Fermi low-temperature partition function; it assumes occupation per quantum state is small.

Using Stirling's approximation gives F = −Nk\_BT[ln(V/(Nλ\_T³)) + 1]. Differentiate to obtain:

> PV = Nk\_BT; U = (3/2)Nk\_BT; C\_V = (3/2)Nk\_B,
> S = Nk\_B[ln(V/(Nλ\_T³)) + 5/2],
> μ = k\_BT ln(nλ\_T³), with n = N/V.

The entropy is the Sackur–Tetrode form for a monatomic gas without additional internal degeneracy. Molecular rotation, vibration and electronic levels add internal partition factors when thermally accessible. The dilute classical condition is nλ\_T³ ≪ 1 per relevant internal degeneracy.

**Worked example.** For N = 10²³ monatomic particles at 300 K, U = (3/2)Nk\_BT ≈ 621.3 J and C\_V ≈ 2.071 J/K. The associated canonical relative energy spread is √[2/(3N)] ≈ 2.58 × 10⁻¹².

### 1.11 Entropy of Mixing and Gibbs' Paradox

**In simple words:** Mixing two distinguishable gases opens additional distinguishable arrangements. Removing a partition between identical equilibrium gases does not create the same new distinguishable alternatives.

For different ideal gases initially at the same T and P, let species A and B expand from volumes V\_A,V\_B to total V. Their entropy change is:

> ΔS\_mix = k\_B[N\_A ln(V/V\_A) + N\_B ln(V/V\_B)]
> = −k\_B[N\_A ln x\_A + N\_B ln x\_B],

where x\_A = N\_A/(N\_A + N\_B) and similarly for B. For equal amounts, the result is (N\_A + N\_B)k\_B ln 2. Here N\_A labels the number of particles of species A, not Avogadro's constant; context distinguishes them.

Applying a permanently labelled classical-particle count to identical gases would predict an artificial mixing entropy even when the final macroscopic state is unchanged. The N! correction in indistinguishable counting restores extensivity and removes that spurious result in the classical dilute limit. For identical gases at equal initial T and density, removing the divider gives zero thermodynamic mixing entropy in the thermodynamic description.

**Chemistry connection.** Different chemical species remain distinguishable for this counting. “Both gases look colourless” does not make them the same species. The relevant distinction is in physical state counting and separability, not unaided visual appearance.

### 1.12 Thermodynamic Potentials and Response Relations

**In simple words:** Different potentials organise different experimental controls. Their derivatives give the variables conjugate to those controls.

| Potential | Definition | Differential |
|---|---|---|
| Internal energy U | Fundamental energy | dU = T dS − P dV + μ dN |
| Helmholtz F | U − TS | dF = −S dT − P dV + μ dN |
| Enthalpy H\_th | U + PV | dH\_th = T dS + V dP + μ dN |
| Gibbs G\_th | U + PV − TS | dG\_th = −S dT + V dP + μ dN |
| Grand potential Φ\_G | U − TS − μN | dΦ\_G = −S dT − P dV − N dμ |

At fixed N, equality of F's mixed partial derivatives gives (∂S/∂V)\_T = (∂P/∂T)\_V. For Gibbs potential, the corresponding Maxwell relation is (∂S/∂P)\_T = −(∂V/∂T)\_P. These follow from differentiable state functions, not from memorising unrelated identities.

Define α\_P = (1/V)(∂V/∂T)\_P,N and κ\_T as above. A useful response identity is C\_P − C\_V = TVα\_P²/κ\_T. For an ideal gas, α\_P = 1/T and κ\_T = 1/P; substitute PV = Nk\_BT to obtain C\_P − C\_V = Nk\_B, or R per mole.

**Try it.** Which potential is natural for fixed T,V,N? **Answer:** Helmholtz F. For fixed T,P,N, use Gibbs G\_th.

## भाग 3: Put the Ideas Together

### The Same Three Sites in Two Ensembles

Microcanonically, fixing total energy ε allows only 100,010,001. Energy variance is zero, and each site has excitation probability 1/3. Canonically, fixing βε = ln 3 permits all eight configurations with different weights. Each site has excitation probability 1/4; total mean energy is 3ε/4 and variance is 9ε²/16. These are different preparations, so their different averages are consistent.

In a large system away from singular regimes, suitably matched ensembles often agree for local/macroscopic averages to the required accuracy. They do not become identical probability distributions for every quantity: constraints still determine whether total energy or total particle number can fluctuate.

## भाग 4: Check Your Understanding

### 1.13 Common Mistakes and Their Corrections

- Phase-space dimension is not ordinary spatial dimension.
- Distinguish a microstate, an energy value and an energy degeneracy.
- Liouville volume preservation does not by itself prove equal a priori weights or thermalisation.
- A partition function normalises weights; its terms are not already normalised probabilities.
- State what is held fixed in a derivative, especially β,z and μ in the grand ensemble.
- Distinguish the grand potential Φ\_G from multiplicity Ω.
- Fixed T permits energy fluctuations; fixed N excludes global number fluctuations.
- Use N! for the stated identical dilute-gas count, not indiscriminately for labelled lattice sites.
- The Sackur–Tetrode formula here describes the translational monatomic model.
- Mixing different species and removing a partition between identical equilibrium gases are different counting situations.
- Keep molecular k\_B and molar R conventions separate.
- A relative-fluctuation estimate assumes the relevant correlations are not macroscopic.

## भाग 5: Practice Questions with Explanations

#### Question U1-01

Three labelled two-state sites have total energy ε. How many accessible configurations have this energy? 

- **A.**  3 
- **B.**  2 
- **C.**  6 
- **D.**  8 

**Answer: A.**  Exactly one site is excited, so the configurations are 100,010,001. Eight counts all energies, not the specified shell.

#### Question U1-02

Four labelled sites contain exactly two excitations. What is the multiplicity? 

- **A.**  4 
- **B.**  6 
- **C.**  8 
- **D.**  16 

**Answer: B.**  Choose the two excited sites: 4!/(2!2!) = 6. The restriction on total excitation number matters.

#### Question U1-03

For independent systems with multiplicities Ω\_A and Ω\_B, the combined multiplicity is what? 

- **A.**  Ω\_A + Ω\_B 
- **B.**  ln(Ω\_A + Ω\_B) 
- **C.**  Ω\_AΩ\_B 
- **D.**  Ω\_A/Ω\_B 

**Answer: C.**  Every allowed state of A can be paired with every allowed state of B, so the counts multiply and their entropies add.

#### Question U1-04

What is the phase-space dimension of N unconstrained classical point particles in three dimensions? 

- **A.**  3N 
- **B.**  N 
- **C.**  9N 
- **D.**  6N 

**Answer: D.**  Each particle requires three position coordinates and three momentum coordinates. Phase-space dimension is not physical space dimension.

#### Question U1-05

Which factor corrects the classical ideal-gas counting of N identical particles? 

- **A.**  1/N! 
- **B.**  N! 
- **C.**  1/N² 
- **D.**  2N 

**Answer: A.**  Interchanging identical particle labels does not create a new physical state; dividing the labelled count by N! removes that overcounting.

#### Question U1-06

For one free particle in three dimensions, how does its translational density of states depend on positive energy? 

- **A.**  E² 
- **B.**  E^(1/2) 
- **C.**  E^(−1) 
- **D.**  A constant 

**Answer: B.**  Momentum-shell volume contributes p²dp and E is proportional to p², leaving a density proportional to the square root of energy.

#### Question U1-07

What does Liouville's theorem state for Hamiltonian phase flow? 

- **A.**  Every system is ergodic 
- **B.**  All states have equal energy 
- **C.**  The phase-space flow preserves volume 
- **D.**  Every distribution is time independent at fixed coordinates 

**Answer: C.**  Hamiltonian flow is incompressible in canonical phase space. Ergodicity and equal a priori probabilities require further assumptions.

#### Question U1-08

Which step makes the phase-space divergence vanish in Hamilton's equations? 

- **A.**  Setting all velocities to zero 
- **B.**  Neglecting momenta 
- **C.**  Assuming a uniform spatial density 
- **D.**  Cancellation of equal mixed second derivatives of H 

**Answer: D.**  The derivatives of ∂H/∂p and −∂H/∂q cancel pairwise when the Hamiltonian is sufficiently smooth.

#### Question U1-09

Which variables characterise a microcanonical ensemble? 

- **A.**  Fixed N,V,E 
- **B.**  Fixed N,V,T 
- **C.**  Fixed μ,V,T 
- **D.**  Fixed P,T and unrestricted N 

**Answer: A.**  An isolated system has specified energy and particle number; its accessible microstates lie in the chosen energy shell.

#### Question U1-10

What is the microcanonical entropy for Ω accessible equally weighted states? 

- **A.**  k\_BΩ 
- **B.**  k\_B ln Ω 
- **C.**  ln Ω/k\_B 
- **D.**  −k\_BΩ² 

**Answer: B.**  The logarithm converts multiplicative state counts into additive entropy. Its argument is a dimensionless count.

#### Question U1-11

Thermal equilibrium between two large systems exchanging energy requires equality of what entropy derivative? 

- **A.**  ∂S/∂V at fixed T 
- **B.**  S itself 
- **C.**  ∂S/∂E 
- **D.**  Total particle number in each system 

**Answer: C.**  Maximising total entropy at fixed combined energy gives equality of inverse temperatures, since ∂S/∂E = 1/T.

#### Question U1-12

In deriving the canonical law, the large reservoir approximation chiefly keeps which quantity effectively constant? 

- **A.**  System energy in every microstate 
- **B.**  Reservoir particle momentum 
- **C.**  System probability for every energy 
- **D.**  Reservoir temperature 

**Answer: D.**  Expanding reservoir entropy to first order in the exchanged energy gives a fixed inverse temperature multiplying the system energy.

#### Question U1-13

A nondegenerate state has energy ε and Boltzmann factor x = 1/3 relative to a ground state. What is its probability? 

- **A.**  1/4 
- **B.**  1/3 
- **C.**  3/4 
- **D.**  1/9 

**Answer: A.**  Normalisation includes both states: Z = 1 + x = 4/3, and p\_excited = x/Z = 1/4.

#### Question U1-14

Three independent two-state sites each have excited probability 1/4. What is their mean energy? 

- **A.**  ε/4 
- **B.**  3ε/4 
- **C.**  3ε 
- **D.**  ε 

**Answer: B.**  Add the three mean site energies. Each contributes ε/4, even though the total energy fluctuates between preparations.

#### Question U1-15

What is the partition function of three independent identical two-state sites with factor x? 

- **A.**  1 + x³ 
- **B.**  3(1 + x) 
- **C.**  (1 + x)³ 
- **D.**  (1 − x)^(−3) 

**Answer: C.**  The partition functions multiply for independent sites, and each site contributes one ground and one excited state.

#### Question U1-16

Which canonical derivative yields U at fixed N,V? 

- **A.**  ∂ln Z/∂β without a minus sign 
- **B.**  −∂Z/∂V 
- **C.**  ∂ln Z/∂N at fixed E 
- **D.**  −∂ln Z/∂β 

**Answer: D.**  Differentiating each Boltzmann weight contributes −E. Division by Z produces the normalised mean energy.

#### Question U1-17

Which expression gives canonical Helmholtz free energy? 

- **A.**  −k\_BT ln Z 
- **B.**  k\_BT Z 
- **C.**  −k\_B ln Z 
- **D.**  U/T 

**Answer: A.**  F has energy units; the logarithm of the dimensionless partition function must be multiplied by k\_BT.

#### Question U1-18

Which expression gives pressure from F? 

- **A.**  (∂F/∂T)\_(V,N) 
- **B.**  −(∂F/∂V)\_(T,N) 
- **C.**  F/V for every system 
- **D.**  −(∂F/∂N)\_(T,V) 

**Answer: B.**  The differential dF = −S dT − P dV + μ dN identifies pressure with the negative volume derivative at fixed T,N.

#### Question U1-19

What is the canonical relation between energy variance and heat capacity? 

- **A.**  Var(E) = k\_BTC\_V 
- **B.**  Var(E) = C\_V/(k\_BT²) 
- **C.**  Var(E) = k\_BT²C\_V 
- **D.**  Var(E) = U² for every system 

**Answer: C.**  The second β derivative of ln Z is the variance; converting β to T gives the factor k\_BT².

#### Question U1-20

Three independent sites have energies 0,ε and excited probability 1/4. What is Var(E\_total)? 

- **A.**  3ε²/16 
- **B.**  9ε²/4 
- **C.**  Zero 
- **D.**  9ε²/16 

**Answer: D.**  One site has variance ε²p(1 − p) = 3ε²/16. Independent variances add over three sites.

#### Question U1-21

For an ordinary extensive noncritical system, relative energy fluctuations usually scale as what power of N? 

- **A.**  N^(−1/2) 
- **B.**  N 
- **C.**  N^(1/2) 
- **D.**  N^(−2) 

**Answer: A.**  Energy variance scales as N, hence its standard deviation scales as the square root of N while a nonzero extensive mean scales as N.

#### Question U1-22

Which quantity can fluctuate in a grand-canonical ensemble in addition to energy? 

- **A.**  Specified reservoir temperature 
- **B.**  Particle number 
- **C.**  Fixed container volume 
- **D.**  Boltzmann's constant 

**Answer: B.**  Thermal and particle contact with a reservoir allow both energy and particle exchange; temperature and chemical potential are control parameters.

#### Question U1-23

How is fugacity defined here? 

- **A.**  z = βμ 
- **B.**  z = exp(−βU) 
- **C.**  z = exp(βμ) 
- **D.**  z = μ/T without k\_B 

**Answer: C.**  Fugacity z is dimensionless and conveniently replaces chemical potential in the grand partition sum.

#### Question U1-24

What is the grand partition function in terms of canonical Z\_N? 

- **A.**  Ξ = Σ\_N N Z\_N 
- **B.**  Ξ = Z\_N/N! for one fixed N 
- **C.**  Ξ = ln Z\_N 
- **D.**  Ξ = Σ\_N z^N Z\_N 

**Answer: D.**  Summing over all allowed particle numbers, with fugacity weights, accounts for particle exchange with the reservoir.

#### Question U1-25

At fixed z,V, what does −∂βln Ξ give? 

- **A.**  U 
- **B.**  U − μN 
- **C.**  Entropy 
- **D.**  Pressure divided by T 

**Answer: A.**  Treating z and β as independent variables leaves only the energy in the Boltzmann exponent to be differentiated.

#### Question U1-26

At fixed μ,V, what does −∂βln Ξ give? 

- **A.**  U + μN 
- **B.**  U − μN 
- **C.**  N only 
- **D.**  U with no qualification 

**Answer: B.**  At fixed chemical potential the exponent is −β(E − μN), so its derivative produces the mean of E − μN.

#### Question U1-27

Which derivative yields mean particle number? 

- **A.**  −∂ln Ξ/∂V 
- **B.**  ∂ln Ξ/∂T at fixed N 
- **C.**  z(∂ln Ξ/∂z)\_(β,V) 
- **D.**  ln Ξ/z 

**Answer: C.**  Differentiating z^N counts N and the factor z restores the normalised weighted sum.

#### Question U1-28

What is the grand potential of a uniform macroscopic system without additional work terms? 

- **A.**  −k\_BT ln Ξ = U 
- **B.**  k\_BT ln Ξ = S 
- **C.**  −k\_BTΞ = −PV 
- **D.**  −k\_BT ln Ξ = −PV 

**Answer: D.**  The logarithm of Ξ defines the grand potential, whose thermodynamic value is −PV under the stated homogeneous equilibrium conditions.

#### Question U1-29

Which equilibrium number-fluctuation identity is correct? 

- **A.**  Var(N) = k\_BT(∂N/∂μ)\_(T,V) 
- **B.**  Var(N) = (∂N/∂T)\_(μ,V) 
- **C.**  Var(N) = N² always 
- **D.**  Var(N) = 0 in every gas 

**Answer: A.**  The μ derivative of the grand-canonical mean brings down a second factor of N and subtracts the product of means.

#### Question U1-30

For a classical ideal gas in the grand ensemble, what is Var(N)? 

- **A.**  Zero 
- **B.**  Mean N 
- **C.**  Mean N squared 
- **D.**  3 times mean N/2 

**Answer: B.**  Its grand partition function is exponential in activity, giving a Poisson particle-number distribution and equal mean and variance.

#### Question U1-31

For this ideal gas, why is grand-canonical Var(E) larger than canonical Var(E) at the same mean N,T? 

- **A.**  Temperature fluctuates as an uncontrolled variable 
- **B.**  Each particle gains an extra spatial dimension 
- **C.**  Number fluctuations contribute additional energy fluctuations 
- **D.**  The particle mass changes 

**Answer: C.**  A varying number of particles changes the total energy in addition to the kinetic-energy variation at fixed particle count.

#### Question U1-32

What is the grand-canonical Var(E) for a classical monatomic ideal gas? 

- **A.**  (3/2)N(k\_BT)² 
- **B.**  (9/4)N²(k\_BT)² 
- **C.**  Zero 
- **D.**  (15/4)N(k\_BT)² 

**Answer: D.**  Conditional kinetic-energy variance contributes 3N(k\_BT)²/2; number fluctuations add 9N(k\_BT)²/4.

#### Question U1-33

The relative number variance Var(N)/N² equals which compressibility expression? 

- **A.**  k\_BTκ\_T/V 
- **B.**  k\_BTVκ\_T 
- **C.**  κ\_T/(k\_BT) 
- **D.**  k\_BT/κ\_T 

**Answer: A.**  Using the isothermal number response gives a dimensionless relative variance k\_BTκ\_T/V for a uniform equilibrium system.

#### Question U1-34

What is the thermal wavelength used for a nonrelativistic particle of mass m? 

- **A.**  h/(mk\_BT) 
- **B.**  h/√(2πmk\_BT) 
- **C.**  √(2πmk\_BT)/h 
- **D.**  hc/(k\_BT) 

**Answer: B.**  The translational Gaussian momentum integral produces this wavelength. It has units of length and decreases as temperature increases.

#### Question U1-35

Which is the classical monatomic ideal-gas canonical partition function? 

- **A.**  (Vλ³)^N 
- **B.**  N!(V/λ³)^N 
- **C.**  (V/λ³)^N/N! 
- **D.**  exp(Nλ³/V) 

**Answer: C.**  Each particle contributes the dimensionless single-particle translational factor V/λ³, and identical-particle counting supplies 1/N!.

#### Question U1-36

When is the classical ideal-gas counting reliable for a spinless gas? 

- **A.**  nλ³ is much larger than one 
- **B.**  T is exactly zero 
- **C.**  Every particle occupies the same state 
- **D.**  nλ³ is much smaller than one 

**Answer: D.**  A small phase-space occupancy makes exchange effects small; high temperature and low density favour this regime.

#### Question U1-37

What is U for a classical monatomic ideal gas with N particles? 

- **A.**  3Nk\_BT/2 
- **B.**  Nk\_BT/2 
- **C.**  5Nk\_BT/2 
- **D.**  Nk\_BT² 

**Answer: A.**  Three quadratic translational kinetic-energy terms each contribute k\_BT/2 by equipartition.

#### Question U1-38

What is the total C\_V of that gas? 

- **A.**  5Nk\_B/2 
- **B.**  3Nk\_B/2 
- **C.**  Nk\_B 
- **D.**  3Nk\_BT/2 

**Answer: B.**  Heat capacity is the fixed-volume derivative of U with respect to T, so its units are energy per temperature.

#### Question U1-39

For different ideal species with fractions x\_i, what is the mixing entropy? 

- **A.**  k\_BΣ\_i N\_i ln x\_i 
- **B.**  Zero for every pair of gases 
- **C.**  −k\_BΣ\_i N\_i ln x\_i 
- **D.**  −k\_BΣ\_i ln N\_i 

**Answer: C.**  Each species gains accessible volume; since 0 &lt; x\_i &lt; 1, the negative logarithm makes the mixing entropy positive.

#### Question U1-40

Removing a partition between identical ideal gases initially at equal T and density gives which macroscopic mixing entropy? 

- **A.**  2Nk\_B ln 2 necessarily 
- **B.**  −Nk\_B ln 2 
- **C.**  An infinite entropy 
- **D.**  Zero 

**Answer: D.**  No physically distinguishable species mixing occurs under these conditions; consistent identical-particle counting removes the apparent labelled-state entropy increase.

#### Question U1-41

Which fundamental differential applies to U for a simple compressible system? 

- **A.**  dU = T dS − P dV + μ dN 
- **B.**  dU = −S dT − P dV 
- **C.**  dU = T dS + P dV − μ dN 
- **D.**  dU = −T dS + μ dV 

**Answer: A.**  The independent natural variables of U are S,V,N; the pressure work carries a minus sign in this convention.

#### Question U1-42

Which variables are natural for Helmholtz free energy F? 

- **A.**  S,V,N 
- **B.**  T,V,N 
- **C.**  T,P,N 
- **D.**  T,V,μ 

**Answer: B.**  Subtracting TS from U changes the entropy variable to temperature and gives dF = −S dT − P dV + μ dN.

#### Question U1-43

Which Maxwell relation follows from dF at fixed N? 

- **A.**  (∂S/∂V)\_T = −(∂P/∂T)\_V 
- **B.**  (∂S/∂T)\_V = (∂P/∂V)\_T 
- **C.**  (∂S/∂V)\_T = (∂P/∂T)\_V 
- **D.**  S = P for an ideal gas 

**Answer: C.**  Equality of mixed second derivatives of F equates these derivatives, with both minus signs cancelling.

#### Question U1-44

For a stable single phase, which identity connects heat capacities? 

- **A.**  C\_P − C\_V = −TVα²/κ\_T 
- **B.**  C\_P/C\_V = TVα²κ\_T 
- **C.**  C\_P + C\_V = TVα/κ\_T 
- **D.**  C\_P − C\_V = TVα²/κ\_T 

**Answer: D.**  The identity follows from the entropy differential and thermal expansion; positive κ\_T makes the difference nonnegative.

#### Question U1-45

For N monatomic ideal-gas particles, what is C\_P − C\_V? 

- **A.**  Nk\_B 
- **B.**  k\_B/N 
- **C.**  3Nk\_B/2 
- **D.**  Zero 

**Answer: A.**  Substituting α = 1/T and κ\_T = 1/P into TVα²/κ\_T and using PV = Nk\_BT gives Nk\_B.


## भाग 6: Quick Revision and Terminology

### 6.1 Sixty Revision Points

1. A microstate specifies microscopic details; a macrostate fixes a few bulk quantities.
2. Multiplicity counts microstates consistent with the declared macrostate.
3. Three labelled two-state sites have eight configurations over all energies.
4. Their energy multiplicities are 1,3,3,1 for 0,ε,2ε,3ε.
5. N labelled two-state sites with r excitations have multiplicity N!/[r!(N − r)!].
6. Independent multiplicities multiply, while the associated entropies add.
7. An unconstrained three-dimensional N-particle phase space has dimension 6N.
8. Classical phase-space counting uses cells with factors of h and an identical-particle N! correction.
9. The integrated state count and the density of states are different functions.
10. For one free three-dimensional particle, the density of states scales as √E.
11. Hamiltonian phase flow preserves phase-space volume.
12. Liouville's theorem follows from cancellation of mixed Hamiltonian derivatives.
13. Liouville's theorem alone proves neither ergodicity nor equal a priori probabilities.
14. Incompressibility concerns phase flow, not necessarily uniform spatial particle density.
15. A microcanonical ensemble describes specified N,V,E with an adopted energy-shell convention.
16. Microcanonical entropy is S = k\_B ln Ω for the stated accessible-state count.
17. The entropy derivative (∂S/∂E)\_(V,N) equals 1/T.
18. Thermal equilibrium maximises combined entropy under a fixed total-energy constraint.
19. A canonical system exchanges energy with a large thermal reservoir.
20. The canonical microstate probability is exp(−βE\_i)/Z.
21. The inverse temperature β equals 1/(k\_BT), not 1/T.
22. The partition function normalises microstate probabilities.
23. Energy-level degeneracy multiplies a level's Boltzmann weight.
24. Independent canonical partition functions multiply.
25. One two-state site has Z = 1 + exp(−βε).
26. For exp(−βε) = 1/3, a site's excited probability is 1/4.
27. Three such independent sites have U = 3ε/4.
28. Their total energy variance is 9ε²/16.
29. Canonical U equals −∂βln Z at fixed N,V.
30. Helmholtz free energy is F = −k\_BT ln Z.
31. Entropy follows from S = −(∂F/∂T)\_(V,N).
32. Pressure follows from P = −(∂F/∂V)\_(T,N).
33. The second β derivative of ln Z is the canonical energy variance.
34. At fixed N,V, Var(E) = k\_BT²C\_V.
35. Ordinary relative fluctuations shrink as N^(−1/2) under extensive noncritical conditions.
36. A grand-canonical system exchanges both energy and particles with its reservoir.
37. Grand-canonical controls include T,V,μ.
38. Fugacity z = exp(βμ) is dimensionless.
39. The grand partition function is Ξ = Σ\_N z^NZ\_N.
40. Mean particle number is z∂zln Ξ at fixed β,V.
41. The energy derivative −∂βln Ξ gives U when z is held fixed.
42. At fixed μ instead, that derivative gives U − μN.
43. The grand potential is −k\_BT ln Ξ and equals −PV for a uniform macroscopic system.
44. Number variance equals k\_BT(∂N/∂μ)\_(T,V).
45. For a classical grand-canonical ideal gas, particle number is Poisson distributed.
46. Its particle-number mean equals its variance.
47. Grand-canonical ideal-gas energy variance is 15N(k\_BT)²/4.
48. Canonical ideal-gas energy variance is 3N(k\_BT)²/2.
49. The additional grand-canonical variance comes from fluctuating particle number.
50. Relative number variance equals k\_BTκ\_T/V in the uniform equilibrium relation.
51. Thermal wavelength is λ = h/√(2πmk\_BT).
52. The classical ideal-gas canonical partition function is (V/λ³)^N/N!.
53. For a spinless gas, nλ³ much smaller than one favours the classical regime.
54. Monatomic ideal-gas energy is 3Nk\_BT/2 and C\_V is 3Nk\_B/2.
55. Consistent identical-particle counting makes entropy extensive in its classical regime.
56. Mixing different ideal species gives −k\_BΣ\_i N\_i ln x\_i.
57. Removing a partition between identical equilibrium gases produces no species-mixing entropy.
58. For a simple compressible system, dU = T dS − P dV + μ dN.
59. Helmholtz free energy gives the Maxwell relation (∂S/∂V)\_T = (∂P/∂T)\_V.
60. For a stable single phase, C\_P − C\_V = TVα²/κ\_T; an ideal gas gives Nk\_B.

### 6.2 Hindi-Supported Glossary

| English term | Hindi aid | Plain-English meaning |
|---|---|---|
| Microstate | सूक्ष्म अवस्था | A fully specified microscopic configuration |
| Macrostate | स्थूल अवस्था | Description by a few macroscopic variables |
| Multiplicity | बहुलता | Number of microstates compatible with a stated macrostate |
| Ensemble | सांख्यिकीय समुच्चय | Probability description of many possible system states |
| Phase space | अवस्था समष्टि | Space of independent positions and momenta |
| Density of states | अवस्थाओं का घनत्व | State count per energy interval |
| Entropy | एंट्रॉपी | State function related to microscopic probability/counting |
| Partition function | विभाजन फलन | Sum of statistical weights |
| Reservoir | ऊष्मा या कण भंडार | Large surroundings maintaining the relevant intensive controls |
| Chemical potential | रासायनिक विभव | Thermodynamic variable conjugate to particle number |
| Fugacity | फ्यूगैसिटी | Dimensionless weight z = e^(βμ) in this convention |
| Fluctuation | उतार-चढ़ाव | Variation about an average |
| Compressibility | संपीड्यता | Fractional volume response to pressure |
| Heat capacity | ऊष्मा धारिता | Temperature derivative of energy or enthalpy under stated controls |
| Indistinguishable | अविभेद्य | Not counted as separate states merely by swapping particle labels |

### 6.3 Formula Sheet with Conditions

| Result | Conditions or interpretation |
|---|---|
| S = k\_B ln Ω | Microcanonical state count with a consistent shell convention |
| β = 1/(k\_BT) | Inverse energy scale |
| Z = Σe^(−βEᵢ) | Fixed V,N canonical microstate sum |
| U = −∂β ln Z; F = −k\_BT ln Z | Canonical derivative at fixed V,N |
| Var(E) = k\_BT²C\_V | Ordinary canonical setting and fixed V,N |
| Ξ = Σ\_N zᴺZ\_N; z = e^(βμ) | Grand canonical ensemble |
| ⟨N⟩ = z∂z ln Ξ; U = −∂β ln Ξ at fixed z | Keep grand independent variables explicit |
| Var(N) = k\_BT(∂⟨N⟩/∂μ)\_T,V | Grand number fluctuations |
| Var(N)/⟨N⟩² = k\_BTκ\_T/V | Homogeneous grand/subvolume description |
| Z\_N = (V/λ\_T³)ᴺ/N! | Dilute identical monatomic classical gas |
| λ\_T = h/√(2πmk\_BT) | Thermal wavelength convention |
| C\_P − C\_V = TVα\_P²/κ\_T | Simple compressible equilibrium system at fixed N |

---

# Unit 2: Quantum Statistics and Interacting Systems


## भाग 1: Start Here

Two new ingredients enter. Quantum indistinguishability changes which occupation patterns are allowed and how they are counted. Interactions then make the energy depend on arrangements rather than on independent particles alone.

Keep the notation separate: z is fugacity, g\_s an internal degeneracy and z\_c a lattice coordination number. The symbol m may denote particle mass in a gas or mean spin in an Ising calculation; each section identifies its meaning.

## भाग 2: Build the Ideas

### 2.1 Density Matrices: Mixtures and Coherence

**In simple words:** A density operator describes both a known pure state and a statistical mixture of preparations. It keeps quantum amplitudes distinct from classical mixing probabilities.

For pure state ∣ψ⟩, ρ = ∣ψ⟩⟨ψ∣. For a mixture prepared in states ∣ψᵢ⟩ with probabilities wᵢ, ρ = Σᵢwᵢ∣ψᵢ⟩⟨ψᵢ∣. The probabilities obey wᵢ ≥ 0 and Σwᵢ = 1. Different mixtures can represent the same density operator, so that decomposition need not be unique.

In an orthonormal basis, ρ is Hermitian, positive semidefinite and has Tr ρ = 1. Trace is the sum of diagonal entries. Its eigenvalues are nonnegative and sum to one. A pure state has ρ² = ρ and Tr ρ² = 1; a genuinely mixed state has Tr ρ² &lt; 1.

**Worked comparison.** In the basis ↑,↓, the pure state (∣↑⟩ + ∣↓⟩)/√2 has a density matrix with rows (1/2,1/2) and (1/2,1/2). An equal incoherent mixture of ↑ and ↓ instead has rows (1/2,0) and (0,1/2). Both have equal z-spin probabilities. Only the pure state retains the off-diagonal coherence that makes its x-spin outcome definite. Their purities are 1 and 1/2.

The average observable is ⟨A⟩ = Tr(ρA). For a canonical quantum ensemble, ρ = e^(−βH)/Z with Z = Tr e^(−βH). In an energy basis its diagonal entries are Boltzmann probabilities. Von Neumann entropy is S = −k\_B Tr(ρ ln ρ), evaluated through the eigenvalues; ln ρ is a matrix function, not an entry-by-entry logarithm.

For closed unitary evolution, iħρ̇ = [H,ρ]. Its eigenvalues and von Neumann entropy remain unchanged. Thermal relaxation in contact with a bath requires an appropriate open-system description; the closed commutator equation alone does not make an arbitrary state canonical.

**Try it.** For diagonal ρ with entries 3/4,1/4, calculate purity. **Answer:** 9/16 + 1/16 = 5/8, so the state is mixed.

### 2.2 Indistinguishable Particles and Occupation Numbers

**In simple words:** Exchanging identical quantum particles does not create a new physically labelled configuration. Bosons and fermions have different exchange symmetries and occupation rules.

Identical bosons have symmetric many-particle states and integer spin; identical fermions have antisymmetric states and half-integer spin. In the nonrelativistic course these are the applicable exchange rules; a full spin–statistics derivation belongs to relativistic quantum theory.

A single one-particle quantum state can contain 0,1,2,… bosons. For one fermion species with every internal label included in that state, its occupation is 0 or 1. This is Pauli exclusion. Two electrons with opposite spin can occupy the same spatial orbital because their full one-particle states are different.

An occupation list n₁,n₂,… specifies how many particles occupy each one-particle level. It must satisfy Σnᵣ = N and, for independent particles, E = Σnᵣεᵣ. Degenerate one-particle states must be counted separately or supplied with the appropriate degeneracy factor.

For two particles in two single-particle states, the bosonic occupation patterns are (2,0),(1,1),(0,2). For two identical fermions with no additional state label, only (1,1) is allowed. A permanently labelled classical count would distinguish “particle A in state 1 and B in state 2” from the swapped labels; that is a different counting model.

### 2.3 Deriving the Three Distributions

**In simple words:** Calculate the grand partition factor of one level by summing its allowed occupations. Different allowed sums produce Bose and Fermi denominators.

For a one-particle state of energy ε, define x = ze^(−βε) = e^(−β(ε − μ)). Independent levels make the full grand partition function a product of their factors.

For bosons, q\_B = Σ\_(n=0)^∞xⁿ = 1/(1 − x), for x &lt; 1. The mean occupation is x∂ln q\_B/∂x = x/(1 − x). For fermions, q\_F = 1 + x and the same derivative gives x/(1 + x). Therefore:

> f\_B(ε) = 1/[e^(β(ε − μ)) − 1],
> f\_F(ε) = 1/[e^(β(ε − μ)) + 1].

For the ideal classical occupation sum, q\_MB = Σxⁿ/n! = eˣ, giving f\_MB = x = e^(−β(ε − μ)). This is also the common low-occupation limit of the Bose and Fermi functions when x ≪ 1. “Classical statistics” is an approximation about state occupation, not a declaration that identical particles become physically distinguishable.

Use N = Σᵣf(εᵣ), U = Σᵣεᵣf(εᵣ), or replace sums by density-of-states integrals when appropriate. For one independent level, the variance is x∂f/∂x. It gives f(1 + f) for bosons, f(1 − f) for fermions and f for the classical Poisson limit. Bosonic enhancement and fermionic suppression already appear in these single-level fluctuations.

**Worked example.** If β(ε − μ) = ln 3, then x = 1/3. The three occupations are f\_B = 1/2, f\_F = 1/4 and f\_MB = 1/3. A mean Bose occupation of 1/2 does not restrict individual occupation to zero or one.

### 2.4 Classical Limit and Weak Quantum Degeneracy

**In simple words:** Compare the thermal wavelength with particle spacing. When wave packets overlap strongly in phase-space occupancy, exchange statistics can no longer be ignored.

For a uniform nonrelativistic gas, define η = nλ\_T³/g\_s with n = N/V. Small η corresponds to small fugacity and dilute occupation per internal state. Both quantum distributions approach Maxwell–Boltzmann at leading order.

For a weakly degenerate ideal gas, retain the first exchange correction. The number integral gives η = z + z²/2^(3/2) + … for bosons and η = z − z²/2^(3/2) + … for fermions. The pressure integral similarly has denominators 2^(5/2). Eliminating z yields:

> P/(nk\_BT) = 1 − η/2^(5/2) + … for bosons,
> P/(nk\_BT) = 1 + η/2^(5/2) + … for fermions.

These are ideal-gas exchange effects, not forces introduced between particles. Here “weakly degenerate” means that a small-fugacity expansion with leading quantum corrections is useful. A crossover region with η of order one needs the full integrals; a low-temperature Sommerfeld expansion is a different approximation.

**Try it.** For fermions with η = 0.1, estimate the first pressure correction. **Answer:** η/2^(5/2) ≈ 0.01768, so P/(nk\_BT) ≈ 1.01768 within the expansion's accuracy.

### 2.5 The Ideal Bose Gas and Condensation

**In simple words:** In a uniform 3D ideal Bose gas, the excited states can hold only a finite density at a given low temperature when the chemical potential approaches the ground energy. The remaining particles accumulate macroscopically in the ground state.

Take one internal species, energy zero at the ground level and free-particle excitation ε = p²/(2m). In the thermodynamic limit, the excited-state count is:

> N\_ex = (V/λ\_T³)g\_(3/2)(z),
> g\_ν(z) = Σ\_(l=1)^∞zˡ/l^ν.

The function label ν here is an index of the Bose function, not particle spin. The density-of-states integral produces g\_(3/2) because g(ε) is proportional to √ε. At z → 1 from below, g\_(3/2)(1) = ζ(3/2) ≈ 2.612, a finite value. Set N equal to this maximum excited population at T\_c:

> T\_c = [2πħ²/(mk\_B)] [n/ζ(3/2)]^(2/3).

For T &lt; T\_c, the leading thermodynamic-limit excited population scales as T^(3/2), so:

> N₀/N = 1 − (T/T\_c)^(3/2).

At T = T\_c/2, the condensate fraction is 1 − 2^(−3/2) ≈ 0.6464. For m ≈ 1.44 × 10⁻²⁵ kg and n = 10²⁰ m⁻³, the ideal critical scale is about 4.0 × 10⁻⁷ K. Actual trapped interacting atomic gases require the appropriate trapping and interaction model.

The ground-state occupation is treated separately from the continuum integral. At finite N the chemical potential approaches but remains below the lowest level under the usual finite-system description; the sharp transition is a thermodynamic-limit statement. Uniform noninteracting gases in one and two dimensions do not have this same finite-temperature thermodynamic condensation criterion because the excited-state integral behaves differently. Traps and finite size change the analysis.

Condensation refers to macroscopic occupation of a state; it is not the ordinary liquefaction of a gas into a dense droplet. The ideal Bose model contains no attractive molecular force causing liquefaction.

### 2.6 Photons and Planck Radiation

**In simple words:** A thermal radiation field is a Bose gas of photon modes. Their number can change through absorption and emission, so equilibrium photon number does not impose an independent chemical potential.

For equilibrium blackbody photons, μ = 0 and the two transverse polarisations give mode density per volume per ordinary frequency dν: g(ν)/V = 8πν²/c³. Each mode has mean photon energy hν/[e^(βhν) − 1], excluding the temperature-independent zero-point part from thermal radiation energy. Multiply them:

> u(ν,T) = (8πhν³/c³)/[e^(hν/(k\_BT)) − 1].

u(ν,T)dν is energy per volume in that frequency interval. Do not substitute angular frequency ω into this formula without changing both hν = ħω and the density per interval.

At low x = hν/(k\_BT), eˣ − 1 ≈ x gives Rayleigh–Jeans. At high x, the denominator is approximately eˣ, producing the Wien exponential tail. Integrating with x as variable uses ∫₀^∞x³/(eˣ − 1)dx = π⁴/15 and gives total energy density u\_total = a\_radT⁴, where a\_rad = 8π⁵k\_B⁴/(15h³c³). Isotropic radiation pressure is u\_total/3.

The frequency-spectrum maximum satisfies 3(1 − e^(−x)) = x, with positive root near 2.821. The maximum of the wavelength spectrum has a different dimensionless root because changing spectral variable also changes the interval Jacobian. A peak wavelength is not obtained by simply taking c divided by the peak frequency of a different spectral density.

**Try it.** If blackbody temperature doubles, how does total thermal radiation energy per volume change? **Answer:** It increases by 2⁴ = 16.

### 2.7 The Ideal Fermi Gas at Zero Temperature

**In simple words:** Pauli exclusion fills the lowest one-particle states one by one. Even at zero temperature, most particles cannot occupy the lowest spatial state.

At T = 0, f\_F is one below E\_F and zero above it, apart from the boundary convention at exactly E\_F. For internal degeneracy g\_s, count the filled momentum sphere:

> N = g\_sV(4πp\_F³/3)/h³; k\_F = (6π²n/g\_s)^(1/3).

With ε = ħ²k²/(2m), E\_F = ħ²k\_F²/(2m). For electrons with two spin states, g\_s = 2 and k\_F = (3π²n)^(1/3). Integrating ε times the √ε density of states to E\_F gives:

> U₀ = (3/5)NE\_F; P₀ = (2/5)nE\_F; T\_F = E\_F/k\_B.

This is degeneracy pressure of the nonrelativistic ideal gas. It persists at zero temperature and is not predicted by a classical P = nk\_BT approximation there. Relativistic high-density systems require a different energy–momentum relation.

**Worked scale.** For electron density n = 8.5 × 10²⁸ m⁻³ and free-electron mass, E\_F is about 7.05 eV and T\_F about 8.18 × 10⁴ K. These are model energy scales, not a metal's melting temperature. Real bands and interactions can change the effective electronic properties.

### 2.8 Strong Degeneracy and Free Electrons in Metals

**In simple words:** At temperatures far below T\_F, only a thin energy region around the Fermi surface can change occupation appreciably. Most filled states are blocked from low-energy excitations.

For a smooth function φ(ε), the Sommerfeld expansion has the leading form:

> ∫₀^∞φ(ε)f\_F(ε)dε = ∫₀^μφ(ε)dε + (π²/6)(k\_BT)²φ′(μ) + …

It assumes k\_BT is small compared with the scales on which the density/other integrand factors vary near μ. Apply it to the number integral first, holding N fixed. In the 3D free-particle model:

> μ(T) = E\_F[1 − (π²/12)(T/T\_F)² + …].

Then apply it to the energy integral:

> U(T) = (3/5)NE\_F[1 + (5π²/12)(T/T\_F)² + …],
> C\_V = (π²/2)Nk\_B(T/T\_F) + …; S = (π²/2)Nk\_B(T/T\_F) + …

The pressure remains 2U/(3V) for this homogeneous nonrelativistic ideal model. The leading electronic heat capacity is proportional to T, whereas classical equipartition would give a constant (3/2)Nk\_B for translation.

**Worked example.** With T\_F = 8.1 × 10⁴ K and T = 300 K, T/T\_F ≈ 0.003704. Then C\_V/(Nk\_B) ≈ 0.01828. The thermal energy window is only of relative order T/T\_F around the Fermi surface. This explains a small electronic heat capacity even though the electrons carry substantial zero-temperature kinetic energy.

**Try it.** If a strongly degenerate ideal Fermi gas doubles T while remaining in that regime, what happens to its leading C\_V? **Answer:** It doubles, rather than remaining constant.

### 2.9 Cluster Expansion from Intermolecular Interactions

**In simple words:** For a dilute interacting gas, organise corrections by groups of particles connected through their interactions. A pair is the first nontrivial cluster.

For a classical gas with pair potential u(r), the configurational Boltzmann factor is exp[−βΣ\_(i&lt;j)u(r\_ij)]. Define the Mayer function f\_ij = e^(−βu(r\_ij)) − 1. Then the factor becomes ∏\_(i&lt;j)(1 + f\_ij). Expanding this product produces pair, triple and larger interaction graphs. The logarithm of the grand partition function selects connected clusters rather than independent disconnected repetitions.

Choose activity a\_cl = z/λ\_T³, with inverse-volume units, and write:

> ln Ξ/V = a\_cl + b₂a\_cl² + b₃a\_cl³ + …,
> βP = a\_cl + b₂a\_cl² + b₃a\_cl³ + …,
> n = a\_cl + 2b₂a\_cl² + 3b₃a\_cl³ + …

The coefficients b\_l in this convention have units volume^(l−1). In particular b₂ = ½∫f(r)d³r. Textbooks sometimes absorb thermal-wavelength powers and use dimensionless cluster coefficients; compare conventions before copying a formula.

Invert the number series: a\_cl = n − 2b₂n² + (8b₂² − 3b₃)n³ + …. Substitute into βP to obtain:

> βP = n + B₂n² + B₃n³ + …,
> B₂ = −b₂; B₃ = 4b₂² − 2b₃.

This shows how the fugacity/activity cluster expansion becomes a density virial expansion. They are related series, not the same coefficients under two names. The dilute expansion has a limited regime and cannot automatically be extrapolated through a dense-fluid transition.

### 2.10 Second Virial Coefficients and a Chemistry Connection

**In simple words:** The first density correction averages the effect of a pair interaction. Repulsive exclusion tends to increase pressure; attraction can reduce it.

For an isotropic pair potential in 3D:

> B₂(T) = −½∫[e^(−βu(r)) − 1]d³r
> = −2π∫₀^∞[e^(−βu(r)) − 1]r²dr.

For hard spheres of diameter d, u is infinite for r &lt; d and zero outside. Thus the Mayer function is −1 inside the excluded sphere and zero outside. Integration gives B₂ = 2πd³/3, four times one sphere's physical volume πd³/6. It has volume-per-particle units in the number-density expansion.

For a number-density van der Waals convention, P = nk\_BT/(1 − bn) − an². Expand for bn ≪ 1 to get B₂ = b − a/(k\_BT). For the molar equation (P + a\_m/V\_m²)(V\_m − b\_m) = RT, the corresponding molar coefficient is B₂,m = b\_m − a\_m/(RT). Do not use molar R and molar coefficients in a particle-density formula without converting units.

The temperature where a given B₂ vanishes is a Boyle-temperature condition for the leading virial correction. It does not make all higher virial coefficients vanish or turn the interacting gas into an exactly ideal gas at every density.

**Try it.** Does a positive B₂ mean that P/(nk\_BT) initially rises or falls above one as density increases? **Answer:** It rises at the leading dilute order.

### 2.11 The Ising Model and Mean-Field Theory

**In simple words:** Put a binary variable on each lattice site and reward neighbouring alignment. The model tests how local interactions can create collective order.

Let sᵢ = ±1 and:

> H = −JΣ\_(nearest-neighbour bonds)sᵢsⱼ − hΣᵢsᵢ.

J &gt; 0 favours parallel spins. h is an energy-valued field coupling; if a physical field B couples to a moment μ\_s, write h = μ\_sB with the appropriate magnetic convention. It is not dimensionally correct to substitute a field in tesla directly for an energy h.

Mean-field theory replaces each neighbour by mean spin m = ⟨sᵢ⟩. For z\_c neighbours, the effective one-site energy is −(z\_cJm + h)s. Its partition factor gives the self-consistency equation:

> m = tanh[β(z\_cJm + h)].

For h = 0 and small m, tanh x = x − x³/3 + …. The nonzero solution begins at k\_BT\_c^MF = z\_cJ. Close below that temperature, m² is approximately 3(T\_c^MF − T)/T\_c^MF. Above it, linear response gives χ\_s = (∂m/∂h) = 1/[k\_B(T − T\_c^MF)]. This susceptibility uses the energy field h, not an unconverted SI magnetic susceptibility.

A consistent mean-field free-energy expression per site is f\_MF(m) = z\_cJm²/2 − k\_BT ln[2cosh β(z\_cJm + h)]. The first term corrects double counting of the bonds. Differentiation reproduces m = tanh[β(z\_cJm + h)]. This approximation neglects correlated fluctuations and can fail qualitatively in low dimension.

### 2.12 Exact One-Dimensional Ising Chain

**In simple words:** In one dimension the partition sum can be reorganised as repeated multiplication of a two-by-two matrix. This gives an exact result for the nearest-neighbour chain.

For N sites with periodic boundary s\_(N+1) = s₁, split each field contribution equally over its adjacent bonds. The transfer matrix is T\_ss′ = exp[βJss′ + βh(s + s′)/2], with rows:

| Row/column labels | s′ = +1 | s′ = −1 |
|---|---|---|
| s = +1 | e^(β(J + h)) | e^(−βJ) |
| s = −1 | e^(−βJ) | e^(β(J − h)) |

The periodic partition function is Z\_N = Tr Tᴺ. Diagonalising this two-by-two matrix gives:

> λ\_± = e^(βJ)cosh(βh) ± √[e^(2βJ)sinh²(βh) + e^(−2βJ)].

Thus Z\_N = λ\_+ᴺ + λ\_−ᴺ. At h = 0, λ\_+ = 2cosh K and λ\_− = 2sinh K, with K = βJ. The largest eigenvalue controls the thermodynamic free energy per site:

> f = −k\_BT ln(2cosh K),
> u = −Jtanh K; c\_V/k\_B = K²sech²K.

These are analytic at every finite positive T, so the short-range chain has no finite-temperature ordering transition. Its spontaneous magnetisation is zero for T &gt; 0 when the thermodynamic-limit/zero-field definition is taken appropriately. Ground states order at T = 0; the conclusion is not “the model can never have aligned states”.

At zero field in the infinite chain, ⟨s₀s\_r⟩ = (tanh K)^r. For lattice spacing a\_lat, the correlation length is ξ = −a\_lat/ln(tanh K), finite for T &gt; 0 and diverging as T → 0. An isolated domain wall costs finite energy 2J, while many possible wall positions supply entropy; finite-temperature fluctuations therefore destroy long-range order in this model.

![Exact one-dimensional chain correlations at two finite temperatures.](images/statistical/ising_correlations.png)

### 2.13 Ising Models in One, Two and Three Dimensions

**In simple words:** A mean-field equation does not know enough about long fluctuating domains. Comparing dimensions shows the limits of replacing neighbours by one average.

| Lattice/model | Mean-field k\_BT\_c/J | More accurate conclusion |
|---|---|---|
| 1D nearest-neighbour chain, z\_c = 2 | 2 | Exact finite-temperature transition absent; T\_c = 0 |
| 2D square lattice, z\_c = 4 | 4 | Exact zero-field T\_c = 2J/[k\_B ln(1 + √2)] ≈ 2.269J/k\_B |
| 3D simple cubic lattice, z\_c = 6 | 6 | A finite-temperature transition exists; the general model is studied with numerical and approximation methods rather than a simple exact closed-form solution |

Mean field tends to overestimate ordering because it suppresses fluctuation effects. Its one-dimensional prediction is qualitatively wrong. In two dimensions the exact zero-field square-lattice result supplies a clear quantitative comparison. In three dimensions it remains an approximation, not an exact transition-temperature formula.

The macroscopic mean spin is an **order parameter (क्रम प्राचल)**: it distinguishes symmetry-related ordered states below a transition from the symmetric zero-field disordered average above it. Unit 3 develops the corresponding Landau free-energy picture and explains why critical fluctuations require more than a simple mean-field expansion.

## भाग 3: Put the Ideas Together

### Three Different Sources of a Pressure Correction

The classical ideal gas gives P = nk\_BT. An ideal quantum gas changes occupation counting and produces an exchange correction even without pair forces. A dilute classical interacting gas changes the configurational partition sum and produces a Mayer/virial correction. A dense real quantum material can contain both exchange and interaction effects and may require a more complete model. The sign of one small correction is not evidence that every microscopic effect has the same origin.

### A Consistent Approximation Route

First identify the particles and their internal degeneracy. Estimate η = nλ\_T³/g\_s or T/T\_F to choose classical, weak-degeneracy or low-temperature tools. For interactions, check whether a low-density cluster expansion is meaningful. For a lattice spin model, state the lattice, field convention and approximation. Keep exact transfer-matrix results separate from mean-field estimates.

## भाग 4: Check Your Understanding

### 2.14 Common Mistakes and Their Corrections

- A pure superposition and an incoherent mixture can share one basis's probabilities while differing in coherence.
- Matrix logarithms and trace entropy are evaluated through the operator spectrum.
- Pauli exclusion concerns a complete one-particle state, including spin.
- Bose minus and Fermi plus appear in their occupation denominators.
- Large mean Bose occupation is allowed; a full fermionic state is limited to one particle.
- Uniform 3D ideal Bose condensation is not the same as ordinary liquid condensation.
- Equilibrium blackbody photons have μ = 0; conserved atomic particles generally do not.
- Distinguish frequency and angular-frequency spectral densities.
- T\_F is an energy scale, not a melting temperature.
- Small-fugacity and Sommerfeld expansions apply in different regimes.
- Keep molar and particle-density virial conventions separate.
- Ising h has energy units; z\_c is coordination, not fugacity.
- The mean-field transition temperature is not exact in every dimension.
- A finite positive-temperature 1D correlation length is compatible with locally correlated spins but no long-range order.

## भाग 5: Practice Questions with Explanations

#### Question U2-01

What conditions must a density matrix satisfy? 

- **A.**  Every entry must be positive and real 
- **B.**  Hermitian, positive semidefinite and unit trace 
- **C.**  Trace zero and determinant one 
- **D.**  It must always be a projection 

**Answer: B.**  Quantum probabilities require nonnegative eigenvalues and unit trace. A mixed state need not satisfy ρ² = ρ.

#### Question U2-02

Which test identifies a pure density matrix? 

- **A.**  Trρ = 0 
- **B.**  Tr(ρ²) = 0 
- **C.**  Tr(ρ²) = 1 
- **D.**  Every off-diagonal entry vanishes 

**Answer: C.**  A normalised pure state is a rank-one projector. Unit trace alone holds for both pure and mixed states.

#### Question U2-03

What is the purity of the two-state equal incoherent mixture I/2? 

- **A.**  1 
- **B.**  0 
- **C.**  2 
- **D.**  1/2 

**Answer: D.**  Squaring I/2 gives I/4, whose trace in a two-dimensional space is 1/2.

#### Question U2-04

Two states give identical probabilities in the |0⟩,|1⟩ basis. Must their density matrices be identical? 

- **A.**  No; other measurements can reveal different coherences 
- **B.**  Yes, one basis completely fixes every matrix entry 
- **C.**  Yes, if both have trace one 
- **D.**  No quantum state can have equal probabilities 

**Answer: A.**  Diagonal entries in one basis do not specify off-diagonal entries; a changed measurement basis can distinguish the states.

#### Question U2-05

How is the expectation of observable A computed from ρ? 

- **A.**  Trρ times TrA 
- **B.**  Tr(ρA) 
- **C.**  det(ρA) 
- **D.**  Tr(A/ρ) 

**Answer: B.**  The trace rule includes both populations and coherences in a basis-independent expectation value.

#### Question U2-06

Which density matrix describes canonical thermal equilibrium? 

- **A.**  βH/Z 
- **B.**  exp(βH)Z 
- **C.**  exp(−βH)/Z 
- **D.**  H/TrH for every Hamiltonian 

**Answer: C.**  The operator Boltzmann weight is normalised by its trace Z. Its eigenstate weights reproduce canonical probabilities.

#### Question U2-07

Does unitary evolution alone change a closed system's von Neumann entropy? 

- **A.**  Yes, it always increases it 
- **B.**  Yes, it always makes a pure state maximally mixed 
- **C.**  It sets the temperature to zero 
- **D.**  No, its density-matrix eigenvalues are preserved 

**Answer: D.**  A unitary similarity transformation preserves eigenvalues and therefore −k\_BTr(ρ ln ρ). Relaxation needs additional physical reasoning.

#### Question U2-08

What is the allowed occupation of a single fermionic state, including its spin label? 

- **A.**  0 or 1 
- **B.**  Any nonnegative integer 
- **C.**  Exactly 2 
- **D.**  Any real number between zero and infinity in a microstate 

**Answer: A.**  Pauli exclusion limits each complete single-particle state to at most one identical fermion. Mean occupation may be fractional.

#### Question U2-09

What is the allowed occupation of a single bosonic state? 

- **A.**  Only 0 or 1 
- **B.**  Any nonnegative integer 
- **C.**  Only even integers 
- **D.**  Exactly 1 

**Answer: B.**  Identical bosons can share a state; the grand sum includes n = 0,1,2 and onward when it converges.

#### Question U2-10

With x = exp[−β(ε − μ)], what is a bosonic single-state grand factor? 

- **A.**  1 + x 
- **B.**  1 − x 
- **C.**  1/(1 − x), for x &lt; 1 
- **D.**  exp(−x) 

**Answer: C.**  The unrestricted occupancy sum is geometric. Convergence requires x &lt; 1 for the finite-state expression.

#### Question U2-11

What is a fermionic single-state grand factor? 

- **A.**  1/(1 − x) 
- **B.**  exp(x) 
- **C.**  x/(1 − x) 
- **D.**  1 + x 

**Answer: D.**  Only the unoccupied and occupied states contribute, with weights one and x respectively.

#### Question U2-12

At x = 1/3, what is the Bose mean occupancy? 

- **A.**  1/2 
- **B.**  1/4 
- **C.**  1/3 
- **D.**  2 

**Answer: A.**  The Bose mean is x/(1 − x), so (1/3)/(2/3) = 1/2.

#### Question U2-13

At x = 1/3, what is the Fermi mean occupancy? 

- **A.**  1/2 
- **B.**  1/4 
- **C.**  1/3 
- **D.**  3/4 

**Answer: B.**  The Fermi mean is x/(1 + x), giving (1/3)/(4/3) = 1/4.

#### Question U2-14

What is the variance of the occupation of one Bose state with mean f? 

- **A.**  f(1 − f) 
- **B.**  f² − 1 
- **C.**  f(1 + f) 
- **D.**  Zero 

**Answer: C.**  Differentiating the mean with respect to the logarithm of its activity gives enhanced Bose occupation fluctuations.

#### Question U2-15

What is the variance of the occupation of one Fermi state with mean f? 

- **A.**  f(1 + f) 
- **B.**  1/f 
- **C.**  f² + 1 
- **D.**  f(1 − f) 

**Answer: D.**  A single Fermi-state occupation is a Bernoulli variable. Its variance vanishes for an empty or fully occupied state.

#### Question U2-16

When do Bose and Fermi distributions both approach Maxwell–Boltzmann statistics? 

- **A.**  exp[β(ε − μ)] is much larger than one 
- **B.**  Every state is fully occupied 
- **C.**  Temperature is exactly zero at fixed density 
- **D.**  μ exceeds every energy level 

**Answer: A.**  When mean occupation is dilute, the plus or minus one in the quantum denominator becomes negligible.

#### Question U2-17

For internal degeneracy g\_s, which dilute-gas parameter should be small? 

- **A.**  n/(g\_sλ³) 
- **B.**  nλ³/g\_s 
- **C.**  g\_sT/n 
- **D.**  λ/(nT) 

**Answer: B.**  Density per internal state multiplied by thermal volume estimates quantum occupancy; it is dimensionless.

#### Question U2-18

What is the sign of the leading exchange pressure correction for ideal bosons at fixed n,T? 

- **A.**  Positive 
- **B.**  Always zero 
- **C.**  Negative 
- **D.**  Undefined in every dilute gas 

**Answer: C.**  Bose exchange lowers the pressure relative to the classical gas in the weak-degeneracy expansion; fermionic exchange raises it.

#### Question U2-19

For spinless η = nλ³ = 0.1, what is the magnitude of the leading relative exchange pressure correction? 

- **A.**  About 0.177 
- **B.**  About 1.77 
- **C.**  Exactly 0.1 
- **D.**  About 0.0177 

**Answer: D.**  The coefficient is η/2^(5/2), approximately 0.01768. The sign depends on Bose or Fermi statistics.

#### Question U2-20

For a uniform ideal three-dimensional Bose gas, what causes condensation as T falls? 

- **A.**  The excited states have a finite maximum density at μ approaching the ground energy 
- **B.**  The ground state becomes a fermionic state 
- **C.**  Every excited-state energy becomes zero 
- **D.**  Particle conservation stops applying 

**Answer: A.**  At fixed total density the excited-state capacity saturates; the surplus particles form a macroscopic ground-state population.

#### Question U2-21

Which equation locates T\_c for a uniform spinless ideal Bose gas in three dimensions? 

- **A.**  nλ\_c³ = 0 
- **B.**  nλ\_c³ = ζ(3/2) 
- **C.**  nλ\_c = ζ(3) 
- **D.**  k\_BT\_c = mc² 

**Answer: B.**  The three-dimensional nonrelativistic density-of-states integral gives the Bose function of index 3/2 at unit fugacity.

#### Question U2-22

Below T\_c, what is N\_0/N in that model? 

- **A.**  1 − T\_c/T 
- **B.**  (T/T\_c)³ 
- **C.**  1 − (T/T\_c)^(3/2) 
- **D.**  1 for every T below T\_c 

**Answer: C.**  The excited density scales as T^(3/2) after its chemical potential reaches the limiting ground-state value.

#### Question U2-23

At T = T\_c/2, approximately what fraction is condensed? 

- **A.**  0.500 
- **B.**  0.354 
- **C.**  0.875 
- **D.**  0.646 

**Answer: D.**  Substitute one half into 1 − (T/T\_c)^(3/2); the excited fraction is about 0.354.

#### Question U2-24

Why do ordinary equilibrium cavity photons have μ = 0? 

- **A.**  Their number is not conserved in thermal exchange with the walls 
- **B.**  They obey Pauli exclusion 
- **C.**  Their energy is zero 
- **D.**  Their density is independent of temperature 

**Answer: A.**  Walls can create and absorb photons, so a photon-number constraint is absent in ordinary thermal equilibrium.

#### Question U2-25

How does blackbody radiation energy density depend on temperature? 

- **A.**  T 
- **B.**  T⁴ 
- **C.**  T² 
- **D.**  T^(3/2) 

**Answer: B.**  The photon density of states and Bose occupation integral together yield the Stefan–Boltzmann fourth-power dependence.

#### Question U2-26

What relation connects equilibrium radiation pressure and energy density? 

- **A.**  P = 3u 
- **B.**  P = u/T 
- **C.**  P = u/3 
- **D.**  P = u² 

**Answer: C.**  Isotropic massless radiation carries momentum with angular averaging that gives one third of the energy density as pressure.

#### Question U2-27

Why do the maxima of frequency and wavelength blackbody spectra not follow by merely substituting λ = c/ν into the peak location? 

- **A.**  Photon energy does not depend on frequency 
- **B.**  The temperature changes during substitution 
- **C.**  Wavelength spectra violate energy conservation 
- **D.**  Spectral densities transform with a Jacobian 

**Answer: D.**  Energy per frequency interval and per wavelength interval are different density functions; the interval transformation shifts the maximum.

#### Question U2-28

For a spin-degenerate free Fermi gas in three dimensions, how is k\_F related to density? 

- **A.**  k\_F = (6π²n/g\_s)^(1/3) 
- **B.**  k\_F = nλ³ 
- **C.**  k\_F = (n/g\_s)³ 
- **D.**  k\_F = √(2πn) 

**Answer: A.**  Counting occupied wavevector states in the Fermi sphere gives n = g\_sk\_F³/(6π²).

#### Question U2-29

At zero temperature, what is U/N for a three-dimensional nonrelativistic free Fermi gas? 

- **A.**  E\_F 
- **B.**  3E\_F/5 
- **C.**  E\_F/2 
- **D.**  3k\_BT/2 

**Answer: B.**  Integrating E times the square-root density of states up to E\_F and dividing by N yields 3E\_F/5.

#### Question U2-30

What is the corresponding zero-temperature pressure? 

- **A.**  nE\_F 
- **B.**  nE\_F/5 
- **C.**  2nE\_F/5 
- **D.**  Zero 

**Answer: C.**  The nonrelativistic ideal-gas relation P = 2U/(3V), with U = 3NE\_F/5, gives 2nE\_F/5.

#### Question U2-31

Which condition justifies the Sommerfeld expansion for a smooth free-electron density of states near E\_F? 

- **A.**  T is much larger than T\_F 
- **B.**  The gas is always dilute in phase-space occupancy 
- **C.**  The chemical potential is far below the ground state 
- **D.**  T is much smaller than T\_F 

**Answer: D.**  Sommerfeld expansion describes a strongly degenerate Fermi gas, with thermal changes concentrated near the Fermi surface.

#### Question U2-32

How does the leading electronic heat capacity vary at low temperature in that model? 

- **A.**  It is proportional to T 
- **B.**  It is constant at 3Nk\_B/2 
- **C.**  It is proportional to T⁴ 
- **D.**  It vanishes at every positive temperature 

**Answer: A.**  Only a fraction of order T/T\_F of electrons can change occupation, producing C\_V ≈ (π²/2)Nk\_B T/T\_F.

#### Question U2-33

Which quantity is the Mayer function for pair potential u(r)? 

- **A.**  exp[βu(r)] + 1 
- **B.**  exp[−βu(r)] − 1 
- **C.**  βu(r) exactly 
- **D.**  ln u(r) 

**Answer: B.**  Subtracting one removes the noninteracting contribution and isolates the interaction contribution to the cluster expansion.

#### Question U2-34

What are the units of a\_cl = z/λ³ used in the cluster expansion? 

- **A.**  Dimensionless 
- **B.**  Volume 
- **C.**  Inverse volume 
- **D.**  Energy 

**Answer: C.**  Fugacity z is dimensionless; dividing by thermal volume gives an activity with number-density units.

#### Question U2-35

Given ln Ξ/V = a\_cl + b₂a\_cl², what is the density through second order? 

- **A.**  n = a\_cl + b₂a\_cl² 
- **B.**  n = 2a\_cl + b₂a\_cl² 
- **C.**  n = b₂/a\_cl 
- **D.**  n = a\_cl + 2b₂a\_cl² 

**Answer: D.**  Applying a\_cl∂/∂a\_cl to ln Ξ/V brings down the cluster order as a multiplier.

#### Question U2-36

What relation connects the second virial and cluster coefficients in this convention? 

- **A.**  B₂ = −b₂ 
- **B.**  B₂ = b₂ 
- **C.**  B₂ = 2b₂ 
- **D.**  B₂ = b₂² 

**Answer: A.**  Eliminate activity using a\_cl = n − 2b₂n² and substitute into the pressure expansion to obtain the minus sign.

#### Question U2-37

What is B₂ for hard spheres with centre exclusion distance d? 

- **A.**  πd³/6 
- **B.**  2πd³/3 
- **C.**  4πd² 
- **D.**  −2πd³/3 

**Answer: B.**  The integral of the Mayer function is minus the excluded volume 4πd³/3, and B₂ is minus one half of that integral.

#### Question U2-38

Relative to the geometric volume of one sphere of diameter d, how large is its hard-sphere B₂? 

- **A.**  Equal 
- **B.**  Twice 
- **C.**  Four times 
- **D.**  Eight times 

**Answer: C.**  The particle volume is πd³/6. Dividing 2πd³/3 by this gives four, with d consistently a diameter.

#### Question U2-39

What is B₂(T) in the molecular van der Waals convention? 

- **A.**  b − a/(RT) with unchanged molecular a 
- **B.**  b + a/(k\_BT) 
- **C.**  a − bT 
- **D.**  b − a/(k\_BT) 

**Answer: D.**  Expanding the molecular equation P = nk\_BT/(1 − bn) − an² gives the second virial coefficient b − a/(k\_BT).

#### Question U2-40

What does the Boyle temperature condition B₂(T\_B) = 0 guarantee? 

- **A.**  The leading density correction to ideal pressure vanishes 
- **B.**  Every interaction vanishes at every density 
- **C.**  All higher virial coefficients vanish 
- **D.**  The gas must condense 

**Answer: A.**  Cancellation of the second virial term does not remove higher-order density corrections or all interaction effects.

#### Question U2-41

For ferromagnetic nearest-neighbour Ising mean field, what is the zero-field critical temperature? 

- **A.**  J/(z\_ck\_B) 
- **B.**  z\_cJ/k\_B 
- **C.**  Zero in every dimension 
- **D.**  2πJ/k\_B 

**Answer: B.**  Linearising m = tanh[βz\_cJm] around zero gives βz\_cJ = 1; this is a mean-field prediction.

#### Question U2-42

What does the symbol h mean in the Ising Hamiltonian −JΣs\_is\_j − hΣs\_i used here? 

- **A.**  Planck's constant 
- **B.**  Magnetic induction in tesla without any conversion 
- **C.**  An energy-valued field conjugate to the dimensionless spin 
- **D.**  Probability of spin up 

**Answer: C.**  The coefficient multiplying a dimensionless spin has energy units. A laboratory magnetic field needs the appropriate magnetic-moment factor.

#### Question U2-43

At zero field, what are the transfer-matrix eigenvalues of the nearest-neighbour chain? 

- **A.**  e^K and e^(−K) only 
- **B.**  cos K and sin K 
- **C.**  2K and −2K 
- **D.**  2cosh K and 2sinh K 

**Answer: D.**  Diagonalising the symmetric two-by-two transfer matrix gives the sum and difference of e^K and e^(−K).

#### Question U2-44

What is the exact zero-field finite-temperature ordering result for an infinite short-range one-dimensional Ising chain? 

- **A.**  No spontaneous order at any positive temperature 
- **B.**  A transition at 2J/k\_B 
- **C.**  A transition at 4J/k\_B 
- **D.**  Full magnetisation at every positive temperature 

**Answer: A.**  Its correlations decay as a power of tanh K for any finite K, so their range is finite at positive temperature.

#### Question U2-45

What is the zero-field chain's thermodynamic nearest-neighbour correlation? 

- **A.**  1 at every T 
- **B.**  tanh[J/(k\_BT)] 
- **C.**  exp[J/(k\_BT)] 
- **D.**  Zero at every positive T 

**Answer: B.**  Differentiating the exact free energy gives the bond energy −Jtanh K, hence the nearest-neighbour spin product is tanh K.


## भाग 6: Quick Revision and Terminology

### 6.1 Sixty Revision Points

1. A density matrix is Hermitian, positive semidefinite and normalised to trace one.
2. Pure-state density matrices satisfy ρ² = ρ.
3. Purity Trρ² equals one for a pure state and is smaller for a mixed state.
4. The two-state equal incoherent mixture I/2 has purity 1/2.
5. Coherence is described relative to a specified basis.
6. Identical populations in one basis need not imply identical quantum states.
7. An expectation value is Tr(ρA).
8. Canonical equilibrium has ρ = exp(−βH)/Z.
9. Von Neumann entropy is −k\_BTr(ρ ln ρ).
10. Closed unitary evolution preserves density-matrix eigenvalues and von Neumann entropy.
11. Bosons permit any nonnegative integer occupancy of one state.
12. Fermions permit only zero or one particle in a complete single-particle state.
13. Spin labels are part of the single-state specification.
14. For x = exp[−β(ε − μ)], the Bose grand factor is 1/(1 − x).
15. The Bose geometric sum requires x &lt; 1 in its finite-state expression.
16. The Fermi grand factor is 1 + x.
17. The mean Bose occupancy is x/(1 − x).
18. The mean Fermi occupancy is x/(1 + x).
19. The dilute Maxwell–Boltzmann occupancy is x.
20. Bose occupation variance is f(1 + f).
21. Fermi occupation variance is f(1 − f).
22. Quantum distributions approach the classical law at small occupancy.
23. With internal degeneracy g\_s, the dilute parameter is nλ³/g\_s.
24. Weak Bose exchange lowers pressure at fixed n,T relative to the classical value.
25. Weak Fermi exchange raises pressure at fixed n,T relative to the classical value.
26. The leading relative exchange correction has magnitude η/2^(5/2).
27. Uniform ideal three-dimensional Bose condensation occurs when excited states saturate.
28. The limiting Bose chemical potential approaches the ground-state energy from below.
29. For a spinless gas, nλ\_c³ = ζ(3/2).
30. The ideal uniform condensate fraction is 1 − (T/T\_c)^(3/2) below T\_c.
31. At T = T\_c/2 the condensate fraction is approximately 0.6464.
32. Dimensionality, confinement and interactions matter when extending the ideal BEC argument.
33. Ordinary equilibrium cavity photons have zero chemical potential.
34. Photon number need not be conserved in thermal exchange with material walls.
35. The Planck law contains two photon polarisation states.
36. Radiation energy density is proportional to T⁴ and pressure is u/3.
37. Frequency and wavelength spectral densities require the transformation Jacobian.
38. A zero-temperature Fermi gas fills states up to E\_F.
39. The three-dimensional wavevector count gives k\_F = (6π²n/g\_s)^(1/3).
40. For nonrelativistic particles, E\_F = ℏ²k\_F²/(2m).
41. At zero temperature, free-gas U = 3NE\_F/5.
42. At zero temperature, free-gas P = 2nE\_F/5.
43. The Fermi temperature is T\_F = E\_F/k\_B.
44. Sommerfeld expansion applies to a strongly degenerate gas with T much smaller than T\_F.
45. The leading low-temperature free-electron C\_V is (π²/2)Nk\_B T/T\_F.
46. The Mayer function is exp[−βu(r)] − 1.
47. Classical cluster activity a\_cl = z/λ³ has inverse-volume units.
48. The second cluster coefficient is b₂ = (1/2)∫f\_M(r)d³r in the stated convention.
49. Density is obtained by applying a\_cl∂/∂a\_cl to ln Ξ/V.
50. Eliminating activity gives B₂ = −b₂ and B₃ = 4b₂² − 2b₃.
51. Hard-sphere B₂ = 2πd³/3 when d is the centre exclusion distance.
52. That hard-sphere B₂ is four times one particle's geometric volume.
53. The molecular van der Waals coefficient is B₂ = b − a/(k\_BT).
54. Molecular and molar virial coefficients require consistent particle or mole units.
55. The Boyle condition cancels the second virial term, not every interaction correction.
56. Ising mean field satisfies m = tanh[β(z\_cJm + h)].
57. Mean field predicts T\_c = z\_cJ/k\_B and misses important spatial fluctuations.
58. The periodic zero-field chain has transfer eigenvalues 2cosh K and 2sinh K.
59. Its thermodynamic bond correlation is tanh K and correlation length is −a/ln(tanh K).
60. The short-range one-dimensional Ising chain has no spontaneous order at any positive temperature.

### 6.2 Hindi-Supported Glossary

| English term | Hindi aid | Plain-English meaning |
|---|---|---|
| Density matrix | घनत्व आव्यूह | Operator describing a pure preparation or statistical mixture |
| Coherence | कलासंबद्धता | Relative-phase information represented by appropriate off-diagonal terms |
| Purity | शुद्धता | Trace of the squared density operator |
| Boson | बोसॉन | Particle with symmetric exchange statistics |
| Fermion | फर्मिऑन | Particle with antisymmetric exchange statistics |
| Occupation number | अधिभोग संख्या | Number of particles in one complete single-particle state |
| Degenerate gas | क्वांटम-प्रभावी गैस | Gas for which quantum state occupation significantly affects statistics |
| Condensate | संघनित अवस्था का अंश | Macroscopic population of a selected quantum state |
| Fermi energy | फर्मी ऊर्जा | Highest filled energy at zero temperature in the ideal model |
| Cluster expansion | समूह विस्तार | Series organised by connected interacting particle groups |
| Virial coefficient | विरियल गुणांक | Coefficient in a density expansion of the equation of state |
| Transfer matrix | अंतरण आव्यूह | Matrix organising neighbouring-state statistical weights |
| Mean field | माध्य क्षेत्र | Approximation replacing fluctuating neighbours by their average |
| Order parameter | क्रम प्राचल | Quantity distinguishing the ordered phase |
| Correlation length | सहसंबंध लंबाई | Distance scale over which connected fluctuations remain correlated |

### 6.3 Formula Sheet with Conditions

| Result | Conditions or interpretation |
|---|---|
| ρ = Σwᵢ∣ψᵢ⟩⟨ψᵢ∣; ⟨A⟩ = Tr(ρA) | Normalised statistical mixture |
| Tr ρ² = 1 for pure, less than 1 for mixed | Positive trace-one density operator |
| f\_B = [e^(β(ε − μ)) − 1]⁻¹ | Ideal bosonic occupations |
| f\_F = [e^(β(ε − μ)) + 1]⁻¹ | Ideal fermionic occupations |
| η = nλ\_T³/g\_s ≪ 1 | Dilute quantum occupation/classical leading limit |
| T\_c = [2πħ²/(mk\_B)][n/2.612]^(2/3) | Uniform 3D ideal one-species Bose gas |
| N₀/N = 1 − (T/T\_c)^(3/2) | Same model below T\_c, thermodynamic limit |
| E\_F = ħ²(3π²n)^(2/3)/(2m) | 3D nonrelativistic electrons with spin degeneracy 2 |
| U₀ = 3NE\_F/5; C\_V ≈ (π²/2)Nk\_BT/T\_F | Ideal Fermi model and strongly degenerate heat-capacity limit |
| B₂ = −½∫(e^(−βu) − 1)d³r | Classical pair-interaction second virial coefficient |
| m = tanh[β(z\_cJm + h)] | Ising mean field with energy-valued h |
| Z\_chain = λ\_+ᴺ + λ\_−ᴺ | Exact nearest-neighbour periodic 1D transfer-matrix result |

---

# Unit 3: Phase Transitions and Fluctuating Motion


## भाग 1: Start Here

Equilibrium averages can change abruptly or develop singular responses near a transition. Fluctuations also evolve in space and time, carrying information about diffusion and dissipation. This unit connects those two ideas rather than treating random motion as an unrelated appendix.

The order parameter m used in Landau theory is a field describing local order; the particle mass in Brownian equations will be written M. The drag coefficient ζ is different from the critical exponent γ. The definitions keep physically different quantities from sharing an unexplained symbol.

## भाग 2: Build the Ideas

### 3.1 Order Parameters and Landau Free Energy

**In simple words:** Describe the ordered state by a quantity that can choose between symmetry-related values. Expand a free energy in that quantity and find which values are stable.

For a ferromagnetic Ising-like transition, m is mean spin or a proportional magnetisation. At zero ordering field, the model is invariant under m → −m. A uniform free-energy density can therefore be expanded in even powers:

> f(m,T) = f₀(T) + ½r m² + ¼u m⁴ − H\_m m,
> r = a(T − T\_c), with a &gt; 0 and u &gt; 0 near the assumed continuous transition.

H\_m is the field conjugate to m per unit volume in this expression. It is not the unconverted energy-per-site Ising h from Unit 2. Coefficients have units consistent with f being energy per volume and the chosen units of m.

Set H\_m = 0 and minimise f: df/dm = rm + um³ = 0. For r &gt; 0, m = 0 is stable because f″(0) = r &gt; 0. For r &lt; 0, the m = 0 solution is unstable and the two minima are:

> m₀ = ±√(−r/u); f\_min − f₀ = −r²/(4u).

Their positive curvature is −2r. The magnitude of m₀ grows continuously from zero, so this is the elementary Landau continuous-transition model.

![For positive quadratic coefficient the Landau free energy has one minimum; for negative coefficient it has two symmetry-related minima.](images/statistical/landau_minima.png)

For a finite exactly symmetric system, averaging equally over the two ordered orientations can still give ⟨m⟩ = 0. Spontaneous symmetry breaking is defined by the thermodynamic limit with an infinitesimal selecting field or appropriate boundary conditions, then removing the field. A vanishing unselected finite-system mean alone does not prove the absence of ordering correlations.

**Worked example.** In scaled free-energy units take r = −1 and u = 1. Minima are m = ±1 and f − f₀ = −1/4. The point m = 0 has negative curvature and is not the stable phase.

### 3.2 Susceptibility, Heat Capacity and First-Order Transitions

**In simple words:** Response functions describe how a minimum moves when temperature or field changes. A discontinuous jump requires a different free-energy shape than the positive-quartic continuous model.

The equation of state is H\_m = rm + um³. Differentiate at fixed T to get χ\_m = ∂m/∂H\_m = 1/(r + 3um²). Above T\_c, m = 0 and χ\_m = 1/r. In a selected ordered minimum below T\_c, χ\_m = 1/(−2r). Both diverge on approaching the mean-field critical point, with different amplitudes.

For r = a(T − T\_c), the ordered free-energy lowering is −a²(T − T\_c)²/(4u). Entropy density is −∂f\_min/∂T and heat-capacity density is −T∂²f\_min/∂T². The singular model contribution below T\_c is Ta²/(2u), producing a finite jump relative to the disordered branch. There is no latent heat in this simple continuous transition because the first temperature derivative is continuous at T\_c.

For a first-order example, let u &lt; 0 and add +vm⁶/6 with v &gt; 0 for stability. At H\_m = 0, coexistence between m = 0 and nonzero minima occurs when both their free energies and stationary conditions agree. Put y = m². Solving them gives:

> y\_coexist = −3u/(4v); r\_coexist = 3u²/(16v).

The order parameter jumps at positive r, so the transition occurs before the m = 0 curvature reaches zero. Metastable local minima and equilibrium coexistence are different concepts.

**Worked check.** With scaled u = −4 and v = 3, coexistence has r = 1 and m² = 1. For m = 1, df/dm = 1 − 4 + 3 = 0 and f − f₀ = 1/2 − 1 + 1/2 = 0, equal to m = 0. This explicit equality identifies the transition rather than simply locating any local extremum.

### 3.3 Critical Exponents

**In simple words:** Near a continuous transition, quantities often follow powers of distance from the critical point. The exponents describe those powers, while amplitudes depend on microscopic details.

Let t = (T − T\_c)/T\_c. Use a selected ordered phase when defining m below T\_c. The standard labels are:

| Exponent | Defining critical behaviour | Elementary mean-field value |
|---|---|---|
| β\_c | m ∝ (−t)^β\_c below T\_c | 1/2 |
| γ\_c | χ ∝ abs(t)^(−γ\_c) | 1 |
| δ\_c | At t = 0, m ∝ H\_m^(1/δ\_c) for positive field | 3 |
| α\_c | Singular heat capacity ∝ abs(t)^(−α\_c) | 0, a jump in this model |
| ν\_c | Correlation length ξ ∝ abs(t)^(−ν\_c) | 1/2 |
| η\_c | Critical connected correlation ∝ R^(−(d − 2 + η\_c)) | 0 in the Gaussian model |

The subscript c keeps the exponent β\_c distinct from thermal β = 1/(k\_BT). From m₀ = √(−r/u), β\_c = 1/2. The susceptibility formulas give γ\_c = 1. At r = 0, H\_m = um³ gives δ\_c = 3.

Mean-field values are not exact for every system. For the short-range 2D square-lattice Ising model at zero field, β\_c = 1/8, γ\_c = 7/4, ν\_c = 1 and η\_c = 1/4. Its heat capacity has a logarithmic singularity, conventionally α\_c = 0, which is different from a finite mean-field jump even though the exponent label is zero in both cases.

Universality means systems with different microscopic details can share critical exponents when dimensionality, symmetry, interaction range and other relevant features match. It does not mean all phase transitions have the same exponents.

### 3.4 Spatially Varying Order and Correlation Length

**In simple words:** Neighbouring regions resist changing independently. Add an energy cost for spatial variation so that the theory can describe domains and correlated fluctuations.

Use the Landau–Ginzburg functional:

> F[m] = ∫dᵈx [½r m² + ¼u m⁴ + ½c(∇m)² − H\_m m], with c &gt; 0.

The gradient penalty disfavors abrupt spatial differences. Above T\_c, expand about m = 0 and retain the quadratic terms. A Fourier component of wave number k has stiffness r + ck². Long wavelengths have small k and become soft as r → 0. The corresponding length is:

> ξ = √(c/r), for r &gt; 0 in this Gaussian description.

This gives ν\_c = 1/2 when r is proportional to t. In a selected ordered phase, the local curvature is −2r, so the corresponding Gaussian length uses √[c/(−2r)]. At criticality this approximation has to be assessed against fluctuations rather than extended blindly.

For a periodic volume V, choose m\_k = V^(−1/2)∫m(x)e^(−ik·x)dᵈx. Gaussian equilibrium fluctuations then satisfy ⟨|δm\_k|²⟩ = k\_BT/(r + ck²) with the appropriate paired real-field Fourier modes. This is the Ornstein–Zernike quadratic result in the declared normalisation.

**Try it.** If a positive r decreases by a factor of 4 at fixed c, how does ξ change? **Answer:** It doubles. The increased length means larger regions fluctuate together.

### 3.5 Scale Transformations and Dimensional Analysis

**In simple words:** Group neighbouring degrees of freedom into blocks, then change the measuring scale. Near a critical point, repeating this process reveals which features matter at long distances.

A scale transformation changes length by a factor b &gt; 1. A correlation length diverging as |t|^(−ν\_c) implies the thermal scaling variable has exponent y\_t = 1/ν\_c. A common critical homogeneity form for the singular free-energy density is:

> f\_s(t,H\_m) = b^(−d) f\_s(t b^(y\_t), H\_m b^(y\_h)),

with nonuniversal unit factors understood in defining scaling fields. Choose b = |t|^(−1/y\_t) to relate temperature powers to length scaling. When hyperscaling is valid, 2 − α\_c = dν\_c. Combining susceptibility and correlation scaling gives γ\_c = ν\_c(2 − η\_c). Other common identities are α\_c + 2β\_c + γ\_c = 2 and γ\_c = β\_c(δ\_c − 1) under their scaling assumptions.

Dimensional analysis of the short-range scalar field theory gives the quartic interaction its special role at upper critical dimension d = 4. A simple Ginzburg estimate compares fluctuations within one correlation volume with the squared ordered mean. Its ratio scales, apart from constants, as k\_BTu c^(−d/2)|r|^((d − 4)/2). Below four dimensions it grows as r approaches zero, warning that mean-field exponents fail sufficiently near criticality. At four dimensions logarithmic effects can occur. Hyperscaling also has qualifications, particularly above the upper critical dimension; do not force every mean-field exponent into it in arbitrary d.

The essential physical idea is not merely changing units. Coarse graining also averages over short-distance fluctuations and changes effective parameters. A full renormalisation-group calculation extends this introductory scaling account.

### 3.6 Space–Time Correlations and Static Response

**In simple words:** A connected correlation asks whether a fluctuation here predicts a fluctuation somewhere else or at a later time, after subtracting the background average.

For a homogeneous stationary equilibrium field, define C(R,t) = ⟨δm(R,t)δm(0,0)⟩, with δm = m − ⟨m⟩. Without subtracting the mean, long-distance order contributes ⟨m⟩² and can hide the fluctuation behaviour.

Near a continuous critical point, the equal-time connected correlation has the scaling form C(R,0) ∝ R^(−(d − 2 + η\_c))f(R/ξ). Away from criticality the scaling function cuts off correlations at large R, often exponentially in short-range models. At criticality ξ diverges and the power-law range can extend macroscopically.

For a quantity A coupled to an external control f\_ext through energy −f\_ext A, differentiate its canonical average. If A has no explicit f\_ext dependence, the derivative is:

> ∂⟨A⟩/∂f\_ext = β(⟨A²⟩ − ⟨A⟩²).

This is a static fluctuation–response relation. For a uniform field H\_m coupled through −H\_m∫m(x)dᵈx, translational invariance gives χ\_m = (1/(k\_BT))∫C(R,0)dᵈR. Large correlated regions can therefore produce a large susceptibility. The relation requires the appropriate equilibrium ensemble and conjugate-field convention.

**Connection to Unit 2.** In the 1D Ising chain, C(r) = (tanh βJ)^abs(r) at zero field. It decays for all T &gt; 0, with finite ξ. Summing the correlations gives a large low-temperature response without a finite-temperature ordering transition.

### 3.7 Fluctuations and Transport

**In simple words:** Transport measures how a disturbance moves or relaxes. Equilibrium fluctuations can reveal the same motion without first applying a large disturbance.

Fick's law for a simple dilute concentration field is J\_n = −D∇n. Combined with particle conservation, it gives ∂n/∂t = D∇²n for constant D. Fourier's heat law and viscous momentum transport use their own currents and response coefficients. The sign directs flux down the relevant gradient in these ordinary dissipative examples.

For tracer diffusion, write displacement Δx(t) = ∫₀^tv\_x(s)ds. In a stationary equilibrium state with zero mean velocity, expand its square and use the velocity autocorrelation C\_v(s) = ⟨v\_x(s)v\_x(0)⟩:

> ⟨Δx²(t)⟩ = 2∫₀^t(t − s)C\_v(s)ds.

If the correlation integral converges and long-time diffusion exists, divide by 2t and take t → ∞:

> D = ∫₀^∞C\_v(s)ds = (1/d)∫₀^∞⟨v(s) · v(0)⟩ds

for an isotropic d-dimensional system. This is the Green–Kubo diffusion relation. Other transport coefficients require the appropriate current correlations and thermodynamic prefactors, not this velocity formula copied unchanged.

**Chemistry connection.** Diffusion of a tracer in a liquid arises from many microscopic collisions. A mean concentration profile can evolve smoothly even though each tracer follows an irregular path. A vanishing mean displacement in an unbiased ensemble does not mean each molecule stays at its starting point.

### 3.8 Brownian Motion and the Langevin Equation

**In simple words:** A heavy particle in a fluid loses directed motion through drag but is continually kicked by thermal fluctuations. Both effects are needed for equilibrium.

Use one component of velocity v and particle mass M. A simple Markovian Langevin model is:

> M dv/dt = −ζv + η(t) + F\_ext(t),
> ⟨η(t)⟩ = 0; ⟨η(t)η(t′)⟩ = 2ζk\_BT δ(t − t′).

ζ is a drag coefficient with units kg/s. η is a random force, and its correlation coefficient has units force² times time. The white-noise approximation represents short bath memory after coarse graining; it does not claim literal independent molecular impulses at arbitrarily short physical times.

Set F\_ext = 0 and define τ = M/ζ. The solution is:

> v(t) = v(0)e^(−t/τ) + (1/M)∫₀^te^(−(t − s)/τ)η(s)ds.

For a specified initial v₀ independent of later noise, ⟨v(t)⟩ = v₀e^(−t/τ). Insert the noise covariance into the double integral to get the conditional variance Var[v(t)] = (k\_BT/M)(1 − e^(−2t/τ)). At long time it approaches the Maxwell equilibrium variance k\_BT/M.

For an initially equilibrium velocity distribution, the stationary autocorrelation is C\_v(t) = (k\_BT/M)e^(−abs(t)/τ). Green–Kubo integration gives:

> D = (k\_BT/M)τ = k\_BT/ζ.

This is the Einstein diffusion–mobility relation. In the constant-drag model the steady small-force mobility is μ\_v = 1/ζ, since ⟨v⟩\_steady = F\_ext/ζ.

### 3.9 From Ballistic Motion to Diffusion

**In simple words:** A particle first remembers its initial velocity, then repeated collisions erase that memory. Its displacement changes from quadratic to linear growth in time.

For the stationary equilibrium initial velocity assumed in the correlation calculation, insert C\_v into the displacement formula:

> ⟨Δx²(t)⟩ = 2D[t − τ(1 − e^(−t/τ))].

For t ≪ τ, expand the exponential. The linear terms cancel and the leading result is (k\_BT/M)t², ballistic motion. For t ≫ τ, the leading result is 2Dt, ordinary diffusion in one component. In d dimensions the isotropic mean-squared displacement is 2dDt at long time.

![A set of random trajectories can have near-zero average displacement while its mean-squared displacement grows.](images/statistical/brownian_paths.png)

**Worked example.** Let D = 2.0 × 10⁻¹² m²/s. After 1 s in the long-time regime, the one-dimensional root-mean-square displacement is √(2Dt) = 2.0 μm. The three-dimensional root-mean-square distance is √(6Dt) ≈ 3.46 μm. Do not use the one-component factor for the full distance.

If every trajectory is prepared with exactly zero initial velocity instead of an equilibrium velocity distribution, its very-short-time displacement statistics differ. State the preparation before using a crossover formula.

### 3.10 Fluctuation–Dissipation with Explicit Conventions

**In simple words:** Thermal noise and friction are linked. Friction alone cools the particle towards rest; noise alone heats it without a stationary balance. Their equilibrium strengths must match.

Suppose a general white random force has ⟨η(t)η(t′)⟩ = A\_ηδ(t − t′). The Langevin solution gives stationary variance A\_η/(2Mζ). Equipartition requires M⟨v²⟩/2 = k\_BT/2, so A\_η = 2ζk\_BT. This derives the noise amplitude used above rather than assuming an arbitrary fluctuation strength.

For an oscillatory weak force with time convention e^(−iωt), the velocity mobility is μ\_v(ω) = 1/(ζ − iMω). Define the two-sided equilibrium velocity spectrum by S\_v(ω) = ∫\_(−∞)^∞e^(iωt)C\_v(t)dt. Fourier transforming the exponential correlation yields:

> S\_v(ω) = 2ζk\_BT/(ζ² + M²ω²) = 2k\_BT Re μ\_v(ω).

This is a classical fluctuation–dissipation relation in the stated two-sided convention. One-sided spectra and ordinary-frequency conventions use different normalisation factors. A quantum high-frequency treatment also differs; the classical white-noise relation is not a universal formula for every frequency and bath.

**Try it.** At fixed T, doubling ζ changes the long-time diffusion coefficient by what factor? **Answer:** It halves D = k\_BT/ζ, even though the random-force covariance amplitude doubles. Faster damping and stronger force noise must be considered together.

### 3.11 The Fokker–Planck Equation

**In simple words:** Langevin describes random trajectories. Fokker–Planck describes how the probability density of many such trajectories changes. They are two levels of description of the same specified stochastic model.

For constant diffusion coefficient D, take a small-time position increment Δx = A(x)Δt + √(2D)ΔW. The random increment ΔW has zero mean and variance Δt. To leading order, conditional mean displacement is AΔt and mean squared displacement is 2DΔt. Taylor-expand a smooth test function f(x + Δx), average, and divide by Δt:

> d⟨f⟩/dt = ⟨A f′ + D f″⟩.

Write the averages as integrals against P(x,t) and integrate by parts with appropriate vanishing boundary terms. Since this holds for every test function:

> ∂P/∂t = −∂(AP)/∂x + D∂²P/∂x².

The associated probability current is J\_P = AP − D∂P/∂x. Probability conservation follows when the boundary fluxes have the stated closed, reflecting or decaying behaviour. Space-dependent diffusion requires the matching stochastic convention and derivative form; the constant-D formula is the model taught here.

For free diffusion A = 0 and initial position x₀, the full-line solution is P(x,t) = exp[−(x − x₀)²/(4Dt)]/√(4πDt), for t &gt; 0. Its integral is one, its mean is x₀ and variance is 2Dt.

### 3.12 Equilibrium Checks for Fokker–Planck Models

**In simple words:** A proposed stochastic equation should reproduce the correct equilibrium density and variance when coupled to an equilibrium bath. Substitution is an effective way to catch signs and factors.

For the velocity Langevin process, the density equation is:

> ∂P(v,t)/∂t = (ζ/M)∂(vP)/∂v + (ζk\_BT/M²)∂²P/∂v².

Substitute P\_eq(v) ∝ e^(−Mv²/(2k\_BT)). Its derivative is −MvP\_eq/(k\_BT). The probability current in velocity space is −(ζ/M)vP − (ζk\_BT/M²)P′, which vanishes for this Maxwell distribution.

For overdamped position motion in a smooth potential V(x), take A = −V′/ζ and D = k\_BT/ζ. The equation becomes:

> ∂P/∂t = (1/ζ)∂(V′P)/∂x + D∂²P/∂x².

Its zero-current solution is P\_eq ∝ e^(−V/(k\_BT)), if normalisable with the stated boundary conditions. For a harmonic trap V = kx²/2 with k &gt; 0, the equilibrium variance is k\_BT/k. A uniform free-particle distribution on an infinite line is not normalisable, so it is not a stationary probability state there even though the local diffusion equation admits a constant formal solution.

## भाग 3: Put the Ideas Together

### One Bath, Three Consistent Descriptions

For a Brownian particle, start with drag ζ and temperature T. The Langevin force covariance must be 2ζk\_BTδ(t − t′). This gives velocity variance k\_BT/M, correlation time M/ζ and diffusion coefficient k\_BT/ζ. The velocity Fokker–Planck equation has the same Maxwell stationary variance. In a harmonic trap, the overdamped position equation gives k\_BT/k. These agreements check both the physical model and its conventions.

The same reasoning connects to criticality. Large static correlations produce large susceptibility; long relaxation times can make equilibration slow. The static Landau approximation does not automatically specify the dynamical relaxation law. Additional dynamical assumptions are needed for time correlations and transport.

## भाग 4: Check Your Understanding

### 3.13 Common Mistakes and Their Corrections

- Find stable minima, not just stationary points of a free energy.
- Distinguish coexistence from a metastable minimum or a loss of local stability.
- Define spontaneous order with the appropriate thermodynamic-limit and field selection.
- Critical exponents are not universally equal to mean-field values.
- A zero heat-capacity exponent can accompany a jump or a logarithmic singularity.
- A scale transformation includes coarse graining, not only changing the ruler's unit.
- Connected correlations subtract the mean background.
- A transport correlation formula must use the appropriate current and prefactor.
- Zero ensemble mean displacement does not mean zero mean-squared displacement.
- State whether the Brownian initial velocity is fixed or sampled from equilibrium.
- The drag ζ and inverse relaxation time ζ/M have different units.
- Noise amplitude, diffusion coefficient and spectral normalisation must use one consistent convention.
- A formal stationary function must also be normalisable and meet boundary conditions.
- Static free-energy theory alone does not determine every dynamical critical property.

## भाग 5: Practice Questions with Explanations

#### Question U3-01

For f = rm²/2 + um⁴/4 at zero field and u &gt; 0, which minimum is stable for r &gt; 0? 

- **A.**  m = ±√(r/u) 
- **B.**  Every m 
- **C.**  m = 0 
- **D.**  No minimum exists 

**Answer: C.**  The quadratic and quartic terms are both positive away from the origin, and the curvature at zero is r &gt; 0.

#### Question U3-02

For r &lt; 0,u &gt; 0, where are the stable uniform zero-field minima? 

- **A.**  m = 0 only 
- **B.**  m = ±r/u 
- **C.**  m = ±√(r/u) 
- **D.**  m = ±√(−r/u) 

**Answer: D.**  Stationarity gives m(r + um²) = 0; the two nonzero solutions have positive curvature −2r.

#### Question U3-03

If r = −1,u = 1, what is the minimum free-energy density relative to f(0)? 

- **A.**  −1/4 
- **B.**  1/4 
- **C.**  −1/2 
- **D.**  −1 

**Answer: A.**  At m = ±1, the quadratic term is −1/2 and the quartic term is 1/4, so the sum is −1/4.

#### Question U3-04

What is the mean-field zero-field susceptibility above T\_c in the declared Landau field convention? 

- **A.**  r 
- **B.**  1/r 
- **C.**  1/(2r) 
- **D.**  Zero 

**Answer: B.**  Linearising rm + um³ = H\_m about m = 0 gives m = H\_m/r for small field.

#### Question U3-05

What is that susceptibility within a selected ordered phase below T\_c? 

- **A.**  1/r 
- **B.**  −2r 
- **C.**  1/(−2r) 
- **D.**  Zero 

**Answer: C.**  At m₀² = −r/u, the curvature is r + 3um₀² = −2r. Response is its inverse.

#### Question U3-06

Why must the field convention be stated when quoting a susceptibility? 

- **A.**  All fields have identical units 
- **B.**  Susceptibility is always dimensionless 
- **C.**  It removes the need to define the order parameter 
- **D.**  Its units and numerical factors depend on the conjugate field 

**Answer: D.**  An Ising energy field and a Landau energy-density field are different quantities; the derivative must use the specified conjugate pair.

#### Question U3-07

With r = a(T − T\_c), what is the Landau order-parameter exponent for u &gt; 0? 

- **A.**  1/2 
- **B.**  1 
- **C.**  2 
- **D.**  0 

**Answer: A.**  Below T\_c, m₀ is proportional to √(T\_c − T), giving β\_c = 1/2 in mean field.

#### Question U3-08

What is the leading Landau susceptibility exponent? 

- **A.**  1/2 
- **B.**  1 
- **C.**  3 
- **D.**  2 

**Answer: B.**  Since susceptibility scales as the inverse of the distance from T\_c on either side, its exponent γ\_c is one.

#### Question U3-09

At r = 0,u &gt; 0, how does the equilibrium order parameter scale with small H\_m? 

- **A.**  m is proportional to H\_m³ 
- **B.**  m is independent of field 
- **C.**  m is proportional to H\_m^(1/3) 
- **D.**  m is proportional to H\_m² 

**Answer: C.**  The stationarity equation becomes um³ = H\_m, yielding the critical-isotherm exponent δ\_c = 3.

#### Question U3-10

Why is a sixth-order positive term needed when the quartic Landau coefficient u is negative? 

- **A.**  To force every transition to be continuous 
- **B.**  To eliminate all nonzero minima 
- **C.**  To set the quadratic term to zero 
- **D.**  To stabilise the polynomial at large absolute m 

**Answer: D.**  A negative quartic term alone makes the truncated polynomial unbounded below; a positive sixth-order term restores large-m stability.

#### Question U3-11

For u &lt; 0,v &gt; 0 in f = rm²/2 + um⁴/4 + vm⁶/6, where does zero-field coexistence occur? 

- **A.**  r = 3u²/(16v) 
- **B.**  r = 0 necessarily 
- **C.**  r = −u²/v 
- **D.**  r = u/v 

**Answer: A.**  Simultaneous stationarity and equality with f(0) yield a positive r, so coexistence precedes loss of local stability at the origin.

#### Question U3-12

At that first-order coexistence, what is m² in the nonzero phase? 

- **A.**  −u/v 
- **B.**  −3u/(4v) 
- **C.**  u/(4v) 
- **D.**  Zero 

**Answer: B.**  Eliminating r between stationarity and equal free energy gives the positive jump value −3u/(4v).

#### Question U3-13

For u = −4,v = 3, which pair gives coexistence? 

- **A.**  r = 0 and m² = 1 
- **B.**  r = −1 and m² = 4 
- **C.**  r = 1 and m² = 1 
- **D.**  r = 3 and m² = 4 

**Answer: C.**  The coexistence formulas give r = 1 and m² = 1, and direct substitution makes the two phase free energies equal.

#### Question U3-14

What distinguishes a continuous transition in the simple quartic Landau model from the first-order case discussed here? 

- **A.**  There can be no change in susceptibility 
- **B.**  The free energy has no temperature dependence 
- **C.**  The system has no fluctuations 
- **D.**  The order parameter approaches zero continuously at T\_c 

**Answer: D.**  For positive quartic coefficient the stable nonzero minimum shrinks continuously to zero; response functions may still become singular.

#### Question U3-15

What does universality refer to near a critical point? 

- **A.**  Suitable systems share exponents despite different microscopic details 
- **B.**  Every system has the same critical temperature 
- **C.**  All spatial dimensions give the same exponents 
- **D.**  Interactions never matter 

**Answer: A.**  Long-distance critical behaviour can depend mainly on dimension, symmetry and interaction range, while nonuniversal scales differ.

#### Question U3-16

Does α\_c = 0 always mean a finite heat-capacity jump? 

- **A.**  Yes, in every model 
- **B.**  No; logarithmic divergence is also compatible with a zero power exponent 
- **C.**  It means heat capacity is exactly zero 
- **D.**  It means no transition exists 

**Answer: B.**  Mean field has a jump, while the two-dimensional Ising model has a logarithmic singularity; the power exponent alone does not distinguish them.

#### Question U3-17

What is the exact order-parameter exponent of the short-range two-dimensional Ising model? 

- **A.**  1/2 
- **B.**  1 
- **C.**  1/8 
- **D.**  3/2 

**Answer: C.**  The exact two-dimensional Ising exponent differs from the mean-field value, illustrating the importance of critical fluctuations.

#### Question U3-18

What does a positive gradient coefficient c penalise in Landau–Ginzburg theory? 

- **A.**  Uniform temperature by itself 
- **B.**  Every nonzero uniform order parameter 
- **C.**  The mere existence of a boundary 
- **D.**  Rapid spatial variation of the order parameter 

**Answer: D.**  The term c|∇m|²/2 raises the free energy of spatially varying configurations.

#### Question U3-19

Above T\_c in the Gaussian approximation, what is the correlation length? 

- **A.**  √(c/r) 
- **B.**  c/r² 
- **C.**  √(r/c) 
- **D.**  1/(cr) 

**Answer: A.**  Comparing the quadratic stiffness r + ck² identifies an inverse length squared r/c, so ξ = √(c/r).

#### Question U3-20

What happens to ξ as r approaches zero from above in this approximation? 

- **A.**  It vanishes 
- **B.**  It diverges 
- **C.**  It stays equal to c 
- **D.**  It becomes negative 

**Answer: B.**  Long-wavelength fluctuations become softer, and the Gaussian correlation length grows as r^(−1/2).

#### Question U3-21

For the normalised Fourier convention in the text, what is the Gaussian mode variance above T\_c? 

- **A.**  k\_BT(r + ck²) 
- **B.**  (r − ck²)/(k\_BT) 
- **C.**  k\_BT/(r + ck²) 
- **D.**  Zero for every nonzero k 

**Answer: C.**  Equipartition applied to each quadratic mode gives an inverse stiffness, with the precise normalisation declared in the Fourier transform.

#### Question U3-22

Below the upper critical dimension where hyperscaling applies, which relation is correct? 

- **A.**  2 + α\_c = ν\_c/d 
- **B.**  α\_c = d + ν\_c 
- **C.**  γ\_c = dν\_c always 
- **D.**  2 − α\_c = dν\_c 

**Answer: D.**  Equating the singular free-energy scale with one correlated volume yields hyperscaling, subject to its regime of validity.

#### Question U3-23

What is the upper critical dimension of the ordinary short-range scalar quartic theory? 

- **A.**  4 
- **B.**  1 
- **C.**  2 
- **D.**  6 

**Answer: A.**  The quartic interaction becomes marginal at four spatial dimensions; logarithmic effects require care there.

#### Question U3-24

What does the Ginzburg criterion assess? 

- **A.**  Whether every process is reversible 
- **B.**  Whether neglected fluctuations are small enough for mean field to be reliable 
- **C.**  Whether photons conserve particle number 
- **D.**  Whether a density matrix is pure 

**Answer: B.**  It compares fluctuations within a correlated region to the mean-field order scale and identifies a critical region where mean field fails.

#### Question U3-25

Which relation links susceptibility, correlation length and anomalous exponent under standard scaling assumptions? 

- **A.**  γ\_c = ν\_cη\_c 
- **B.**  γ\_c = 2ν\_c + d 
- **C.**  γ\_c = ν\_c(2 − η\_c) 
- **D.**  γ\_c = α\_c/ν\_c 

**Answer: C.**  Integrating the critical connected correlation up to its range ξ produces this scaling relation.

#### Question U3-26

What is the connected correlation of two random quantities A and B? 

- **A.**  ⟨AB⟩ + ⟨A⟩⟨B⟩ 
- **B.**  ⟨A⟩/⟨B⟩ 
- **C.**  ⟨A²⟩ alone 
- **D.**  ⟨AB⟩ − ⟨A⟩⟨B⟩ 

**Answer: D.**  Subtracting the product of means isolates correlated fluctuations rather than a static mean background.

#### Question U3-27

For H = H₀ − fA with no explicit field dependence of A, what is ∂⟨A⟩/∂f in equilibrium? 

- **A.**  βVar(A) 
- **B.**  −βVar(A) 
- **C.**  Var(A)/β 
- **D.**  β⟨A⟩² 

**Answer: A.**  Differentiating both the numerator and normalisation of the Boltzmann average yields the connected variance with a positive sign.

#### Question U3-28

For a stationary one-dimensional tracer, which Green–Kubo relation gives D when the integral converges? 

- **A.**  D = C\_v(0) only 
- **B.**  D = ∫₀^∞C\_v(t)dt 
- **C.**  D = ∫₀^∞t²C\_v(t)dt 
- **D.**  D = 1/∫₀^∞C\_v(t)dt 

**Answer: B.**  The long-time growth rate of the displacement variance is twice the integral of one-component velocity memory.

#### Question U3-29

If C\_v(0) = k\_BT/M and C\_v(t) decays exponentially with time τ, what is D? 

- **A.**  k\_BT/(Mτ) 
- **B.**  Mτ/(k\_BT) 
- **C.**  k\_BTτ/M 
- **D.**  k\_BTτ² 

**Answer: C.**  Integrating the exponential supplies a factor τ, giving length squared per time as required for diffusion.

#### Question U3-30

In Mv̇ = −ζv + η, what are the units of ζ? 

- **A.**  Force 
- **B.**  Energy per temperature 
- **C.**  Inverse length 
- **D.**  Mass per time 

**Answer: D.**  Drag force is ζ times velocity, so ζ has units force divided by velocity, or kg/s.

#### Question U3-31

What is the inertial relaxation time? 

- **A.**  τ = M/ζ 
- **B.**  τ = ζ/M 
- **C.**  τ = Mζ 
- **D.**  τ = k\_BT/ζ 

**Answer: A.**  The homogeneous velocity equation has decay rate ζ/M; its reciprocal is the relaxation time.

#### Question U3-32

What equilibrium white-force correlation is consistent with this drag convention? 

- **A.**  ⟨η(t)η(t′)⟩ = ζδ(t − t′)/(k\_BT) 
- **B.**  ⟨η(t)η(t′)⟩ = 2ζk\_BTδ(t − t′) 
- **C.**  ⟨η(t)η(t′)⟩ = 0 
- **D.**  ⟨η(t)η(t′)⟩ = 2Mk\_BT for all times 

**Answer: B.**  This amplitude makes the stationary velocity variance k\_BT/M; the delta function supplies the inverse-time unit.

#### Question U3-33

For a specified initial velocity v₀, what is the conditional mean velocity without external force? 

- **A.**  v₀ for every t 
- **B.**  v₀e^(t/τ) 
- **C.**  v₀e^(−t/τ) 
- **D.**  Zero at every t including t = 0 

**Answer: C.**  The zero-mean random force does not alter the deterministic mean relaxation from the chosen initial condition.

#### Question U3-34

What is the conditional velocity variance for that fixed initial velocity? 

- **A.**  k\_BT/M at t = 0 
- **B.**  (k\_BT/M)e^(2t/τ) 
- **C.**  Zero for all t 
- **D.**  (k\_BT/M)[1 − e^(−2t/τ)] 

**Answer: D.**  Noise accumulates from zero conditional variance and approaches the equilibrium value as the initial preparation is forgotten.

#### Question U3-35

What is the equilibrium velocity autocorrelation? 

- **A.**  (k\_BT/M)e^(−abs(t)/τ) 
- **B.**  (k\_BT/M)e^(abs(t)/τ) 
- **C.**  (k\_BT/M)t² 
- **D.**  Zero at t = 0 

**Answer: A.**  Equipartition fixes its initial amplitude and dissipative relaxation gives exponential decay in this model.

#### Question U3-36

What is the Einstein relation for constant drag? 

- **A.**  D = ζk\_BT 
- **B.**  D = k\_BT/ζ 
- **C.**  D = ζ/(k\_BT) 
- **D.**  D = M/ζ 

**Answer: B.**  Thermal diffusion and the zero-frequency mobility 1/ζ are linked by equilibrium fluctuation–dissipation.

#### Question U3-37

What is the short-time equilibrium inertial displacement variance? 

- **A.**  2Dt at arbitrarily small t 
- **B.**  D/t 
- **C.**  (k\_BT/M)t² 
- **D.**  k\_BT/M independent of t 

**Answer: C.**  Before velocity has relaxed, displacement is approximately vt, so its variance is ⟨v²⟩t².

#### Question U3-38

What is the leading long-time one-dimensional displacement variance? 

- **A.**  Dt² 
- **B.**  6Dt 
- **C.**  D/t 
- **D.**  2Dt 

**Answer: D.**  One Cartesian coordinate diffuses with variance 2Dt; the three-dimensional squared displacement has mean 6Dt for isotropic diffusion.

#### Question U3-39

For D = 2 × 10^(−12) m²/s and t = 1 s, what is the one-dimensional rms diffusive displacement? 

- **A.**  2 micrometres 
- **B.**  4 micrometres 
- **C.**  2 millimetres 
- **D.**  1 micrometre 

**Answer: A.**  The rms displacement is √(2Dt) = √(4 × 10^(−12)) m = 2 × 10^(−6) m.

#### Question U3-40

With e^(−iωt) force convention, what is the velocity mobility? 

- **A.**  1/(ζ + Mω) 
- **B.**  1/(ζ − iMω) 
- **C.**  ζ − iMω 
- **D.**  iω/ζ 

**Answer: B.**  Substituting an oscillating mean velocity into the linear Langevin equation gives (ζ − iMω)v = F.

#### Question U3-41

For a two-sided velocity spectrum, which classical equilibrium relation applies? 

- **A.**  S\_v(ω) = k\_BT Im μ(ω) 
- **B.**  S\_v(ω) = μ(ω)/(k\_BT) 
- **C.**  S\_v(ω) = 2k\_BT Re μ(ω) 
- **D.**  S\_v(ω) = 0 for ω ≠ 0 

**Answer: C.**  Fourier transforming the exponential correlation yields the same Lorentzian as twice k\_BT times the real mobility under this convention.

#### Question U3-42

Which Fokker–Planck equation describes constant D and drift A(x,t)? 

- **A.**  ∂tP = ∂x(AP) − D∂x²P 
- **B.**  ∂tP = AP + DP 
- **C.**  ∂tP = D∂xP only 
- **D.**  ∂tP = −∂x(AP) + D∂x²P 

**Answer: D.**  Probability conservation supplies the drift divergence; a positive second-derivative term gives diffusive spreading.

#### Question U3-43

What is the variance of the free-diffusion Gaussian starting at a definite x₀? 

- **A.**  2Dt 
- **B.**  Dt² 
- **C.**  D/(2t) 
- **D.**  Zero 

**Answer: A.**  The normalised propagator is exp[−(x − x₀)²/(4Dt)]/√(4πDt), a Gaussian with variance 2Dt.

#### Question U3-44

For overdamped motion in V(x), what is the drift? 

- **A.**  V′(x)/ζ 
- **B.**  −V′(x)/ζ 
- **C.**  −ζV(x) 
- **D.**  V(x)/(k\_BT) 

**Answer: B.**  The deterministic force is −V′; dividing by drag gives the overdamped velocity, directed downhill in potential energy.

#### Question U3-45

For V = κx²/2 with κ &gt; 0, what is the equilibrium positional variance? 

- **A.**  κ/(k\_BT) 
- **B.**  2κk\_BT 
- **C.**  k\_BT/κ 
- **D.**  Zero 

**Answer: C.**  The Boltzmann density is Gaussian with exponent −κx²/(2k\_BT), so its variance is k\_BT/κ.


## भाग 6: Quick Revision and Terminology

### 6.1 Sixty Revision Points

1. An order parameter describes the distinction between ordered and disordered phases.
2. Uniform Landau equilibrium is found by stationarity and a stability test.
3. For positive quartic coefficient, the zero-field minimum is m = 0 when r &gt; 0.
4. For r &lt; 0,u &gt; 0, the stable minima satisfy m₀² = −r/u.
5. The ordered minimum free-energy density is −r²/(4u).
6. The field coefficient in a free-energy density has the corresponding density units.
7. Landau susceptibility above T\_c equals 1/r in the stated field convention.
8. Within a selected ordered phase, susceptibility below T\_c equals 1/(−2r).
9. For r proportional to T − T\_c, mean-field β\_c is 1/2.
10. Mean-field γ\_c equals one and δ\_c equals three.
11. A zero heat-capacity power exponent does not distinguish a jump from a logarithm.
12. The simple quartic Landau theory gives a finite mean-field heat-capacity jump.
13. A negative quartic coefficient requires a positive higher-order stabilising term.
14. For a positive sixth-order coefficient v, first-order coexistence has m² = −3u/(4v).
15. The same coexistence occurs at r = 3u²/(16v), with u &lt; 0.
16. At that coexistence, the disordered minimum can remain locally stable.
17. Finite systems and spontaneous symmetry breaking require care with limits and selected phases.
18. Universality concerns suitable shared long-distance behaviour rather than identical transition temperatures.
19. Dimension, symmetry and interaction range help determine a universality class.
20. The exact two-dimensional Ising β\_c is 1/8, different from mean field.
21. A gradient term penalises spatial variation in Landau–Ginzburg theory.
22. The Gaussian quadratic stiffness of a mode is r + ck² above T\_c.
23. For the declared Fourier normalisation, its variance is k\_BT/(r + ck²).
24. Above T\_c, Gaussian correlation length is ξ = √(c/r).
25. That correlation length diverges as the mean-field transition is approached.
26. The Gaussian correlation-length exponent is ν\_c = 1/2.
27. Standard correlation scaling gives γ\_c = ν\_c(2 − η\_c).
28. Hyperscaling 2 − α\_c = dν\_c requires its appropriate fluctuation-dominated regime.
29. The ordinary short-range quartic theory has upper critical dimension four.
30. The Ginzburg criterion tests whether mean-field fluctuations are negligibly small.
31. A connected correlation subtracts the product of separate means.
32. For coupling −fA, static equilibrium response is βVar(A) when A has no explicit field dependence.
33. Spatially integrated connected correlations determine susceptibility with the stated normalisation.
34. Transport concerns flow and the relaxation or spreading of disturbances.
35. One-component velocity memory gives D = ∫₀^∞C\_v(t)dt when the integral converges.
36. The displacement variance is 2∫₀ᵗ(t − s)C\_v(s)ds for stationary velocities.
37. The inertial Langevin equation is Mv̇ = −ζv + η + F.
38. Drag coefficient ζ has units of mass divided by time.
39. The velocity relaxation time is τ = M/ζ.
40. White thermal force has correlation 2ζk\_BTδ(t − t′) in this convention.
41. For specified v₀, the conditional mean velocity is v₀e^(−t/τ).
42. Its conditional variance is (k\_BT/M)[1 − e^(−2t/τ)].
43. Equilibrium velocity variance is k\_BT/M for one component.
44. Equilibrium velocity correlation decays as (k\_BT/M)e^(−abs(t)/τ).
45. The constant-drag Einstein relation is D = k\_BT/ζ.
46. The equilibrium inertial MSD is 2D[t − τ(1 − e^(−t/τ))].
47. Its short-time leading term is (k\_BT/M)t², describing ballistic motion.
48. Its long-time leading term is 2Dt in one dimension.
49. Isotropic three-dimensional diffusion gives mean squared displacement 6Dt.
50. For e^(−iωt) forcing, velocity mobility is 1/(ζ − iMω).
51. The two-sided equilibrium velocity spectrum is 2k\_BT times the real mobility.
52. Noise spectral conventions must be declared before comparing numerical prefactors.
53. Constant-D Fokker–Planck evolution is ∂tP = −∂x(AP) + D∂x²P.
54. Its probability current is J = AP − D∂xP.
55. Free diffusion from a point gives a normalised Gaussian with variance 2Dt.
56. The velocity Fokker–Planck equation has diffusion coefficient ζk\_BT/M².
57. Its equilibrium is the Maxwell velocity Gaussian, not a uniform velocity distribution.
58. Overdamped motion in a potential has drift −V′/ζ.
59. Zero-current equilibrium is proportional to exp[−V/(k\_BT)] when it can be normalised.
60. A harmonic trap V = κx²/2 has equilibrium positional variance k\_BT/κ.

### 6.2 Hindi-Supported Glossary

| English term | Hindi aid | Plain-English meaning |
|---|---|---|
| Order parameter | क्रम प्राचल | Quantity selecting or measuring an ordered phase |
| Free-energy minimum | मुक्त ऊर्जा का न्यूनतम | Stable equilibrium candidate under stated controls |
| Susceptibility | प्रवृत्ति, प्रतिक्रिया गुणांक | Response of the order parameter to its conjugate field |
| Critical exponent | क्रांतिक घातांक | Power characterising a critical singularity |
| Universality | सार्वत्रिकता | Shared long-distance critical behaviour across suitable models |
| Coarse graining | स्थूल-स्तरीय औसतीकरण | Combining short-scale degrees of freedom into larger blocks |
| Connected correlation | संबद्ध सहसंबंध | Correlation after subtracting the mean background |
| Transport | परिवहन | Flow or spreading of conserved quantities and disturbances |
| Brownian motion | ब्राउनी गति | Irregular motion driven by thermal collisions |
| Drag | श्यान प्रतिरोध | Force opposing directed motion in the model |
| Random force | यादृच्छिक बल | Stochastic contribution from unresolved bath motion |
| Relaxation time | विश्रांति समय | Time scale for loss of a specified disturbance or memory |
| Diffusion | विसरण | Statistical spreading at long times |
| Mobility | गतिशीलता | Mean-velocity response per weak applied force |
| Probability current | प्रायिकता धारा | Flow in a probability-conservation equation |

### 6.3 Formula Sheet with Conditions

| Result | Conditions or interpretation |
|---|---|
| m₀² = −r/u | Uniform zero-field Landau minima with r &lt; 0,u &gt; 0 |
| χ\_above = 1/r; χ\_below = 1/(−2r) | Selected mean-field phase and declared conjugate field |
| ξ = √(c/r) | Gaussian disordered phase, r &gt; 0 |
| χ = β times an equilibrium variance | Observable coupled through minus field times observable |
| D = ∫₀^∞C\_v(t)dt | One velocity component, convergent stationary tracer correlation |
| Mv̇ = −ζv + η | Markovian inertial Brownian model |
| ⟨η(t)η(t′)⟩ = 2ζk\_BTδ(t − t′) | Classical equilibrium white-force convention |
| C\_v(t) = (k\_BT/M)e^(−abs(t)/τ) | Equilibrium initial velocity, τ = M/ζ |
| D = k\_BT/ζ | Constant drag Einstein relation |
| MSD\_1D = 2D[t − τ(1 − e^(−t/τ))] | Equilibrium inertial crossover |
| ∂tP = −∂x(AP) + D∂x²P | Constant-D drift–diffusion model |
| P\_eq ∝ e^(−V/(k\_BT)) | Overdamped equilibrium, D = k\_BT/ζ and valid normalisation/boundaries |

---


# Appendix 1: Learning and Answer-Writing Plan

The author of this revised guide is **Shiwali Sharma**. The aim is to let a returning learner rebuild the reasoning needed for MGSU Statistical Mechanics, rather than memorise a page of disconnected equations.

## A Six-Week Route

| Week | Main work | Evidence that you are ready to move on |
|---|---|---|
| 1 | Probability bridge, multiplicities, phase space and Liouville theorem | Enumerate three two-state sites; explain what incompressible Hamiltonian flow does and does not imply |
| 2 | Canonical and grand-canonical ensembles; thermodynamic derivatives | Derive a distribution from a reservoir, declare fixed variables and calculate a variance |
| 3 | Density matrices, quantum occupations, Bose and Fermi gases | Distinguish purity from coherence; choose the correct occupancy rule and limiting approximation |
| 4 | Cluster expansion, virial coefficients and Ising models | Eliminate activity to second order; compare the exact chain with mean field |
| 5 | Landau theory, critical exponents and spatial correlations | Find and classify minima; state when mean field and hyperscaling need qualification |
| 6 | Langevin dynamics, response and Fokker–Planck equation | Connect drag, diffusion, noise and equilibrium; solve a Gaussian spreading problem |

A week is a planning unit, not a deadline. With a long gap in mathematics, repeat the bridge and derivations before increasing the number of practice questions. Work in short sessions: read one concept, close the book, explain it aloud, and solve one small example without looking. Mark the step that failed, rather than labelling the whole topic “difficult”.

## How to Write a Derivation

Start with the physical system and the variables held fixed. Define each new symbol. Write the probability law or governing equation before differentiating it. Show the intermediate operation that changes one line into the next. Finish with the result, its units and its assumptions.

For a canonical heat-capacity question, for example, state fixed N,V, define β = 1/(k\_BT), write Z = Σexp(−βE), obtain U = −∂βln Z, then differentiate U with respect to temperature. The relation Var(E) = k\_BT²C\_V follows from the same calculation. Writing only the final identity does not demonstrate the connection.

Keep a distinction between a definition, a derived identity, an approximation and a model prediction. S = −k\_BTr(ρ ln ρ) is a definition of the quantum entropy used here. Canonical variance identities follow from the equilibrium distribution. Stirling's formula is an approximation. The Curie temperature z\_cJ/k\_B is a mean-field prediction and fails for the one-dimensional short-range chain at finite temperature.

## A Revision Page That You Make Yourself

Divide one page into four columns: physical question, starting equation, final relation, and conditions. For example, “How far does a Brownian particle spread?” starts with the velocity correlation and ends with the inertial mean-square displacement. Its conditions include an equilibrium initial velocity and the stated white-noise model. A condition written beside a formula is easier to remember than one hidden on another page.

Use Hindi aids to clarify meaning, then practise the English statement needed in an answer. “Fluctuation — उतार-चढ़ाव — a random deviation from an average” is useful; replacing every English term with an unfamiliar technical translation is less helpful. Read subscripts aloud: C\_V means heat capacity with volume fixed, while C\_P has pressure fixed.

## Self-Assessment Without Guessing Marks

Use the 45 MCQs in each unit to find conceptual errors. After choosing an option, write one sentence explaining why a distractor is wrong. For derivations, use the extended questions below. These are newly written practice questions, not authenticated previous examination questions. Check the current university examination instructions for the actual paper format and assessment split.


# Appendix 2: Extended Practice with Solution Routes

## Unit 1

### E1. Count First, Then Average

Three labelled sites have energies 0 and ε each. Enumerate the microstates at total energy ε. Then put all three sites in contact with a reservoir such that exp(−βε) = 1/3. Find the mean total energy and its variance. Explain why the microcanonical and canonical answers describe different preparations.

**Solution route:** The isolated shell contains 100,010,001, each with probability 1/3, and total energy exactly ε. In the canonical preparation each site is independently excited with probability (1/3)/(1 + 1/3) = 1/4. The number of excitations is binomial with mean 3/4 and variance 9/16. Thus U = 3ε/4 and Var(E) = 9ε²/16. A fluctuation of one site's energy is possible even in the microcanonical shell, while the shell's total energy is fixed. Do not confuse these two observables.

### E2. Derive the Canonical Law

An isolated composite consists of a small system and a much larger reservoir. Derive the probability of a system microstate and identify the approximation.

**Solution route:** A system state of energy E\_i has reservoir multiplicity Ω\_R(E\_total − E\_i). Expand S\_R(E\_total − E\_i) to first order: S\_R ≈ S\_R(E\_total) − E\_i/T. Divide by k\_B, exponentiate and normalise to obtain p\_i = exp(−βE\_i)/Z. The reservoir must be large enough for its temperature to be effectively constant; higher entropy derivatives quantify corrections. A degenerate energy level has probability equal to its multiplicity times the single-microstate probability.

### E3. Connect Heat Capacity and Variance

Starting from Z, derive the canonical energy fluctuation formula and discuss why ordinary relative fluctuations become small in a large noncritical system.

**Solution route:** Differentiate ln Z once to obtain −U and twice to obtain ⟨E²⟩ − ⟨E⟩². At fixed N,V, ∂β/∂T = −1/(k\_BT²), hence Var(E) = k\_BT²C\_V. If U and C\_V both scale as N, the standard deviation divided by U scales as N^(−1/2). This argument needs revision near singular responses or when a mean energy vanishes by choice of energy origin; an absolute variance remains well defined.

### E4. Separate Two Grand-Canonical Derivatives

Use Ξ(β,z,V) to obtain N and U for a classical monatomic ideal gas. Explain why differentiating at fixed μ changes the energy formula.

**Solution route:** Ξ = exp(zV/λ³), with λ proportional to β^(1/2). Then N = z∂zln Ξ = zV/λ³ and U = −(∂βln Ξ)\_z = 3N/(2β). At fixed μ, z = exp(βμ) also changes, and −(∂βln Ξ)\_μ = U − μN. The independent variables must therefore be written beside the derivative.

### E5. Explain Mixing Entropy

Equal amounts of two different ideal gases initially occupy equal volumes at the same temperature and pressure. Find the mixing entropy. Compare with removal of a partition between identical gases in the same initial thermodynamic state.

**Solution route:** Each different species expands from V to 2V, giving ΔS = 2Nk\_B ln 2 if N particles of each species are used. For identical equilibrium gases, there is no new species distinction and no macroscopic mixing entropy. The consistent identical-particle counting and its N! factor remove the spurious discontinuity of a labelled-particle treatment.

### E6. Derive a Response Identity

Show that C\_P − C\_V = TVα²/κ\_T for a stable single-phase simple compressible system.

**Solution route:** Begin with dS = (C\_V/T)dT + (∂P/∂T)\_V dV, using the Maxwell relation from F. On a constant-pressure path, dV/dT = Vα, so C\_P − C\_V = TVα(∂P/∂T)\_V. The total differential of V gives (∂P/∂T)\_V = α/κ\_T. For an ideal gas, α = 1/T and κ\_T = 1/P, yielding Nk\_B. Keep total and per-particle heat capacities distinct.

## Unit 2

### E7. Diagnose Two Density Matrices

In the basis |0⟩,|1⟩ compare ρ\_A = (1/2)[[1,1],[1,1]] and ρ\_B = (1/2)[[1,0],[0,1]]. Both give equal probabilities in this basis. Are they the same state?

**Solution route:** Both have trace one and nonnegative eigenvalues. However, ρ\_A² = ρ\_A and Trρ\_A² = 1, while Trρ\_B² = 1/2. A measurement in the |+⟩,|−⟩ basis gives probabilities 1,0 for A and 1/2,1/2 for B. The off-diagonal terms encode coherence relative to the chosen basis. Equal probabilities for one measurement do not specify the whole quantum state.

### E8. Obtain Quantum Occupations

Derive single-state Bose and Fermi grand partition factors and calculate the mean and variance of occupation.

**Solution route:** Put x = exp[−β(ε − μ)]. Bosons have q = Σxⁿ = 1/(1 − x), x &lt; 1, whereas fermions have q = 1 + x. Apply x∂xln q for the mean and x∂x again for the variance. The results are f\_B = x/(1 − x), Var n = f\_B(1 + f\_B), and f\_F = x/(1 + x), Var n = f\_F(1 − f\_F). State spin as part of the single-state label.

### E9. Locate Bose Condensation

For a uniform ideal gas of spinless bosons in three dimensions, derive the critical temperature and the condensate fraction below it. Discuss one limit of the argument.

**Solution route:** Integrate the excited-state density of states to get N\_ex = (V/λ³)g\_(3/2)(z). As μ approaches the ground energy from below, z approaches one after setting that energy to zero. The maximum excited density is ζ(3/2)/λ³. Solve nλ\_c³ = ζ(3/2) for T\_c and obtain N\_0/N = 1 − (T/T\_c)^(3/2). The uniform ideal continuum argument does not imply finite-temperature condensation in all dimensions or for every trap.

### E10. Compare Photons and Electrons

Explain why equilibrium cavity photons use μ = 0, while the electron chemical potential in a low-temperature metal lies close to E\_F. State one thermodynamic consequence for each system.

**Solution route:** Ordinary thermal photon number is not conserved because walls create and absorb photons; equilibrium selects μ = 0. Integrating their Bose distribution gives radiation energy density proportional to T⁴ and pressure u/3. Electron number is constrained; Pauli exclusion fills states up to E\_F at zero temperature. Only a narrow thermal region near the Fermi surface changes occupation at low T, producing electronic heat capacity proportional to T rather than the classical 3Nk\_B/2.

### E11. Extract the Second Virial Coefficient

Given ln Ξ/V = a\_cl + b₂a\_cl² + O(a\_cl³), derive P/(k\_BT) = n + B₂n² + O(n³). Calculate B₂ for hard spheres of centre-to-centre exclusion distance d.

**Solution route:** Obtain n = a\_cl + 2b₂a\_cl². Invert to a\_cl = n − 2b₂n² and substitute to find B₂ = −b₂. For hard spheres, f\_M = −1 inside radius d and zero outside. Thus b₂ = −(1/2)(4πd³/3), and B₂ = 2πd³/3. This is four times the volume of a sphere of diameter d. Do not use d as its radius when comparing these volumes.

### E12. Solve and Compare an Ising Chain

Write the periodic one-dimensional nearest-neighbour Ising transfer matrix at zero field, obtain its eigenvalues and the thermodynamic free energy per site. Compare the prediction about ordering with mean field.

**Solution route:** The matrix is [[e^K,e^(−K)],[e^(−K),e^K]], K = J/(k\_BT). Its eigenvalues are 2cosh K and 2sinh K; Z\_N is the sum of their Nth powers. For fixed positive T as N grows, f = −k\_BT ln(2cosh K). The zero-field correlation decays as (tanh K)^r, with finite correlation length at every positive T. Hence there is no finite-temperature spontaneous ordering in this chain, whereas mean field incorrectly predicts T\_c = 2J/k\_B. The zero-temperature and thermodynamic limits require care.

## Unit 3

### E13. Classify Landau Minima

For f(m) = rm²/2 + um⁴/4 − H\_m m, u &gt; 0, find the zero-field minima and the susceptibility on both sides of the transition.

**Solution route:** Stationarity gives rm + um³ = 0. For r &gt; 0 the stable minimum is m = 0; for r &lt; 0 the two stable minima satisfy m² = −r/u, while m = 0 is unstable. Linearise rm + um³ = H\_m about the selected minimum to obtain χ = 1/(r + 3um₀²). This is 1/r above and 1/(−2r) below. A susceptibility below T\_c refers to a selected phase, not arbitrary jumping between both minima.

### E14. Find First-Order Coexistence

Add vm⁶/6 with u &lt; 0 and v &gt; 0 at zero field. Show that coexistence with m = 0 occurs before the curvature at the origin vanishes.

**Solution route:** Put y = m². A nonzero stationary point obeys r + uy + vy² = 0. Equality of free energies requires ry/2 + uy²/4 + vy³/6 = 0. Eliminate r to obtain y = −3u/(4v) and r = 3u²/(16v) &gt; 0. The origin still has positive curvature there, and the order parameter jumps. For u = −4,v = 3 the coexistence values are r = 1,y = 1; direct substitution gives f = 0 at both minima.

### E15. Connect Correlation and Response

For a Hamiltonian H₀ − fA derive the equilibrium static response to f. Relate this to a spatial correlation function for a uniform system.

**Solution route:** Differentiate the normalised Boltzmann average of A with respect to f, assuming A has no explicit f dependence. The derivative is β(⟨A²⟩ − ⟨A⟩²). For A the spatial integral of an order-parameter density, expand its variance as a double integral of the connected correlation. Translational invariance converts susceptibility per volume to β∫C(R)dR. The conjugate field and normalisation determine which factors of volume appear.

### E16. Derive Diffusion from Velocity Memory

An equilibrium Brownian particle has C\_v(t) = (k\_BT/M)e^(−t/τ) for t ≥ 0. Obtain its displacement variance and the short- and long-time limits.

**Solution route:** Write Δx = ∫v(s)ds and use stationarity to reduce the double correlation integral to 2∫₀ᵗ(t − s)C\_v(s)ds. The result is 2D[t − τ(1 − e^(−t/τ))], D = k\_BTτ/M = k\_BT/ζ. Expansion at small t gives (k\_BT/M)t², the ballistic regime. At large t, the leading term is 2Dt. The exact expression approaches this line with a constant offset; replacing it by 2Dt at all times loses inertia.

### E17. Fix the Noise Strength

For Mv̇ = −ζv + η with ⟨η(t)η(t′)⟩ = A\_ηδ(t − t′), determine A\_η from equilibrium and obtain the zero-frequency mobility.

**Solution route:** Integrate the decaying Green function against the noise. Its stationary velocity variance is A\_η/(2Mζ). Equipartition requires k\_BT/M, hence A\_η = 2ζk\_BT. A constant weak force gives terminal mean velocity F/ζ, so mobility is 1/ζ and D = k\_BT times mobility. For an oscillating force with e^(−iωt) convention, μ(ω) = 1/(ζ − iMω). The two-sided spectral form is S\_v(ω) = 2k\_BT Re μ(ω).

### E18. Verify a Fokker–Planck Equilibrium

For overdamped motion in V(x) = κx²/2, κ &gt; 0, derive the probability current and the normalised zero-current equilibrium. Find its variance.

**Solution route:** Drift A = −κx/ζ gives J = −κxP/ζ − D∂xP. Set J = 0 and use D = k\_BT/ζ to obtain ∂xln P = −κx/(k\_BT). Integrating and normalising gives P\_eq = √[κ/(2πk\_BT)]exp[−κx²/(2k\_BT)] and ⟨x²⟩ = k\_BT/κ. This is a confined equilibrium; for V = 0 on the whole real line a constant stationary solution cannot be normalised.


# Appendix 3: Sources and Further Study

The teaching text, small examples, practice questions and diagrams in this revision are written for this guide. References support syllabus alignment and further study; they are not a claim that a question appeared in a university examination.

| Source | How to use it |
|---|---|
| [MGSU M.Sc. Physics syllabus](https://www.mgsubikaner.ac.in/PDF/68c7df9cd7f02.pdf), Statistical Mechanics PHY6.0-CC-104, printed pages 11–12 | Check the three-unit course scope; confirm the applicable academic-session and examination instructions separately |
| R. K. Pathria and Paul D. Beale, Statistical Mechanics | Develop ensemble methods, ideal quantum gases and fluctuations after the elementary examples |
| F. Reif, Fundamentals of Statistical and Thermal Physics | Revisit probability, thermal contact and the connection between microscopic and thermodynamic reasoning |
| Kerson Huang, Statistical Mechanics | Study density matrices, quantum statistics and interacting systems in a more compact treatment |
| [David Tong, Statistical Physics](https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S1.html), University of Cambridge | Read ensemble derivations, then follow the course chapters on classical and quantum gases and phase transitions |
| [David Tong, Statistical Field Theory](https://www.damtp.cam.ac.uk/user/tong/sft/sfthtml/S1.html), University of Cambridge | Extend Landau theory to correlations, scaling and the limits of mean field |
| [MIT Brownian motion lecture](https://web.mit.edu/8.Math/www/lectures/lec21/index.html) | Compare Langevin and Fokker–Planck descriptions; keep track of the author's noise conventions |
| [MIT 8.334 lecture on dynamics](https://www.mit.edu/~8.334/lectures/lec25.pdf) | Follow the relation among stochastic evolution, equilibration and fluctuation–dissipation |

## Final Readiness Check

Before finishing a topic, answer four questions: What is fluctuating? What is fixed? Which approximation has been made? What measurement would the final equation predict? If those answers are clear, the symbols are serving a physical explanation.
