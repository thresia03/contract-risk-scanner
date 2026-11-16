# Contract Risk Report — TechVendor Ltd.

## Risk Rating
**High** — The contract contains multiple P1 clauses, most significantly Section 5.1, which irrevocably assigns all Customer Data to Vendor, with Section 6.2 (unlimited Customer liability) and Section 3.2 (12-month auto-renewal bound by 7 days' notice) also rated P1.

## Critical Summary
The most dangerous clause is Section 5.1, which irrevocably assigns all Customer Data to Vendor, and Section 5.2 then lets Vendor use, license, and commercialise that data during and after the term without notice or compensation. The most important Customer obligation is the non-renewal notice in Section 3.2: Customer must give written notice at least seven days before the end of the current term or be bound to the full renewal fee for another twelve months. Before signing, strike or rewrite Section 5.1 so Customer keeps ownership of its data and grants Vendor only a limited licence to process it to deliver the Services, and negotiate a cap on Customer's liability in Section 6.2.

## P1 Critical Clauses
| Clause type | Excerpt | Risk explanation | Confidence |
|---|---|---|---|
| Auto-renewal without adequate notice (§3.2) | "unless Customer provides written notice of non-renewal at least seven (7) days prior to the end of the then-current term. Failure to give timely notice shall bind Customer to the full renewal fee." | Each 12-month renewal occurs automatically unless Customer gives notice only 7 days before term end; failure binds Customer to the full renewal fee. | High — explicit |
| Uncapped liability (§6.2) | "shall be unlimited and shall include all direct and indirect losses, costs, and expenses incurred by Vendor." | Customer liability to Vendor is unlimited and includes indirect losses. Section 6.1 excludes Vendor's liability for indirect damages and loss of data, so the regime is one-sided. | High — explicit |
| Unilateral data assignment to Vendor (§5.1, §5.2) | "All data, content, records, and information uploaded to or generated through the Services by Customer or its users ("Customer Data") is hereby irrevocably assigned to Vendor." | Customer Data is irrevocably assigned to Vendor. Section 5.2 allows use, aggregation, licensing and commercialisation "during and after the term" for "any other business purpose" without notice or compensation. | High — explicit |
| Possible punitive penalty (late-payment interest, §2.1) | "Late amounts accrue interest at 1.5% per month." | Interest accrues on late amounts at 1.5% per month, with no grace period or cap stated. Whether this is punitive is an assessment, not stated in the contract. | Medium — rate is explicit, "punitive" is judgment |

## P2 Major Clauses
| Clause type | Excerpt | Risk explanation | Confidence |
|---|---|---|---|
| Broad indemnification (§6.3) | "Customer shall indemnify and hold harmless Vendor against all claims arising from Customer's use of the Services." | One-way indemnity for "all claims", with no reciprocal Vendor indemnity and no stated cap or carve-out. | High — explicit |
| Price escalation trigger (§2.2) | "Vendor may increase the subscription fees by up to fifteen percent (15%) in each contract year, effective upon written notice to Customer." | Fees may rise up to 15% every contract year on written notice, "without the need for Customer's consent or approval." | High — explicit |
| Customer data ownership ambiguity (§5.1) | "Customer retains no further rights in data once submitted, as set out below." | The sentence says Customer "retains no further rights" and refers to terms "set out below" without defining Customer's residual position. | Medium — wording explicit, effect open to interpretation |

## P3 Minor Clauses
| Clause type | Excerpt | Risk explanation | Confidence |
|---|---|---|---|
| Notice period (breach cure, §4.2) | "fails to cure such breach within fifteen (15) days of notice." | Mutual termination right for material breach after a 15-day cure period. "Materially breaches" is not defined. | High — explicit |
| Termination-for-convenience timeline (§4.1) | "Either party may terminate this Agreement for convenience by giving thirty (30) days' prior written notice to the other party." | Either party may exit on 30 days' notice. Under §4.3 no refunds are due for prepaid fees. | High — explicit |
| Governing law (§10) | "This Agreement shall be governed by and construed in accordance with the laws of the State of Delaware, United States, without regard to its conflict of laws principles." | Delaware law governs, though Vendor is registered in England and Wales. | High — explicit |
| Dispute resolution forum (§10) | "The parties submit to the exclusive jurisdiction of the state and federal courts located in Delaware." | Exclusive Delaware courts; no arbitration or escalation step is stated. | High — explicit |

## Key Obligations
### Acme Corp (Customer)
- Pay the annual subscription fee in Schedule B within thirty (30) days of receipt of each invoice (cl. 2.1).
- Pay all fees accrued through the effective date of termination; no refunds for prepaid fees (cl. 4.3).
- Give written notice of non-renewal at least seven (7) days before the end of the then-current term, or be bound to the full renewal fee (cl. 3.2).
- Indemnify and hold harmless Vendor against all claims arising from Customer's use of the Services (cl. 6.3).
- Customer's liability to Vendor is unlimited and includes all direct and indirect losses, costs, and expenses incurred by Vendor (cl. 6.2).
- Keep confidential the other party's non-public information and use it solely to perform the Agreement; survives three (3) years after termination (cl. 7).
- Amendments must be in writing and signed by both parties (cl. 11).
- Not assign the Agreement without Vendor's consent (cl. 11).

### TechVendor Ltd. (Vendor)
- Provide Customer access to the cloud-based workflow automation platform per Schedule A (cl. 1).
- Use commercially reasonable efforts to make the Services available 99.5% of the time in any calendar month, excluding scheduled maintenance (cl. 1).
- Keep confidential the other party's non-public information and use it solely to perform the Agreement; survives three (3) years after termination (cl. 7).
- Amendments must be in writing and signed by both parties (cl. 11).
- Not assign the Agreement without Customer's consent, except that Vendor may assign it to an affiliate or successor (cl. 11).

## Run Info
- Input file: input/sample_contract.txt
- Date: 2026-11-16
- Model: sonnet (coordinator); haiku (sub-agents)
- Sub-agents used: clause-agent, obligation-agent, risk-agent
- Coordinator edits: dropped a clause-agent finding that Vendor liability is "uncapped" (§6.1) because the contract text does not say so; folded §5.2 into the §5.1 finding.

---
GATE: FAIL
