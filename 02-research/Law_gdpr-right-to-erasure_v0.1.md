# The legal right of erasure — what it actually covers

**Retrieved:** 2026-08-22
**Why it matters:** Foundations §5.4 says records of a person are never destroyed, and a flag was raised that this collides with erasure law. **This stub checks that flag. The collision is real but much narrower than the flag implied.**

> **Scope note, added after Foundations §1.2 was written.** Erasure law is **praxis, not foundations**. It binds an implementer in a jurisdiction, not a theory of cost — capitalism carries no data-protection chapter; banks do. **This stub is reference material for whoever operates a trust network, not an open problem against the theory.** It stays here because it is useful, and it was worth checking a flag rather than leaving it standing on a guess.

**Primary sources**
- [GDPR Article 17 — Right to erasure ("right to be forgotten")](https://gdpr-info.eu/art-17-gdpr/)
- [GDPR Article 89 — Safeguards and derogations for archiving, research and statistical purposes](https://gdpr.algolia.com/gdpr-article-89)
- [ICO — Right to erasure](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/individual-rights/right-to-erasure/)
- [ICO — Exemptions under the research provisions](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/the-research-provisions/exemptions/)
- [Irish Data Protection Commission — The right to erasure (Articles 17 & 19)](https://www.dataprotection.ie/en/individuals/know-your-rights/right-erasure-articles-17-19-gdpr)
- [IAPP — How GDPR changes the rules for research](https://iapp.org/news/a/how-gdpr-changes-the-rules-for-research)

---

## 1. What it applies to

**Personal data** — information relating to an identified or identifiable living person, held by a controller. It is a right to have *that controller* erase *that data*, on request, on specific grounds.

**It is not a general right to be removed from history**, and it is **not absolute**. That is the correction: §5.4 was written as though it were.

## 2. The six grounds where erasure applies — Article 17(1)

1. The data are no longer necessary for the purpose they were collected for.
2. Consent is withdrawn and there is no other legal basis.
3. The person objects under Art 21 and there are no overriding legitimate grounds.
4. The data were unlawfully processed.
5. Erasure is required by another legal obligation.
6. The data were collected from a child for an information-society service.

## 3. The five exemptions — Article 17(3). Three of them apply here

Erasure does **not** apply where processing is necessary:

| Exemption | Applies to Aequitas? |
|---|---|
| (a) Freedom of expression and information | Not directly |
| **(b) Compliance with a legal obligation, or a task in the public interest** | **Yes — and this is the ordinary one.** |
| (c) Public health | No |
| **(d) Archiving in the public interest, scientific or historical research, or statistical purposes** — where erasure "is likely to render impossible or seriously impair the achievement" of those objectives (with Art 89 safeguards) | **Yes — and this is the strong one.** |
| **(e) Establishment, exercise or defence of legal claims** | **Yes, for disputed records.** |

### 3.1 (b) — accounting records already outlive erasure requests

**This is not a novel argument. It is how every business already operates.** Statutory retention of accounting and tax records overrides an erasure request for the duration of the retention period. Per the ICO, a controller under a legal obligation to process may refuse.

- UK: **six years** from the end of the accounting period (HMRC).
- Germany: **ten years** for accounting documents and commercial correspondence (Handelsgesetzbuch).

**Aequitas is an accounting system.** The category its records fall into is the category that already has mandatory retention.

**⚠️ But the window is finite.** Six or ten years is not forever, and §5.4 says forever. **This exemption covers the near term and does not, on its own, license permanent retention.**

### 3.2 (d) — the research and archiving exemption is the one that matters

No time limit attaches to this one, which is why it is the stronger argument for a permanent record.

**And it is not a lawyer's costume.** Foundations §5.3c rules that **trust networks are laboratories, not banks** — their goal is truth, their method is published, their discipline is replication. A ledger of material flows kept for recomputation as the science improves (§3.3) is, on its face, **processing for scientific and statistical purposes**. The exemption bites where erasure would *seriously impair* those objectives, and §5.4's own argument is exactly that: **recomputation cannot run over deleted records.**

**Art 89 attaches safeguards**, chiefly data minimisation and **pseudonymisation where the purpose can still be achieved**. Aequitas is unusually well placed here: the **uniqueness ≠ identification** ruling (`00-strategy/C2_information_capture.md` §3, §8) means a network must establish that an account is *one human*, never *which* human. **A pseudonymised ledger is the design, not a concession made to satisfy Art 89.**

## 4. What survives — the honest residue

1. **Exemptions are case-by-case, necessary and proportionate — never blanket.** Regulators are explicit about this. **Aequitas cannot claim a standing exemption for its whole corpus**; each refusal has to stand on its own facts. A system whose answer is *"we never delete anything, by design"* is asserting exactly the blanket position the guidance rejects.
2. **No exemption clearly licenses *permanent* retention of *identified* personal data by a *private* body.** The archiving exemption was drafted with public-interest archives in mind, and applies to private holders who hold records of public interest under an obligation to preserve them. **Whether a trust network qualifies is an open question, not a settled one.**
3. **Partial compliance is the normal outcome elsewhere** — some data deleted, some retained. **Aequitas has no partial mode.** That mismatch is the sharpest practical edge.
4. **This is one jurisdiction family.** UK GDPR mirrors it; Brazil's LGPD, California's CPRA, India's DPDP Act and China's PIPL all grant deletion rights with their own exemption sets. **Not checked here.**

## 5. Effect on the project

**Downgrade the flag.** §5.4 said Aequitas "cannot honour it without breaking recomputation," implying a head-on conflict with an absolute right. **The right is not absolute, three exemptions apply, and the strongest one has no time limit.**

**Keep a narrower flag.** The live risk is not *"erasure law forbids this"*. It is:

> **Aequitas needs a blanket, permanent, private-body exemption, and the guidance says exemptions are not blanket.**

That is an argument to be made and possibly lost — not a contradiction. **Registered against OP-22 and C7 (privacy layer).**

*Next check, if anyone picks this up: whether any regulator has ruled on a private append-only ledger claiming the Art 17(3)(d) research exemption. Not searched.*
