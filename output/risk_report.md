# Contract Risk Report — TechVendor Ltd. (input/sample_contract.txt)

## Risk Rating
**High**: Section 5.1 irrevocably assigns all Customer Data to Vendor, which is a P1 unilateral data assignment, and the contract also contains other P1 clauses (7-day auto-renewal notice in 3.2 and unlimited Customer liability in 6.2).

### Critical Summary
The most dangerous clause is Section 5.1, which irrevocably assigns all Customer Data to Vendor, and Section 5.2 lets Vendor commercialise that data during and after the term without notice or compensation. The most important Customer obligation is under Section 3.2, which requires written non-renewal notice at least seven days before the end of the current term, failing which Customer is bound to the full renewal fee. Before signing, strike the assignment in Section 5.1 and limit Vendor's rights in Customer Data to what is needed to provide the Services.

## P1 Critical Clauses
| Clause type | Excerpt | Risk explanation | Confidence |
|---|---|---|---|
| Auto-renewal without adequate notice | "shall automatically renew for successive periods of twelve (12) months unless Customer provides written notice of non-renewal at least seven (7) days prior to the end of the then-current term" | Non-renewal notice is only seven days before term end, and missed notice binds Customer to the full renewal fee (3.2). A 12-month renewal is triggered with a short notice window. | High — renewal and notice period are stated explicitly |
| Uncapped liability | "Customer's liability to Vendor arising out of this Agreement, whether in contract, tort, or otherwise, shall be unlimited" | Customer's liability is unlimited under any cause of action, and 6.2 adds all direct and indirect losses, costs, and expenses. Vendor's liability has no stated cap (6.1). | High — 6.2 expressly states unlimited liability |
| Unilateral data assignment to vendor | "All data, content, records, and information uploaded to or generated through the Services by Customer or its users ("Customer Data") is hereby irrevocably assigned to Vendor." | Customer Data is irrevocably assigned to Vendor by this clause alone, with no reciprocal grant back to Customer. Customer keeps no ownership of its uploaded data (5.1). | High — "irrevocably assigned" is explicit |
| Punitive penalty (late payment interest) | "Late amounts accrue interest at 1.5% per month." | The stated rate is 1.5% per month, which is about 18% per year, on any late amount. Whether this is punitive is a judgement, so the classification is less certain. | Medium — rate is explicit, but the punitive characterisation is interpretive |

## P2 Major Clauses
| Clause type | Excerpt | Risk explanation | Confidence |
|---|---|---|---|
| Price escalation trigger | "Vendor may increase the subscription fees by up to fifteen percent (15%) in each contract year, effective upon written notice to Customer." | Vendor may raise fees by up to 15% each contract year on notice alone. Customer's consent is not required (2.2). | High — percentage, frequency, and no-consent language are explicit |
| Customer data ownership ambiguity | "Vendor may use, analyse, aggregate, license, and commercialise Customer Data for analytics, product development, benchmarking, and any other business purpose, during and after the term of this Agreement" | Vendor may use and commercialise Customer Data for any business purpose, during and after the term, without notice or compensation (5.2). This conflicts with 5.1's statement that Customer "retains no further rights in data," so the ownership position is unclear. | High — 5.1 and 5.2 contain the stated terms and their conflict is visible in the text |
| Broad indemnification | "Customer shall indemnify and hold harmless Vendor against all claims arising from Customer's use of the Services." | Customer indemnifies Vendor against all claims arising from Customer's use, with no reciprocal Vendor indemnity and no stated cap (6.3). | High — indemnity scope and one-way direction are explicit |
| Asymmetric limitation of liability | "Vendor's liability to Customer under or in connection with this Agreement is limited to the extent expressly stated in this Section." | The clause refers to a limit that is not stated in Section 6. It also excludes loss of data and consequential loss for Vendor (6.1), while Customer's liability is unlimited (6.2). | Medium — the reference to an unstated limit is clear, but its effect depends on how a court would read it |
| Asymmetric assignment | "Neither party may assign this Agreement without the other's consent, except Vendor may assign it to an affiliate or successor." | Vendor may assign to an affiliate or successor without Customer consent. Customer has no equivalent right (11). | High — the one-sided exception is explicit |

## P3 Minor Clauses
| Clause type | Excerpt | Risk explanation | Confidence |
|---|---|---|---|
| Termination for convenience timeline | "Either party may terminate this Agreement for convenience by giving thirty (30) days' prior written notice to the other party." | Either party, including Vendor, may exit on 30 days' notice. This sits alongside the 12-month term and the 15% price-adjustment right, and prepaid fees are not refundable (4.3). | High — notice period is explicit |
| Cure period for breach termination | "Either party may terminate immediately upon written notice if the other party materially breaches this Agreement and fails to cure such breach within fifteen (15) days of notice." | Termination for material breach requires a 15-day cure period. The clause does not define "materially breaches." | High — cure period and immediate termination are explicit |
| Governing law | "This Agreement shall be governed by and construed in accordance with the laws of the State of Delaware, United States, without regard to its conflict of laws principles." | Delaware law governs the Agreement. Vendor is described as a company registered in England and Wales, so this is a cross-border choice. | High — governing law is expressly stated |
| Dispute resolution forum | "The parties submit to the exclusive jurisdiction of the state and federal courts located in Delaware." | Disputes must go to Delaware state or federal courts, on an exclusive basis. No arbitration or alternative dispute resolution is provided. | High — exclusive forum is expressly stated |

## Key Obligations

### Acme Corp
- Pay the annual subscription fee set out in Schedule B within thirty (30) days of receipt of each invoice; late amounts accrue interest at 1.5% per month (2.1).
- Give written notice of non-renewal at least seven (7) days before the end of the then-current term; failure to do so binds Customer to the full renewal fee (3.2).
- Pay all fees accrued through the effective date of termination (4.3).
- Indemnify and hold harmless Vendor against all claims arising from Customer's use of the Services (6.3).
- Bear unlimited liability to Vendor under or in connection with the Agreement, including all direct and indirect losses, costs, and expenses incurred by Vendor (6.2).
- Keep confidential all non-public information disclosed by Vendor that is marked confidential or would reasonably be understood to be confidential, and use it solely to perform its obligations under the Agreement; this survives for three (3) years after termination (7).
- Not assign the Agreement without Vendor's consent (11).
- Make any amendment to the Agreement in writing and signed by both parties (11).

### TechVendor Ltd.
- Provide Customer with access to its cloud-based workflow automation platform (the "Services") in accordance with the service descriptions in Schedule A (1).
- Use commercially reasonable efforts to make the Services available 99.5% of the time in any calendar month, excluding scheduled maintenance (1).
- Keep confidential all non-public information disclosed by Customer that is marked confidential or would reasonably be understood to be confidential, and use it solely to perform its obligations under the Agreement; this survives for three (3) years after termination (7).
- Not assign the Agreement without Customer's consent, except that Vendor may assign it to an affiliate or successor (11).
- Make any amendment to the Agreement in writing and signed by both parties (11).

## Run Info
- Input file: input/sample_contract.txt
- Date: 2026-11-16
- Model: sonnet (coordinator); haiku (sub-agents)
- Sub-agents used: clause-agent, obligation-agent, risk-agent

---
GATE: FAIL
