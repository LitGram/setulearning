Classical Mechanics · Shiwali Sharma

## A Note to the Returning Student

You may remember an equation without remembering why it works. You may understand a scientific idea but find the mathematical notation unfamiliar. Both are normal starting points after a long break from study.

This book begins again where necessary. It explains the background immediately before using it. If your B.Sc. was in Chemistry, the connections to molecular motion, vibration and atomic scattering will help you place the new ideas. These connections are explained rather than assumed.

Classical mechanics asks a simple question: given a system and its surroundings, how will it move? Newton's method answers with forces. Lagrange's method often answers with energies and a convenient choice of coordinates. Hamilton's method describes the same motion using coordinates and momenta. You will learn how these descriptions connect.

The course still requires derivations and substantial problems. Read the explanation first, work through the calculation on paper, and then try the nearby practice question. A correct answer includes the conditions under which an equation is valid.

### How to Use a Topic

Read “In simple words” before the formal statement. When a symbol is unfamiliar, use the notation table below. Work through the first example without rushing. Next, cover the solution and solve it again. Finally, attempt the practice question and explain the physical meaning of your result aloud.

Hindi meanings are memory aids. Continue using the English technical term in your notes and answers. Each unit ends with a glossary and revision material. The practice questions in this book are original model questions, not authenticated previous-year examination questions.

### Course and Examination Context

The coverage follows the MGSU programme brochure applicable to admissions in 2025–26, especially the Classical Mechanics course on PDF pages 9–10. The Semester 1 table lists 20 internal and 80 external marks, while general prose elsewhere in the brochure describes a 100-mark theory examination. Use the current university examination notice and your college instructions to resolve the applicable assessment scheme. The brochure describes three question-paper sections; this book uses short, medium and extended practice answers without inventing a fixed marks distribution.

Source: [MGSU M.Sc. Physics programme brochure](https://www.mgsubikaner.ac.in/PDF/68c7df9cd7f02.pdf). The topics below are the working syllabus map. Prerequisite refreshers are learning support, not additional claims about the syllabus.

| Unit | What you will learn |
|---|---|
| 1 | Particle mechanics, conservation laws, open systems, constraints, generalized coordinates, D'Alembert's principle, Lagrange's equations, gyroscopic and dissipative forces, gauge and Galilean invariance, symmetries, momenta and integrals of motion |
| 2 | Variational principles, Hamiltonian mechanics, principal and characteristic functions, Hamilton–Jacobi theory, canonical transformations and their group property, generating functions and infinitesimal generators, Poisson brackets and theorems, small oscillations and normal coordinates |
| 3 | Rotating frames and inertial forces, terrestrial and astronomical Coriolis applications, two-body central forces, effective potential, circular-orbit stability, orbit closure, Kepler motion, satellites and Rutherford scattering |

## Contents

- [Before Unit 1: Rebuilding the Basics](#bridge)
- [Unit 1: Newtonian and Lagrangian Mechanics](#unit-1)
- [Unit 2: Hamiltonian Formulation and Canonical Methods](#unit-2)
- [Unit 3: Rotating Frames and Central Force Motion](#unit-3)
- [Appendix 1: A Practical Study Route](#appendix-strategy)
- [Appendix 2: Extended Model Questions and Solution Routes](#appendix-pyq)
- [Appendix 3: References and Further Reading](#appendix-references)


## Before Unit 1: Rebuilding the Basics

### Position, Velocity and Acceleration

Position tells us where an object is relative to a chosen origin. In one dimension it is x; in three dimensions it is the vector r = x î + y ĵ + z k̂. A vector has both magnitude and direction. Its three components are the distances measured along three perpendicular axes.

**Displacement (विस्थापन)** is the change in position. **Velocity (वेग)** is the rate at which position changes. **Acceleration (त्वरण)** is the rate at which velocity changes.

> v = dx/dt = ẋ; a = dv/dt = d²x/dt² = ẍ.

A dot means one derivative with respect to time. Two dots mean two derivatives. A derivative measures the local rate of change; it is the slope of a graph at a point. For x = 3t², differentiation gives v = 6t and a = 6. If x is in metres and t in seconds, the coefficient 3 carries units m/s².

**Worked refresher.** Let x(t) = (2 m/s)t + (1 m/s²)t². Then v(t) = 2 m/s + (2 m/s²)t. At t = 3 s, v = 8 m/s. The acceleration is 2 m/s² at every instant. Notice that position, velocity and acceleration have different units.

### Products of Vectors

The dot product A · B = AB cos θ measures how much of one vector lies along another. It is a scalar. Work uses a dot product because only the component of force along the displacement contributes.

The cross product A × B is perpendicular to both vectors, has magnitude AB sin θ, and follows the right-hand rule. Point the fingers of your right hand along A and curl them towards B; your thumb gives A × B. Torque and angular momentum use cross products. Reversing the order changes the sign.

**Quick check.** A force of 5 N acts perpendicular to a displacement of 2 m. Its work is 5 × 2 × cos 90° = 0 J. It can still change the direction of the motion.

### Momentum, Work and Energy

For a particle of constant mass m, momentum is p = mv. **Momentum (संवेग)** is a vector. The net force is dp/dt. For that fixed mass, this becomes F = ma.

Work is energy transferred by a force acting through a displacement:

> W = ∫ F · dr.

An integral adds the contributions from many small pieces. For constant force parallel to a straight displacement, W = Fs. Kinetic energy is T = ½mv². Potential energy V describes the energy associated with configuration, such as V = mgh near Earth's surface or V = ½kx² for a spring.

We use T for kinetic energy and τ for an oscillation period when there could be confusion. Some other books use K for kinetic energy and T for a period. Always read a symbol's definition in context.

### Ordinary and Partial Derivatives

An ordinary derivative follows a function of one independent variable. A partial derivative changes one variable while holding the others fixed.

For f(x,y) = x² + 3xy, ∂f/∂x = 2x + 3y because y is held fixed; ∂f/∂y = 3x because x is held fixed. In Lagrange's method, q and q̇ are treated as independent arguments while taking partial derivatives. Only afterwards do we evaluate them along the actual motion q(t).

For L(x,ẋ) = ½mẋ² − ½kx², this gives ∂L/∂ẋ = mẋ and ∂L/∂x = −kx. The total time derivative of mẋ is mẍ. This distinction is the calculation at the heart of Lagrange's equation.

### The Chain Rule, Product Rule and Integration by Parts

The chain rule follows a dependence through an intermediate quantity. If x = l sin θ(t), then ẋ = l cos θ θ̇. The product rule is d(uv)/dt = u̇v + uv̇. Rearranging its integral gives integration by parts:

> ∫ u v̇ dt = [uv] at the endpoints − ∫ u̇v dt.

You will use this last identity in the action derivation. Do not try to memorise the entire derivation before recognising this one step.

### Differential Equations and Initial Conditions

An equation involving an unknown function and its derivatives is a differential equation. The oscillator equation ẍ + ω²x = 0 has solutions x = A cos ωt + B sin ωt. Two constants appear because the equation is second order. An initial position and initial velocity determine them.

For x(0) = a and ẋ(0) = 0, A = a and B = 0, so x(t) = a cos ωt. The angular frequency ω is in rad/s; frequency f = ω/(2π) is in hertz; period τ = 2π/ω is in seconds.

### A Short Readiness Check

1. Differentiate x = 4t³. **Answer:** ẋ = 12t², ẍ = 24t, with units supplied by the coefficient.
2. Find ∂(xy²)/∂x. **Answer:** y².
3. A 2 kg mass moves at 3 m/s. Find p and T. **Answer:** p has magnitude 6 kg·m/s; T = 9 J.
4. Can an accelerating object have constant speed? **Answer:** Yes. In uniform circular motion, the velocity direction changes while its magnitude stays fixed.
5. For a spring, differentiate V = ½kx² and find F. **Answer:** dV/dx = kx, so F = −kx.

If one answer was difficult, return to the matching refresher. You can now begin the mechanics without first relearning an entire B.Sc. course.

---

# Unit 1: Newtonian and Lagrangian Mechanics


## भाग 1: Start Here

The first task is to describe the system. Decide which objects belong to it, which forces come from outside it, and which coordinates are independent. Many apparent difficulties disappear after these choices are made.

By the end of the unit, you should be able to move from a physical setup to its energies, form a Lagrangian, derive its equation of motion, and identify conserved quantities. You will also learn why variable-mass systems need a momentum-flow calculation.

## भाग 2: Build the Ideas

### 1.1 Newtonian Mechanics of One and Many Particles

**In simple words:** A many-particle system has both an overall motion and motion within it. A molecule can move through a gas while its atoms vibrate relative to each other. The centre of mass separates these two descriptions.

For a particle of fixed mass, F = dp/dt = ma. For N particles of constant individual masses, define total mass M, centre-of-mass position R and total momentum P:

> M = Σᵢmᵢ; R = (Σᵢmᵢrᵢ)/M; P = Σᵢmᵢvᵢ = M Ṙ.

The summation symbol Σ means “add over all particles”. For two particles, Σᵢmᵢrᵢ means m₁r₁ + m₂r₂. Differentiate R twice, sum the particle equations, and pair the internal forces. If the internal forces obey the action–reaction law, their sum vanishes:

> M R̈ = F\_external.

This equation describes the centre of mass, not every particle separately. Internal spring forces can change the separation of particles even when R moves uniformly.

**Worked example.** Two blocks of masses 2 kg and 3 kg are connected by a spring on a smooth horizontal floor. A horizontal 10 N force acts on one block. The total mass is 5 kg, so R̈ = 10/5 = 2 m/s². We do not need the spring extension to find this overall acceleration. We would need it to find the instantaneous acceleration of either block separately.

**Energy split.** Write rᵢ = R + ρᵢ, where ρᵢ locates particle i relative to the centre of mass. Since Σᵢmᵢρᵢ = 0, its time derivative is also zero. On expanding the squares in the kinetic energy, the mixed term disappears:

> T = ½M Ṙ² + ½Σᵢmᵢρ̇ᵢ².

The first term is translational kinetic energy of the system as a whole. The second is kinetic energy relative to its centre of mass.

**Try it.** Two particles of masses 1 kg and 3 kg lie at x = 0 and x = 4 m. Find R. **Answer:** R = (1 × 0 + 3 × 4)/4 = 3 m, closer to the heavier particle.

### 1.2 Conservation Laws

**In simple words:** A conserved quantity stays constant during the motion. It need not be zero. A freely moving molecule has a constant nonzero momentum.

For a closed particle system with cancelling internal forces, Ṗ = F\_external. Thus zero net external force implies conservation of total momentum. The internal forces can still redistribute momentum among the particles.

Angular momentum about a fixed origin is J = Σᵢ rᵢ × pᵢ. Differentiate r × p. The term v × mv vanishes because a vector crossed with itself is zero. What remains is torque, τ = r × F. If the internal forces are equal, opposite and directed along the particle separation, their internal torques cancel. Therefore J̇ = τ\_external. Zero external torque conserves J.

Use J for angular momentum in this book so that L can denote the Lagrangian. In orbit formulas, ℓ denotes the magnitude of the relative angular momentum.

For fixed masses, Ṫ = ΣᵢFᵢ · vᵢ. If forces follow a velocity-independent potential V(rᵢ,t), substitution gives:

> d(T + V)/dt = ∂V/∂t.

Consequently, a time-independent conservative potential gives constant mechanical energy E = T + V. A potential that explicitly changes with time can supply or remove energy. “The force has a potential” alone is not sufficient for mechanical-energy conservation.

**Worked example.** Two particles initially have momenta +6 and −2 kg·m/s along x. With no external force, their total momentum remains +4 kg·m/s after a collision. Their individual final momenta need not equal their initial values. If they stick together, kinetic energy generally decreases even though momentum is conserved.

**Check your understanding.** Does zero net force imply zero torque about every origin? For a system, a pair of equal opposite forces can have zero resultant force and nonzero torque. The two conservation conditions must be checked separately.

### 1.3 Work, Energy and Conservative Forces

**In simple words:** Work records energy transferred along a displacement. A conservative force allows that transfer to be described by a potential-energy difference.

Start with m v̇ = F. Take its dot product with v. Since d(v²)/dt = 2v · v̇, the left side becomes d(½mv²)/dt. Integrating in time and using dr = v dt gives the work–energy theorem:

> T₂ − T₁ = ∫₁² F · dr.

This theorem also works when friction acts. Friction changes the value of the work; it does not invalidate the theorem.

For a conservative, position-dependent force, F = −∇V. The gradient ∇V lists the spatial rates of change of V; in one dimension the equation is simply Fₓ = −dV/dx. The minus sign means the force points towards decreasing potential energy. Work becomes V₁ − V₂. A closed journey then has zero work from that force. In a simply connected region, a sufficiently smooth force field with ∇ × F = 0 admits such a potential.

Gravity near Earth's surface has V = mgh. A Hooke-law spring has V = ½kx². Dry friction cannot be represented by a single position-only potential. A magnetic Lorentz force does no work because q(v × B) · v = 0, but it is velocity dependent and is not generally described by a scalar position-only potential.

**Worked example.** A block starts from rest and slides down a smooth track through a vertical height of 5 m. Then ½mv² = mgh, so v = √(2gh) = √98 = 9.90 m/s for g = 9.8 m/s². The track shape does not enter because its normal reaction does no work. With friction, its work would have to be included.

**Try it.** For V = 3x² in SI units, find F at x = 2 m. **Answer:** F = −6x = −12 N, towards decreasing x.

### 1.4 Open Systems and Rocket Motion

**In simple words:** A rocket changes its own momentum by sending momentum out with its exhaust. A raindrop changes its momentum by collecting material. Both require us to count momentum crossing the system boundary.

The equation F\_external = dP/dt applies directly to a fixed collection of matter. The rocket alone is an open system. Substituting its changing mass into F = d(Mv)/dt while ignoring the exhaust gives an incorrect equation.

Take positive x in the rocket's direction. At time t the rocket has mass M and speed v. During dt it ejects mass dm &gt; 0 backwards at speed u relative to the rocket. To first order, the exhaust's inertial velocity is v − u. The initial momentum of rocket plus soon-to-be exhaust is Mv. The final momentum is:

> (M − dm)(v + dv) + dm(v − u) = Mv + M dv − u dm,

where dm dv is second order and is dropped. Equating the change to the external impulse gives M dv − u dm = F\_external dt. Since dM = −dm:

> M dv/dt = F\_external − u dM/dt.

The thrust is −u dM/dt, positive when mass leaves backwards. If external force is negligible and u is constant, integrate dv = −u dM/M:

> v − v₀ = u ln(M₀/M).

Here ln is the natural logarithm. The mass ratio is dimensionless. In vertical ascent with constant downward g and no drag, the same assumptions give v − v₀ = u ln(M₀/M) − gt.

**Worked example.** If M₀/M = e and u = 2000 m/s in force-free space, the speed gain is 2000 ln e = 2000 m/s. Burning 50 kg/s with the same exhaust speed gives thrust 2000 × 50 = 100,000 N.

For accretion at incoming inertial velocity w, the momentum balance is Mv̇ = F\_external + (w − v)Ṁ. A falling drop collecting stationary material has Mv̇ = Mg − vṀ when downward is positive. A cart leaking material with no relative horizontal ejection has w = v and no horizontal thrust from the leak.

**Try it.** A rocket has u = 1000 m/s and mass ratio 2 in force-free space. **Answer:** Δv = 1000 ln 2 = 693 m/s.

### 1.5 Constraints and Degrees of Freedom

**In simple words:** A constraint restricts which positions or velocities are possible. A pendulum bob cannot choose its distance from the pivot independently of its angle.

| Classification | Meaning | Example |
|---|---|---|
| Holonomic | Expressible as independent coordinate equations f(q,t) = 0 | A bob at fixed distance l from a pivot |
| Non-holonomic | Not reducible to such coordinate equations; may involve a nonintegrable velocity restriction or an inequality | A wheel rolling on a plane with a freely changing heading |
| Scleronomic | No explicit time dependence in the constraint | A fixed wire |
| Rheonomic | Explicit time dependence in the constraint | A wire whose position is prescribed as a function of time |
| Ideal | Constraint forces do zero total virtual work for allowed virtual displacements | A smooth contact or an ideal inextensible string |

These classifications answer different questions. A moving smooth wire can have a holonomic, rheonomic and ideal constraint. Ideal does not necessarily mean that the constraint does no actual work: a moving support can transfer energy.

For N point particles in three dimensions with k independent holonomic constraints, the local number of configuration degrees of freedom is n = 3N − k. Count independent restrictions rather than every equation one can write.

**Worked example: the pendulum.** A bob free in 3D needs three coordinates. Fixed string length supplies one constraint, leaving two angles for a spherical pendulum. A planar pendulum has the additional restriction that it stays in a vertical plane, leaving one angle. The length condition alone does not reduce a 3D bob to one degree of freedom.

For a planar double pendulum, two particles start with six coordinates. Two plane restrictions and two rod-length restrictions leave two independent angles. A generic rigid body has six configuration degrees of freedom: three for position and three for orientation. A linear molecule treated as point masses has only two independent orientation angles because rotation about its own line does not change that configuration.

**Try it.** A particle moves on the surface of a sphere. **Answer:** Two degrees of freedom: the two angles specifying its surface position.

### 1.6 Generalized Coordinates and Momenta

![The pendulum uses one angle. Radial tension and tangent virtual displacement are perpendicular.](images/classical/pendulum.png)

**In simple words:** A generalized coordinate is a convenient independent label for configuration. It may be an angle or a distance. Choosing it well makes the constraints automatic.

For a planar pendulum choose q = θ, measured from the downward vertical. Set x = l sin θ and y = −l cos θ. Every value of θ automatically satisfies x² + y² = l². Differentiate using the chain rule:

> ẋ = l cos θ θ̇; ẏ = l sin θ θ̇; v² = ẋ² + ẏ² = l²θ̇².

Thus T = ½ml²θ̇². This is the reason an angle coordinate introduces l² into the kinetic energy. It is not an extra formula to memorise.

For several coordinates, write rᵢ = rᵢ(q₁,…,qₙ,t). The generalized velocities are q̇ⱼ. Their units depend on the coordinates: if q is an angle, q̇ is angular velocity.

Define the generalized forces by virtual work:

> δW = ΣᵢFᵢ · δrᵢ = ΣⱼQⱼδqⱼ; Qⱼ = ΣᵢFᵢ · (∂rᵢ/∂qⱼ).

An angular coordinate has a torque-like generalized force. A translational coordinate has a force-like one. The conjugate momentum is pⱼ = ∂L/∂q̇ⱼ. It need not be an ordinary linear momentum: for the pendulum it is ml²θ̇, an angular momentum.

**Try it.** A tangential force F acts at radius l on a planar pendulum. **Answer:** δW = F(l δθ), so Qθ = Fl. Its units are N·m.

### 1.7 Virtual Work and D'Alembert's Principle

**In simple words:** Imagine changing the configuration slightly while freezing the time. Ask which forces contribute work in that imagined change. Ideal constraint forces drop out of this calculation.

A virtual displacement δr is an infinitesimal change compatible with the constraints at a fixed instant, δt = 0. It differs from the actual displacement dr during dt. For a moving constraint, that distinction matters.

For a planar pendulum, δr is tangent to the circle. Tension is radial. Their dot product is zero, so tension does no virtual work. For two blocks joined by an ideal string, the total virtual work of the tension forces cancels when the allowed block displacements are used.

Newton's equation can be rearranged as Fᵢ − ṗᵢ = 0. Multiply by δrᵢ, sum, and remove ideal constraint contributions:

> Σᵢ(Fᵢ\_applied − ṗᵢ) · δrᵢ = 0.

This is D'Alembert's principle. The subtraction is a mathematical rearrangement. It does not say the moving system is physically at rest. It permits the same virtual-work reasoning used in equilibrium to be applied to dynamics.

**Worked example.** For a pendulum at angle θ, the applied tangential force is −mg sin θ. The tangential inertial term is mlθ̈. The virtual displacement along the arc is l δθ. Therefore (−mg sin θ − mlθ̈)l δθ = 0. Since δθ is arbitrary, θ̈ + (g/l)sin θ = 0.

**Try it.** Why was tension absent? **Answer:** Its direction is perpendicular to the allowed virtual displacement; its value need not be found first.

### 1.8 Deriving Lagrange's Equations

**In simple words:** We will express D'Alembert's equation using only independent coordinates. Each independent virtual change must then have a zero coefficient.

Assume fixed particle masses, differentiable holonomic coordinates and ideal constraints. At fixed time:

> δrᵢ = Σⱼ(∂rᵢ/∂qⱼ)δqⱼ.

The applied-force contribution becomes ΣⱼQⱼδqⱼ. To convert the inertial contribution, first write the velocity as vᵢ = Σₖ(∂rᵢ/∂qₖ)q̇ₖ + ∂rᵢ/∂t. This gives the identity ∂vᵢ/∂q̇ⱼ = ∂rᵢ/∂qⱼ. For T = ½Σᵢmᵢvᵢ²:

> ∂T/∂q̇ⱼ = Σᵢmᵢvᵢ · (∂rᵢ/∂qⱼ).

Take the total time derivative using the product rule:

> d/dt(∂T/∂q̇ⱼ) = Σᵢmᵢv̇ᵢ · (∂rᵢ/∂qⱼ) + Σᵢmᵢvᵢ · d/dt(∂rᵢ/∂qⱼ).

The final derivative equals ∂vᵢ/∂qⱼ, where q̇ is held fixed. Hence the final sum equals ∂T/∂qⱼ. Rearranging:

> Σᵢmᵢv̇ᵢ · (∂rᵢ/∂qⱼ) = d/dt(∂T/∂q̇ⱼ) − ∂T/∂qⱼ.

Substitution into D'Alembert's principle gives a sum of these expressions multiplied by the independent δqⱼ. Each coefficient must vanish:

> d/dt(∂T/∂q̇ⱼ) − ∂T/∂qⱼ = Qⱼ.

If the forces have a velocity-independent potential V(q,t), Qⱼ = −∂V/∂qⱼ. Define the **Lagrangian** L = T − V. Since ∂V/∂q̇ⱼ = 0, we obtain:

> d/dt(∂L/∂q̇ⱼ) − ∂L/∂qⱼ = 0, for j = 1,…,n.

If additional nonconservative generalized forces act, put Qⱼ\_nonconservative on the right. For a regular Lagrangian there are n second-order equations. Initial coordinates and velocities determine a trajectory.

**A first application.** For L = ½mẋ² − ½kx², the two needed derivatives are mẋ and −kx. The equation becomes mẍ + kx = 0. Its sign gives a restoring acceleration towards x = 0, as expected.

### 1.9 Applications: From Energies to Motion

**In simple words:** Use the same route every time: choose coordinates, find T and V, form L, differentiate, and interpret the equation. Do not start by guessing the final equation.

#### The Planar Pendulum

Choose θ from the downward vertical. We already found T = ½ml²θ̇². Relative to the lowest point, the height is l(1 − cos θ), so V = mgl(1 − cos θ). Then:

> L = ½ml²θ̇² − mgl(1 − cos θ).
> ∂L/∂θ̇ = ml²θ̇; d/dt(∂L/∂θ̇) = ml²θ̈; ∂L/∂θ = −mgl sin θ.
> θ̈ + (g/l)sin θ = 0.

Only after obtaining this exact ideal-pendulum equation should we use sin θ ≈ θ for small angles in radians. The result is θ̈ + (g/l)θ = 0, with ω = √(g/l) and period τ = 2π√(l/g). A 1 m pendulum has τ ≈ 2.01 s for g = 9.8 m/s².

#### The Atwood Machine

Two masses hang over an ideal massless pulley. Choose x positive downwards for m₁. The string makes m₂ rise by the same x, so both have speed magnitude ẋ.

> T = ½(m₁ + m₂)ẋ²; V = (m₂ − m₁)gx.
> L = ½(m₁ + m₂)ẋ² + (m₁ − m₂)gx.
> (m₁ + m₂)ẍ = (m₁ − m₂)g.

For m₁ = 3 kg and m₂ = 2 kg, ẍ = g/5 = 1.96 m/s². The heavier mass moves down. Equal masses give zero acceleration, a useful check. A pulley with rotational inertia would contribute additional kinetic energy.

#### A Block on an Incline

Choose s measured down a smooth incline of angle α. Then T = ½mṡ² and V = −mgs sin α. Lagrange's equation gives ms̈ = mg sin α. For α = 30°, s̈ = 4.9 m/s². The normal reaction is absent because the coordinate already incorporates the ideal constraint.

#### A Charge in an Electromagnetic Field

With charge e\_c, scalar potential φ and vector potential A, use:

> L = ½mv² − e\_cφ + e\_c v · A.

The velocity-dependent term matters. The canonical momentum is p = mv + e\_cA, different from the mechanical momentum mv. Substituting into the Euler–Lagrange equations gives the Lorentz force. The familiar L = T − V with a position-only V does not cover every possible interaction.

**Try it.** Form L for a vertical mass-spring system using x positive downward from the unstretched spring position. **Answer:** L = ½mẋ² − ½kx² + mgx; the equation is mẍ + kx = mg. Its equilibrium is x₀ = mg/k, and the displacement η = x − x₀ obeys mη̈ + kη = 0.

### 1.10 Cyclic Coordinates and Gauge Freedom

**In simple words:** Sometimes a coordinate is absent from the energy expression even though its velocity appears. The corresponding momentum is then constant. This is how a coordinate choice can reveal a conservation law.

If ∂L/∂qⱼ = 0, Lagrange's equation says d(∂L/∂q̇ⱼ)/dt = 0. The coordinate is **cyclic**, and pⱼ = ∂L/∂q̇ⱼ is conserved. “Absent” means no explicit dependence on that coordinate, not that the coordinate never changes.

**Worked example.** For planar central-force motion, L = ½m(ṙ² + r²θ̇²) − V(r). The angle θ is absent, so pθ = mr²θ̇ is constant. The radial coordinate r generally appears and its momentum need not be constant. The conserved angular momentum also tells us r²θ̇ is constant.

Two Lagrangians can give the same dynamics. Let L′ = L + dF(q,t)/dt. Their actions differ by F(q₂,t₂) − F(q₁,t₁). For variations with fixed endpoint configurations and times, this endpoint difference has zero variation. The Euler–Lagrange equations are unchanged.

**A concrete check.** Take L = ½mẋ² − V(x), F = ax²/2 with constant a. Then L′ = L + axẋ. Now ∂L′/∂ẋ = mẋ + ax, whose time derivative is mẍ + aẋ. Also ∂L′/∂x = −V′(x) + aẋ. Subtraction cancels the aẋ terms and leaves mẍ + V′(x) = 0. The canonical momentum changes, but the trajectory does not.

**Try it.** If L is independent of y but contains ẏ, what is conserved? **Answer:** py = ∂L/∂ẏ, not necessarily ẏ itself for an arbitrary Lagrangian.

### 1.11 Symmetry, Galilean Invariance and the Jacobi Integral

**In simple words:** A symmetry is a change in description that leaves the action unchanged, or changes it only by an endpoint term. Continuous symmetries lead to conserved quantities.

Spatial translations lead to linear momentum, rotations to angular momentum, and time translations to energy. State the symmetry conditions of the actual system: an externally fixed spring breaks translation symmetry, and an explicitly driven potential breaks time-translation symmetry.

#### Galilean Invariance

Compare inertial frames moving at constant relative velocity u, with t′ = t and rᵢ′ = rᵢ − ut. Then vᵢ′ = vᵢ − u. For fixed masses interacting through V(|rᵢ − rⱼ|), separations are unchanged. Expanding the kinetic energy gives:

> L′ − L = −u · Σᵢmᵢvᵢ + ½M u² = dF/dt,
> F = −u · Σᵢmᵢrᵢ + ½M u²t.

The expression inside the derivative contains positions and time. Its derivative produces the velocity terms. By the total-derivative property, the equations have the same form in the two inertial frames.

#### The Energy Function

Define h = Σⱼq̇ⱼpⱼ − L. Differentiate it. The q̈ⱼpⱼ terms cancel the corresponding velocity terms in dL/dt; use ṗⱼ = ∂L/∂qⱼ for the remaining coordinate terms. What survives is:

> dh/dt = −∂L/∂t.

Thus h is a constant of motion when L has no explicit time dependence. For T homogeneous quadratic in velocities and a velocity-independent V, Σq̇ⱼpⱼ = 2T, so h = T + V. For other Lagrangians, first use the definition rather than automatically identifying h with mechanical energy.

**Worked example.** For L = ½mẋ² − ½kx², h = ẋ(mẋ) − L = ½mẋ² + ½kx². Differentiating gives ḣ = ẋ(mẍ + kx) = 0 along the oscillator motion.

An **integral of motion** is any function C(q,q̇,t) that remains constant along a trajectory. Momentum and h are examples under the stated conditions. A first integral can reduce the order of a differential equation and simplify solving it.

### 1.12 Gyroscopic and Dissipative Forces

**In simple words:** Some velocity-dependent forces redirect motion without removing energy. Others reduce mechanical energy. Distinguish them by the power they deliver, F · v.

For a magnetic force, e\_c(v × B) · v = 0, so it does no work. Such a perpendicular velocity-dependent force is a gyroscopic example. More generally, Qᵢ = ΣⱼGᵢⱼq̇ⱼ with antisymmetric G has ΣᵢQᵢq̇ᵢ = 0: each pair cancels. A spinning top also shows gyroscopic dynamics, though its rotational description needs additional coordinates.

Viscous drag F = −b v instead has power −bv². For linear viscous forces, introduce the **Rayleigh dissipation function** R = ½bẋ². It has units of power, not energy. With L retaining the conservative part:

> d/dt(∂L/∂q̇ⱼ) − ∂L/∂qⱼ + ∂R/∂q̇ⱼ = 0.

For a damped spring, L = ½mẋ² − ½kx², so mẍ + bẋ + kx = 0. Its mechanical energy obeys Ė = −bẋ² = −2R. R is half the instantaneous rate of energy loss in this quadratic model.

**Worked example.** For b = 0.4 kg/s and ẋ = 3 m/s, drag is −1.2 N, R = ½(0.4)(9) = 1.8 W, and mechanical energy decreases at 3.6 J/s. A larger speed produces a larger loss rate in this model.

**Try it.** Does friction prevent us from using Lagrange's equations? **Answer:** No. Include its generalized force on the right, or use R when the viscous-force form allows it.

## भाग 3: Put the Ideas Together

### A Bead on a Rotating Rod

A bead of mass m slides without friction along a horizontal rod rotating about a fixed vertical axis at prescribed constant angular speed Ω. Let r be distance from the axis. The rod's orientation is θ = Ωt; it is not a second independent coordinate.

Its speed has radial and transverse components, so v² = ṙ² + Ω²r². With no varying gravitational potential, L = ½m(ṙ² + Ω²r²). The derivatives are ∂L/∂ṙ = mṙ and ∂L/∂r = mΩ²r. Thus:

> r̈ − Ω²r = 0.

With r(0) = r₀ and ṙ(0) = 0, the solution is r = r₀ cosh Ωt, where cosh z = (eᶻ + e⁻ᶻ)/2. The bead moves outwards. The energy function h = ½mṙ² − ½mΩ²r² is conserved, but the physical kinetic energy is ½mṙ² + ½mΩ²r² and grows. The motor maintaining the rod's rotation supplies energy through the moving ideal constraint. This example explains why a conserved energy function need not equal T + V in time-dependent coordinate descriptions.

### A Solution-Writing Route

For any Lagrangian application, sketch the setup, state idealisations, choose independent coordinates, write T and V, form L, display the partial derivatives, and simplify the equation. Check its units and one physical limit. For a derivation, identify where the constraints and endpoint conditions enter rather than merely copying algebra.

## भाग 4: Check Your Understanding

### 1.13 Common Mistakes and Their Corrections

- A fixed length removes one degree of freedom in 3D, not two. A planar restriction is a separate condition.
- For a rocket alone, account for momentum carried by exhaust. Replacing m by m(t) in a closed-system formula is insufficient.
- Distinguish zero actual work from zero virtual work. A moving ideal support may transfer energy.
- Conservation of mechanical energy requires the relevant time-independence condition, not just a force-potential relation.
- Generalized momentum can be angular momentum or contain a vector-potential term. It is not always mv.
- L = T − V applies to the stated mechanical class; velocity-dependent interactions require the appropriate Lagrangian.
- A cyclic coordinate need not be constant. Its conjugate momentum is conserved.
- At fixed endpoints, a total derivative changes the action by an endpoint term and leaves the motion equations unchanged.

**Explain without calculating.** Why do two equal Atwood masses have zero acceleration? Their potential-energy changes cancel, so the Lagrangian has no x-dependent driving term. Why can a molecule vibrate while its centre of mass stays at rest? Internal forces change relative motion without changing total momentum.

## भाग 5: Practice Questions with Explanations

#### Question U1-01

For fixed masses, the centre of mass accelerates according to which force?

- **A.** Net external force
- **B.** Largest internal force
- **C.** Sum of force magnitudes
- **D.** Spring tension alone

**Answer: A.** Internal action–reaction pairs cancel in the total momentum equation, leaving the external resultant.

#### Question U1-02

Two masses 1 kg and 3 kg are at x = 0 and 4 m. Where is their centre of mass?

- **A.** 1 m
- **B.** 3 m
- **C.** 2 m
- **D.** 4 m

**Answer: B.** The mass-weighted position is (1 × 0 + 3 × 4)/4 = 3 m.

#### Question U1-03

A closed system has zero external force. What must remain constant?

- **A.** Each particle velocity
- **B.** Total kinetic energy
- **C.** Total linear momentum
- **D.** Every interparticle distance

**Answer: C.** Internal interactions can change individual velocities and kinetic energy while conserving total momentum.

#### Question U1-04

What condition conserves angular momentum about a fixed inertial origin?

- **A.** Zero kinetic energy
- **B.** Constant position
- **C.** Zero potential energy
- **D.** Zero net torque

**Answer: D.** The angular-momentum derivative equals the net torque under the stated particle-system assumptions.

#### Question U1-05

A force is perpendicular to the displacement at every point. Its work is what?

- **A.** Zero
- **B.** Always positive
- **C.** Always negative
- **D.** Equal to its magnitude

**Answer: A.** The work element is F · dr, which vanishes for perpendicular vectors.

#### Question U1-06

Which condition makes T + V constant for a conservative particle system?

- **A.** V is positive
- **B.** V has no explicit time dependence
- **C.** Velocity is zero once
- **D.** Masses are unequal

**Answer: B.** For a velocity-independent potential, d(T + V)/dt = ∂V/∂t.

#### Question U1-07

For V = ½kx², what is the force?

- **A.** +kx
- **B.** −k/x
- **C.** −kx
- **D.** ½kx

**Answer: C.** The force is the negative position derivative of the potential.

#### Question U1-08

A block falls through 5 m on a smooth track from rest. With g = 9.8 m/s², its final speed is approximately what?

- **A.** 4.90 m/s
- **B.** 49 m/s
- **C.** 98 m/s
- **D.** 9.90 m/s

**Answer: D.** Energy conservation gives v = √(2gh) = √98 m/s.

#### Question U1-09

Why can the rocket alone not be treated as a fixed collection of matter?

- **A.** Exhaust crosses its boundary
- **B.** Its speed is large
- **C.** Gravity is absent
- **D.** Its shape is cylindrical

**Answer: A.** The rocket loses mass and momentum through its exhaust, so a momentum-flux term is required.

#### Question U1-10

For backward exhaust speed u &gt; 0 and Ṁ &lt; 0, the forward thrust is what?

- **A.** uṀ
- **B.** −uṀ
- **C.** −Mv
- **D.** u/M

**Answer: B.** The exhaust term is positive forward because −uṀ &gt; 0 during mass loss.

#### Question U1-11

A force-free rocket has mass ratio e² and constant exhaust speed u. Its speed gain is what?

- **A.** u/2
- **B.** u²
- **C.** 2u
- **D.** e²u

**Answer: C.** The rocket equation gives Δv = u ln e² = 2u.

#### Question U1-12

Exhaust speed is 2000 m/s and the burn rate is 50 kg/s. What is thrust?

- **A.** 40 N
- **B.** 4000 N
- **C.** 25,000 N
- **D.** 100,000 N

**Answer: D.** Thrust is exhaust speed times the positive mass-ejection rate.

#### Question U1-13

A cart leaks sand with the cart's horizontal velocity. Without external horizontal force, what happens to its speed?

- **A.** It stays constant
- **B.** It doubles
- **C.** It falls as 1/M
- **D.** It must become zero

**Answer: A.** The departing sand has zero relative horizontal velocity and creates no horizontal thrust.

#### Question U1-14

Which is a holonomic constraint?

- **A.** An arbitrary nonintegrable velocity relation
- **B.** x² + y² + z² = l²
- **C.** An unspecified friction law
- **D.** A force proportional to speed

**Answer: B.** The fixed-distance condition is a coordinate equation.

#### Question U1-15

What does rheonomic mean?

- **A.** Constraint with friction
- **B.** Constraint involving no time
- **C.** Explicitly time-dependent constraint
- **D.** Constraint removing no motion

**Answer: C.** Rheonomic classifies time dependence, independently of holonomicity.

#### Question U1-16

A smooth moving wire may exert what kind of constraint?

- **A.** Necessarily dissipative
- **B.** Necessarily non-holonomic
- **C.** Neither geometric nor time dependent
- **D.** Ideal and rheonomic

**Answer: D.** Smooth contact has zero allowed virtual work, while prescribed wire motion makes the constraint time dependent.

#### Question U1-17

A fixed-length pendulum free to swing in 3D has how many configuration degrees of freedom?

- **A.** Two
- **B.** One
- **C.** Three
- **D.** Zero

**Answer: A.** One length constraint reduces three coordinates to two independent angles.

#### Question U1-18

What extra restriction reduces a spherical pendulum to the usual planar pendulum?

- **A.** A heavier bob
- **B.** Motion confined to a fixed plane
- **C.** A shorter string
- **D.** Zero gravitational potential

**Answer: B.** Planarity supplies another independent geometric restriction.

#### Question U1-19

A planar double pendulum with two movable bobs has how many degrees of freedom?

- **A.** One
- **B.** Four
- **C.** Two
- **D.** Six

**Answer: C.** The two angles remain after imposing planarity and both fixed rod lengths.

#### Question U1-20

A generic rigid body in three-dimensional space has how many configuration degrees of freedom?

- **A.** Three
- **B.** Nine
- **C.** One
- **D.** Six

**Answer: D.** Three variables locate its centre of mass and three specify its orientation.

#### Question U1-21

What is a generalized coordinate?

- **A.** An independent label of configuration
- **B.** Only a Cartesian distance
- **C.** Always a force
- **D.** Always a momentum

**Answer: A.** Angles and distances can both serve if they independently specify the allowed configuration.

#### Question U1-22

For x = l sin θ and y = −l cos θ, the squared bob speed is what?

- **A.** lθ̇²
- **B.** l²θ̇²
- **C.** θ̇²/l²
- **D.** l²θ²

**Answer: B.** The differentiated coordinate squares add using sin²θ + cos²θ = 1.

#### Question U1-23

If θ is the coordinate and a tangential force F acts at radius l, what is Qθ?

- **A.** F/l
- **B.** F
- **C.** Fl
- **D.** Fθ

**Answer: C.** Virtual work is F(lδθ) = Qθδθ, so Qθ is a torque.

#### Question U1-24

What is held fixed during a virtual displacement?

- **A.** Every coordinate
- **B.** Every velocity
- **C.** Potential energy
- **D.** Time

**Answer: D.** A virtual displacement compares nearby allowed configurations at the same instant.

#### Question U1-25

Why does ideal pendulum tension vanish from the virtual-work sum?

- **A.** It is perpendicular to allowed virtual displacement
- **B.** Its magnitude is zero
- **C.** It is not a force
- **D.** The bob has no acceleration

**Answer: A.** Radial tension has zero dot product with the tangent virtual displacement.

#### Question U1-26

Which is D'Alembert's expression for ideal constraints?

- **A.** ΣFᵢ = 0 always
- **B.** Σ(Fᵢ\_applied − ṗᵢ) · δrᵢ = 0
- **C.** Σpᵢ = 0 always
- **D.** ΣFᵢ · rᵢ = T

**Answer: B.** Subtracting the inertial term rewrites Newton's dynamics in virtual-work form.

#### Question U1-27

For a velocity-independent potential and no additional force, the usual Lagrangian is what?

- **A.** T + V
- **B.** V − 2T
- **C.** T − V
- **D.** TV

**Answer: C.** Using Q = −∂V/∂q turns the kinetic-energy form into Euler–Lagrange equations for T − V.

#### Question U1-28

For L = ½mẋ² − ½kx², what is ∂L/∂ẋ?

- **A.** −kx
- **B.** mẍ
- **C.** ½mẋ
- **D.** mẋ

**Answer: D.** The partial derivative treats x and ẋ as independent arguments.

#### Question U1-29

The Euler–Lagrange equation for that spring is which?

- **A.** mẍ + kx = 0
- **B.** mẍ − kx = 0
- **C.** mẋ + kx = 0
- **D.** kẍ + mx = 0

**Answer: A.** The positive spring term on the left produces a restoring acceleration.

#### Question U1-30

The exact ideal planar-pendulum equation is which?

- **A.** θ̈ + (l/g)sin θ = 0
- **B.** θ̈ + (g/l)sin θ = 0
- **C.** θ̇ + (g/l)θ = 0
- **D.** θ̈ − (g/l)sin θ = 0

**Answer: B.** The gravitational generalized force is −mgl sin θ, and the angular inertia is ml².

#### Question U1-31

When is sin θ ≈ θ appropriate?

- **A.** All θ measured in degrees
- **B.** Only θ = π
- **C.** Small θ measured in radians
- **D.** Every circular motion

**Answer: C.** The leading Taylor term uses radians and is accurate for small angles.

#### Question U1-32

For Atwood masses 3 kg and 2 kg, the ideal acceleration magnitude is what?

- **A.** g
- **B.** 5g
- **C.** g/2
- **D.** g/5

**Answer: D.** The mass difference is 1 kg and their sum is 5 kg, giving a = g/5.

#### Question U1-33

What would a massive pulley add to the energy calculation?

- **A.** Rotational kinetic energy
- **B.** An arbitrary constant force
- **C.** No energy term
- **D.** Only gravitational energy of the string

**Answer: A.** The pulley rotates, so its inertia contributes ½Iω².

#### Question U1-34

If q is cyclic, what is conserved?

- **A.** q itself
- **B.** ∂L/∂q̇
- **C.** q̇ for every L
- **D.** ∂L/∂t

**Answer: B.** The Euler–Lagrange equation makes the conjugate momentum time independent.

#### Question U1-35

For planar central motion, the momentum conjugate to θ is what?

- **A.** mṙ
- **B.** mrθ
- **C.** mr²θ̇
- **D.** mθ̇²

**Answer: C.** Differentiating ½mr²θ̇² with respect to θ̇ gives the angular momentum.

#### Question U1-36

Adding dF(q,t)/dt to L does what to the equations at fixed endpoints?

- **A.** Reverses all forces
- **B.** Removes kinetic energy
- **C.** Always removes the potential
- **D.** Leaves them unchanged

**Answer: D.** The action changes by an endpoint term with zero allowed variation.

#### Question U1-37

Under vᵢ′ = vᵢ − u, what is the kinetic Lagrangian difference?

- **A.** −u · Σmᵢvᵢ + ½Mu²
- **B.** +u · Σmᵢvᵢ
- **C.** Mu
- **D.** −½Mu² only

**Answer: A.** Expand each squared shifted velocity to obtain the cross term and the constant-speed term.

#### Question U1-38

Which function has the required total derivative for that Galilean change?

- **A.** −u · Σmᵢvᵢ
- **B.** −u · Σmᵢrᵢ + ½Mu²t
- **C.** ½Mu²
- **D.** M r²

**Answer: B.** Its time derivative reproduces both terms in L′ − L for constant u and masses.

#### Question U1-39

The energy function h is defined as what?

- **A.** Σqⱼpⱼ + L
- **B.** T − 2V
- **C.** Σq̇ⱼpⱼ − L
- **D.** L/2

**Answer: C.** The definition combines each generalized velocity with its conjugate momentum.

#### Question U1-40

Along Euler–Lagrange motion, ḣ equals what?

- **A.** +∂L/∂t
- **B.** Always zero
- **C.** Always T
- **D.** −∂L/∂t

**Answer: D.** The coordinate and velocity terms cancel, leaving the negative explicit time derivative.

#### Question U1-41

For an ordinary autonomous spring Lagrangian, h equals what?

- **A.** T + V
- **B.** T − V
- **C.** V alone
- **D.** Zero

**Answer: A.** Quadratic kinetic energy and velocity-independent potential make h the mechanical energy.

#### Question U1-42

For viscous force −bẋ, the Rayleigh function is what?

- **A.** bẋ
- **B.** ½bẋ²
- **C.** ½bx²
- **D.** −½mẋ²

**Answer: B.** Its velocity derivative gives bẋ, the damping term placed on the left of Lagrange's equation.

#### Question U1-43

What are the units of a Rayleigh dissipation function?

- **A.** Energy
- **B.** Momentum
- **C.** Power
- **D.** Length

**Answer: C.** For linear drag, 2R is the instantaneous mechanical-energy loss rate.

#### Question U1-44

A magnetic Lorentz force does no work because of which fact?

- **A.** It is independent of charge
- **B.** It is always zero
- **C.** It is parallel to displacement
- **D.** It is perpendicular to velocity

**Answer: D.** The scalar triple product (v × B) · v vanishes.

#### Question U1-45

Why can a bead on a motor-driven rotating rod gain kinetic energy despite ideal contact?

- **A.** The moving constraint can supply actual work
- **B.** Ideal constraints always conserve T
- **C.** Its mass must increase
- **D.** Gravity must do work

**Answer: A.** Zero virtual work at fixed time does not imply zero actual work from a moving support.


## भाग 6: Quick Revision and Terminology

### 6.1 Sixty Revision Points

1. Choose a system boundary before classifying forces as internal or external.
2. A particle approximation ignores size only for the motion being studied.
3. For a fixed-mass particle, p = mv and F = dp/dt = ma.
4. Position, velocity and acceleration have different dimensions.
5. The centre of mass is a mass-weighted average position.
6. For fixed masses, P = M Ṙ.
7. Cancelling internal forces leave M R̈ = F\_external.
8. Centre-of-mass motion does not determine every internal motion.
9. Kinetic energy separates into centre-of-mass translation and relative motion.
10. Zero net external force conserves total momentum.
11. Total momentum may be conserved while individual momenta change.
12. Angular momentum about a fixed origin is r × p.
13. Torque about that origin is r × F.
14. Central internal action–reaction pairs have cancelling internal torques.
15. Zero net external torque conserves total angular momentum.
16. Work is the path integral of F · dr.
17. Only the force component along a displacement contributes work.
18. The work–energy theorem is valid even for nonconservative forces.
19. A position-only conservative force satisfies F = −∇V.
20. Conservative-force work depends only on endpoints.
21. A closed path has zero work from a conservative force.
22. A time-dependent potential can change mechanical energy.
23. For the stated conservative class, d(T + V)/dt = ∂V/∂t.
24. Potential energy can be shifted by an arbitrary constant.
25. The spring potential ½kx² gives force −kx.
26. The rocket alone is an open system.
27. Momentum carried across the boundary must appear in open-system dynamics.
28. Backward exhaust gives forward thrust −uṀ when Ṁ &lt; 0.
29. The ideal rocket equation requires constant relative exhaust speed.
30. In force-free motion, Δv = u ln(M₀/M).
31. The logarithm takes a dimensionless mass ratio.
32. Vertical gravity adds −gt to the ideal constant-g rocket speed gain.
33. Accreted mass enters with its own inertial velocity.
34. Leakage with no relative horizontal ejection gives no horizontal thrust.
35. A holonomic constraint is reducible to coordinate equations.
36. Scleronomic and rheonomic describe explicit time dependence.
37. Ideal constraint forces have zero total allowed virtual work.
38. A moving ideal constraint may do actual work.
39. Count independent constraints rather than redundant equations.
40. For k independent holonomic constraints, n = 3N − k in 3D.
41. A spherical pendulum has two configuration degrees of freedom.
42. A planar pendulum has one configuration degree of freedom.
43. A planar double pendulum has two independent angles.
44. A generic spatial rigid body has three position and three orientation variables.
45. Generalized coordinates automatically incorporate chosen holonomic constraints.
46. An angular generalized force has torque units.
47. Virtual displacement is an allowed configuration change at fixed time.
48. The actual displacement includes the evolution of the constraint in time.
49. D'Alembert's principle uses applied forces minus momentum derivatives.
50. For a velocity-independent potential, the standard Lagrangian is T − V.
51. Treat q and q̇ as independent arguments during partial differentiation.
52. Generalized momentum is pⱼ = ∂L/∂q̇ⱼ.
53. A cyclic coordinate has conserved conjugate momentum.
54. Generalized momentum need not equal ordinary mechanical momentum.
55. Adding a coordinate-time total derivative to L leaves fixed-endpoint dynamics unchanged.
56. Galilean boosts change the free-particle kinetic Lagrangian by a total derivative.
57. The energy function is h = Σq̇ⱼpⱼ − L.
58. Along Euler–Lagrange motion, ḣ = −∂L/∂t.
59. For a quadratic Rayleigh function, mechanical-energy loss rate is 2R without other input.
60. Gyroscopic perpendicular forces redirect motion while supplying zero instantaneous power.

### 6.2 Hindi-Supported Glossary

| English term | Hindi aid | Meaning in this unit |
|---|---|---|
| Displacement | विस्थापन | Change in position |
| Momentum | संवेग | Mass times velocity for a fixed-mass particle |
| Angular momentum | कोणीय संवेग | Moment of momentum about an origin |
| Torque | बल आघूर्ण | Turning effect, r × F |
| Centre of mass | द्रव्यमान केंद्र | Mass-weighted average position |
| Constraint | बंधन | Restriction on allowed configuration or motion |
| Degree of freedom | स्वतंत्रता की कोटि | One independent configuration variable |
| Generalized coordinate | सामान्यीकृत निर्देशांक | Convenient independent configuration label |
| Virtual displacement | आभासी विस्थापन | Allowed imagined change at fixed time |
| Lagrangian | लाग्रांजियन | Function used in the Euler–Lagrange equations |
| Conjugate momentum | संयुग्मी संवेग | Derivative of L with respect to a generalized velocity |
| Cyclic coordinate | चक्रीय निर्देशांक | Coordinate absent explicitly from L |
| Conservation | संरक्षण | Constancy during the motion |
| Symmetry | सममिति | Transformation preserving the action up to an endpoint term |
| Dissipation | क्षय | Loss of mechanical energy into other forms |
| Integral of motion | गति का संरक्षित फलन | Function constant along a trajectory |

### 6.3 Formula Sheet with Conditions

| Result | Conditions to remember |
|---|---|
| M R̈ = F\_external | Fixed total mass; cancelling internal forces |
| E = T + V is constant | Time-independent conservative system |
| Mv̇ = F\_external − uṀ | Exhaust speed u measured backwards relative to rocket |
| Δv = u ln(M₀/M) | Constant u, negligible external force |
| n = 3N − k | k independent holonomic constraints in 3D |
| d/dt(∂L/∂q̇ⱼ) − ∂L/∂qⱼ = Qⱼ\_nonconservative | Appropriate coordinates and ideal constraint treatment |
| pⱼ = ∂L/∂q̇ⱼ | Definition of conjugate momentum |
| h = Σq̇ⱼpⱼ − L; ḣ = −∂L/∂t | Along unforced Euler–Lagrange motion |
| Ė = −2R | Quadratic Rayleigh dissipation with no other energy input |

---

# Unit 2: Hamiltonian Formulation and Canonical Methods


## भाग 1: Start Here

Unit 1 described motion using q and q̇. This unit introduces two further viewpoints: comparing possible paths through the action, and following a point in the space of q and p. The motion is the same; the questions become easier in different descriptions.

Before continuing, check that you can differentiate L = ½mẋ² − ½kx² with respect to x and ẋ. You also need the product rule and integration by parts from the opening refresher. Matrices enter only when we study several oscillators; a small example will explain what they do.

### A Short Matrix Refresher

A matrix is a rectangular array of numbers. It packages several equations without changing their meaning. For example, a matrix with first row (2, −1) and second row (−1, 2), acting on a column (a₁,a₂), produces the column (2a₁ − a₂, −a₁ + 2a₂). Each output comes from multiplying one row by the input column and adding.

For a two-by-two matrix with rows (a,b) and (c,d), its determinant is ad − bc. A homogeneous equation Aa = 0 can have a nonzero vector a only when det A = 0. Otherwise the only solution is a = 0. This fact explains the frequency equation for coupled oscillators later.

An eigenvector is a direction a that the matrix only stretches or reverses: Aa = λa. The number λ is its eigenvalue. A transpose, written Aᵀ, exchanges rows and columns. If a is a column, aᵀ is a row. Thus aᵀMb is one number obtained by matrix multiplication. With M diagonal, it is Σᵢmᵢaᵢbᵢ, an ordinary dot product weighted by masses. Revise Mathematical Physics for more examples; these are the specific matrix ideas used here.

## भाग 2: Build the Ideas

### 2.1 Calculus of Variations

**In simple words:** Ordinary calculus changes a number to find an extreme value. Variational calculus changes an entire function, such as the path of a particle.

A **functional** assigns a number to a function. For example, I[y] = ∫ f(x,y,y′) dx assigns a number to the curve y(x). The brackets remind us that the input is a whole function. Let a nearby curve be yε(x) = y(x) + εη(x), where ε is a small number and η is an arbitrary smooth change that vanishes at the endpoints.

The first-order change is:

> δI = ε∫[(∂f/∂y)η + (∂f/∂y′)η′] dx.

The second term contains η′. Integrate it by parts. The endpoint term [(∂f/∂y′)η] vanishes because η is zero there. Therefore:

> δI = ε∫[∂f/∂y − d/dx(∂f/∂y′)]η dx.

For this to vanish for every allowed η, the bracket must vanish at each interior point:

> ∂f/∂y − d/dx(∂f/∂y′) = 0.

This is the Euler–Lagrange equation of the calculus of variations. Stationary means the first-order change is zero; a minimum is one possible stationary case.

**Worked example: shortest curve in a plane.** Its length is I = ∫√(1 + y′²) dx. Since f does not contain y explicitly, ∂f/∂y′ = y′/√(1 + y′²) is constant. Hence y′ is constant, giving y = ax + b, a straight line. The endpoints determine a and b.

**Try it.** For f = ½y′², derive the equation. **Answer:** ∂f/∂y = 0 and ∂f/∂y′ = y′, so y″ = 0.

### 2.2 Hamilton's Principle and Stationary Action

**In simple words:** The action compares possible time histories between fixed endpoint configurations. The physical path has no first-order action change under a small allowed deformation.

Define action S = ∫ from t₁ to t₂ L(q,q̇,t) dt. It has units J·s. Hamilton's principle is δS = 0 with δq(t₁) = δq(t₂) = 0 and fixed endpoint times. It applies here to the conservative Lagrangian description established in Unit 1; dissipative forces require an extended treatment rather than inserting friction into an ordinary potential.

For one coordinate, vary the action:

> δS = ∫[(∂L/∂q)δq + (∂L/∂q̇)δq̇] dt.

Since δq̇ = d(δq)/dt, integration by parts gives:

> δS = [(∂L/∂q̇)δq] at endpoints + ∫[∂L/∂q − d/dt(∂L/∂q̇)]δq dt.

The endpoint term is zero. The arbitrariness of the interior δq yields Lagrange's equation. Repeat for every independent coordinate in a system with several degrees of freedom.

The phrase “least action” is traditional. The required property is stationarity, not an unconditional minimum. Another related principle, Maupertuis' principle, uses the abbreviated action ∫p · dq at fixed energy for suitable autonomous conservative systems. It has different constraints on the varied paths. Do not replace Hamilton's fixed-time action by it without stating the change.

**Worked example.** With L = ½mẋ², stationarity yields mẍ = 0. The path joining x₁ at t₁ to x₂ at t₂ is x(t) = x₁ + (x₂ − x₁)(t − t₁)/(t₂ − t₁), motion at constant velocity.

**Check your understanding.** Why must δq vanish only at the endpoints? The endpoint positions are fixed while the interior path is varied. Requiring δq = 0 everywhere would leave no variation to test.

### 2.3 Constructing the Hamiltonian

**In simple words:** Replace each velocity by its conjugate momentum. The Hamiltonian then tells us how the coordinates and momenta change together.

First define pⱼ = ∂L/∂q̇ⱼ. If these equations can be solved locally for all velocities, the Lagrangian is regular. Equivalently, the velocity Hessian matrix ∂²L/(∂q̇ᵢ∂q̇ⱼ) has nonzero determinant. This book uses regular mechanical examples. Define:

> H(q,p,t) = Σⱼpⱼq̇ⱼ − L(q,q̇,t), with all q̇ expressed in q,p,t.

This change of variables is a Legendre transformation. Leaving an uneliminated velocity in H defeats its purpose.

Take the total differential. Substituting pⱼ = ∂L/∂q̇ⱼ cancels the dq̇ⱼ terms:

> dH = Σⱼq̇ⱼ dpⱼ − Σⱼ(∂L/∂qⱼ)dqⱼ − (∂L/∂t)dt.

Along Euler–Lagrange motion, ∂L/∂qⱼ = ṗⱼ. Compare with the differential of H as a function of q,p,t. Matching coefficients gives Hamilton's equations:

> q̇ⱼ = ∂H/∂pⱼ; ṗⱼ = −∂H/∂qⱼ; ∂H/∂t = −∂L/∂t.

There are 2n first-order equations, equivalent to the n second-order Lagrange equations. Along the motion dH/dt = ∂H/∂t because the coordinate and momentum terms cancel. Thus an autonomous H is conserved.

**Worked example: the oscillator.** L = ½mẋ² − ½kx² gives p = mẋ, hence ẋ = p/m. Substitute before differentiating:

> H = p(p/m) − [½m(p/m)² − ½kx²] = p²/(2m) + ½kx².

Hamilton's equations give ẋ = p/m and ṗ = −kx. Differentiate the first and substitute the second to recover mẍ + kx = 0.

For a charge e\_c in electromagnetic potentials, p = mv + e\_cA and H = (p − e\_cA)²/(2m) + e\_cφ. This example illustrates why canonical momentum and mechanical momentum must be distinguished.

**Try it.** A free particle has L = ½mẋ². **Answer:** H = p²/(2m), ẋ = p/m, ṗ = 0.

### 2.4 Phase Space and Phase Trajectories

![A harmonic oscillator follows an ellipse in position–momentum space; the arrows show its direction.](images/classical/phase_ellipse.png)

**In simple words:** A position alone does not tell us what happens next. A pendulum at the bottom may be moving left or right. Adding momentum specifies the instantaneous mechanical state.

For n degrees of freedom, phase space has 2n coordinates (q₁,…,qₙ,p₁,…,pₙ). One point is one state. As time passes, the state traces a phase trajectory. Configuration space contains only the n coordinates.

For the oscillator at fixed energy E &gt; 0:

> p²/(2m) + ½kq² = E,
> q²/(2E/k) + p²/(2mE) = 1.

This is an ellipse. Its q-intercepts are ±√(2E/k), and its p-intercepts are ±√(2mE). At the rightmost point, q &gt; 0 and p = 0. Hamilton's equation gives ṗ = −kq &lt; 0, so motion on a plot with q horizontal and p vertical proceeds clockwise.

**Reading the diagram in words:** At maximum right displacement the oscillator momentarily stops; it gains leftward momentum as it approaches the origin; at q = 0 all its energy is kinetic; at maximum left displacement it stops and reverses. The point E = 0 is the equilibrium at the origin.

**Worked example.** Take m = 1 kg, k = 4 N/m and E = 2 J. Then q\_max = 1 m, p\_max = 2 kg·m/s and ω = 2 rad/s. The period is π s. At q = 0.6 m, the potential is 0.72 J, leaving 1.28 J kinetic energy. Thus p = ±1.6 kg·m/s: the sign distinguishes the two directions of travel.

**Try it.** Can two trajectories of the same smooth autonomous Hamiltonian cross at one ordinary phase point with different velocities? **Answer:** No, where the equations have a unique solution. The point fixes the derivatives.

### 2.5 Canonical Transformations

**In simple words:** A useful change of variables should preserve the structure of Hamilton's equations. A transformation with that property is canonical.

Let the old variables be q,p and the new variables Q,P. For smooth locally invertible transformations, the canonical conditions are:

> {Qᵢ,Qⱼ} = 0; {Pᵢ,Pⱼ} = 0; {Qᵢ,Pⱼ} = δᵢⱼ.

The Poisson bracket is defined in section 2.8. For one pair it is {Q,P} = (∂Q/∂q)(∂P/∂p) − (∂Q/∂p)(∂P/∂q). The symbol δᵢⱼ is 1 when i = j and 0 otherwise. A time-dependent canonical transformation also requires the corresponding new Hamiltonian K; simply substituting variables into H is not always sufficient.

**Worked example: scaling.** Q = aq and P = p/a, with constant a ≠ 0, gives {Q,P} = a(1/a) − 0 = 1. For an oscillator, substitution gives K = a²P²/(2m) + kQ²/(2a²). Hamilton's equations in Q,P describe the same trajectories through changed labels.

In contrast, Q = aq and P = ap gives bracket a² and is not canonical unless a² = 1. A visually balanced transformation need not preserve the required structure.

**Try it.** Test Q = q and P = p + cq². **Answer:** {Q,P} = 1, so it is canonical for constant c. The q-dependence in P does not spoil the bracket.

### 2.6 Generating Functions

**In simple words:** A generating function produces the old-to-new variable relations by differentiation. Its choice determines which variables we treat as independent.

For a type-1 function F₁(q,Q,t), require the action integrands to differ by a total differential:

> Σpⱼdqⱼ − Hdt = ΣPⱼdQⱼ − Kdt + dF₁.

Expand dF₁ and compare coefficients. This gives pⱼ = ∂F₁/∂qⱼ, Pⱼ = −∂F₁/∂Qⱼ, and K = H + ∂F₁/∂t. The other types follow by Legendre transformations of F₁:

| Type | Independent variables | Coordinate and momentum relations |
|---|---|---|
| F₁ | q,Q,t | p = ∂F₁/∂q; P = −∂F₁/∂Q |
| F₂ = F₁ + ΣPQ | q,P,t | p = ∂F₂/∂q; Q = ∂F₂/∂P |
| F₃ = F₁ − Σpq | p,Q,t | q = −∂F₃/∂p; P = −∂F₃/∂Q |
| F₄ = F₁ − Σpq + ΣPQ | p,P,t | q = −∂F₄/∂p; Q = ∂F₄/∂P |

For every type, K = H + ∂F/∂t, evaluated using that function's independent variables and then expressed in the new variables. Each type works where its chosen relations can be inverted; one type need not cover every transformation globally.

**Worked example.** Let F₂(q,P) = qP + cq²/2, with constant c carrying the required units. Then p = P + cq and Q = q. Thus P = p − cq. A free-particle H = p²/(2m) becomes K = (P + cQ)²/(2m). Do not replace p by P alone; the momentum shift changes the Hamiltonian's expression.

**Time-dependent example.** F₂ = (q − ut)P gives p = P, Q = q − ut and K = H − uP. The extra term comes from ∂F₂/∂t, and is essential for describing the translated coordinate.

**Try it.** Use F₂ = aqP. **Answer:** p = aP and Q = aq, so P = p/a.

### 2.7 A Complete Canonical Test

**In simple words:** Differentiate first, then assemble the bracket. A sign error changes the conclusion.

Take Q = √(2p)sin q and P = √(2p)cos q. Here q,p are suitably scaled mathematical canonical variables with p &gt; 0. q is an angular variable; dimensional scale factors would be needed if using arbitrary physical coordinates and momenta.

> ∂Q/∂q = √(2p)cos q; ∂Q/∂p = sin q/√(2p).
> ∂P/∂q = −√(2p)sin q; ∂P/∂p = cos q/√(2p).

Substitution gives {Q,P} = cos²q + sin²q = 1. Thus the map is locally canonical on p &gt; 0. Since q is periodic and the square-root derivatives are singular at p = 0, one should not claim a single globally invertible transformation for all real q,p.

**A useful comparison.** Swapping Q and P without changing a sign gives {P,Q} = −1. By contrast, Q = p and P = −q is canonical. Antisymmetry is why the minus sign matters.

**Try it.** Test Q = q², P = p/(2q), for q ≠ 0. **Answer:** The bracket is (2q)(1/(2q)) − 0 = 1. Choose a local branch q &gt; 0 or q &lt; 0 to invert Q.

### 2.8 Poisson Brackets and Poisson's Theorem

**In simple words:** A Poisson bracket tells us how one phase-space quantity changes under the transformation generated by another. The Hamiltonian generates time evolution.

For functions f(q,p,t), g(q,p,t), define:

> {f,g} = Σⱼ[(∂f/∂qⱼ)(∂g/∂pⱼ) − (∂f/∂pⱼ)(∂g/∂qⱼ)].

For f = qᵢ and g = pⱼ, only the matching derivatives survive, giving δᵢⱼ. The q–q and p–p brackets vanish. We reserve curly brackets for classical Poisson brackets and square brackets for quantum commutators.

| Property | Statement | How to see it |
|---|---|---|
| Antisymmetry | {f,g} = −{g,f} | Interchange the two derivative products |
| Linearity | {af + bg,h} = a{f,h} + b{g,h} | Derivatives are linear; a,b are constants |
| Product rule | {fg,h} = f{g,h} + g{f,h} | Apply the derivative product rule |
| Self bracket | {f,f} = 0 | Equal derivative products cancel |
| Jacobi identity | {f,{g,h}} + {g,{h,f}} + {h,{f,g}} = 0 | Expand derivatives; mixed partial terms cancel in pairs |

Use the chain rule along a Hamiltonian trajectory:

> df/dt = Σⱼ[(∂f/∂qⱼ)q̇ⱼ + (∂f/∂pⱼ)ṗⱼ] + ∂f/∂t = {f,H} + ∂f/∂t.

If f has no explicit time dependence, it is conserved exactly when {f,H} = 0. If it does depend explicitly on time, keep ∂f/∂t.

**Poisson's theorem.** If f and g are constants of motion, their bracket is also a constant of motion, though it may be zero or dependent on known constants. To show it, use Jacobi to write:

> d{f,g}/dt = {df/dt,g} + {f,dg/dt} = 0.

This identity includes explicit time derivatives when present. It is the relevant “Poisson theorem” for constructing conserved quantities in this course.

**Worked example.** For H = p²/(2m), f = q − pt/m has {f,H} = p/m and ∂f/∂t = −p/m. They cancel, so f is conserved. It equals the initial position. Testing only {f,H} would wrongly reject it.

**Try it.** Compute {q,p²} and {q²,p²}. **Answer:** 2p and 4qp.

### 2.9 Angular Momentum Brackets and the Quantum Connection

**In simple words:** Rotations have a specific algebra. Classical angular momenta obey that algebra through Poisson brackets; quantum angular momenta express a corresponding relation through commutators.

Write Jₓ = yp\_z − zp\_y, Jᵧ = zp\_x − xp\_z, and J\_z = xp\_y − yp\_x. To calculate {Jₓ,Jᵧ}, sum derivatives over x,y,z. The x and y contributions vanish. The z contribution is (−p\_y)(−x) − (y)(p\_x) = xp\_y − yp\_x. Hence:

> {Jₓ,Jᵧ} = J\_z; {Jᵧ,J\_z} = Jₓ; {J\_z,Jₓ} = Jᵧ.

It follows that {J²,Jₓ} = 2Jᵧ{Jᵧ,Jₓ} + 2J\_z{J\_z,Jₓ} = −2JᵧJ\_z + 2J\_zJᵧ = 0; similarly for the other components. A central potential conserves each angular-momentum component. Poisson's theorem also shows that conservation of Jₓ and Jᵧ entails conservation of their bracket J\_z.

In quantum mechanics, [Â,B̂] = ÂB̂ − B̂Â. The basic canonical correspondence is [q̂,p̂] = iħ, paralleling {q,p} = 1. Likewise [Ĵₓ,Ĵᵧ] = iħĴ\_z. In the Heisenberg picture:

> dÂ/dt = [Â,Ĥ]/(iħ) + ∂Â/∂t.

This is a structural link, not a rule that maps every arbitrary classical expression uniquely into an operator. Operator ordering introduces difficulties for general products. Use the correspondence with its scope stated.

**Try it.** Find {J\_z,Jₓ}. **Answer:** Jᵧ. Reversing the order gives −Jᵧ.

### 2.10 Hamilton's Principal and Characteristic Functions

**In simple words:** Instead of solving separately for every coordinate and momentum, we seek an action function whose derivatives encode the motion.

Hamilton's principal function S(q,α,t) is a type-2 generating function chosen so that the new Hamiltonian K is zero. The new momenta αⱼ and new coordinates βⱼ are then constants. The transformation relations are pⱼ = ∂S/∂qⱼ and βⱼ = ∂S/∂αⱼ. Since K = H + ∂S/∂t, S satisfies the Hamilton–Jacobi equation:

> H(q,∂S/∂q,t) + ∂S/∂t = 0.

A complete integral contains n independent essential constants αⱼ, apart from an irrelevant additive constant, and has the appropriate nondegeneracy for the transformation. The difficulty has moved into finding that function; the method does not guarantee an easy separation for every system.

If H has no explicit time dependence, separate S = W(q,α) − Et. W is Hamilton's characteristic function, and the equation becomes H(q,∂W/∂q) = E.

**First example: a free particle.** For H = p²/(2m), choose S(q,α,t) = αq − α²t/(2m). Then p = α, and β = ∂S/∂α = q − αt/m. Therefore q = β + αt/m, the constant-velocity motion. The constants are the momentum and initial position.

**Oscillator example.** For H = p²/(2m) + ½kq²:

> (dW/dq)²/(2m) + ½kq² = E.
> dW/dq = ±√(2mE − mkq²).

Choose a local branch where momentum is positive. Put A = √(2E/k). Differentiating W = ∫√(2mE − mkq²)dq with respect to E gives √(m/k)arcsin(q/A), up to a choice of integration constant. Thus β = ∂S/∂E = (1/ω)arcsin(q/A) − t, and:

> q(t) = A sin[ω(t + β)], with ω = √(k/m).

The inverse-sine branch describes only part of an oscillation; switch momentum branches at turning points to continue the full trajectory. The amplitude satisfies E = ½kA², connecting the solution to the phase ellipse.

### 2.11 Small Oscillations

**In simple words:** Near a stable equilibrium, a smooth potential looks approximately quadratic. This makes many complicated systems behave like coupled springs.

For one coordinate, write q = q₀ + η, where V′(q₀) = 0. Taylor expansion gives V ≈ V(q₀) + ½V″(q₀)η². For constant effective mass m, the linearised equation is mη̈ + V″(q₀)η = 0. Positive curvature gives oscillations; negative curvature gives exponential growth. Zero curvature needs higher-order analysis.

For n coordinates near a static equilibrium of a conservative natural system:

> T = ½ΣᵢⱼMᵢⱼη̇ᵢη̇ⱼ; V = V₀ + ½ΣᵢⱼKᵢⱼηᵢηⱼ.

M is the mass matrix and K is the matrix of second potential derivatives at equilibrium. They are constant at this approximation. The equations are Mη̈ + Kη = 0. Try η = a cos(ωt + φ); then:

> (K − ω²M)a = 0; det(K − ω²M) = 0.

A nonzero a is possible only when the determinant vanishes. Each eigenvector gives a collective motion pattern, or **normal mode**, with fixed relative amplitudes. Positive-definite M and K give positive ω². Zero eigenvalues can describe free symmetry motions rather than vibrations.

The mass matrix matters. For unequal masses, orthogonality and normalisation use the mass-weighted product aᵀMb. Dividing eigenvectors by their ordinary Euclidean length is not the general prescription for decoupling kinetic energy.

**Chemistry connection.** Atoms displaced slightly from a molecular equilibrium execute collective normal vibrations. The spring picture describes the local curvature of the molecular potential, not literal visible springs between atoms.

### 2.12 Two Coupled Oscillators and Normal Coordinates

![The in-phase and out-of-phase motions stretch the coupling spring differently.](images/classical/normal_modes.png)

**In simple words:** Two moving masses can oscillate together or against each other. The normal coordinates separate those two patterns.

Two identical masses m have outer springs k and a connecting spring k\_c. Let x₁,x₂ be rightward displacements from equilibrium. The extension of the middle spring is x₂ − x₁, so:

> T = ½m(ẋ₁² + ẋ₂²).
> V = ½kx₁² + ½k\_c(x₂ − x₁)² + ½kx₂².

Differentiating V gives mẍ₁ = −(k + k\_c)x₁ + k\_cx₂ and mẍ₂ = k\_cx₁ − (k + k\_c)x₂. Substitute xᵢ = aᵢcos ωt. The determinant condition is:

> (k + k\_c − mω²)² − k\_c² = 0.

For k + k\_c − mω² = +k\_c, ω₁² = k/m and a₂ = a₁. The masses move together and the coupling spring retains its length. For the negative sign, ω₂² = (k + 2k\_c)/m and a₂ = −a₁. The coupling spring stretches and compresses.

Define Q₊ = (x₁ + x₂)/√2 and Q₋ = (x₁ − x₂)/√2. Inverting gives x₁ = (Q₊ + Q₋)/√2 and x₂ = (Q₊ − Q₋)/√2. Substituting and cancelling mixed terms:

> T = ½m(Q̇₊² + Q̇₋²).
> V = ½kQ₊² + ½(k + 2k\_c)Q₋².

These are two independent oscillators. This explicit decoupling explains what a normal coordinate does.

**Numerical example.** Set m = 1 kg, k = 4 N/m and k\_c = 2 N/m. Then ω₁ = 2 rad/s and ω₂ = √8 = 2.828 rad/s. If x₁(0) = a, x₂(0) = 0 and both initial velocities vanish:

> x₁(t) = (a/2)(cos ω₁t + cos ω₂t).
> x₂(t) = (a/2)(cos ω₁t − cos ω₂t).

Both modes are excited. A general initial displacement need not be a single normal mode. In the limit k\_c → 0, the two frequencies coincide and the oscillators become uncoupled.

### 2.13 Group Property of Canonical Transformations

**In simple words:** You can combine allowed changes of variables, undo them, and leave the variables unchanged. These operations stay within the canonical family.

The identity is canonical. The composition of two canonical transformations is canonical because Poisson brackets are preserved at each step. A locally invertible canonical transformation has a canonical inverse. Composition is associative because it is composition of maps. Together these statements give the group property, with attention to the domains where the maps are defined.

For phase coordinates z = (q₁,…,qₙ,p₁,…,pₙ), let A = ∂Z/∂z be the Jacobian matrix and J₀ the block matrix with upper-right block I, lower-left block −I, and zero diagonal blocks. The canonical condition is:

> A J₀ Aᵀ = J₀.

If A and B satisfy it, then (BA)J₀(BA)ᵀ = B(AJ₀Aᵀ)Bᵀ = BJ₀Bᵀ = J₀. This supplies an algebraic composition proof. A canonical map preserves phase-space volume, but volume preservation alone is not sufficient in more than one coordinate–momentum pair.

**Worked example.** Apply Q = aq, P = p/a, followed by X = bQ, Y = P/b. The composite is X = abq, Y = p/(ab), which is canonical. Its inverse scales by 1/(ab).

### 2.14 Infinitesimal Generators

**In simple words:** A finite transformation can be built from many small steps. A generator tells us the direction of the first small step in phase space.

Take F₂(q,P) = ΣqⱼPⱼ + εG(q,P), where ε is small. Differentiating and retaining first-order terms gives:

> δqⱼ = ε∂G/∂pⱼ; δpⱼ = −ε∂G/∂qⱼ.

For any function f, the chain rule gives δf = ε{f,G}. This defines our sign convention. With G = pₓ, δx = ε and δpₓ = 0: momentum generates a translation. With G = J\_z = xp\_y − yp\_x, δx = −εy and δy = εx: angular momentum generates a small rotation about z.

Hamiltonian time evolution itself has δf = dt{f,H} when f has no explicit time dependence. Thus H is the generator of time translations along the motion. This statement connects canonical transformations, dynamics and conservation laws.

**Try it.** Let G = qp for a single pair. **Answer:** δq = εq and δp = −εp. The infinitesimal scaling increases one variable while decreasing its conjugate partner.

## भाग 3: Put the Ideas Together

### One Oscillator in Three Descriptions

Begin with m = 1 kg, k = 4 N/m, q(0) = 1 m and q̇(0) = 0. Lagrange's method gives q̈ + 4q = 0, hence q = cos 2t. The momentum is p = q̇ = −2 sin 2t, with the appropriate SI units.

Hamilton's method starts with H = p²/2 + 2q². Its equations q̇ = p and ṗ = −4q give exactly the same motion. Substitution verifies H = 2 J throughout. The phase path is q² + p²/4 = 1 when the plotted coordinates are measured in metres and kg·m/s.

Hamilton–Jacobi theory gives amplitude √(2E/k) = 1 m and angular frequency √(k/m) = 2 rad/s. Choosing the phase to match the initial condition recovers cos 2t. Agreement among the descriptions is a physical check, not three different motions.

### Which Method Should I Choose?

Use Lagrange's equations to construct motion equations directly from energies and constraints. Use Hamilton's equations when momentum, phase space or canonical changes of variables are central. Use Hamilton–Jacobi theory when the principal function separates conveniently. Use normal coordinates for linearised coupled oscillators.

## भाग 4: Check Your Understanding

### 2.15 Common Mistakes and Their Corrections

- “Stationary” does not automatically mean “minimum”. State the endpoint conditions of the variation.
- Solve for q̇ in terms of p before using H(q,p,t).
- The second Hamilton equation has a minus sign.
- A one-pair bracket test needs a regular domain. For many pairs check all fundamental brackets.
- A time-dependent generating function adds ∂F/∂t to the Hamiltonian.
- Distinguish mathematical local invertibility from a global change of variables.
- Keep explicit time dependence in df/dt = {f,H} + ∂f/∂t.
- Normal-mode eigenvectors for unequal masses use mass-weighted normalisation.
- A Poisson bracket is classical; a commutator multiplies operators in two different orders.
- A complete HJ solution requires the appropriate independent constants. An unexamined particular solution may not determine all trajectories.

**Explain without calculating.** Why does one position correspond to two points on a positive-energy oscillator ellipse? The particle can pass that position with either sign of momentum. Why can a transformation preserve volume yet fail to be canonical in higher dimensions? Volume is one condition; preserving every conjugate bracket is a stronger structure requirement.

## भाग 5: Practice Questions with Explanations

#### Question U2-01

A functional takes what as its input?

- **A.** Only one real number
- **B.** A function or path
- **C.** Only a force vector
- **D.** Only time at one instant

**Answer: B.** An integral such as I[y] assigns a number to a whole curve y(x).

#### Question U2-02

For fixed endpoint variations, what happens to η at the endpoints?

- **A.** It is always one
- **B.** Its derivative must be infinite
- **C.** It vanishes
- **D.** It equals the momentum

**Answer: C.** Endpoint configurations are fixed while the interior path changes.

#### Question U2-03

Which operation removes the derivative on the variation in the action derivation?

- **A.** Taking a determinant
- **B.** Squaring the action
- **C.** Changing mass
- **D.** Integration by parts

**Answer: D.** Integration by parts transfers a derivative and exposes the vanishing boundary term.

#### Question U2-04

Stationary action requires what?

- **A.** Zero first-order allowed variation
- **B.** The smallest energy at every time
- **C.** Zero Lagrangian at every point
- **D.** A global minimum for every path

**Answer: A.** Stationarity concerns the first variation and does not imply an unconditional minimum.

#### Question U2-05

What are the units of action?

- **A.** J/s
- **B.** J·s
- **C.** N/s
- **D.** kg/m

**Answer: B.** Action is the time integral of a quantity with energy units.

#### Question U2-06

For L = ½mẋ², Hamilton's principle gives which motion?

- **A.** Constant nonzero acceleration
- **B.** Exponential growth only
- **C.** Constant velocity
- **D.** Circular motion only

**Answer: C.** The Euler–Lagrange equation is mẍ = 0.

#### Question U2-07

Which definition gives canonical momentum?

- **A.** pⱼ = ∂L/∂qⱼ
- **B.** pⱼ = ∂H/∂t
- **C.** pⱼ = Lqⱼ
- **D.** pⱼ = ∂L/∂q̇ⱼ

**Answer: D.** The velocity derivative defines the momentum used in the Legendre transform.

#### Question U2-08

What must be done before treating H as H(q,p,t)?

- **A.** Eliminate velocities in favour of momenta
- **B.** Set every momentum to zero
- **C.** Discard the potential
- **D.** Differentiate only with respect to time

**Answer: A.** Hamiltonian partial derivatives require the declared independent phase variables.

#### Question U2-09

Which Hamilton equation is correct?

- **A.** ṗ = +∂H/∂q
- **B.** ṗ = −∂H/∂q
- **C.** q̇ = −∂H/∂p
- **D.** p = −∂H/∂t

**Answer: B.** The negative coordinate derivative gives the canonical momentum equation.

#### Question U2-10

For H = p²/(2m) + ½kq², q̇ equals what?

- **A.** −kq
- **B.** mq
- **C.** p/m
- **D.** p²/m

**Answer: C.** Differentiate H with respect to p while holding q fixed.

#### Question U2-11

An n-degree regular Lagrangian system becomes how many first-order Hamilton equations?

- **A.** n
- **B.** n²
- **C.** One
- **D.** 2n

**Answer: D.** Each coordinate and each momentum has a first-order equation.

#### Question U2-12

When an autonomous Hamiltonian generates its motion, what happens to H?

- **A.** It is conserved
- **B.** It vanishes
- **C.** It equals L
- **D.** It increases uniformly

**Answer: A.** The coordinate-momentum derivative terms cancel, leaving dH/dt = ∂H/∂t = 0.

#### Question U2-13

What distinguishes phase space from configuration space?

- **A.** Phase space excludes positions
- **B.** Phase space includes conjugate momenta
- **C.** Both have n dimensions always
- **D.** Configuration space includes all forces

**Answer: B.** A mechanical state needs both the coordinates and momenta.

#### Question U2-14

The positive-energy harmonic-oscillator phase path is what?

- **A.** A straight radial line
- **B.** A parabola
- **C.** An ellipse
- **D.** A spiral for every oscillator

**Answer: C.** Its fixed-energy equation is quadratic positive in q and p.

#### Question U2-15

At the rightmost oscillator phase point, p = 0 and q &gt; 0. Which way does p start changing?

- **A.** Upwards on the p axis
- **B.** It stays zero
- **C.** It becomes undefined
- **D.** Downwards on the p axis

**Answer: D.** Hamilton's equation ṗ = −kq is negative there.

#### Question U2-16

For m = 1 kg, k = 4 N/m and E = 2 J, what is the position amplitude?

- **A.** 1 m
- **B.** 2 m
- **C.** 4 m
- **D.** 0.5 m

**Answer: A.** The amplitude is √(2E/k) = 1 m.

#### Question U2-17

For a single canonical pair, which bracket must a regular transformation preserve?

- **A.** {Q,P} = 0
- **B.** {Q,P} = 1
- **C.** {Q,P} = −1 always
- **D.** {Q,Q} = 1

**Answer: B.** The transformed coordinate and conjugate momentum retain the fundamental bracket.

#### Question U2-18

Which scaling is canonical for nonzero constant a?

- **A.** Q = aq, P = ap for every a
- **B.** Q = q/a, P = p/a for every a
- **C.** Q = aq, P = p/a
- **D.** Q = aq, P = 0

**Answer: C.** The reciprocal scaling makes the derivative product equal to one.

#### Question U2-19

Is Q = p, P = −q canonical?

- **A.** No, its bracket is zero
- **B.** Only if p = q
- **C.** Only if H = 0
- **D.** Yes, its bracket is one

**Answer: D.** The reversed pair requires the minus sign to preserve the bracket orientation.

#### Question U2-20

For F₂(q,P,t), which relation is correct?

- **A.** Q = ∂F₂/∂P
- **B.** Q = −∂F₂/∂P
- **C.** P = ∂F₂/∂q
- **D.** q = −∂F₂/∂P

**Answer: A.** Type 2 uses old coordinates and new momenta as independent variables.

#### Question U2-21

For F₁(q,Q,t), the new momentum is what?

- **A.** +∂F₁/∂Q
- **B.** −∂F₁/∂Q
- **C.** ∂F₁/∂q
- **D.** ∂F₁/∂t

**Answer: B.** Coefficient matching in the action differential supplies the minus sign.

#### Question U2-22

How does explicit time dependence of a generating function enter K?

- **A.** K = H − F
- **B.** K = H for every F
- **C.** K = H + ∂F/∂t
- **D.** K = ∂H/∂t

**Answer: C.** The time coefficient in the differential action relation gives the correction.

#### Question U2-23

For F₂ = qP + cq²/2, what is P in old variables?

- **A.** p + cq
- **B.** q − cp
- **C.** p/c
- **D.** p − cq

**Answer: D.** Differentiate to obtain p = P + cq and solve for P.

#### Question U2-24

For F₂ = (q − ut)P and a free-particle H, what extra term enters K?

- **A.** −uP
- **B.** +uP
- **C.** −uq
- **D.** +ut

**Answer: A.** The partial time derivative at fixed q,P is −uP.

#### Question U2-25

The map Q = √(2p)sin q, P = √(2p)cos q is regular on which stated domain?

- **A.** All real p including zero
- **B.** Locally on p &gt; 0
- **C.** Only p &lt; 0 for real variables
- **D.** Only q = 0

**Answer: B.** The square root and its derivatives require the positive-p domain for the real regular calculation.

#### Question U2-26

What is {q,p²}?

- **A.** p
- **B.** 0
- **C.** 2p
- **D.** −2p

**Answer: C.** Only the q derivative of q and p derivative of p² contribute.

#### Question U2-27

What is {q²,p²}?

- **A.** 2qp
- **B.** 0
- **C.** −4qp
- **D.** 4qp

**Answer: D.** The product of derivatives is (2q)(2p).

#### Question U2-28

What is {f,f}?

- **A.** 0
- **B.** 1
- **C.** f²
- **D.** df/dt

**Answer: A.** The two derivative products are identical and cancel.

#### Question U2-29

Which formula gives the full time derivative of f?

- **A.** {f,H} only in every case
- **B.** {f,H} + ∂f/∂t
- **C.** {H,f} + ∂f/∂t
- **D.** ∂f/∂q only

**Answer: B.** Explicit time dependence must be retained along with phase-space evolution.

#### Question U2-30

For a free particle, which explicitly time-dependent quantity is conserved?

- **A.** q + pt/m
- **B.** qt
- **C.** q − pt/m
- **D.** p + mt

**Answer: C.** Its explicit derivative cancels the Poisson-bracket evolution.

#### Question U2-31

Poisson's theorem says the bracket of two constants of motion is what?

- **A.** Always nonzero
- **B.** Always independent of both
- **C.** Always the Hamiltonian
- **D.** Another constant of motion

**Answer: D.** Jacobi and the time-derivative identity establish conservation; independence is not guaranteed.

#### Question U2-32

Which angular-momentum bracket is correct?

- **A.** {Jₓ,Jᵧ} = J\_z
- **B.** {Jₓ,Jᵧ} = −J\_z
- **C.** {Jₓ,Jᵧ} = 1
- **D.** {Jₓ,Jᵧ} = 0 always

**Answer: A.** The Cartesian canonical brackets produce the cyclic angular-momentum algebra.

#### Question U2-33

What is {J²,J\_z}?

- **A.** J\_z
- **B.** 0
- **C.** J²
- **D.** 1

**Answer: B.** Opposite cross-component contributions cancel.

#### Question U2-34

Which is the quantum canonical commutator?

- **A.** [q̂,p̂] = 1
- **B.** [q̂,p̂] = 0
- **C.** [q̂,p̂] = iħ
- **D.** [q̂,p̂] = −ħ²

**Answer: C.** The quantum commutator parallels the classical fundamental bracket with factor iħ.

#### Question U2-35

Hamilton's principal function satisfies which equation?

- **A.** H + S = 0
- **B.** ∂S/∂q = 0 always
- **C.** S = T − V
- **D.** H(q,∂S/∂q,t) + ∂S/∂t = 0

**Answer: D.** The generating function is chosen so the transformed Hamiltonian is zero.

#### Question U2-36

For an autonomous H, which separation is standard?

- **A.** S = W − Et
- **B.** S = W + Et for the same E convention
- **C.** S = Et only
- **D.** S = W/t

**Answer: A.** The partial time derivative is then −E and H(q,∂W/∂q) = E.

#### Question U2-37

In the free-particle principal function S = αq − α²t/(2m), α represents what?

- **A.** Position
- **B.** Momentum
- **C.** Acceleration
- **D.** Potential energy

**Answer: B.** The coordinate derivative p = ∂S/∂q equals α, identifying the constant as the particle's momentum.

#### Question U2-38

A stable one-coordinate equilibrium with constant mass requires what at quadratic order?

- **A.** V″(q₀) &lt; 0
- **B.** V(q₀) = 0 necessarily
- **C.** V″(q₀) &gt; 0
- **D.** V′(q₀) ≠ 0

**Answer: C.** Positive curvature gives a restoring force after linearisation.

#### Question U2-39

What determines the small-oscillation frequencies?

- **A.** det(K + M) = 1
- **B.** K = M always
- **C.** ω = det M
- **D.** det(K − ω²M) = 0

**Answer: D.** A nonzero mode amplitude requires a singular coefficient matrix.

#### Question U2-40

For unequal masses, normal-mode orthogonality uses which product?

- **A.** aᵀMb
- **B.** aᵀb in every case
- **C.** a + b
- **D.** det(a,b)

**Answer: A.** The kinetic-energy quadratic form defines the relevant mass-weighted inner product.

#### Question U2-41

Two equal masses with outer springs k and coupling k\_c move in phase. Their frequency is what?

- **A.** √((k + 2k\_c)/m)
- **B.** √(k/m)
- **C.** √(k\_c/m)
- **D.** k/m

**Answer: B.** The connecting spring does not change length in the in-phase mode.

#### Question U2-42

For that system, the out-of-phase frequency is what?

- **A.** √(k/m)
- **B.** √((k − 2k\_c)/m)
- **C.** √((k + 2k\_c)/m)
- **D.** 2k\_c/m

**Answer: C.** Opposite displacements activate the middle spring and add restoring stiffness.

#### Question U2-43

Which pair gives the equal-mass normal coordinates?

- **A.** x₁² and x₂²
- **B.** x₁x₂ and x₁/x₂
- **C.** x₁ + 2x₂ and x₁ + 2x₂
- **D.** (x₁ + x₂)/√2 and (x₁ − x₂)/√2

**Answer: D.** The symmetric and antisymmetric combinations diagonalise both quadratic energies.

#### Question U2-44

The composition of two canonical transformations is what?

- **A.** Canonical on its regular domain
- **B.** Never canonical
- **C.** Canonical only when identical
- **D.** Always the identity

**Answer: A.** Preserving the fundamental bracket structure twice preserves it for the composite.

#### Question U2-45

With δf = ε{f,G}, which generator gives δx = ε?

- **A.** G = x
- **B.** G = pₓ
- **C.** G = x²
- **D.** G = H for every system

**Answer: B.** The fundamental bracket {x,pₓ} is one, so momentum generates translations.


## भाग 6: Quick Revision and Terminology

### 6.1 Sixty Revision Points

1. A functional assigns a number to a whole function or path.
2. An allowed fixed-endpoint variation vanishes at both endpoints.
3. Integration by parts transfers the derivative off the variation.
4. The Euler–Lagrange equation follows from arbitrary interior variations.
5. Stationary action means zero first-order allowed variation.
6. Stationary action need not be an unconditional minimum.
7. Action has dimensions of energy times time.
8. Hamilton's principle fixes endpoint configurations and times.
9. Maupertuis' fixed-energy principle has different variation constraints.
10. A regular Lagrangian has a locally invertible velocity-to-momentum relation.
11. The velocity Hessian has nonzero determinant for regularity.
12. Canonical momentum is the velocity derivative of L.
13. The Hamiltonian is H = Σpq̇ − L after eliminating velocities.
14. The Legendre transformation changes independent variables from velocities to momenta.
15. Hamilton's coordinate equation is q̇ = ∂H/∂p.
16. Hamilton's momentum equation is ṗ = −∂H/∂q.
17. There are two first-order equations per canonical pair.
18. The Hamiltonian's total derivative is its explicit time derivative along its flow.
19. An autonomous Hamiltonian is conserved.
20. Configuration space has n dimensions for n independent coordinates.
21. Phase space has 2n dimensions for n canonical pairs.
22. A phase point describes both configuration and conjugate momentum.
23. Positive-energy oscillator phase paths are ellipses.
24. The oscillator position amplitude is √(2E/k).
25. The oscillator momentum amplitude is √(2mE).
26. On a q-horizontal and p-vertical plot, an ordinary oscillator circulates clockwise.
27. A canonical transformation preserves all fundamental Poisson brackets.
28. For one regular pair, {Q,P} = 1 is the bracket condition.
29. For many pairs, also check all Q–Q and P–P brackets.
30. The scaling Q = aq, P = p/a is canonical for a ≠ 0.
31. Canonical exchange requires a sign: Q = p, P = −q.
32. A generating function determines a canonical map through derivatives.
33. F₁ uses q,Q as its independent coordinate arguments.
34. F₂ uses q,P and gives p = F₂\_q and Q = F₂\_P.
35. F₃ uses p,Q and gives q = −F₃\_p and P = −F₃\_Q.
36. F₄ uses p,P and gives q = −F₄\_p and Q = F₄\_P.
37. The transformed Hamiltonian is K = H + ∂F/∂t.
38. Different generating-function types require appropriate local invertibility.
39. The Poisson bracket is antisymmetric and linear.
40. The Poisson bracket satisfies a derivative product rule.
41. The Jacobi identity links three nested Poisson brackets.
42. Every function has zero bracket with itself.
43. The fundamental coordinate-momentum bracket is δᵢⱼ.
44. Along motion, df/dt = {f,H} + ∂f/∂t.
45. Explicitly time-dependent constants of motion require both terms in that formula.
46. Poisson's theorem makes the bracket of conserved functions conserved.
47. Angular momenta satisfy {Jₓ,Jᵧ} = J\_z and cyclic permutations.
48. J² has zero bracket with every angular-momentum component.
49. Quantum commutators are operator differences, not classical derivative brackets.
50. The principal function satisfies H(q,∂S/∂q,t) + ∂S/∂t = 0.
51. For an autonomous Hamiltonian, S = W − Et.
52. Hamilton's characteristic function obeys H(q,∂W/∂q) = E.
53. A complete HJ integral contains the required independent essential constants.
54. Small oscillations follow the quadratic potential expansion about equilibrium.
55. Normal frequencies satisfy det(K − ω²M) = 0.
56. Normal-mode orthogonality generally uses the mass-weighted product.
57. For equal coupled masses, symmetric and antisymmetric coordinates decouple the energies.
58. Canonical transformations have identity, inverse, composition and associativity on regular domains.
59. An infinitesimal generator acts through δf = ε{f,G} in the convention used here.
60. Momentum generates spatial translation and angular momentum generates rotation.

### 6.2 Hindi-Supported Glossary

| English term | Hindi aid | Meaning in this unit |
|---|---|---|
| Variation | परिवर्तन की कल्पित छोटी मात्रा | Small change of an entire path |
| Action | क्रिया | Time integral of the Lagrangian |
| Stationary | प्रथम-क्रम परिवर्तन शून्य | Having zero first-order variation |
| Hamiltonian | हैमिल्टोनियन | Legendre transform of a regular Lagrangian |
| Phase space | अवस्था समष्टि | Space of coordinates and conjugate momenta |
| Canonical transformation | कैनोनिकल रूपांतरण | Change preserving the canonical structure |
| Generating function | जनक फलन | Function producing transformation relations |
| Poisson bracket | प्वासों कोष्ठक | Derivative operation encoding canonical changes |
| Commutator | क्रमविनिमेयक | Difference between two operator orderings |
| Principal function | प्रधान फलन | Time-dependent HJ action function S |
| Characteristic function | अभिलाक्षणिक फलन | Time-separated HJ function W |
| Equilibrium | साम्यावस्था | Configuration with zero net generalized force |
| Normal mode | प्रसामान्य विधा | Collective oscillation with one frequency |
| Normal coordinate | प्रसामान्य निर्देशांक | Coordinate separating a mode |
| Generator | जनक | Function producing an infinitesimal transformation |

### 6.3 Formula Sheet with Conditions

| Result | Condition or interpretation |
|---|---|
| δ∫Ldt = 0 | Allowed path variations with fixed configurations and times at endpoints |
| H = Σpq̇ − L | Eliminate velocities; regular Legendre transform |
| q̇ = ∂H/∂p; ṗ = −∂H/∂q | Canonical variables |
| {f,g} = Σ(f\_q g\_p − f\_p g\_q) | Derivatives at fixed other phase variables |
| df/dt = {f,H} + ∂f/∂t | Along Hamiltonian motion |
| {Qᵢ,Pⱼ} = δᵢⱼ; {Qᵢ,Qⱼ} = {Pᵢ,Pⱼ} = 0 | Complete canonical bracket conditions |
| K = H + ∂F/∂t | Generating-function transformation |
| H(q,∂S/∂q,t) + ∂S/∂t = 0 | Hamilton–Jacobi equation |
| S = W − Et | Autonomous Hamiltonian |
| det(K − ω²M) = 0 | Linearised conservative small oscillations |
| δf = ε{f,G} | First-order transformation; stated generator convention |

---

# Unit 3: Rotating Frames and Central Force Motion


## भाग 1: Start Here

First we change the observer: how does motion look from a rotating platform or from Earth? Then we simplify an interacting pair of particles: how can two moving bodies be described by one relative coordinate? These questions lead to Coriolis forces, planetary orbits and atomic scattering.

Refresh the cross product before starting. For orbit calculations, remember that a polar position uses distance r and angle θ. A change dr and an arc r dθ are perpendicular, so the speed satisfies v² = ṙ² + r²θ̇².

## भाग 2: Build the Ideas

### 3.1 Rotating Frames and Inertial Forces

**In simple words:** An observer's axes can rotate even when a vector is fixed in space. The observed change of a vector must include the rotation of the axes.

For a vector A, let “in” mean a nonrotating inertial frame and “rot” mean axes rotating at angular velocity Ω. For coincident origins, the derivative relation is:

> (dA/dt)\_in = (dA/dt)\_rot + Ω × A.

To see why, write A = A₁e₁ + A₂e₂ + A₃e₃ in the rotating basis. Differentiate both its components and the basis vectors. The components give the rotating derivative; each basis vector obeys deᵢ/dt = Ω × eᵢ, giving the extra term.

Apply the relation to r. Velocity becomes v\_in = v\_rot + Ω × r. Apply it once more:

> a\_in = a\_rot + 2Ω × v\_rot + Ω̇ × r + Ω × (Ω × r).

If the rotating origin also has inertial acceleration a₀, add a₀ to the right. Rearrange F\_real = ma\_in to write the rotating observer's equation:

> ma\_rot = F\_real − ma₀ − 2mΩ × v\_rot − mΩ̇ × r − mΩ × (Ω × r).

| Inertial-force term | Name | When it appears |
|---|---|---|
| −ma₀ | Translational inertial force | Accelerating origin |
| −2mΩ × v\_rot | Coriolis force | Motion relative to rotating axes |
| −mΩ̇ × r | Euler force | Changing angular velocity |
| −mΩ × (Ω × r) | Centrifugal force | Nonzero rotation and distance from the axis |

The centrifugal magnitude is mΩ²r\_perpendicular, where r\_perpendicular is distance from the rotation axis. It is not generally mΩ² times distance from the origin. These terms arise from the frame description. The real forces still come from interactions.

**Worked example.** A 2 kg object rests 0.5 m from the axis on a platform rotating at 3 rad/s. It has v\_rot = 0, so no Coriolis force. Its centrifugal force in the rotating description has magnitude 2 × 9 × 0.5 = 9 N outward. A real inward force is required to keep it stationary on the platform.

### 3.2 Deriving and Interpreting the Coriolis Term

**In simple words:** The factor 2 comes from two contributions: differentiating the rotating-frame velocity and differentiating the rotational part of the velocity.

Take coincident origins and constant Ω. Start with v\_in = v\_rot + Ω × r. The inertial derivative of v\_rot is a\_rot + Ω × v\_rot. The derivative of Ω × r is Ω × v\_in because Ω is constant. Substitute v\_in into this second term:

> a\_in = a\_rot + Ω × v\_rot + Ω × (v\_rot + Ω × r).
> a\_in = a\_rot + 2Ω × v\_rot + Ω × (Ω × r).

Moving the additional acceleration terms to the force side gives F\_C = −2mΩ × v\_rot. The order of the cross product and the minus sign both matter. Its magnitude is 2mΩv\_rot sin α, where α is the angle between Ω and v\_rot. It vanishes when the relative velocity is parallel to the rotation axis.

Since (Ω × v\_rot) · v\_rot = 0, the Coriolis force contributes no instantaneous power in the rotating frame. It can redirect a trajectory. Other forces may simultaneously change the speed; the zero-power statement concerns this term alone.

**Worked direction check.** Let Ω point upwards along +z and let a bead move outwards along +x. Then Ω × v points +y, and the Coriolis force points −y. Its magnitude for m = 1 kg, Ω = 2 rad/s and v\_rot = 0.3 m/s is 1.2 N.

**Try it.** What changes if the bead moves inward? **Answer:** Its relative velocity reverses, so the Coriolis force reverses. The centrifugal force at the same location does not reverse.

### 3.3 Coriolis Effects on Earth and in Astronomy

**In simple words:** Earth's rotation matters most when motion persists over a long time or a large distance. A small acceleration can accumulate a measurable deflection.

Use local axes east, north and upward. At latitude λ, Ω has components (0,Ω cos λ,Ω sin λ). For predominantly horizontal flow, the horizontal deflection depends on f = 2Ω sin λ. It is to the right of the motion in the northern hemisphere and to the left in the southern hemisphere.

#### Winds and Large-Scale Circulation

Air moving towards low pressure is deflected sideways. In the northern hemisphere this supports counterclockwise circulation around a low-pressure region; the southern sense reverses. Friction, pressure gradients and the evolving flow also matter. At the equator f = 0, so this horizontal Coriolis mechanism is weak there. Do not conclude that every component of the full Coriolis force is zero at the equator: vertical motion still couples to the horizontal component of Ω.

#### The Foucault Pendulum

For an ideal small-amplitude pendulum, the swing direction slowly precesses relative to Earth. To leading order its precession-rate magnitude is:

> Ω\_F = Ω |sin λ|; τ\_F = 2π/(Ω |sin λ|).

At a pole, the precession period is one sidereal day. At the equator, the leading-order precession is zero. At latitude 30°, the magnitude is Ω/2 and the period is two sidereal days. The sense reverses between hemispheres. The pendulum plane is approximately inertially fixed in the polar idealisation; at a general latitude the local vertical itself changes direction, so use the derived latitude-dependent result rather than assuming an exactly fixed plane everywhere.

#### A Freely Falling Body

Drop a body from rest relative to Earth, neglect drag, use constant local g and retain only first-order terms in Ω. Its leading vertical velocity is v\_z = −gt. With the local Ω above, the eastward Coriolis acceleration is a\_east = 2Ωg t cos λ. Integrate once from zero initial eastward velocity and once from zero eastward displacement:

> v\_east = Ωg t² cos λ; d\_east = (1/3)Ωg t³ cos λ.

The leading fall time is t = √(2h/g). For h = 100 m, λ = 45°, Ω = 7.292 × 10⁻⁵ s⁻¹ and g = 9.8 m/s², t = 4.518 s and d ≈ 0.0155 m, or 1.55 cm eastward. We used the unperturbed vertical fall in the small correction; feeding the correction back into all components would exceed this first-order approximation.

#### A Rotating Astronomical Description

In a frame co-rotating with an orbiting pair, gravitational forces combine with centrifugal and Coriolis terms. A test body at rest in that rotating frame has no Coriolis force; a small displacement that produces relative motion introduces it. This is relevant when describing motion near orbital equilibrium points. The same frame-transformation equation applies, though the gravitational model differs from the laboratory examples.

### 3.4 Central Forces and the Two-Body Reduction

**In simple words:** A central interaction depends on separation and points along the line joining two particles. Separate the overall translation from the changing separation.

A central force has F = f(r)r̂, where f is positive for repulsion and negative for attraction. Its torque about the force centre is r × F = 0. Thus relative angular momentum J is constant. For J ≠ 0, r and v stay in the plane perpendicular to J. For J = 0, motion is radial along a fixed line.

For two particles interacting through V(|r₁ − r₂|), define:

> M = m₁ + m₂; R = (m₁r₁ + m₂r₂)/M; r = r₁ − r₂.

Invert these definitions: r₁ = R + (m₂/M)r and r₂ = R − (m₁/M)r. Substituting their derivatives in the kinetic energy cancels the mixed term and gives:

> T = ½M Ṙ² + ½μ ṙ²; μ = m₁m₂/(m₁ + m₂).

Here ṙ² means the square of the relative velocity vector's magnitude; in planar polar coordinates it equals ṙ² + r²θ̇². With no external force, M R̈ = 0. The relative motion obeys μ r̈\_vector = −∇V(r). Thus the separation behaves like a particle of **reduced mass (अपचयित द्रव्यमान)** μ.

**Worked example: hydrogen.** With m\_p ≈ 1836m\_e, μ = (1836/1837)m\_e ≈ 0.999456m\_e. The relative coordinate nearly has electron mass, but the small correction is important in accurate atomic calculations. For two identical masses m, μ = m/2, not 2m.

**Try it.** For masses 2 kg and 3 kg, find M and μ. **Answer:** M = 5 kg, μ = 6/5 = 1.2 kg.

### 3.5 Effective Potential and the Orbit Equation

![An attractive inverse-square effective potential has a minimum and two turning points for the illustrated bound energy. Axes use scaled units.](images/classical/effective_potential.png)

**In simple words:** Conserved angular momentum lets us replace the angular motion by an additional term in the radial energy. We can then read possible radial motion from a one-dimensional energy graph.

For the relative motion, let ℓ = μr²θ̇ be the angular-momentum magnitude. The energy is:

> E = ½μṙ² + V\_eff(r); V\_eff(r) = V(r) + ℓ²/(2μr²).

The added term represents angular kinetic energy at fixed ℓ. It rises strongly at small r for ℓ ≠ 0. Allowed radii satisfy E ≥ V\_eff because radial kinetic energy cannot be negative. Turning points satisfy E = V\_eff. The radial equation is μr̈ = −dV\_eff/dr.

To find the orbit shape, define u = 1/r and use θ as the independent variable. Since θ̇ = ℓu²/μ:

> ṙ = −(ℓ/μ)du/dθ; r̈ = −(ℓ²/μ²)u² d²u/dθ².

The radial force equation μ(r̈ − rθ̇²) = f(r) therefore becomes Binet's equation:

> d²u/dθ² + u = −μ f(1/u)/(ℓ²u²).

For attraction f(r) = −κ/r² with κ &gt; 0, the right side is μκ/ℓ². Hence:

> r(θ) = p/[1 + e cos(θ − θ₀)]; p = ℓ²/(μκ).

The constants e and θ₀ set the eccentricity and orientation. In this attractive inverse-square problem with nonzero ℓ, e² = 1 + 2Eℓ²/(μκ²), where potential energy is zero at infinity.

| Eccentricity | Shape | Energy |
|---|---|---|
| e = 0 | Circle | Negative, at the effective-potential minimum |
| 0 &lt; e &lt; 1 | Ellipse | E &lt; 0 |
| e = 1 | Parabola | E = 0 |
| e &gt; 1 | Hyperbola | E &gt; 0 |

For an ellipse, p = a(1 − e²), r\_min = a(1 − e), r\_max = a(1 + e), and E = −κ/(2a). These classifications concern the inverse-square attractive potential, not every arbitrary central force.

**Worked example.** An ellipse has a = 10 units and e = 0.2. Then its closest radius is 8, its farthest is 12 and p = 9.6. The centre of force lies at a focus, not at the ellipse's centre.

### 3.6 Kepler's Laws and Kepler's Equation

**In simple words:** Gravitational attraction determines both the orbit's geometry and the rate at which the body moves along it.

**First law:** A bound nonradial two-body gravitational orbit is an ellipse in the relative coordinate, with the force centre at a focus. This follows from the conic solution with E &lt; 0. For a light planet orbiting a much heavier star, the relative orbit closely matches the planet's orbit about the star.

**Second law:** The line joining the bodies sweeps equal areas in equal times. A small swept triangle has area dA = ½r²dθ. Therefore dA/dt = ½r²θ̇ = ℓ/(2μ), constant. This law holds for any central force because it follows from angular-momentum conservation, not specifically the inverse-square dependence.

**Third law:** For ellipse semiaxes a and b = a√(1 − e²), the area is πab. Divide it by areal velocity:

> τ = 2πμab/ℓ; τ² = (4π²μ/κ)a³.

For gravity κ = Gm₁m₂ and μ/κ = 1/[G(m₁ + m₂)]. Thus τ² = 4π²a³/[G(m₁ + m₂)]. If a central mass M greatly exceeds the orbiting mass, use τ² ≈ 4π²a³/(GM).

#### Kepler's Equation: Position as a Function of Time

An orbit shape r(θ) does not by itself tell us the time. Introduce the eccentric anomaly 𝓔 by the ellipse parametrisation x = a(cos 𝓔 − e), y = a√(1 − e²)sin 𝓔, with the force centre at the origin. This gives r = a(1 − e cos 𝓔).

The area swept from periapsis is A = (ab/2)(𝓔 − e sin 𝓔). Since area grows uniformly and the total area πab is swept in period τ:

> n(t − t\_p) = 𝓔 − e sin 𝓔; n = 2π/τ.

This is Kepler's equation. t\_p is the time of periapsis passage; the left side is the mean anomaly. Solve for 𝓔, then obtain r and the position. For small e, a first estimate is 𝓔 ≈ n(t − t\_p) + e sin[n(t − t\_p)].

**Worked check.** At periapsis 𝓔 = 0 and r = a(1 − e). Half a period later, 𝓔 = π and r = a(1 + e). In a circular orbit e = 0, the equation reduces to uniform angular motion.

### 3.7 Artificial Satellites

**In simple words:** An orbiting satellite is continuously falling under gravity while its sideways motion prevents it from reaching the surface in the ideal model.

For a circular orbit around a much heavier spherical planet, gravitational acceleration supplies the inward acceleration v²/r:

> v\_c = √(GM/r); τ = 2π√(r³/GM).

The orbital radius r is measured from the planet's centre. If altitude is h and surface radius is R, use r = R + h. The satellite mass cancels from these ideal equations.

The gravitational potential is −GMm/r with zero at infinity. Circular kinetic energy is GMm/(2r), so total energy is E = −GMm/(2r). For threshold escape from radius r with no subsequent propulsion or losses, set E = 0:

> v\_escape = √(2GM/r) = √2 v\_c.

For an elliptical orbit with semimajor axis a, combine E = −GMm/(2a) with E = ½mv² − GMm/r to obtain the vis-viva relation v² = GM(2/r − 1/a).

**Worked satellite example.** Take GM = 3.982 × 10¹⁴ m³/s², R = 6400 km and h = 1600 km. Then r = 8.0 × 10⁶ m. The circular speed is √(3.982 × 10¹⁴/8.0 × 10⁶) = 7055 m/s. The period is 2πr/v ≈ 7125 s, or 1.98 h. The rounded constants determine the precision of the answer.

#### Geostationary Motion

A geostationary satellite stays over one equatorial longitude in the ideal Earth-fixed description. It needs a circular equatorial prograde orbit and a period matching Earth's rotation relative to distant stars: one sidereal day, approximately 86,164 s, or 23 h 56 min 4 s. A 24 h solar day is a close approximation, not the exact rotation period.

Using GM ≈ 3.986 × 10¹⁴ m³/s² gives r ≈ 42,164 km. Subtracting an equatorial radius near 6378 km gives altitude about 35,786 km. A geosynchronous inclined or eccentric orbit has the matching period but is not fixed at one point in the sky. See [ESA's geostationary-orbit description](https://www.esa.int/ESA\_Multimedia/Images/2020/03/Geostationary\_orbit).

**Try it.** If a circular orbital radius increases by a factor of 4, how do speed and period change? **Answer:** Speed halves and period increases by a factor of 8.

### 3.8 Rutherford Scattering

**In simple words:** A beam particle that passes near a charged nucleus is deflected more strongly than one that passes far away. Relate that initial offset to the final angle, then convert beam area into scattering solid angle.

Use the repulsive Coulomb potential V = κ/r, κ = Z₁Z₂e²/(4πε₀) &gt; 0. In the relative coordinate, let incoming speed be v∞, energy E = ½μv∞² and impact parameter b. The **impact parameter (संघट्ट प्राचल)** is the perpendicular distance from the centre to the incoming asymptote. Angular momentum is ℓ = μv∞b. The scattering angle χ is the change between incoming and outgoing velocity directions.

For the repulsive force, Binet's equation has negative constant right side. With closest approach at θ = 0, its solution can be written:

> u = (μκ/ℓ²)(e cos θ − 1); e² = 1 + 2Eℓ²/(μκ²).

At infinity u → 0, so the asymptote angle θ∞ satisfies cos θ∞ = 1/e. The deflection is χ = π − 2θ∞. Therefore sin(χ/2) = cos θ∞ = 1/e. Using e² − 1 = (2Eb/κ)² gives:

> tan(χ/2) = κ/(2Eb); b = (κ/(2E))cot(χ/2).

This is the geometry linking initial offset to scattering angle. Small b gives large deflection; b → 0 gives χ → π.

For a uniform incident beam, particles in an annulus of area dσ = 2πb |db| enter a corresponding angular ring of solid angle dΩ = 2πsin χ |dχ|. Thus:

> dσ/dΩ = (b/sin χ)|db/dχ|.

Differentiate b: |db/dχ| = (κ/(4E))csc²(χ/2). Use sin χ = 2sin(χ/2)cos(χ/2) to simplify:

> dσ/dΩ = (κ/(4E))² / sin⁴(χ/2).

The units are area per steradian. For a target much heavier than the projectile, the laboratory angle and energy approximately match this fixed-centre or centre-of-mass description. For comparable masses, transform the kinematics rather than silently using the same angles.

The formula assumes a nonrelativistic point-Coulomb interaction in the relevant region and single-scattering conditions. Atomic screening matters at very small angles; nuclear-size and other interactions matter at sufficiently close approach. The formula is not a complete model at every angle and energy. The classic observations established concentrated nuclear charge; the simple scattering argument alone does not measure one universal nuclear radius.

### 3.9 Scattering Numericals

#### Impact Parameter

An alpha particle has E = 5 MeV and scatters from gold at χ = 60° in the heavy-target approximation. Use Z₁ = 2, Z₂ = 79 and e²/(4πε₀) ≈ 1.44 MeV·fm. First calculate κ = 2 × 79 × 1.44 = 227.52 MeV·fm. Then:

> b = [227.52/(2 × 5)]cot 30° fm = 39.41 fm.

The MeV units cancel, leaving femtometres. One fm is 10⁻¹⁵ m. The incoming asymptote misses the centre by this distance; it is not the closest actual separation.

#### Closest Approach

For a head-on encounter, b = 0 and ℓ = 0. At the turning point all relative kinetic energy has become potential energy, so r\_min = κ/E = 45.50 fm in this example. For b ≠ 0, set radial velocity to zero in the full energy:

> E = ℓ²/(2μr\_min²) + κ/r\_min.

Since ℓ²/(2μ) = Eb², solve Er\_min² − κr\_min − Eb² = 0. The positive root is r\_min = κ/(2E) + √[(κ/(2E))² + b²]. For b = 39.41 fm it is about 68.26 fm. Angular motion still exists at this radial turning point.

#### Comparing Cross-Sections

At fixed E and charges, compare χ = 30° with 90°. The ratio is sin⁴45°/sin⁴15° = 0.25/0.004487 ≈ 55.7. The differential cross-section near 30° is about 56 times the value near 90°. This compares equal small solid-angle acceptances, not arbitrary detector areas at different distances.

**Try it.** Double E while keeping χ fixed. **Answer:** The differential cross-section falls to one quarter. The impact parameter for that same angle halves.

### 3.10 Stability of Circular Orbits and Orbit Closure

**In simple words:** A circular orbit requires an exact radial balance. Stability asks whether a small radial disturbance stays small. Closure asks whether an orbit eventually repeats its shape and motion. They are different questions.

At fixed nonzero ℓ, circular radius r₀ satisfies V\_eff′(r₀) = 0, or V′(r₀) = ℓ²/(μr₀³). A small radial displacement η obeys μ η̈ + V\_eff″(r₀)η = 0. Thus the radial oscillation frequency satisfies:

> ω\_r² = [V″(r₀) + 3V′(r₀)/r₀]/μ.

Positive ω\_r² gives linear radial stability. Negative ω\_r² gives instability. Zero curvature needs further analysis.

**Power-law force example.** For f(r) = −a/rⁿ with a &gt; 0, V′ = a/rⁿ and V″ = −na/rⁿ⁺¹. Hence ω\_r² = (3 − n)a/(μr₀ⁿ⁺¹). The circular orbit is linearly stable for n &lt; 3, unstable for n &gt; 3, and marginal at this order for n = 3. The angular frequency of the circular orbit obeys ω\_θ² = a/(μr₀ⁿ⁺¹). Their near-circular ratio is √(3 − n).

For small radial oscillations, the azimuth gained in one radial period is approximately Δθ = 2πω\_θ/ω\_r. A rational frequency ratio permits closure in this approximation; an irrational ratio produces a precessing pattern rather than exact repetition. For a general finite-amplitude orbit, use the full radial integral:

> Δθ = 2∫ from r\_min to r\_max [ℓ/(r²√(2μ(E − V\_eff(r))))] dr.

The full orbit closes when Δθ/(2π) is rational. Bertrand's theorem identifies the attractive inverse-square and isotropic harmonic-oscillator potentials as the special smooth central-force cases in which all bounded noncollision orbits are closed. This statement is much stronger than saying one particular orbit closes.

**Checks.** Inverse-square attraction has n = 2, so ω\_r = ω\_θ and the ellipse closes. The isotropic oscillator force has n = −1, so ω\_r = 2ω\_θ; two radial cycles occur per revolution. Its ellipse is centred on the force centre, unlike the gravitational ellipse with the centre at a focus.

## भाग 3: Put the Ideas Together

### Read a Gravitational Effective Potential

For V = −κ/r, V\_eff = −κ/r + ℓ²/(2μr²). As r → 0, the positive inverse-square term dominates and the effective potential rises. As r → ∞, it approaches zero from below. The minimum occurs at r₀ = ℓ²/(μκ), with E\_min = −μκ²/(2ℓ²).

At E = E\_min the orbit is circular. Between E\_min and zero there are two radial turning points and a bound ellipse. At E = 0 there is an escape parabola. At positive E the particle can come from infinity and return there on a hyperbola. These conclusions follow from the graph and the allowed-energy inequality before solving the orbit equation.

### Reading a Motion Diagram

In an orbit sketch, mark the force centre, a radius r, the tangent velocity and the orbital plane. In a scattering sketch, mark the incoming asymptote, b, closest approach and χ. In a rotating-frame sketch, mark Ω and v\_rot before taking a cross product. An unlabelled sketch often conceals the very sign or angle that the calculation needs.

## भाग 4: Check Your Understanding

### 3.11 Common Mistakes and Their Corrections

- Coriolis force uses velocity relative to the rotating frame.
- Centrifugal distance is measured from the rotation axis.
- “Rightward deflection in the north” describes the horizontal-flow approximation, not every possible three-dimensional velocity.
- At the equator, the horizontal Coriolis parameter vanishes; the full vector force need not vanish.
- Use reduced mass for relative two-body motion and total mass for centre-of-mass translation.
- The energy–eccentricity table needs the attractive inverse-square assumptions.
- Circular-orbit existence, stability and general orbit closure are separate tests.
- Use radius from the centre in satellite formulas, not altitude alone.
- A geostationary period is one sidereal day; 24 h is an approximation.
- Do not confuse scattering angle, its half-angle, impact parameter and closest approach.

**Explain without calculating.** Why does a planet speed up near periapsis? Conservation of ℓ makes r²θ̇ constant and the tangential speed ℓ/(μr) larger at smaller r. Why can an orbit be stable but not closed? Bounded disturbances need not bring radial and angular phases back into alignment after a finite number of cycles.

## भाग 5: Practice Questions with Explanations

#### Question U3-01

Why does a vector derivative gain Ω × A in rotating axes?

- **A.** The vector mass changes
- **B.** The vector loses magnitude
- **C.** The basis vectors rotate
- **D.** Time stops

**Answer: C.** Differentiate the components and the changing basis separately.

#### Question U3-02

Which relative velocity enters the Coriolis force?

- **A.** Only centre-of-mass velocity
- **B.** Only the platform rim velocity
- **C.** Only inertial velocity without transformation
- **D.** Velocity measured in the rotating frame

**Answer: D.** The extra term is −2mΩ × v\_rot after transforming the acceleration.

#### Question U3-03

An object rests relative to a uniformly rotating platform. Its Coriolis force is what?

- **A.** Zero
- **B.** Always mΩ²r
- **C.** Always 2mΩ²r
- **D.** Equal to its weight

**Answer: A.** Its rotating-frame velocity is zero even though its inertial velocity need not be.

#### Question U3-04

What distance enters the centrifugal magnitude mΩ²r\_perpendicular?

- **A.** Distance from any chosen origin
- **B.** Distance from the rotation axis
- **C.** Height above the ground
- **D.** Total path length

**Answer: B.** Only the component perpendicular to the axis contributes to the double cross product.

#### Question U3-05

Which term appears when Ω changes with time?

- **A.** −mΩ × v only
- **B.** +mΩ²r always inward
- **C.** −mΩ̇ × r
- **D.** −mṙ

**Answer: C.** The Euler force comes from differentiating the angular velocity.

#### Question U3-06

An accelerating frame origin contributes which inertial term?

- **A.** +ma₀
- **B.** −mv
- **C.** mΩ²
- **D.** −ma₀

**Answer: D.** Moving the origin acceleration from the acceleration side to the force side gives the negative sign.

#### Question U3-07

For Ω along +z and v\_rot along +x, Coriolis force points where?

- **A.** −y
- **B.** +y
- **C.** +x
- **D.** +z

**Answer: A.** The cross product Ω × v is +y, and the force has an overall minus sign.

#### Question U3-08

For m = 1 kg, Ω = 2 s⁻¹ and perpendicular v\_rot = 0.3 m/s, the Coriolis magnitude is what?

- **A.** 0.6 N
- **B.** 1.2 N
- **C.** 0.15 N
- **D.** 2.3 N

**Answer: B.** Use 2mΩv for perpendicular vectors.

#### Question U3-09

Why does the Coriolis term do no instantaneous work in its rotating description?

- **A.** It is always absent
- **B.** It points along the radius
- **C.** It is perpendicular to relative velocity
- **D.** It equals gravity

**Answer: C.** Its power is (−2mΩ × v\_rot) · v\_rot = 0.

#### Question U3-10

For horizontal motion in the northern hemisphere, the usual horizontal Coriolis deflection is to which side?

- **A.** Left
- **B.** Always north
- **C.** Always east
- **D.** Right

**Answer: D.** The vertical component Ω sin λ determines the horizontal deflection.

#### Question U3-11

At the equator, which statement is correct?

- **A.** The horizontal parameter f = 2Ω sin λ vanishes
- **B.** Every three-dimensional Coriolis force vanishes
- **C.** Earth stops rotating
- **D.** Centrifugal force vanishes everywhere

**Answer: A.** The full Ω vector still has a horizontal component, which can couple to vertical motion.

#### Question U3-12

At latitude 30°, what is the ideal Foucault precession period magnitude?

- **A.** Half a sidereal day
- **B.** Two sidereal days
- **C.** One hour
- **D.** Zero

**Answer: B.** The precession rate is Ω sin 30° = Ω/2.

#### Question U3-13

A body dropped from rest relative to Earth has a first-order Coriolis deflection in which direction?

- **A.** West
- **B.** North everywhere
- **C.** East
- **D.** Towards the rotation axis everywhere

**Answer: C.** The downward leading velocity gives an eastward acceleration 2Ωgt cos λ.

#### Question U3-14

For that drop, displacement grows with which power of leading fall time?

- **A.** t
- **B.** t²
- **C.** t⁻¹
- **D.** t³

**Answer: D.** The Coriolis acceleration grows as t and is integrated twice.

#### Question U3-15

At a rotating orbital equilibrium point, a body stationary in that frame has what Coriolis force?

- **A.** Zero
- **B.** Maximum possible
- **C.** Equal to centrifugal force necessarily
- **D.** Equal to gravity necessarily

**Answer: A.** Coriolis depends on the body's relative velocity, which is zero at rest.

#### Question U3-16

A central force depends on what and points in which direction?

- **A.** Time only, always upward
- **B.** Separation, along the separation
- **C.** Speed only, along velocity
- **D.** Temperature only, towards north

**Answer: B.** A central force has the form f(r)r̂ in the model used here.

#### Question U3-17

Why is central-force angular momentum conserved?

- **A.** The force is always zero
- **B.** The energy is always positive
- **C.** Torque about the force centre is zero
- **D.** The orbit is always circular

**Answer: C.** The cross product of r with a parallel or antiparallel force vanishes.

#### Question U3-18

For nonzero angular momentum, central-force motion lies where?

- **A.** On every plane in turn
- **B.** Only on a straight line
- **C.** Only on a sphere
- **D.** In a fixed plane

**Answer: D.** Both r and v remain perpendicular to the conserved angular-momentum vector.

#### Question U3-19

What is the reduced mass of two equal masses m?

- **A.** m/2
- **B.** 2m
- **C.** m²
- **D.** Zero

**Answer: A.** Substituting in μ = m₁m₂/(m₁ + m₂) gives m²/(2m).

#### Question U3-20

For masses 2 kg and 3 kg, the reduced mass is what?

- **A.** 5 kg
- **B.** 1.2 kg
- **C.** 6 kg
- **D.** 0.5 kg

**Answer: B.** Their product divided by their sum is 6/5 kg.

#### Question U3-21

With no external force, the two-body centre of mass does what?

- **A.** Always stays at the origin
- **B.** Orbits the lighter mass
- **C.** Moves uniformly
- **D.** Accelerates with reduced mass

**Answer: C.** Its acceleration is zero; its initial velocity may be nonzero.

#### Question U3-22

At fixed angular momentum ℓ, the effective potential is what?

- **A.** V − ℓ²/(2μr²)
- **B.** V + ℓr
- **C.** V/μ
- **D.** V + ℓ²/(2μr²)

**Answer: D.** The added positive term is the angular kinetic energy expressed at fixed ℓ.

#### Question U3-23

Which inequality identifies allowed radial positions?

- **A.** E ≥ V\_eff
- **B.** E &lt; V\_eff
- **C.** E = 0 always
- **D.** V\_eff &gt; 0 always

**Answer: A.** The difference E − V\_eff equals nonnegative radial kinetic energy.

#### Question U3-24

At a radial turning point, which quantity vanishes?

- **A.** Total speed necessarily
- **B.** Radial velocity
- **C.** Angular momentum necessarily
- **D.** Potential energy necessarily

**Answer: B.** Angular motion can persist even when ṙ = 0.

#### Question U3-25

For inverse-square attraction, what substitution simplifies the orbit equation?

- **A.** u = r²
- **B.** u = ln t
- **C.** u = 1/r
- **D.** u = E/r

**Answer: C.** The Binet equation becomes a linear equation in u(θ).

#### Question U3-26

For an attractive inverse-square nonradial orbit with E &lt; 0, which shape is possible?

- **A.** Only hyperbola
- **B.** Only parabola
- **C.** Every arbitrary spiral
- **D.** Ellipse including a circle

**Answer: D.** The eccentricity relation gives 0 ≤ e &lt; 1 for allowed bound energies.

#### Question U3-27

Where is the gravitational force centre in a Kepler ellipse?

- **A.** At a focus
- **B.** Always at its geometric centre
- **C.** At every point of the major axis
- **D.** On the minor-axis endpoint

**Answer: A.** The polar conic is written with the force centre at a focus.

#### Question U3-28

An ellipse has a = 10 and e = 0.2. Its closest radius is what?

- **A.** 10
- **B.** 8
- **C.** 12
- **D.** 2

**Answer: B.** Periapsis radius is a(1 − e).

#### Question U3-29

What conservation law gives Kepler's equal-area law?

- **A.** Kinetic energy alone
- **B.** Linear momentum of the planet alone
- **C.** Angular momentum
- **D.** Zero total energy

**Answer: C.** Areal velocity is ℓ/(2μ), constant for a central interaction.

#### Question U3-30

For an exact two-body gravitational relative orbit, the period involves which mass?

- **A.** Only μ in the denominator of G
- **B.** m₁ − m₂
- **C.** The smaller mass alone
- **D.** m₁ + m₂

**Answer: D.** Using μ/κ = 1/[G(m₁ + m₂)] gives the exact period relation.

#### Question U3-31

Which is Kepler's equation for an ellipse?

- **A.** n(t − t\_p) = 𝓔 − e sin 𝓔
- **B.** n(t − t\_p) = e + 𝓔²
- **C.** r = at
- **D.** 𝓔 = E/t

**Answer: A.** It follows by equating swept ellipse area with uniform areal growth.

#### Question U3-32

For e = 0, Kepler's equation describes what?

- **A.** An escaping parabola
- **B.** Uniform circular angular motion
- **C.** A stopped satellite
- **D.** A radial collision

**Answer: B.** The eccentric-anomaly correction vanishes in the circular limit.

#### Question U3-33

Which radius belongs in the circular satellite-speed formula?

- **A.** Altitude alone
- **B.** Planet diameter plus altitude
- **C.** Planet radius plus altitude
- **D.** Orbit circumference

**Answer: C.** The gravitational force depends on separation from the planet's centre.

#### Question U3-34

Increasing a circular orbital radius by a factor of 4 changes speed by which factor?

- **A.** 2
- **B.** 4
- **C.** 1/4
- **D.** 1/2

**Answer: D.** Circular speed scales as r⁻¹ᐟ².

#### Question U3-35

The threshold escape speed at radius r compared with circular speed there is what?

- **A.** √2 times
- **B.** Twice
- **C.** Half
- **D.** The same

**Answer: A.** Set the total energy to zero instead of its negative circular value.

#### Question U3-36

What period must an ideal geostationary satellite match?

- **A.** Exactly 24 solar hours
- **B.** One sidereal day
- **C.** One lunar month
- **D.** One year

**Answer: B.** Its angular speed must match Earth's rotation relative to distant stars.

#### Question U3-37

Which orbit can be geostationary?

- **A.** Any inclined orbit with a 24 h period
- **B.** Any polar circle
- **C.** Circular equatorial prograde
- **D.** Any retrograde ellipse

**Answer: C.** The orbit must keep both latitude and longitude fixed in the Earth-fixed idealisation.

#### Question U3-38

Impact parameter means what?

- **A.** Actual closest separation
- **B.** Nuclear radius
- **C.** Final detector distance
- **D.** Offset of the incoming asymptote from the force centre

**Answer: D.** It labels the incoming trajectory before the force has significantly deflected it.

#### Question U3-39

For repulsive Coulomb scattering at fixed E, which encounter gives the greatest deflection?

- **A.** Smallest b
- **B.** Largest b
- **C.** Largest positive radius at infinity
- **D.** Every b gives the same angle

**Answer: A.** The relation tan(χ/2) = κ/(2Eb) increases as b decreases.

#### Question U3-40

The Rutherford cross-section contains which angular factor?

- **A.** 1/sin²χ
- **B.** 1/sin⁴(χ/2)
- **C.** sin⁴χ
- **D.** cos χ

**Answer: B.** Differentiating the impact-parameter relation produces the half-angle fourth power.

#### Question U3-41

If the beam energy doubles at fixed angle and charges, the Rutherford differential cross-section becomes what?

- **A.** One half
- **B.** Twice
- **C.** One quarter
- **D.** Four times

**Answer: C.** The cross-section is proportional to E⁻² in the stated model.

#### Question U3-42

For head-on repulsive scattering, closest approach is what?

- **A.** κ/(2E)
- **B.** 2κ/E
- **C.** Zero
- **D.** κ/E

**Answer: D.** With zero angular momentum, the turning-point energy is entirely κ/r\_min.

#### Question U3-43

A circular central-force orbit is linearly radially stable when which condition holds?

- **A.** V\_eff″(r₀) &gt; 0
- **B.** V\_eff″(r₀) &lt; 0
- **C.** V\_eff(r₀) = 0
- **D.** ℓ = 0 necessarily

**Answer: A.** A local effective-potential minimum produces a restoring radial force.

#### Question U3-44

For f = −a/rⁿ, which range gives linear circular-orbit radial stability?

- **A.** n &gt; 3
- **B.** n &lt; 3
- **C.** Only n = 3
- **D.** All n

**Answer: B.** The radial frequency squared is proportional to 3 − n.

#### Question U3-45

Does stability by itself guarantee a closed orbit?

- **A.** Yes for every central potential
- **B.** Only if energy is positive
- **C.** No, radial and angular phases must also repeat
- **D.** Only if mass is one

**Answer: C.** A stable bound path can precess without ever exactly repeating.


## भाग 6: Quick Revision and Terminology

### 6.1 Sixty Revision Points

1. A rotating basis contributes Ω × A to an inertial vector derivative.
2. For coincident origins, v\_in = v\_rot + Ω × r.
3. The Coriolis acceleration term is 2Ω × v\_rot.
4. The centrifugal force is −mΩ × (Ω × r).
5. The Euler force is −mΩ̇ × r.
6. An accelerating origin contributes inertial force −ma₀.
7. Inertial forces describe the chosen noninertial frame.
8. Centrifugal magnitude uses distance from the rotation axis.
9. Coriolis force vanishes for zero relative velocity.
10. Coriolis force also vanishes for relative velocity parallel to Ω.
11. The Coriolis term alone does zero power in the rotating frame.
12. The right-hand rule and the overall minus sign determine Coriolis direction.
13. Earth's horizontal Coriolis parameter is f = 2Ω sin λ.
14. Horizontal flow deflects right in the northern hemisphere and left in the southern.
15. The full vector Coriolis force need not vanish at the equator.
16. Ideal Foucault precession-rate magnitude is Ω times the absolute value of sin λ.
17. Polar Foucault precession takes one sidereal day.
18. The leading Foucault precession vanishes at the equator.
19. A dropped body has first-order eastward Coriolis deflection.
20. The leading free-fall time is √(2h/g).
21. The eastward drop displacement is Ωgt³cos λ/3 in the stated approximation.
22. Use the unperturbed trajectory when computing a first-order small correction.
23. A stationary body in a co-rotating astronomical frame has no Coriolis force.
24. A central force is directed along the separation vector.
25. The torque of a central force about its centre is zero.
26. Nonradial central-force motion stays in a fixed plane.
27. Zero-angular-momentum central motion is radial.
28. The two-body centre of mass uses total mass M.
29. Relative two-body motion uses μ = m₁m₂/(m₁ + m₂).
30. For equal masses m, the reduced mass is m/2.
31. For one very heavy mass, μ approaches the lighter mass.
32. Relative kinetic energy in polar coordinates is ½μ(ṙ² + r²θ̇²).
33. The relative angular momentum magnitude is ℓ = μr²θ̇.
34. At fixed ℓ, V\_eff = V + ℓ²/(2μr²).
35. Allowed radii satisfy E ≥ V\_eff.
36. Radial turning points satisfy E = V\_eff.
37. At a radial turning point, angular motion may continue.
38. Binet's substitution is u = 1/r with θ as the independent variable.
39. Attractive inverse-square nonradial paths are conic sections.
40. The inverse-square eccentricity relation is e² = 1 + 2Eℓ²/(μκ²).
41. For attractive inverse-square motion, negative energy gives a circle or ellipse.
42. Zero energy gives the escape parabola and positive energy a hyperbola.
43. The force centre lies at a focus of a gravitational ellipse.
44. Elliptical closest and farthest radii are a(1 − e) and a(1 + e).
45. Gravitational ellipse energy is −κ/(2a).
46. The areal velocity ℓ/(2μ) is constant for any central force.
47. The exact gravitational relative-orbit period uses m₁ + m₂.
48. Kepler's equation connects mean anomaly to eccentric anomaly.
49. Satellite formulas use orbital radius from the planetary centre.
50. Circular orbital speed scales as r⁻¹ᐟ² and period as r³ᐟ².
51. Threshold escape speed is √2 times circular speed at the same radius.
52. Geostationary motion requires circular equatorial prograde motion with sidereal period.
53. Impact parameter is the incoming asymptote offset, not closest approach.
54. Repulsive Coulomb scattering obeys b = κ cot(χ/2)/(2E).
55. Rutherford differential cross-section varies as E⁻² and csc⁴(χ/2).
56. Head-on repulsive closest approach is κ/E.
57. A circular orbit requires V\_eff′(r₀) = 0.
58. Positive V\_eff″ gives linear radial stability; zero needs more analysis.
59. For force −a/rⁿ, linear circular-orbit stability requires n &lt; 3.
60. Stable motion need not close; orbit closure also requires repeating radial and angular phases.

### 6.2 Hindi-Supported Glossary

| English term | Hindi aid | Meaning in this unit |
|---|---|---|
| Inertial frame | जड़त्वीय निर्देश तंत्र | Frame in which unmodified Newtonian equations apply |
| Rotating frame | घूर्णनशील निर्देश तंत्र | Description using axes that rotate |
| Centrifugal force | अपकेंद्री बल | Rotation-dependent outward inertial-force term |
| Coriolis force | कोरिऑलिस बल | Inertial term depending on relative velocity |
| Central force | केंद्रीय बल | Force along the separation with magnitude depending on it |
| Reduced mass | अपचयित द्रव्यमान | Effective mass of relative two-body motion |
| Effective potential | प्रभावी स्थितिज ऊर्जा | Potential plus angular-energy term at fixed ℓ |
| Turning point | प्रत्यावर्तन बिंदु | Radius at which radial velocity is zero |
| Eccentricity | उत्केन्द्रता | Parameter describing departure from a circular conic |
| Periapsis | निकटतम कक्षीय बिंदु | Closest orbital point to the force centre |
| Sidereal day | नाक्षत्र दिवस | Earth's rotation period relative to distant stars |
| Impact parameter | संघट्ट प्राचल | Offset of the incoming asymptote |
| Cross-section | अनुप्रस्थ परिच्छेद | Effective beam area associated with a scattering outcome |
| Stability | स्थायित्व | Small perturbations remain small in the stated sense |
| Closed orbit | बंद कक्षा | Orbit repeating after a finite time |

### 6.3 Formula Sheet with Conditions

| Result | Conditions |
|---|---|
| F\_C = −2mΩ × v\_rot | Rotating-frame velocity |
| F\_cf = −mΩ × (Ω × r) | Centrifugal term; use distance to axis for magnitude |
| d\_east = Ωg t³ cos λ/3 | First order in Ω, drop from rest, no drag, local constant g |
| μ = m₁m₂/(m₁ + m₂) | Relative two-body description |
| V\_eff = V + ℓ²/(2μr²) | Central potential at fixed ℓ |
| u″ + u = −μf(1/u)/(ℓ²u²) | Nonradial central motion; prime means θ derivative |
| r = p/(1 + e cos θ), p = ℓ²/(μκ) | Attractive inverse-square interaction, chosen apsidal axis |
| τ² = 4π²a³/[G(m₁ + m₂)] | Relative gravitational ellipse |
| n(t − t\_p) = 𝓔 − e sin 𝓔 | Elliptical Kepler motion |
| v\_c = √(GM/r); v\_escape = √(2GM/r) | Ideal central gravity, heavy primary |
| b = κ cot(χ/2)/(2E) | Repulsive Coulomb relative scattering |
| dσ/dΩ = (κ/(4E))²csc⁴(χ/2) | Rutherford assumptions and correct frame |
| V\_eff′(r₀) = 0; V\_eff″(r₀) &gt; 0 | Circular orbit and linear radial stability |

---


# Appendix 1: A Practical Study Route

## When You Are Learning the Course

Begin with the readiness check. Keep a small notation page and add a symbol only after writing its meaning and units. Study one main topic at a time. A useful session contains explanation, one calculation done with help, the same calculation done independently, and one nearby problem.

In Unit 1, spend extra practice on choosing coordinates and constructing energies. Then repeat a complete pendulum or spring calculation until you can explain each derivative. Move to the Atwood machine and rotating rod to see what changes when constraints or coordinates change.

In Unit 2, describe one oscillator using L, H and a phase ellipse. Use a simple canonical scaling before tackling generating functions. Practise Poisson brackets by differentiating explicitly. Learn the free-particle HJ example before the oscillator example. For normal modes, calculate the energy of each collective pattern rather than memorising its frequency alone.

In Unit 3, draw every vector-direction problem. Separate the frame calculation from the physical-force calculation. Use the effective potential to classify a gravitational orbit, then derive the conic. Keep satellite radius distinct from altitude and scattering offset distinct from closest approach.

## If Only Three Revision Days Remain

This schedule assumes you have already studied the course. It cannot replace first-time learning of all prerequisites.

| Day | Main revision | Independent work |
|---|---|---|
| 1 | Constraints, D'Alembert, Lagrange applications, conservation and open systems | Derive the pendulum equation; solve an Atwood and rocket problem; explain one conservation condition |
| 2 | Hamilton equations, canonical maps, Poisson brackets, HJ and normal modes | Construct an oscillator H; test two maps; solve two coupled oscillators; write the free-particle principal function |
| 3 | Rotating frames, central orbits, stability, satellites and scattering | Reconstruct the acceleration transformation; derive the area law; solve one satellite and one scattering example |

At the end of each day, use the unit practice questions to identify misunderstandings. Correct them in your notes. Do not infer that an easy question guarantees a similar examination question. Use current departmental guidance and authenticated papers to understand the examination format.


# Appendix 2: Extended Model Questions and Solution Routes

These questions are original practice material. The solution routes identify the steps needed; the main text supplies the complete derivations and worked examples. No question here is labelled as an authenticated previous-year question.

## Unit 1

**1. Derive Lagrange's equations from D'Alembert's principle.** State fixed masses, ideal constraints and independent holonomic coordinates. Express δrᵢ through δqⱼ, identify Qⱼ, use the kinetic-energy derivative identity, and set the coefficients of the independent virtual displacements to zero. For a position-dependent potential, substitute Qⱼ = −∂V/∂qⱼ to obtain the L equation. See section 1.8.

**2. Apply Lagrange's equation to a planar pendulum.** Choose angle from the downward vertical, find T and the rise l(1 − cos θ), and display all three derivatives in the equation. Obtain θ̈ + (g/l)sin θ = 0 before using the small-angle limit. State why tension is absent. See section 1.9.

**3. Derive the rocket equation and discuss its limits.** Follow the momentum of the rocket and emitted fuel over dt. Retain the exhaust velocity relative to the rocket, drop only second-order differentials, and include any external impulse. Integrate only after stating constant u and the external-force assumption. See section 1.4.

**4. Explain the energy function and give a case where it differs from mechanical energy.** Define h, differentiate along Euler–Lagrange motion and show ḣ = −∂L/∂t. Use the rotating-rod example to distinguish its constant h from the bead's increasing kinetic energy. See section 1.11 and Part 3 of Unit 1.

**5. Demonstrate Galilean invariance for a closed interacting system.** Expand velocities shifted by constant u, show that relative separations are unchanged, and identify F = −u · Σmᵢrᵢ + ½Mu²t whose derivative is L′ − L. Conclude that the Euler–Lagrange equations are unchanged. See section 1.11.

## Unit 2

**6. Derive Hamilton's equations by a Legendre transformation.** Define p, solve for q̇, form H, take its differential, cancel velocity differentials, use Lagrange's equations, and compare independent dq,dp,dt coefficients. Apply the result to the oscillator. See section 2.3.

**7. Obtain the four generating-function relations.** Start with the differential action relation for F₁. Use F₂ = F₁ + ΣPQ, F₃ = F₁ − Σpq and F₄ = F₁ − Σpq + ΣPQ. Differentiate each to read the signs, and retain the explicit time derivative in K. See section 2.6.

**8. Establish Poisson's theorem and apply it to angular momentum.** Derive df/dt from the chain rule and Hamilton equations. Use Jacobi to show the bracket of two conserved functions is conserved. Calculate {Jₓ,Jᵧ} explicitly before using the cyclic algebra. See sections 2.8–2.9.

**9. Explain principal and characteristic functions and solve the free particle.** Derive the HJ equation by choosing a type-2 generator with K = 0. Check S = αq − α²t/(2m), obtain p = α and β = q − αt/m, and recover uniform motion. State the autonomous separation S = W − Et. See section 2.10.

**10. Find the frequencies and normal coordinates of two coupled equal masses.** Construct both energies, differentiate the middle-spring term carefully, form the determinant, find the symmetric and antisymmetric eigenvectors, and substitute Q₊,Q₋ to show the decoupled energies. See sections 2.11–2.12.

**11. Explain the group property and infinitesimal generators.** State identity, inverse and associative composition, then use bracket preservation or the Jacobian identity to establish closure under composition. Differentiate F₂ = ΣqP + εG and verify translations with G = pₓ and rotations with G = J\_z. See sections 2.13–2.14.

## Unit 3

**12. Derive the general rotating-frame acceleration relation.** Differentiate a vector in a rotating basis, apply it to position and velocity, and retain origin acceleration and changing Ω when relevant. State the assumptions under which those terms vanish. Identify every inertial force. See sections 3.1–3.2.

**13. Estimate the eastward deflection of a falling body.** Set east–north–up axes, write local Ω, insert the leading downward velocity −gt, and integrate the eastward acceleration twice. Use the leading fall time and state the first-order approximation. See section 3.3.

**14. Reduce the two-body problem and derive the Kepler orbit.** Invert R,r to express both positions, split T into total and reduced masses, use conserved ℓ, and derive Binet's equation with u = 1/r. For inverse-square attraction obtain the conic and classify its energy. See sections 3.4–3.5.

**15. Derive Kepler's area and period laws and explain Kepler's equation.** Use dA/dt = ℓ/(2μ), divide the ellipse area by this rate, and substitute the gravitational parameters. Introduce the eccentric anomaly to convert swept area into n(t − t\_p) = 𝓔 − e sin 𝓔. See section 3.6.

**16. Discuss circular-orbit stability and closure.** Find the stationary effective-potential radius, expand to second order and examine its curvature. For −a/rⁿ show the factor 3 − n. Distinguish this local test from the full orbit-closure condition and the scope of Bertrand's theorem. See section 3.10.

**17. Derive Rutherford's differential cross-section.** Specify the repulsive Coulomb potential and reference frame, derive b = κ cot(χ/2)/(2E) from the hyperbolic orbit, compare incident annulus area with scattered solid angle, differentiate b and simplify the half-angle factors. Discuss the approximation limits. See sections 3.8–3.9.

**18. A satellite at radius r has its circular speed increased instantaneously to escape speed. Compare its energies.** Before the impulse, E\_i = −GMm/(2r); after it, E\_f = 0. The kinetic-energy increase is GMm/(2r), and speed changes from √(GM/r) to √(2GM/r). This is an ideal tangential impulse with no losses; the later path has zero Kepler energy. See section 3.7.


# Appendix 3: References and Further Reading

## Course References

The official syllabus lists N. C. Rana and P. S. Joag, *Classical Mechanics*; H. Goldstein, *Classical Mechanics*; A. Sommerfeld, *Mechanics*; I. Percival and D. Richards, *Introduction to Dynamics*; and D. E. Rutherford, *Classical Mechanics*. Use a library edition compatible with your lecturer's notation. Goldstein, Poole and Safko's later edition is also useful for advanced study. These are reading references; the numerical examples and teaching prose here are independently written.

## Online Checks and Learning Resources

- [MGSU programme brochure](https://www.mgsubikaner.ac.in/PDF/68c7df9cd7f02.pdf): course coverage and the published examination context. The brochure's general assessment prose and semester table differ, as noted in the preface.
- [David Tong: Classical Dynamics](https://www.damtp.cam.ac.uk/user/tong/dynamics.htm): further study of variational, Lagrangian and Hamiltonian methods.
- [MIT OpenCourseWare: Central Force Motion and Orbits](https://ocw.mit.edu/courses/16-07-dynamics-fall-2009/resources/mit16\_07f09\_lec16/): orbit geometry and energy-based analysis.
- [INFLIBNET: Central Force Motion II](https://ebooks.inflibnet.ac.in/phyp01/chapter/central-force-motion-ii/): additional reading on circular-orbit stability and closure.
- [TU Delft: Scattering](https://qiweb.tudelft.nl/mecharela/scattering/): further treatment of classical central-force scattering.
- [ESA: Geostationary Orbit](https://www.esa.int/ESA\_Multimedia/Images/2020/03/Geostationary\_orbit): the sidereal period and orbital requirements.

## A Final Learning Check

You are ready to move on when you can choose coordinates for a new setup, construct its energies, justify the equation you use, follow the units through a calculation, and explain the answer in ordinary English. Use the Hindi meanings when they help recall the idea, then practise expressing it with its English technical term.

**End of Classical Mechanics guide.**
