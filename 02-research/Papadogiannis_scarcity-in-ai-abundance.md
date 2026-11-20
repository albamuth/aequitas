# Scarcity in an Age of AI Abundance

**Version:** 0.1
**Type:** working paper
**Author(s):** Agisilaos Papadogiannis (independent researcher; no institution listed)
**Published:** SSRN working paper No. 6639022, DOI [10.2139/ssrn.6639022](https://doi.org/10.2139/ssrn.6639022). A web search listing dates it 21 April 2026; the Crossref record says only "2026". An earlier version is [SSRN No. 5924462](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5924462), posted December 2025. Not peer-reviewed.
**Retrieved:** 2026-11-19
**URL:** [SSRN abstract page](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6639022) (the page refused every fetch with HTTP error 403; the paper's existence is confirmed by the [Crossref record](https://api.crossref.org/works/10.2139/ssrn.6639022))
**Read:** abstract only, plus secondary descriptions. **The full text was not read.**
**Local copy:** none

> **What this note rests on.** Three things were read. (1) The abstract, as held in the Crossref record. (2) [Richard Turnock's companion post](https://turnock.substack.com/p/scarcity-in-an-age-of-ai-abundance) (Substack, September 2026), which describes the paper's sections, equations and table. Turnock says he wrote it with the help of an AI model, so its details need checking against the paper. (3) Two summaries on the site Shades of Singularity: [the post-scarcity page](https://shadesofsingularity.com/shades/post-scarcity-transition/) and [the end-of-work essay](https://shadesofsingularity.com/essays/end-of-work/). Every section and page number below comes from Turnock's post, not from the paper.

## Why this matters to Aequitas

The paper argues that cheap production does not end scarcity. It says the shortage moves to whatever is still hard to copy, and that the owners of that thing collect the gain. Aequitas holds two positions this tests. One is the author's claim of 2026-11-19 that scarcity today is largely artificial. The other is the cost rule, which says no seller adds rent. The paper lists five places where a shortage can remain, and two of them are physical.

## Key findings

- **Two definitions (abstract).** *Technological abundance* means AI-heavy production gets much cheaper and more capable. *Economic abundance* means households can afford an essential bundle of goods and services. That needs household resources (wages, income from assets, and government transfers) to grow at least as fast as the cost of the bundle.
- **The central claim (abstract).** The first does not, in general, produce the second. A fall in cost moves the shortage, "migrating rents toward the layers that remain scarce". A rent here is income a holder collects because the thing they hold is short, above what it cost to provide.
- **Five layers where scarcity and rent can sit (abstract).**
  1. Physical resources and land.
  2. Infrastructure: power, computing capacity, chip fabrication. The secondary summaries add grid connections and data centres.
  3. Capabilities: skills and organisational know-how, including knowledge that depends on trust between people.
  4. Institutions: the rules that decide who may access or use something. Examples in the summaries are permits, regulatory approval and clinical trials.
  5. Jurisdictions: the territories whose authority enforces those rules and provides security. The paper keeps this apart from layer 4 on purpose.
- **The formal part (abstract; Section 5.1, equations 1 to 3, per Turnock).** Each layer has a total rent. Each actor has a share of control in each layer, and the shares in a layer sum to 1. An actor's rent is the sum, over the five layers, of its share times that layer's rent. Economic abundance fails when rent grows in the layers that matter most and households hold few claims on those layers.
- **A worked case with digits (per Turnock, his Figure 4).** Two actors and two layers. Total rent goes from 150 units to 180 units. One actor ends with 160 and the other with 20. I did not see the paper's own table, so treat these digits as Turnock's reading.
- **Three mechanisms that stop cheap production from reaching households (Section 3, per Turnock).** Sellers with market power keep the saving. The bottleneck shifts to another layer. Ownership and distribution decide who gets the gain. Turnock also reports a fourth, a threshold of digital access. About 2.6 billion people are offline and get nothing from cheaper AI services. The source of that figure was not seen.
- **A historical case with no AI in it (Section 1.2, pp. 5-6, per Turnock).** Mechanical refrigeration ended the local and seasonal shortage of perishable food. The shortage moved to cold warehouses, special transport, reliable power, port access and the capital to build cold chains. Rent went to the owners of those.
- **Two examples (per Shades of Singularity).** AI may push the cost of generating a kilowatt-hour toward zero, while the land, the permits and the grid connection for a solar farm stay short. Medical knowledge may become free, while regulatory approval, clinical trials and manufacturing capacity still limit treatment.
- **Application (abstract).** The semiconductor supply chain in Asia, where infrastructure, institutions and jurisdictions interact across borders. The paper also names likely winners and losers among industries and households (Table 1, pp. 53-55, 24 actor types across the 5 layers, per Turnock), and draws consequences for inequality, investment and the politics of transfers.
- **Labour.** Per Turnock, the paper expects robots to displace routine service work such as cleaning, stocking and warehouse picking. It treats that labour as becoming plentiful, not short.

## What we can use

- **"Cheap to make" is not "affordable to live".** This is the most useful distinction in the paper. Aequitas already has the second condition as arithmetic. [Foundations §5.5.3](../00-strategy/Aequitas_Foundations.md) sets a lower bound on the floor (the hours of credit a person receives each day for being alive): the floor, times the tolerance (the multiple of credit and backing that a person's debit may reach), times 365, must cover a year of essentials. Worked: a broad US basket takes 965 hours a year. At a tolerance of 1.2 the floor must be at least 965 ÷ (1.2 × 365) = 2.2 hours a day. The paper's economic abundance is the same test stated in money.
- **The five layers as a checklist for stress tests.** For each layer, ask what Aequitas does when that thing is short.

| Kind of scarcity the paper says remains | How Aequitas treats it today |
|---|---|
| **Land and space** | Land is not owned. A structure's occupation of a space is a debit, discharged only by restoring the space ([Foundations §3.7](../00-strategy/Aequitas_Foundations.md)). Nobody collects land rent. **Which use gets a contested site is not settled by cost.** Foundations §4.6 and §5.5.3 hand that to a queue, a lottery or pledge-priority. |
| **Physical resources** (minerals, water) | Counted as material in the debit of whoever consumes them. Foundations §3.5 reports the project's own measurement: critical minerals and the energy transition bind an isolated United States. Counting a shortage does not end it. |
| **Energy and the grid** | Counted, and already measured as the tightest constraint: energy sits at 0.19 of what a median standard needs at the current build (Foundations §3.5). **This agrees with the paper.** |
| **Computing capacity and chip fabrication** | A plant at full capacity is a physically scarce output. Cost says what a chip took. It does not say who gets the last one (Foundations §4.6). Pledges, which are hours people commit in advance, signal how much more to build. **Aequitas has no rule for sharing out a plant's output during the years it takes to build another.** |
| **Skills and organisational know-how** | Training is credited work done in advance. An hour of a rare expert is credited the same as any other hour, so a rare skill earns no premium. **Aequitas has no rule for who gets a scarce expert's time other than a queue or a lottery.** The sections read for this note give no rule for know-how that one organisation holds and others cannot copy. |
| **Institutions** (permits, approvals, access rules) | Aequitas keeps working institutions and changes only the accounting. A permit queue is a queue. **Aequitas has no answer to a slow or captured permitting body.** That is a matter of how a network governs itself, which Aequitas does not prescribe. |
| **Jurisdictions** (enforcement, security, export controls) | **No answer.** A trust network can be any size, and Foundations has rules that reach across two networks. Nothing in the sections read deals with a state that blocks a supply chain. |
| **Household purchasing power** | The floor and the tolerance, as worked above. This is the one place where Aequitas has a direct, numbered answer. |
| **Being offline** (2.6 billion people, per Turnock) | A weakness for Aequitas too. An accounting system needs records. People outside a network are estimated statistically and receive no credit. |

- **A rent test for Aequitas itself.** The paper's formula says: find the scarce layer, then find who controls it. Aequitas removes rent by rule. The useful question is whether anything in Aequitas behaves like a rent on a scarce layer. Three candidates to test: custody of a scarce asset such as a fabrication plant, a place in a queue, and pledges that pile onto whoever holds the scarce thing. Foundations §4.6 already admits the last one as a popularity contest.
- **The refrigeration case.** It is a historical analogue for public writing. It shows a shortage moving after a real technical gain, with no AI involved.
- **The Asian semiconductor chain.** It is a ready case of a shortage made by borders and rules. It fits the scenario suite's work on blockades and sector-level shortages.
- **A counterweight to [Saadia](Saadia_trekonomics.md).** Saadia treats post-scarcity as a choice about organisation. This paper says a choice about organisation still meets layers 1 and 2. The wiki page on [post-scarcity](../01-wiki/post-scarcity.md) could cite both.

## What it gets wrong / limitations

- **It is not peer-reviewed.** It is an SSRN working paper by an independent researcher. [The author's own profile](https://github.com/apapadogiannis/apapadogiannis) describes him as an engineer by training who now does unfunded research in finance. The [OpenAlex index](https://api.openalex.org/works?search=%22Scarcity%20in%20an%20Age%20of%20AI%20Abundance%22) shows 1 citation.
- **It has no data, as far as the secondary descriptions show.** Turnock reports no dataset, no calibration and no empirical test. The table of winners and losers is a set of qualitative scores chosen by judgment. The paper itself calls the table one plausible mapping and not a forecast (per the search summary of the abstract page).
- **The formal result is close to a definition.** If an actor's rent is the sum of shares times layer rents, then it rises with the share and with the layer rent. That follows from the formula. It tests nothing.
- **It is about a future with advanced AI.** It measures nothing about today's capacity or today's consumption. It cannot confirm or refute a claim about the present.
- **It takes rent and ownership as given.** The paper never asks what happens where no holder may charge more than cost. So it does not separate two things Aequitas must separate: a shortage that exists because the thing is physically short, and a shortage of access that exists because an owner charges for it. Its conclusion about households depends on the second. Under the cost rule only the first is left.
- **The author's other work holds that scarcity is the source of value.** His profile lists a paper titled [*The Productivity Myth: Why Scarcity Drives All Value*](https://ssrn.com/abstract=5367197) (link not verified; title only, the paper was not read). Aequitas is a theory of cost and does not measure value (Foundations §0). His frame and ours do not share a starting point, and his paper is partly written for investors choosing winners.
- **It does not cover several kinds of scarcity we expected.** Nothing read mentions attention, status or a person's time. Trust appears only inside layer 3, as know-how that depends on trust.
- **It treats human labour as becoming plentiful.** Foundations §3.5 measures the opposite for today: the world's working hours cover about 0.63 of what a typical United States life for everyone would need. The two are about different dates, so this is a gap and not a contradiction.
- **Our reading is thin.** The full text was not read. The summary we were given before this note was accurate as far as it went, but it left out the paper's main point, which is about who collects the rent.

## Against the claim that scarcity is artificial

The claim under test (2026-11-19): scarcity today is largely artificial; productive capacity exceeds consumption; much is hoarded by a few; much is wasted on war, luxury, planned obsolescence, surplus dumping and needless cheap goods.

**What the source contradicts or limits**

- **Two of the five layers are physical.** Land, minerals, power, grid connections and fabrication capacity are short because they are slow or impossible to copy. Take away every rent-taker and they are still short. On this paper's account, scarcity is not only artificial.
- **A shortage moves when it is relieved.** The refrigeration case and the solar-farm example both show the next constraint appearing once the first is gone. If that pattern holds, ending hoarding and waste would expose the next physical bottleneck. It would not by itself produce plenty. This is my inference from the paper's mechanism, not a sentence in it.
- **"Capacity exceeds consumption" is an aggregate statement, and the paper works layer by layer.** A total can exceed need while one layer, such as energy, cannot deliver. Foundations §3.5 already has that result: energy at 0.19, land at 1.10 and water at 5.22 of what a median standard needs.
- **Rent follows scarcity in this paper. It does not cause it.** Ownership decides who collects. Turnock found no passage where the paper says owners create the shortage. So the paper does not support the step from "a few people collect" to "a few people cause".
- **Skill and know-how are treated as really scarce.** The paper puts them in a layer of their own. That fits the project's own finding that hours of work are short.

**What the source supports**

- **"Much is hoarded by a few", in one specific sense.** The paper's whole mechanism is that the gains from cheaper production go to whoever controls the scarce layer, and households hold few claims there. That is a claim about income from control. It is not a claim about stockpiles.
- **Part of scarcity is made by rules.** Layers 4 and 5 are permits, approvals, access rules, borders and export controls. People wrote all of them. Turnock notes these two layers respond to policy more than the others do.
- **Sellers with market power keep cost savings.** This matches Foundations §4.6, which says much scarcity is produced by holding supply back.

**What the source does not address**

- War, luxury, planned obsolescence, surplus dumping and needless cheap goods. None appears in anything read.
- Whether today's productive capacity exceeds today's consumption. The paper has no measurement of either.
- Whether removing rent would be enough to make essentials affordable. The paper never considers a system without rent.

## Related

- [Saadia, *Trekonomics*](Saadia_trekonomics.md): the opposite position, post-scarcity as a choice about organisation.
- [George, land and rent](George_land-and-rent.md): the classic account of rent going to whoever holds the scarce site.
- [DeLanda, markets and antimarkets](DeLanda_markets-antimarkets.md): concentrated sellers who set supply and price.
- [Veblen, conspicuous consumption](Veblen_conspicuous-consumption.md): status scarcity, which this paper leaves out.
- Wiki: [post-scarcity](../01-wiki/post-scarcity.md) · [debit-tolerance](../01-wiki/debit-tolerance.md) · [pledge-and-signal](../01-wiki/pledge-and-signal.md) · [cost-not-price](../01-wiki/cost-not-price.md) · [land-and-remediation](../01-wiki/land-and-remediation.md) · [books-never-balance](../01-wiki/books-never-balance.md) · [markets-vs-antimarkets](../01-wiki/markets-vs-antimarkets.md)
- [Foundations](../00-strategy/Aequitas_Foundations.md): §0 (cost, not value), §3.5 (hours and energy are short), §3.7 (land), §4.6 (who gets the last one), §5.5.3 (the floor and the tolerance).
