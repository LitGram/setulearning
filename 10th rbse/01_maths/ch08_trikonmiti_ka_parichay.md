# अध्याय 8: त्रिकोणमिति का परिचय (Introduction to Trigonometry) — स्मार्ट अध्ययन मार्गदर्शिका

**विषय:** गणित (Mathematics) | **विषय कोड:** 09  
**कक्षा:** 10वीं (माध्यमिक शिक्षा बोर्ड राजस्थान, अजमेर — RBSE)  
**अध्याय ID:** `math_ch08` | **इकाई:** त्रिकोणमिति (Trigonometry)  
**निर्धारित अंक भार:** 8 अंक (Board Exam Weightage: 8 Marks)  
**प्रश्न-प्रारूप:** इस अध्याय का निर्धारित भार 8 अंक है। प्रश्नों की संख्या और प्रकार परीक्षा-वर्ष के अनुसार बदल सकते हैं; कोई निश्चित प्रारूप नहीं है।

---

## 🌟 स्मार्ट गाइड प्रवेश: 10 सेकंड में अध्याय का सार

> **अध्यापक की सलाह:** इस अध्याय में समकोण त्रिभुज के अनुपात, विशिष्ट कोणों के मान और त्रिकोणमितीय सर्वसमिकाओं का अभ्यास करें:
> 1. समकोण त्रिभुज में 'लाल / कका' (LAL / KKA) से 6 अनुपात।  
> 2. विशिष्ट कोणों ($0^\circ, 30^\circ, 45^\circ, 60^\circ, 90^\circ$) की 30-सेकंड फिंगर-ट्रिक मान सारणी।  
> 3. सर्वसमिका सिद्ध करने का 1 जादुई नियम: **"सब कुछ $\sin$ और $\cos$ में बदल दो!"**  
> इन अवधारणाओं का अभ्यास अध्याय की तैयारी में मदद करेगा; किसी अंक या प्रश्न-प्रकार की गारंटी नहीं होती।

---

## 1. कॉन्सेप्ट एट अ ग्लांस (Concept at a Glance: 5-Minute Mind Map)

### 1.1 समकोण त्रिभुज एवं 6 त्रिकोणमितीय अनुपात
समकोण त्रिभुज $ABC$ में (जहाँ $\angle B = 90^\circ$):
* न्यूनकोण $\theta$ के ठीक सामने वाली भुजा = **लंब ($L$)** (Perpendicular)
* समकोण ($90^\circ$) के सामने वाली सबसे बड़ी भुजा = **कर्ण ($K$)** (Hypotenuse)
* $\theta$ से सटी तीसरी भुजा = **आधार ($A$)** (Base)

```
        A
        | \
 लंब (L)|  \ कर्ण (K)
        |   \
        B----C (कोण θ)
         आधार (A)
```

$$\text{पाइथागोरस प्रमेय: } \mathbf{K^2 = L^2 + A^2} \quad (\text{कर्ण}^2 = \text{लंब}^2 + \text{आधार}^2)$$

### 🎯 'लाल / कका' (LAL / KKA) याद रखने का अचूक सूत्र:

$$\mathbf{\frac{\text{L}}{\text{K}} = \sin\theta, \quad \frac{\text{A}}{\text{K}} = \cos\theta, \quad \frac{\text{L}}{\text{A}} = \tan\theta}$$
$$\mathbf{\frac{\text{K}}{\text{L}} = \csc\theta, \quad \frac{\text{K}}{\text{A}} = \sec\theta, \quad \frac{\text{A}}{\text{L}} = \cot\theta}$$

### 1.2 व्युत्क्रम एवं भागफल संबंध (Reciprocal & Quotient Relations)
* $\csc\theta = \frac{1}{\sin\theta} \iff \sin\theta \cdot \csc\theta = 1$
* $\sec\theta = \frac{1}{\cos\theta} \iff \cos\theta \cdot \sec\theta = 1$
* $\cot\theta = \frac{1}{\tan\theta} \iff \tan\theta \cdot \cot\theta = 1$
* **भागफल संबंध:** $\mathbf{\tan\theta = \frac{\sin\theta}{\cos\theta}}$ तथा $\mathbf{\cot\theta = \frac{\cos\theta}{\sin\theta}}$

---

## 2. विशिष्ट कोणों की जादुई मान सारणी (0°, 30°, 45°, 60°, 90°)

### 🖐️ 30-सेकंड में सारणी बनाने की 'हथेली ट्रिक':
केवल पहली पंक्ति ($\sin\theta$) के लिए $0, 1, 2, 3, 4$ लिखकर 4 से भाग देकर वर्गमूल लें:
$$\sqrt{\frac{0}{4}}=0, \quad \sqrt{\frac{1}{4}}=\frac{1}{2}, \quad \sqrt{\frac{2}{4}}=\frac{1}{\sqrt{2}}, \quad \sqrt{\frac{3}{4}}=\frac{\sqrt{3}}{2}, \quad \sqrt{\frac{4}{4}}=1$$

| अनुपात / कोण | $0^\circ$ | $30^\circ$ | $45^\circ$ | $60^\circ$ | $90^\circ$ |
|---|:---:|:---:|:---:|:---:|:---:|
| **$\sin\theta$** | $0$ | $\frac{1}{2}$ | $\frac{1}{\sqrt{2}}$ | $\frac{\sqrt{3}}{2}$ | $1$ |
| **$\cos\theta$** (उल्टे क्रम में लिखें) | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{\sqrt{2}}$ | $\frac{1}{2}$ | $0$ |
| **$\tan\theta$** ($\sin \div \cos$) | $0$ | $\frac{1}{\sqrt{3}}$ | $1$ | $\sqrt{3}$ | अपरिभाषित |
| **$\csc\theta$** ($\sin$ का उल्टा) | अपरिभाषित | $2$ | $\sqrt{2}$ | $\frac{2}{\sqrt{3}}$ | $1$ |
| **$\sec\theta$** ($\cos$ का उल्टा) | $1$ | $\frac{2}{\sqrt{3}}$ | $\sqrt{2}$ | $2$ | अपरिभाषित |
| **$\cot\theta$** ($\tan$ का उल्टा) | अपरिभाषित | $\sqrt{3}$ | $1$ | $\frac{1}{\sqrt{3}}$ | $0$ |

---

## 3. तीन मौलिक त्रिकोणमितीय सर्वसमिकाएँ (Fundamental Identities)

ये सर्वसमिकाएँ वहाँ लागू होती हैं जहाँ उनमें प्रयुक्त त्रिकोणमितीय अनुपात परिभाषित हों।

1. **प्रथम सर्वसमिका:**  
   $$\mathbf{\sin^2\theta + \cos^2\theta = 1}$$  
   *रूपांतरण:* $\sin^2\theta = 1 - \cos^2\theta \iff \cos^2\theta = 1 - \sin^2\theta$

2. **द्वितीय सर्वसमिका:**  
   $$\mathbf{1 + \tan^2\theta = \sec^2\theta}$$  
   *रूपांतरण:* $\sec^2\theta - \tan^2\theta = 1 \iff \tan^2\theta = \sec^2\theta - 1$

3. **तृतीय सर्वसमिका:**  
   $$\mathbf{1 + \cot^2\theta = \csc^2\theta}$$  
   *रूपांतरण:* $\csc^2\theta - \cot^2\theta = 1 \iff \cot^2\theta = \csc^2\theta - 1$

---

## 4. सर्वसमिका सिद्ध करने की रणनीतियाँ

जब $LHS = RHS$ सिद्ध करना हो, तो इन तरीकों पर विचार करें:

### 🌟 गोल्डन रूल 1: सब कुछ $\sin$ और $\cos$ में बदलें!
यदि प्रश्न में $\tan, \cot, \sec, \csc$ दिखाई दे और सीधे कोई सर्वसमिका न लगे, तो तुरंत लिखें:
$$\tan\theta = \frac{\sin\theta}{\cos\theta}, \quad \cot\theta = \frac{\cos\theta}{\sin\theta}, \quad \sec\theta = \frac{1}{\cos\theta}, \quad \csc\theta = \frac{1}{\sin\theta}$$
इसके बाद ल.स.प. (LCM) लेकर सरल करें।

### 🌟 गोल्डन रूल 2: संयुग्मी (Conjugate) से गुणा (परिमेयकरण)
जब भी आपको $\sqrt{\frac{1 + \sin\theta}{1 - \sin\theta}}$ या $\frac{1}{1 \pm \cos\theta}$ जैसा रूप दिखे:
अंश और हर में विपरीत चिह्न वाले पद (जैसे $1 + \sin\theta$) से गुणा करें। नीचे $1 - \sin^2\theta = \cos^2\theta$ बन जाएगा और रूट हट जाएगा!

### 🌟 गोल्डन रूल 3: बीजीय सर्वसमिकाओं का प्रयोग
* $a^2 - b^2 = (a - b)(a + b)$
* $(a + b)^2 = a^2 + 2ab + b^2$
* $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$

---

## 5. बोर्ड परीक्षा के 4 मुख्य टाइप (Exam Question Archetypes with Solved Models)

### टाइप 1: समकोण त्रिभुज से अनुपात निकालना (1 अंक)
* **मॉडल उदाहरण:** यदि $\tan A = \frac{4}{3}$ हो, तो $\sin A$ और $\cos A$ का मान ज्ञात कीजिए।  
  *हल:* $\tan A = \frac{\text{लंब}}{\text{आधार}} = \frac{4}{3}$। माना लंब $= 4k$, आधार $= 3k$  
  कर्ण $= \sqrt{(4k)^2 + (3k)^2} = \sqrt{16k^2 + 9k^2} = \sqrt{25k^2} = 5k$  
  $\sin A = \frac{\text{लंब}}{\text{कर्ण}} = \frac{4k}{5k} = \mathbf{\frac{4}{5}}$  
  $\cos A = \frac{\text{आधार}}{\text{कर्ण}} = \frac{3k}{5k} = \mathbf{\frac{3}{5}}$

### टाइप 2: कोण मानों को रखकर गणना करना (2 अंक)
* **मॉडल उदाहरण:** मान ज्ञात कीजिए: $\frac{2\tan 30^\circ}{1 + \tan^2 30^\circ}$  
  *हल:* हम जानते हैं कि $\tan 30^\circ = \frac{1}{\sqrt{3}}$  
  $$= \frac{2\left(\frac{1}{\sqrt{3}}\right)}{1 + \left(\frac{1}{\sqrt{3}}\right)^2} = \frac{\frac{2}{\sqrt{3}}}{1 + \frac{1}{3}} = \frac{\frac{2}{\sqrt{3}}}{\frac{4}{3}} = \frac{2}{\sqrt{3}} \times \frac{3}{4} = \frac{3}{2\sqrt{3}} = \mathbf{\frac{\sqrt{3}}{2}} \quad (= \sin 60^\circ)$$

### टाइप 3: $A$ और $B$ के मान ज्ञात करना
* **मॉडल उदाहरण:** यदि $\tan(A + B) = \sqrt{3}$ और $\tan(A - B) = \frac{1}{\sqrt{3}}$ हो, जहाँ $0^\circ < A + B \leq 90^\circ$, $0^\circ < A - B < 90^\circ$, तो $A$ और $B$ का मान ज्ञात कीजिए।
  *हल:*  
  $\tan(A + B) = \sqrt{3} \implies A + B = 60^\circ \quad \dots (1)$ (क्योंकि $\tan 60^\circ = \sqrt{3}$)  
  $\tan(A - B) = \frac{1}{\sqrt{3}} \implies A - B = 30^\circ \quad \dots (2)$ (क्योंकि $\tan 30^\circ = \frac{1}{\sqrt{3}}$)  
  समीकरण (1) और (2) को जोड़ने पर:  
  $2A = 90^\circ \implies \mathbf{A = 45^\circ}$  
  $A$ का मान (1) में रखने पर: $45^\circ + B = 60^\circ \implies \mathbf{B = 15^\circ}$  
  **उत्तर:** $\mathbf{A = 45^\circ}$ तथा $\mathbf{B = 15^\circ}$।

### टाइप 4: सर्वसमिका सिद्ध करने का 4-अंक का प्रश्न (Section D)
* **मॉडल उदाहरण 1:** सिद्ध कीजिए कि (जहाँ $0^\circ<A<90^\circ$): $\sqrt{\frac{1 + \sin A}{1 - \sin A}} = \sec A + \tan A$  
  *हल:*  
  $$LHS = \sqrt{\frac{1 + \sin A}{1 - \sin A}}$$  
  अंश और हर में $(1 + \sin A)$ से गुणा (परिमेयकरण) करने पर:  
  $$= \sqrt{\frac{(1 + \sin A)(1 + \sin A)}{(1 - \sin A)(1 + \sin A)}} = \sqrt{\frac{(1 + \sin A)^2}{1 - \sin^2 A}}$$  
  चूँकि $1 - \sin^2 A = \cos^2 A$:  
  $$= \sqrt{\frac{(1 + \sin A)^2}{\cos^2 A}} = \frac{1 + \sin A}{\cos A} = \frac{1}{\cos A} + \frac{\sin A}{\cos A} = \mathbf{\sec A + \tan A} = RHS$$  
  **(इति सिद्धम् / Hence Proved)**

* **मॉडल उदाहरण 2:** सिद्ध कीजिए: $(\sin A + \csc A)^2 + (\cos A + \sec A)^2 = 7 + \tan^2 A + \cot^2 A$  
  *हल:*  
  $$LHS = (\sin^2 A + 2\sin A\csc A + \csc^2 A) + (\cos^2 A + 2\cos A\sec A + \sec^2 A)$$  
  हम जानते हैं कि $\sin A\csc A = 1$ तथा $\cos A\sec A = 1$:  
  $$= (\sin^2 A + \cos^2 A) + 2(1) + 2(1) + \csc^2 A + \sec^2 A$$  
  चूँकि $\sin^2 A + \cos^2 A = 1$:  
  $$= 1 + 2 + 2 + (1 + \cot^2 A) + (1 + \tan^2 A)$$  
  $$= 7 + \tan^2 A + \cot^2 A = RHS$$  
  **(इति सिद्धम्)**

---

## 6. मिस्टेक बस्टर (Mistake Buster — सावधान! यहाँ कटते हैं अंक)

| छात्र क्या गलती करते हैं? | परीक्षक क्या देखता है? | सही टॉपर शैली |
|---|---|---|
| न्यूनकोण बदलते ही लंब और आधार का बदलना भूल जाना। | $\sin A$ और $\sin C$ में लंब अलग-अलग भुजाएँ होती हैं। | कोण के ठीक सामने वाली भुजा को लंब मानें: $\angle A$ के लिए लंब $BC$ है, जबकि $\angle C$ के लिए लंब $AB$ है! |
| $\sin^2 A + \cos^2 A = 1$ की जगह $\sin A + \cos A = 1$ लिख देना। | बिना वर्ग के सर्वसमिका सत्य नहीं होती। | घात 2 अवश्य देखें: $\sin^2\theta + \cos^2\theta = 1$। |
| $\sin(A + B)$ को कोष्ठक खोलकर $\sin A + \sin B$ लिख देना। | $\sin$ कोई गुणनफल नहीं बल्कि एक संक्रिया/अनुपात है। | $\sin(A + B) \neq \sin A + \sin B$। |
| $\tan 60^\circ$ का मान $\frac{1}{\sqrt{3}}$ लिख देना। | मान सारणी में $\tan 30^\circ = \frac{1}{\sqrt{3}}$ तथा $\tan 60^\circ = \sqrt{3}$ होता है। | मान रखने से पहले रफ़ पेज पर सारणी के मुख्य मान अवश्य लिख लें। |

---

## 7. अभ्यास प्रश्न (ये प्रश्न अभ्यास के लिए हैं; पुराने बोर्ड प्रश्नों से मिलान प्रमाणित नहीं है)

1. **[Practice set]** $\sin^2 30^\circ + \cos^2 30^\circ$ का मान है:  
   (A) $0$  
   (B) $1$  
   (C) $2$  
   (D) $\frac{1}{2}$  
   *हल:* सर्वसमिका से $\sin^2\theta + \cos^2\theta = 1$। **उत्तर: (B)**

2. **[Practice set]** सिद्ध कीजिए कि: $\frac{\cos A}{1 + \sin A} + \frac{1 + \sin A}{\cos A} = 2\sec A$ (4 अंक)  
   *हल:* $LHS = \frac{\cos^2 A + (1 + \sin A)^2}{\cos A(1 + \sin A)} = \frac{\cos^2 A + 1 + 2\sin A + \sin^2 A}{\cos A(1 + \sin A)} = \frac{2 + 2\sin A}{\cos A(1 + \sin A)} = \frac{2(1 + \sin A)}{\cos A(1 + \sin A)} = \frac{2}{\cos A} = 2\sec A$।

3. **[Practice set]** $9\sec^2 A - 9\tan^2 A$ का मान बराबर है:  
   (A) $1$  
   (B) $9$  
   (C) $8$  
   (D) $0$  
   *हल:* $9(\sec^2 A - \tan^2 A) = 9(1) = 9$। **उत्तर: (B)**

4. **[Practice set]** मान ज्ञात कीजिए: $2\tan^2 45^\circ + \cos^2 30^\circ - \sin^2 60^\circ$ (2 अंक)  
   *हल:* $2(1)^2 + \left(\frac{\sqrt{3}}{2}\right)^2 - \left(\frac{\sqrt{3}}{2}\right)^2 = 2 + 0 = 2$।

5. **[Practice set]** यदि न्यूनकोण $\theta$ के लिए $\cos\theta = \frac{12}{13}$ हो, तो $\tan\theta$ का मान लिखिए। (1 अंक)  
   *हल:* $L = \sqrt{13^2 - 12^2} = 5 \implies \tan\theta = \frac{5}{12}$।

6. **[Practice set]** सिद्ध कीजिए: $\frac{1 - \tan^2 45^\circ}{1 + \tan^2 45^\circ} = \cos 90^\circ$ (1 अंक)  
   *हल:* $\frac{1 - 1}{1 + 1} = 0 = \cos 90^\circ$।

7. **[Practice set]** सिद्ध कीजिए कि: $\frac{\sin\theta - 2\sin^3\theta}{2\cos^3\theta - \cos\theta} = \tan\theta$ (4 अंक)  
   *हल:* $LHS = \frac{\sin\theta(1 - 2\sin^2\theta)}{\cos\theta(2\cos^2\theta - 1)} = \tan\theta \left[\frac{\cos^2\theta + \sin^2\theta - 2\sin^2\theta}{2\cos^2\theta - (\cos^2\theta + \sin^2\theta)}\right] = \tan\theta \left[\frac{\cos^2\theta - \sin^2\theta}{\cos^2\theta - \sin^2\theta}\right] = \tan\theta$।

---

## 8. अतिरिक्त अभ्यास प्रश्न

### वस्तुनिष्ठ प्रश्न (MCQs) [प्रत्येक 1 अंक]

**Q1.** $(1 + \tan^2\theta)(1 - \sin\theta)(1 + \sin\theta)$ का मान है:  
(A) $0$  
(B) $1$  
(C) $-1$  
(D) $2$  

**Q2.** यदि $4\tan\theta = 3$ हो, तो $\frac{4\sin\theta - \cos\theta}{4\sin\theta + \cos\theta}$ बराबर है:  
(A) $\frac{2}{3}$  
(B) $\frac{1}{2}$  
(C) $\frac{1}{3}$  
(D) $\frac{3}{4}$  

**Q3.** $\frac{1 - \tan^2 30^\circ}{1 + \tan^2 30^\circ}$ का मान बराबर है:  
(A) $\cos 60^\circ$  
(B) $\sin 60^\circ$  
(C) $\tan 60^\circ$  
(D) $\sin 30^\circ$  

**Q4.** यदि $\sin\theta = \cos\theta$ हो, तो $\theta$ का मान है ($0^\circ \leq \theta \leq 90^\circ$):  
(A) $30^\circ$  
(B) $45^\circ$  
(C) $60^\circ$  
(D) $90^\circ$  

---

### रिक्त स्थान [प्रत्येक 1 अंक]
1. $\tan 45^\circ$ का संख्यात्मक मान ________ होता है।
2. $\sec^2\theta - 1 = $ ________ होता है।
3. $\sin\theta$ का अधिकतम मान ________ हो सकता है।

---

### निबंधात्मक प्रश्न (4 अंक)
1. सिद्ध कीजिए: $\frac{\tan\theta}{1 - \cot\theta} + \frac{\cot\theta}{1 - \tan\theta} = 1 + \sec\theta\csc\theta$
2. सिद्ध कीजिए: $\frac{\csc A}{\csc A - 1} + \frac{\csc A}{\csc A + 1} = 2\sec^2 A$

---

## 9. फटाफट 1-मिनट चीट शीट (Pre-Exam Rapid Cheat Sheet)

1. लाल / कका: $\sin = L/K, \cos = A/K, \tan = L/A$।
2. $\tan\theta = \frac{\sin\theta}{\cos\theta}, \cot\theta = \frac{\cos\theta}{\sin\theta}$।
3. $\sin^2\theta + \cos^2\theta = 1$।
4. $1 + \tan^2\theta = \sec^2\theta \iff \sec^2\theta - \tan^2\theta = 1$।
5. $1 + \cot^2\theta = \csc^2\theta \iff \csc^2\theta - \cot^2\theta = 1$।
6. $\sin 30^\circ = \cos 60^\circ = \frac{1}{2}$।
7. $\sin 45^\circ = \cos 45^\circ = \frac{1}{\sqrt{2}}$।
8. $\sin 60^\circ = \cos 30^\circ = \frac{\sqrt{3}}{2}$।
9. $\tan 30^\circ = \frac{1}{\sqrt{3}}, \tan 45^\circ = 1, \tan 60^\circ = \sqrt{3}$।
10. जब कुछ समझ न आए, तो सर्वसमिका में सब कुछ $\sin$ और $\cos$ में बदलें!

---

## 10. संपूर्ण व्याख्यात्मक उत्तर-कुंजी (Explanatory Answer Key)

* **Q1. उत्तर: (B) 1** — $(\sec^2\theta)(1 - \sin^2\theta) = (\sec^2\theta)(\cos^2\theta) = 1$।
* **Q2. उत्तर: (B) 1/2** — अंश व हर को $\cos\theta$ से भाग देने पर: $\frac{4\tan\theta - 1}{4\tan\theta + 1} = \frac{3 - 1}{3 + 1} = \frac{2}{4} = \frac{1}{2}$।
* **Q3. उत्तर: (A) $\cos 60^\circ$** — $\frac{1 - 1/3}{1 + 1/3} = \frac{2/3}{4/3} = \frac{2}{4} = \frac{1}{2} = \cos 60^\circ$।
* **Q4. उत्तर: (B) 45°** — $\frac{\sin\theta}{\cos\theta} = 1 \implies \tan\theta = 1 \implies \theta = 45^\circ$।

### रिक्त स्थान
1. 1  
2. $\tan^2\theta$  
3. 1  

---

## 11. 10-मिनट आत्म-मूल्यांकन टेस्ट (Quick Self-Test)

**पूर्णांक: 10 अंक | समय: 10 मिनट**
1. $\tan 60^\circ$ का मान लिखिए। *(1 अंक)*
2. यदि न्यूनकोण $A$ के लिए $\sin A = \frac{3}{5}$ हो, तो $\cos A$ का मान ज्ञात कीजिए। *(1 अंक)*
3. मान ज्ञात कीजिए: $5\cos^2 60^\circ + 4\sec^2 30^\circ - \tan^2 45^\circ$। *(2 अंक)*
4. सिद्ध कीजिए कि: $\frac{1 + \sec A}{\sec A} = \frac{\sin^2 A}{1 - \cos A}$। *(2 अंक)*
5. सिद्ध कीजिए कि: $\frac{\cos A - \sin A + 1}{\cos A + \sin A - 1} = \csc A + \cot A$। *(4 अंक)*

### आत्म-मूल्यांकन उत्तर-संकेत
1. $\tan60^\circ=\sqrt{3}$।
2. न्यूनकोण $A$ मानकर $\cos A=\sqrt{1-(3/5)^2}=4/5$।
3. $5(1/4)+4(4/3)-1=67/12$।
4. LHS $=1+\cos A$; RHS $=(1-\cos^2 A)/(1-\cos A)=1+\cos A$ (जहाँ हर शून्य न हो)।
5. RHS को $(1+\cos A)/\sin A$ लिखें। क्रॉस-मल्टिप्लाई करने पर बायाँ गुणनफल $\sin A(1+\cos A-\sin A)=\sin A+\sin A\cos A-\sin^2 A$ और दायाँ गुणनफल $(1+\cos A)(\cos A+\sin A-1)=\cos^2 A+\sin A+\sin A\cos A-1$ है। $\sin^2 A+\cos^2 A=1$ से ये बराबर हैं (जहाँ मूल व्यंजक परिभाषित हों)।
