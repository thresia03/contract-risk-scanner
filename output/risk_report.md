# Contract Risk Report — TechVendor Ltd. (input/sample_contract.txt)

## Risk Rating
**High** — Section 5.1 irrevocably assigns all Customer Data to Vendor, and Section 6.2 leaves Customer's liability unlimited, both P1 findings.

### Critical Summary
The most dangerous clause is Section 5.1, which irrevocably assigns all Customer Data uploaded to or generated through the Services to Vendor, and Section 5.2 lets Vendor commercialise that data during and after the term without notice or compensation. The most important customer obligation is Section 3.2, which auto-renews the Agreement for 12-month terms unless Customer gives non-renewal notice at least seven days before term end, and binds Customer to the full renewal fee if it does not. Before signing, Customer should strike or narrow the Section 5.1 data assignment and extend the non-renewal notice period in Section 3.2.

## P1 Critical Clauses
| Clause type | Excerpt (max 30 words) | Risk explanation |
|---|---|---|
| Auto-renewal without adequate notice (3.2) | "this Agreement shall automatically renew for successive periods of twelve (12) months unless Customer provides written notice of non-renewal at least seven (7) days prior" | Non-renewal notice is due only 7 days before term end. Failure to give timely notice "shall bind Customer to the full renewal fee." |
| Uncapped liability (6.2) | "Customer's liability to Vendor ... shall be unlimited and shall include all direct and indirect losses, costs, and expenses incurred by Vendor." | Customer's liability is stated as unlimited and includes indirect losses. No cap is stated. |
| Limitation of Vendor liability (6.1) | "Vendor's liability to Customer ... is limited to the extent expressly stated in this Section." | Section 6 states no monetary cap for Vendor. Vendor also excludes "loss of data," which is not excluded for Customer under 6.2. |
| Unilateral data assignment to vendor (5.1) | "All data, content, records, and information uploaded to or generated through the Services by Customer or its users ("Customer Data") is hereby irrevocably assigned to Vendor." | Customer Data is irrevocably assigned to Vendor, with no reversion or return stated. |
| Data use rights without notice or compensation (5.2) | "Vendor may use, analyse, aggregate, license, and commercialise Customer Data for analytics, product development, benchmarking, and any other business purpose" | Vendor may use and license Customer Data for any business purpose during and after the term. The clause states this occurs "without further notice or compensation to Customer." |
| Unilateral IP assignment to vendor (8) | "Vendor retains all rights, title, and interest in the Services, including all improvements and derivative works." | Improvements and derivative works are retained by Vendor. Customer receives only a "limited, non-exclusive, non-transferable right to access the Services during the term." |
| Punitive late-payment penalty (2.1) | "Late amounts accrue interest at 1.5% per month." | Stated rate is 1.5% per month on late amounts. Classified here as a penalty under the P1 taxonomy. |

## P2 Major Clauses
| Clause type | Excerpt (max 30 words) | Risk explanation |
|---|---|---|
| Price escalation trigger (2.2) | "Vendor may increase the subscription fees by up to fifteen percent (15%) in each contract year, effective upon written notice to Customer." | Vendor may raise fees up to 15% each contract year. The clause adds that increases take effect "without the need for Customer's consent or approval." |
| Broad indemnification (6.3) | "Customer shall indemnify and hold harmless Vendor against all claims arising from Customer's use of the Services." | Customer indemnifies Vendor against "all claims" arising from its use of the Services. No cap or carve-out is stated. |
| Customer data ownership ambiguity (5.1) | "Customer retains no further rights in data once submitted, as set out below." | The clause does not define which rights Customer retains. It conflicts with the irrevocable assignment stated in the next sentence of 5.1. |
| Exclusivity | — | None found |

## P3 Minor Clauses
| Clause type | Excerpt (max 30 words) | Risk explanation |
|---|---|---|
| Termination-for-convenience timeline (4.1) | "Either party may terminate this Agreement for convenience by giving thirty (30) days' prior written notice to the other party." | Mutual right to terminate for convenience on 30 days' written notice. |
| Cure period for breach termination (4.2) | "fails to cure such breach within fifteen (15) days of notice." | Immediate termination right for material breach applies if the breach is not cured within 15 days of notice. |
| Refund and termination payment terms (4.3) | "No refunds shall be due for prepaid fees." | Prepaid fees are non-refundable on termination. Customer must pay all fees accrued through the termination date. |
| Governing law (10) | "This Agreement shall be governed by and construed in accordance with the laws of the State of Delaware, United States" | Delaware law governs, without regard to its conflict of laws principles. |
| Dispute resolution forum (10) | "The parties submit to the exclusive jurisdiction of the state and federal courts located in Delaware." | Disputes must be heard exclusively in Delaware state or federal courts. |

## Key Obligations
### Acme Corp
- Pay the annual subscription fee set out in Schedule B within thirty (30) days of receipt of each invoice (cl. 2.1).
- Late amounts accrue interest at 1.5% per month (cl. 2.1).
- Give written notice of non-renewal at least seven (7) days before the end of the then-current term; failure to do so binds Acme Corp to the full renewal fee (cl. 3.2).
- Pay all fees accrued through the effective date of termination; no refunds are due for prepaid fees (cl. 4.3).
- Indemnify and hold harmless TechVendor Ltd. against all claims arising from Acme Corp's use of the Services (cl. 6.3).
- Liability to TechVendor Ltd. is unlimited and includes all direct and indirect losses, costs, and expenses incurred by TechVendor Ltd. (cl. 6.2).
- Keep TechVendor Ltd.'s confidential information confidential and use it solely to perform obligations under the Agreement; this survives three (3) years after termination (cl. 7).
- All Customer Data is irrevocably assigned to TechVendor Ltd. (cl. 5.1).

### TechVendor Ltd.
- Provide Acme Corp with access to the cloud-based workflow automation platform in accordance with the service descriptions in Schedule A (cl. 1).
- Use commercially reasonable efforts to make the Services available 99.5% of the time in any calendar month, excluding scheduled maintenance (cl. 1).
- Keep Acme Corp's confidential information confidential and use it solely to perform obligations under the Agreement; this survives three (3) years after termination (cl. 7).
- Not assign the Agreement without Acme Corp's consent, except that it may assign to an affiliate or successor (cl. 11).
- Amendments to the Agreement must be in writing and signed by both parties (cl. 11).

## Run Info
- Input file: input/sample_contract.txt
- Date: 2026-11-14
- Model: coordinator sonnet; sub-agents haiku
- Sub-agents used: clause-agent, obligation-agent, risk-agent roles. The custom agent definitions in .claude/agents/ were not registered in this session, so each role ran as a haiku general-purpose agent with the agent file's instructions. They ran in parallel.

---
GATE: FAIL
